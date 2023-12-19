class KonversiSuhu:
    def __init__(self, suhu, unit_awal):
        self.suhu = suhu
        self.unit_awal = unit_awal
        self.val = suhu

    def get_celcius(self):
        return self.val

    def to_fahrenheit(self):
        if self.unit_awal == "C":
            return (9/5 * self.suhu) + 32
        elif self.unit_awal == "F":
            return self.suhu
        elif self.unit_awal == "R":
            return (9/5 * self.suhu) + 32
        elif self.unit_awal == "K":
            return (9/5 * (self.suhu - 273)) + 32

    def to_reamur(self):
        if self.unit_awal == "C":
            return 4/5 * self.suhu
        elif self.unit_awal == "F":
            return 4/9 * (self.suhu - 32)
        elif self.unit_awal == "R":
            return self.suhu
        elif self.unit_awal == "K":
            return 4/5 * (self.suhu - 273)

    def to_kelvin(self):
        if self.unit_awal == "C":
            return self.suhu + 273
        elif self.unit_awal == "F":
            return 5/9 * (self.suhu - 32) + 273
        elif self.unit_awal == "R":
            return self.suhu + 273
        elif self.unit_awal == "K":
            return self.suhu

    def tampilkan_hasil(self):
        print(f"{self.val} {self.unit_awal} sama dengan:")
        print(f"{self.to_fahrenheit():.2f} Fahrenheit")
        print(f"{self.to_reamur():.2f} Reamur")
        print(f"{self.to_kelvin():.2f} Kelvin")


def main():
    print("Konversi Suhu")

    # Input suhu dan unit
    suhu_input = float(input("Masukkan suhu: "))
    unit_input = input("Masukkan unit suhu (C/F/R/K): ").upper()

    # Membuat objek KonversiSuhu
    konversi_objek = KonversiSuhu(suhu_input, unit_input)

    # Menampilkan hasil konversi
    konversi_objek.tampilkan_hasil()

if __name__ == "__main__":
    main()
