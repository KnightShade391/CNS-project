from CBC_Binary import applyCBC

pltxt = ("0" * 256) + ("1" * 0)
initVect = ("0" * 127) + ("1" * 1)
deskey1 = ("0" * 1) + ("1" * 63)
deskey2 = ("0" * 0) + ("1" * 64)

c = applyCBC(pltxt, deskey1, deskey2, initVect)
print(c, sep = "\n")