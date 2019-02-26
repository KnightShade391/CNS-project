def p10(text):
    return "".join([text[i-1] for i in (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)])

def p8(text):
    return "".join([text[i-1] for i in (6, 3, 7, 4, 8, 5, 10, 9)])

def p4(text):
    return "".join([text[i-1] for i in (2, 4 ,3, 1)])

def ip(text):
    return "".join([text[i-1] for i in (2, 6, 3, 1, 4, 8, 5, 7)])

def ipInv(text):
    return "".join([text[i-1] for i in (4, 1, 3, 5, 7, 2, 8, 6)])

def expansion(text):
    return "".join([text[i-1] for i in (4, 1, 2, 3, 2, 3, 4, 1)])

def sBox(text):
    S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
    ]

    S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
    ]

    s0 = bin(S0[int(text[0] + text[3], 2)][int(text[1] + text[2], 2)])[2:].zfill(2)
    s1 = bin(S1[int(text[4] + text[7], 2)][int(text[5] + text[6], 2)])[2:].zfill(2)

    return (s0 + s1)

def swap(text):
    return (text[4:] + text[:4])

def leftCircularShift(text, n):
    return (text[n:] + text[:n])

def generateKeys(key):
    perm10 = p10(key)
    ls1 = leftCircularShift(perm10[:5], 1) + leftCircularShift(perm10[5:], 1)
    k1 = p8(ls1)
    ls2 = leftCircularShift(ls1[:5], 2) + leftCircularShift(ls1[5:], 2)
    k2 = p8(ls2)
    return [k1, k2]

def fiestalRound(text, key):
    left = text[:4]
    right = text[4:]
    exp = expansion(right)
    xor = bin(int(exp, 2) ^ int(key, 2))[2:].zfill(8)
    s = sBox(xor)
    perm4 = p4(s)
    xor = bin(int(left, 2) ^ int(perm4, 2))[2:].zfill(4)
    return (xor + right)

def SDESEncrypt(plaintext, key):
    k1, k2 = generateKeys(key)
    initPerm = ip(plaintext)
    f1 = fiestalRound(initPerm, k1)
    text = swap(f1)
    f2 = fiestalRound(text,  k2)
    ciphertext = ipInv(f2)
    return ciphertext

def SDESDecrypt(ciphertext, key):
    k1, k2 = generateKeys(key)
    initPerm = ip(ciphertext)
    f1 = fiestalRound(initPerm, k2)
    text = swap(f1)
    f2 = fiestalRound(text,  k1)
    plaintext = ipInv(f2)
    return plaintext

plaintext = "Hello"
ciphertext = ""
for c in plaintext:
    ciphertext += chr(int(SDESEncrypt(bin(ord(c))[2:].zfill(8), "1100011110"), 2))
    print(SDESEncrypt(bin(ord(c))[2:].zfill(8), "1100011110"))
print(ciphertext)
p = ""
for c in ciphertext:
    p += chr(int(SDESDecrypt(bin(ord(c))[2:].zfill(8), "1100011110"), 2))
print(p)