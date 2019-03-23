from DES import applyDES
from utils import convertToAscii, convertToBinary, xor, splitIntoParts

ENCRYPT = "ENCRYPT"

# a mehtod to perform encryption
def CBCEncryptRound(firstHalfFeedback, lastHalfFeedback, firstHalfText, lastHalfText, iv1, iv2, DESKey1, DESKey2):
    # apply des for the two halves of the feedback
    firstHalfRes = applyDES(firstHalfFeedback, DESKey1, ENCRYPT)
    lastHalfRes = applyDES(lastHalfFeedback, DESKey2, ENCRYPT)
    
    # xor the two des results with a half of the plain text
    firstHalfCipher = xor(firstHalfText, firstHalfRes, 64)
    lastHalfCipher = xor(lastHalfText, lastHalfRes, 64)

    # apply des for the xor'd results
    lastCipher = applyDES(firstHalfCipher, DESKey2, ENCRYPT)
    firstCipher = applyDES(lastHalfCipher, DESKey1, ENCRYPT)

    # xor the result of des with a half of the initial vector
    firstCipher = xor(firstCipher, iv1, 64)
    lastCipher = xor(lastCipher, iv2, 64)

    # return the cipher text
    return [firstCipher, lastCipher]

# a method to apply the CBC based on the mode
def applyCBC(text, DESKey1, DESKey2, inititalVector):
    # convert all parameters into binary
    # text = convertToBinary(text)
    inititalVector = convertToBinary(inititalVector)
    DESKey1 = convertToBinary(DESKey1)
    DESKey2 = convertToBinary(DESKey2)

    # divide the text into blocks each of size 128 bits
    textIntoParts = splitIntoParts(text, 128)

    # split the inititalVector into 2 halves each of 64bit length
    firstHalf = inititalVector[:64]
    lastHalf = inititalVector[64:]

    # shift the first half of the initial vector once and second half twice
    iv1 = firstHalf[1:] + firstHalf[0]
    iv2 = lastHalf[2:] + lastHalf[:2]

    # check if encryption or decryption
    firstHalf, lastHalf = CBCEncryptRound(firstHalf, lastHalf, textIntoParts[0][:64], textIntoParts[0][64:], iv1, iv2, DESKey1, DESKey2)
    # add the first cipher into the list
    result = [firstHalf + lastHalf]

    for i in range(1, len(textIntoParts)):
        # shift the first half of the initial vector once and second half twice
        iv1 = iv1[1:] + iv1[0]
        iv2 = iv2[2:] + iv2[:2]
        # check if encryption or decryption

        firstHalf, lastHalf = CBCEncryptRound(lastHalf, firstHalf, textIntoParts[i][:64], textIntoParts[i][64:], iv1, iv2, DESKey1, DESKey2)
        # add the cipher into the list
        result.append(firstHalf + lastHalf)

    return result