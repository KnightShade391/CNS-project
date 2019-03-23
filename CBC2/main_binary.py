from CBC_Binary import applyCBC

pltxt = ("0" * 254) + ("1" * 2)
initVect = "myciphermycipher"
deskey1 = "deskey01"
deskey2 = "deskeymy"

c = applyCBC(pltxt, deskey1, deskey2, initVect)
print(c, sep = "\n")