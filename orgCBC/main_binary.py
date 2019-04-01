from CBC_Binary import applyCBC

pltxt = ("0" * 255) + ("1" * 0)
initVect = ("0" * 64) + ("1" * 0)
deskey = ("0" * 30) + ("1" * 34)

c = applyCBC(pltxt, deskey, initVect, "ENCRYPT")
print(c, sep = "\n")