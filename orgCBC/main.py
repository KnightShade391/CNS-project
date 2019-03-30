from CBC import applyCBC

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

pltxt = "plaintxttxtnialp"
initVect = "mycipher"
deskey = "deskeymy"

c = applyCBC(pltxt, deskey, initVect, ENCRYPT)
d = applyCBC(c, deskey, initVect, DECRYPT)

print(c, d, sep = "\n")