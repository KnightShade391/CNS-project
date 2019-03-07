from DES import applyDES

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

def convertToBinary(text):
    textToBin = ""
    for c in text:
        textToBin += bin(ord(c))[2:].zfill(8)
    return textToBin

def convertToAscii(ciphers):
    ciphertxt = ""
    for cipher in ciphers:
        cipherIntoParts = [cipher[i:i+8] for i in range(0, len(cipher), 8)]
        for c in cipherIntoParts:
            ciphertxt += chr(int(c, 2))
    return ciphertxt

def CBCRound(firstHalfFeedback, lastHalfFeedback, firstHalfText, lastHalfText, DESKey1, DESKey2):
    # apply des for the two halves
    firstHalfRes = applyDES(firstHalfFeedback, DESKey1, ENCRYPT)
    lastHalfRes = applyDES(lastHalfFeedback, DESKey2, ENCRYPT)
    # xor the result of each half with a half of the plain text
    firstHalfCipher = bin(int(firstHalfText, 2) ^ int(firstHalfRes, 2))[2:].zfill(64)
    lastHalfCipher = bin(int(lastHalfText, 2) ^ int(lastHalfRes, 2))[2:].zfill(64)
    return [firstHalfCipher, lastHalfCipher]

def applyCBC(text, DESKey1, DESKey2, CBCKey, mode):
    # convert all parameters into binary
    text = convertToBinary(text)
    CBCKey = convertToBinary(CBCKey)
    DESKey1 = convertToBinary(DESKey1)
    DESKey2 = convertToBinary(DESKey2)

    # divide the text into blocks each of size 128 bits
    textIntoParts = [text[i:i+128] for i in range(0, len(text), 128)]

    # split the CBCKey into 2 halves each of 64bit length
    firstHalf = CBCKey[:64]
    lastHalf = CBCKey[64:]

    # perform the first round
    firstHalf, lastHalf = CBCRound(firstHalf, lastHalf, textIntoParts[0][:64], textIntoParts[0][64:], DESKey1, DESKey2)
    ciphers = [firstHalf + lastHalf]

    for i in range(1, len(textIntoParts)):
        # apply the round function using crossed feedback of the previous round
        if(mode == ENCRYPT):
            firstHalf, lastHalf = CBCRound(lastHalf, firstHalf, textIntoParts[i][:64], textIntoParts[i][64:], DESKey1, DESKey2)
        else:
            firstHalf, lastHalf = CBCRound(textIntoParts[i - 1][64:], textIntoParts[i - 1][:64], textIntoParts[i][:64], textIntoParts[i][64:], DESKey1, DESKey2)
        ciphers.append(firstHalf + lastHalf)
    
    # convert the binary back to characters
    return convertToAscii(ciphers)