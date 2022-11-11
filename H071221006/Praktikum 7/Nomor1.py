#Nomor1
#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57

import re

string1 = str(input("Masukkan string: "))

var1 = re.compile("[A-Za-z24680]{40}([\s13579]{5})$")
result = var1.fullmatch(string1)
if result:
    print("true")
else:
    print("false")
