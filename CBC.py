from DES import applyDES
from conversion import convertToBinary, convertToAscii

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

def CBCRound(firstHalfFeedback, lastHalfFeedback, firstHalfText, lastHalfText, DESKey1, DESKey2, mode):
    # apply des for the two halves
    firstHalfRes = applyDES(firstHalfFeedback, DESKey1, mode)
    lastHalfRes = applyDES(lastHalfFeedback, DESKey2, mode)
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

    ciphers = []
    for i in range(len(textIntoParts)):
        # apply the round function
        lastHalf, firstHalf = CBCRound(firstHalf, lastHalf, textIntoParts[i][:64], textIntoParts[i][64:], DESKey1, DESKey2, mode)
        ciphers.append(lastHalf + firstHalf)
        print(ciphers)
    
    # convert the binary back to characters
    return convertToAscii(ciphers)

pltxt = "plaintxtplaintxtplaintxtplaintxt"
cbckey = "myciphermycipher"
deskey1 = "mydeskey"
deskey2 = "mydeskey"

c = applyCBC(pltxt, deskey1, deskey2, cbckey, ENCRYPT)
d = applyCBC(c, deskey1, deskey2, cbckey, DECRYPT)

print(c, d, sep = "\n")