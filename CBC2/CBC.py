from DES import applyDES
from utils import convertToAscii, convertToBinary, xor, splitIntoParts, pad_chars
from threading import Thread

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"
res = {}

def callDES(text, key, mode, index):
    r = applyDES(text, key, mode)
    res[index] = r

# a mehtod to perform encryption
def CBCEncryptRound(firstHalfFeedback, lastHalfFeedback, firstHalfText, lastHalfText, iv1, iv2, DESKey1, DESKey2):
    # apply des for the two halves of the feedback
    threads = [None] * 2
    args = [[firstHalfFeedback, DESKey1, ENCRYPT], [lastHalfFeedback, DESKey2, ENCRYPT]]
    for i in range(2):
        threads[i] = Thread(target = callDES, args = (args[i][0], args[i][1], args[i][2], i))
        threads[i].start()
    for i in range(2):
        threads[i].join()
    firstHalfRes = res[0]
    lastHalfRes = res[1]
    res.clear()
    threads.clear()
    args.clear()
    
    # xor the two des results with a half of the plain text
    firstHalfCipher = xor(firstHalfText, firstHalfRes, 64)
    lastHalfCipher = xor(lastHalfText, lastHalfRes, 64)

    # apply des for the xor'd results
    threads = [None] * 2
    args = [[firstHalfCipher, DESKey2, ENCRYPT], [lastHalfCipher, DESKey1, ENCRYPT]]
    for i in range(2):
        threads[i] = Thread(target = callDES, args = (args[i][0], args[i][1], args[i][2], i))
        threads[i].start()
    for i in range(2):
        threads[i].join()
    lastCipher = res[0]
    firstCipher = res[1]
    res.clear()
    threads.clear()
    args.clear()

    # xor the result of des with a half of the initial vector
    firstCipher = xor(firstCipher, iv1, 64)
    lastCipher = xor(lastCipher, iv2, 64)

    # return the cipher text
    return [firstCipher, lastCipher]

# a mehtod to perform decryption
def CBCDecryptRound(firstHalfFeedback, lastHalfFeedback, firstHalfCipher, lastHalfCipher, iv1, iv2, DESKey1, DESKey2):
    # xor the halves of cipher text and initial vector
    firstHalfCipher = xor(firstHalfCipher, iv1, 64)
    lastHalfCipher = xor(lastHalfCipher, iv2, 64)

    # apply des for the two halves of cipher text in decryption mode
    threads = [None] * 2
    args = [[firstHalfCipher, DESKey1, DECRYPT], [lastHalfCipher, DESKey2, DECRYPT]]
    for i in range(2):
        threads[i] = Thread(target = callDES, args = (args[i][0], args[i][1], args[i][2], i))
        threads[i].start()
    for i in range(2):
        threads[i].join()
    firstHalfRes1 = res[0]
    lastHalfRes1 = res[1]
    res.clear()
    threads.clear()
    args.clear()

    # apply des for the two halves of the feedback in encryption mode
    threads = [None] * 2
    args = [[lastHalfFeedback, DESKey1, ENCRYPT], [firstHalfFeedback, DESKey2, ENCRYPT]]
    for i in range(2):
        threads[i] = Thread(target = callDES, args = (args[i][0], args[i][1], args[i][2], i))
        threads[i].start()
    for i in range(2):
        threads[i].join()
    firstHalfRes2 = res[0]
    lastHalfRes2 = res[1]
    res.clear()
    threads.clear()
    args.clear()

    # cross xor the halves the two des results
    firstHalfText = xor(firstHalfRes2, lastHalfRes1, 64)
    lastHalfText = xor(firstHalfRes1, lastHalfRes2, 64)

    # return the plain text
    return [firstHalfText, lastHalfText]

# a method to apply the CBC based on the mode
def applyCBC(text, DESKey1, DESKey2, inititalVector, mode):
    # convert all parameters into binary
    if(mode == DECRYPT):
        text = convertToBinary(text)
    else:
        text = pad_chars(text)
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
    if(mode == ENCRYPT):
        firstHalf, lastHalf = CBCEncryptRound(firstHalf, lastHalf, textIntoParts[0][:64], textIntoParts[0][64:], iv1, iv2, DESKey1, DESKey2)
    else:
        firstHalf, lastHalf = CBCDecryptRound(lastHalf, firstHalf, textIntoParts[0][:64], textIntoParts[0][64:], iv1, iv2, DESKey1, DESKey2)
    # add the first cipher/plaintext into the list
    result = [firstHalf + lastHalf]

    for i in range(1, len(textIntoParts)):
        # shift the first half of the initial vector once and second half twice
        iv1 = iv1[1:] + iv1[0]
        iv2 = iv2[2:] + iv2[:2]
        # check if encryption or decryption
        if(mode == ENCRYPT):
            firstHalf, lastHalf = CBCEncryptRound(lastHalf, firstHalf, textIntoParts[i][:64], textIntoParts[i][64:], iv1, iv2, DESKey1, DESKey2)
        else:
            firstHalf, lastHalf = CBCDecryptRound(textIntoParts[i - 1][:64], textIntoParts[i - 1][64:], textIntoParts[i][:64], textIntoParts[i][64:], iv1, iv2, DESKey1, DESKey2)
        # add the cipher/plaintext into the list
        result.append(firstHalf + lastHalf)

    if mode == DECRYPT:
        extraChars = int(result[-1], 2)
        result = result[:-1]
        decryptText = convertToAscii("".join(result))
        #print(decryptText[:-extraChars])
        return decryptText[:-extraChars]
    else:    
    # convert the binary back to characters
        return convertToAscii("".join(result))
