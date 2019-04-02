from CBC import applyCBC
from utils import *
import base64

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"
initVect = "helloworldholayo"
c, d, = "", ""

print("-" * 60)
print("MENU\n1-ENCRYPT \n2-DECRYPT \n3-Exit")
print("-" * 60)
while(True):
    ch = int(input("Enter your choice (1/2/3): "))
    if(ch == 1):
        pltxt = input("Enter the message: ")
        k1, k2 = getDESKeys()
        k = open("keys.txt", "w")
        k.write(k1 + " " + k2)
        k.close()
        print("Encrypting...")
        print("Cipher text: ", end = "")
        c = applyCBC(pltxt, k1, k2, initVect, ENCRYPT)
        print(c)
        fh = open("./e.txt", "wb")
        fh.write(c.encode("utf-8"))
        fh.close()
    elif(ch == 2):
        k = open("keys.txt", "r")
        k1, k2 = k.readline().split()
        k.close()
        ef = input("Enter the path where the cipher text file is present: ")
        try:
            tr = open(ef, "rb")
            tr = tr.read()
        except:
            print("Invalid path!")
            exit(0)
        c = tr.decode("utf-8")
        print("Decrypting...")
        d = applyCBC(c, k1, k2, initVect, DECRYPT)
        print("Plain text:", d)
    elif(ch == 3):
        exit(0)
    else:
        print("Invalid choice!")
        exit(0)
    print("-" * 60)

# pltxt = input("Enter a message: ")
# # pltxt = ("a" * 1) + ("b" * 1)
# deskey1, deskey2 = getDESKeys()

# c = applyCBC(pltxt, deskey1, deskey2, initVect, ENCRYPT)
# d = applyCBC(c, deskey1, deskey2, initVect, DECRYPT)

# print(c, d, sep = "\n")