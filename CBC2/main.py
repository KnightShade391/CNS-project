from CBC import applyCBC
from utils import *

ENCRYPT = "ENCRYPT"
DECRYPT = "DECRYPT"

pltxt = "cnsprojectcnsprojectcnsproject122"
# pltxt = ("a" * 1) + ("b" * 1)
initVect = "helloworldholayo"
deskey1 = "deskey01"
deskey2 = "deskeymy"

c = applyCBC(pltxt, deskey1, deskey2, initVect, ENCRYPT)
d = applyCBC(c, deskey1, deskey2, initVect, DECRYPT)

print(c, d, sep = "\n")