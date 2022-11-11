a = input() 
b = input() 

try :
    with open(f"{a}.txt", "r") as origin :
        x = origin.read()
except :
    print("\nGagal")
else :
    with open(f"{b}.txt", "w") as copy :
        copy.write(x)
    print("\nBerhasil")
    
