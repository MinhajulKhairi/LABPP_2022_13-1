#Nomor2

print("Selamat datang untuk memulai Silahkan input data anda")
name = str(input("Input nama: "))
age = int(input("Input umur: "))
address = str(input("Input alamat: "))

list_name = []
list_name.append(name)
list_age = []
list_age.append(age)
list_address = []
list_address.append(address)

n = 0
while n >= 0:
    n += 1
    print("="*50)
    if n == 1:
        print(f"\nSelamat datang {name} silahkan pilih opsi")

    print("\n1. Detail anda")
    print("2. Ubah nama")
    print("3. Ubah umur")
    print("4. Ubah alamat")
    print("5. Keluar")
        
    print("="*50)
    x = int(input("\nInput opsi: "))

    print("="*50)
    if x == 1:
        print("\nData anda adalah")
        print(f"Nama: {list_name[0]}")
        print(f"Umur: {list_age[0]}")
        print(f"Alamat: {list_address[0]}")
    elif x == 2:
        new_name = str(input("\nSilahkan Input nama baru: "))
        list_name.clear()
        list_name.append(new_name)
        print("Data anda sukses diperbarui")
    elif x == 3:
        new_age = int(input("\nSilahkan Input umur baru: "))
        list_age.clear()
        list_age.append(new_age)
        print("Data anda sukses diperbarui")
    elif x == 4:
        new_address = str(input("\nSilahkan Input alamat baru: "))
        list_address.clear()
        list_address.append(new_address)
        print("Data anda sukses diperbarui")
    elif x == 5:
        print(f"\nSelamat tinggal {list_name[0]}")
    else:
        print("Inputan salah")
        break
        
        

            
    



