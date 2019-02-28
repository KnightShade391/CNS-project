# references:
# http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm 
# -> contains an example of whole DES process with all 16 keys
# -> check if all keys u generate are same as in the site

# https://academic.csuohio.edu/yuc/security/Chapter_06_Data_Encription_Standard.pdf
# -> Its the DES reference pdf
# -> contains the DES process with key generation

# https://github.com/RobinDavid/pydes/blob/master/pydes.py
# -> contains the DES program in python


# description:
# key is 64 bit
# generateKeys shud return a list of 16 keys

# key = "0001001100110100010101110111100110011011101111001101111111110001"
# def generateKeys(key):
#     return [k1, k2, k3, ..., k16]