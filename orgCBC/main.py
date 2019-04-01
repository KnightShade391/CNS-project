from CBC import applyCBC
from utils import *

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

# pltxt = "plaintxttxtnialp"
pltxt = ("a" * 16) + ("b" * 0)
initVect = "mycipher"
deskey = "deskeymy"

c = applyCBC(pltxt, deskey, initVect, ENCRYPT)
d = applyCBC(c, deskey, initVect, DECRYPT)

print(convertToBinary(c), d, sep = "\n")