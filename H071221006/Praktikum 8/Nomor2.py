class Kubus:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def setPanjang(self,panjang):
        self.panjang = panjang
    def getPanjang(self):
        return self.panjang
    def setLebar(self,lebar):
        self.lebar = lebar
    def getLebar(self):
        return self.lebar
    def setTinggi(self,tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self.tinggi
    def setMassa(self, massa):
        self.massa = massa
    def getMassa(self):
        return self.massa
    def getMassaJenis(self):
        self.MassaJenis = self.massa / (self.panjang * self.lebar * self.tinggi)
        return self.MassaJenis

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))
massa = float(input("Masukkan massa: "))

kubus = Kubus(panjang, lebar, tinggi)

kubus.setMassa(massa)
print("Massa jenis: ", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa jenis: ", kubus.getMassaJenis())
