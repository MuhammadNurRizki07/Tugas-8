print("Konversi Suhu")

suhu = float(input("Masukkan suhu: "))
unit_awal = input("Masukkan unit suhu (C/F/R/K): ").upper()

fahrenheit = None
reamur = None
kelvin = None

if unit_awal == "C":
        fahrenheit = (9/5 * suhu) + 32
        reamur = 4/5 * suhu
        kelvin = suhu + 273
elif unit_awal == "F":
        suhu_celcius = (suhu - 32) * 5/9
        fahrenheit = suhu
        reamur = 4/5 * suhu_celcius
        kelvin = suhu_celcius + 273
elif unit_awal == "R":
        suhu_celcius = 5/4 * suhu
        fahrenheit = (9/5 * suhu_celcius) + 32
        reamur = suhu
        kelvin = suhu_celcius + 273
elif unit_awal == "K":
        suhu_celcius = suhu - 273
        fahrenheit = (9/5 * suhu_celcius) + 32
        reamur = 4/5 * suhu_celcius
        kelvin = suhu

print(f"{suhu} {unit_awal} sama dengan:")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{reamur:.2f} Reamur")
print(f"{kelvin:.2f} Kelvin")

()
