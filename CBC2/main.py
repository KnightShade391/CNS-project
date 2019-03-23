from CBC import applyCBC

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

pltxt = "plaintxttxtnialp"
initVect = "myciphermycipher"
deskey1 = "deskey01"
deskey2 = "deskeymy"

c = applyCBC(pltxt, deskey1, deskey2, initVect, ENCRYPT)
d = applyCBC(c, deskey1, deskey2, initVect, DECRYPT)

print(c, d, sep = "\n")