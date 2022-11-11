#Nomor2

try:
    a = input() 
    b = input() 
    c = 0

    with open(f"{a}.txt", "r") as origin :
        for x in origin:
            if len(x)>c:
                c = len(x)

    with open(f"{a}.txt", "r") as origin :
        baris = 1
        banyak_baris = len(origin.readlines())
       
    with open(f"{a}.txt","r") as origin :
        copy = open(f"{b}.txt","w")
        for i in origin:
            if baris < banyak_baris:
                new_text = f"{i.rstrip():>{c}}\n"
            else:
                new_text = f"{i.rstrip():>{c}}"
            copy.write(new_text)
            baris += 1
        copy.close()
    print("\nberhasil")
except:
    print("\nGagal")

        
    
