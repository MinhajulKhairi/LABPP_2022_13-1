import re
import os

name = []
email = []
password = []
n = 0  #untuk perulangan email
b = 0  #untuk menyimpan berapa data yang sudah disimpan di dalam file
c = 0  #untuk mengetahui berapa inputan data yang tersimpan di file


while True:
    print("="*50)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda")

    print("\n1. Detail Anda")
    print("2. Ubah Nama")
    print('3. Jumlah Data Pada File')
    print("4. Save Data Pada File")
    print('5. Buat Data Baru')
    print('6. Keluar')

    # try:
    x = int(input("\nSilahkan Pilih Opsi Anda: "))
    print("="*50)

    if x == 1:
            if b == 0:
                print("Data anda kosong")
            elif b > 0:
                print("\nData anda adalah")
                print(f"Nama: {name[0]}")
                print(f"Email: {email[0]}")
                print(f"Password: {password[0]}")
            
    elif x == 2:
            if b == 0:
                print("Data anda kosong")
            elif b > 0:
                new_name = str(input("\nSilahkan Input nama baru: "))
                name.clear()
                name.append(new_name)
                print("Data anda sukses diperbarui")
            
    elif x == 3:
        file_baru = input("Masukkan nama file: ") 
        if os.path.exists(f'{file_baru}.txt'):
            print(f'Jumlah data pada file: {b} data')
        else:
            print(f'Tidak terdapat file dengan nama {file_baru}.txt')
            print("Jumlah data pada file: 0 data")

    elif x == 4:
        file = input("Masukkan file: ")
        with open(f'{file}.txt', 'a') as file:
            if c == 1:
                    file.write('+'+'='*50+'+')
                    file.write('\n|'+'Data yang tersimpan')
                    file.write('\n+'+'='*50+'+')
                    file.write(f'\n|'+'Nama'+' '*11+':'+f'{name[0]}')
                    file.write('\n|'+'Email'+' '*10+':'+f'{email[0]}')
                    file.write(f'\n|'+'Password'+' '*7+':'+f'{password[0]}')
                    file.write('\n+'+'='*50+'+')
                    c += 1
                    

            elif c > 1:
                file.write(f'\n|'+'Nama'+' '*11+':'+f'{name[0]}')
                file.write('\n|'+'Email'+' '*10+':'+f'{email[0]}')
                file.write(f'\n|'+'Password'+' '*7+':'+f'{password[0]}')
                file.write('\n+'+'='*50+'+')
                c += 1
                
                
    elif x == 5:
            n -= 1
            name.clear()
            email.clear()
            password.clear()
            Name = input("Silahkan masukkan nama: ")
            while n < 0:
                Email = input("Silahkan masukkan email: ")
                y = re.findall(r"^[a-z]+@student[.]unhas[.]ac[.]id$", Email)
                if y:
                    Password = input("Silahkan masukkan password: ")
                    if len(Password) >= 8 and len(Password) <= 20:
                        z = re.findall(r"[A-Z]+[a-z]+[0-9]|[A-Z]+[0-9]+[a-z]|[a-z]+[A-Z]+[0-9]|[a-z]+[0-9]+[A-Z]|[0-9]+[A-Z]+[a-z]|[0-9]+[a-z]+[A-Z]", Password)
                        if z:
                            n += 1
                            b += 1
                            c += 1
                                        
                            name.append(Name)      
                            email.append(Email)                           
                            password.append(Password)                      
                        else:
                            print("Password tidak sesuai")
                    else:
                        print("Password anda terlalu lemah")
                else:
                    print("Email anda salah")
        
                            
    elif x == 6:
            print("Sampai jumpa")
            break

    
