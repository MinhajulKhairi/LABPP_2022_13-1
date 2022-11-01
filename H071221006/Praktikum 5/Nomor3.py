#Nomor3

x = set(map(int,input("Input array ke 1: ").split()))
y = set(map(int,input("Input array ke 2: ").split()))

z = x.intersection(y)
z = tuple(z)

print(f"Terdapat {len(z)} duplikat yaitu {z}")

