#Nomor3

try:
    file = input()
    range1 = int(input())
    nama = []
    nim = []
    angkatan = []

    for i in range(range1):
        name = input()
        NIM = input()
        year = input()
        nama.append(name)
        nim.append(NIM)
        angkatan.append(year)

    nama_panjang = nama[0]
    for x in nama_panjang:
        if len(x) > len(nama_panjang):
            nama_panjang = x
    x = len(nama_panjang)

    if x <= 20:
        if len(NIM) == 10:
            if len(year) == 4:
                with open(f'{file}.txt', 'x') as file:
                    file.write('+'+'-'*(len(nama_panjang)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    file.write('|'+'nama'+' '*(len(nama_panjang)-5+2)+'|')
                    file.write('NIM'+' '*(10-4+2)+'|\n')
                    file.write('Angkatan'+' '*(10-9)+'|\n')
                    file.write('+'+'-'*(len(nama_panjang)+2)+'+')
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                
                    for i in range(file):
                        panjang_nama = nama[0]
                        for x in name:
                            if len(i) > len(panjang_nama):
                                panjang_nama = i
                        file.write(f'| {nama[i]} '+' '*(len(nama_panjang)-len(nama[i])))
                        file.write(f'| {nim[i]}'+' '*1)
                        file.write(f'| {angkatan[i]}'+' '*5+'|\n')
                        
                    file.write(('+'+'-'*(len(panjang_nama)+2)+'+'))
                    file.write('-'*12+'+')
                    file.write('-'*10+'+\n')
                    print("berhasil")
            else:
                print("gagal")
        else:
            print("gagal")
            
    else:
        print("gagal")

except:
    print("Gagal")
