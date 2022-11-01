matriks11 = []
for row1 in range(1,3):
    matriks12 = []
    for column1 in range(1,3):
        matriks_1 = int(input(f"Input nilai matriks pertama index {row1},{column1}: "))
        matriks12.append(matriks_1)
    matriks11.append(matriks12)

matriks21 = []
for row2 in range(1,3):
    matriks22 = []
    for column2 in range(1,3):
        matriks_2 = int(input(f"Input nilai matriks kedua index {row2},{column2}: "))
        matriks22.append(matriks_2)
    matriks21.append(matriks22)

multiplier1 = []
multiplier2 = []

r1c1 = (matriks11[0][0]*matriks21[0][0]) + (matriks11[0][1]*matriks21[1][0])
multiplier1.append(r1c1)
r1c2 = (matriks11[0][0]*matriks21[0][1]) + (matriks11[0][1]*matriks21[1][1])
multiplier1.append(r1c2)
r2c1 = (matriks11[1][0]*matriks21[0][0]) + (matriks11[1][1]*matriks21[1][0])
multiplier2.append(r2c1)
r2c2 = (matriks11[1][0]*matriks21[0][1]) + (matriks11[1][1]*matriks21[1][1])
multiplier2.append(r2c2)

print("<<< Hasil perkalian matriks >>>")
print(f"| {matriks11[0][0]}, {matriks11[0][1]} | x | {matriks21[0][0]}, {matriks21[0][1]} | = | {multiplier1[0]}, {multiplier1[1]} |")
print(f"| {matriks11[1][0]}, {matriks11[1][1]} |   | {matriks21[1][0]}, {matriks21[1][1]} |   | {multiplier2[0]}, {multiplier2[1]} |")
