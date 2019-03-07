from CBC import applyCBC

pltxt = "plaintxtplaintxtplaintxtplaintxttxtnialptxtnialp"
cbckey = "myciphermycipher"
deskey1 = "mydeskey"
deskey2 = "mydeskey"
ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

c = applyCBC(pltxt, deskey1, deskey2, cbckey, ENCRYPT)
d = applyCBC(c, deskey1, deskey2, cbckey, DECRYPT)

print("Cipher text: " + c, "Plain text: " + d, sep = "\n")