from CBC import applyCBC

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

pltxt = "12345678901234567890123456789012"
initVect = "helloworldholayo"
deskey1 = "deskey01"
deskey2 = "deskeymy"

c = applyCBC(pltxt, deskey1, deskey2, initVect, ENCRYPT)
d = applyCBC(c, deskey1, deskey2, initVect, DECRYPT)

print(c, d, sep = "\n")