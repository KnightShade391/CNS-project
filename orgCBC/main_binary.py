from CBC_Binary import applyCBC

pltxt = ("0" * 253) + ("1" * 3)
initVect = "mycipher"
deskey = "deskeymy"

c = applyCBC(pltxt, deskey, initVect, "ENCRYPT")
print(c, sep = "\n")