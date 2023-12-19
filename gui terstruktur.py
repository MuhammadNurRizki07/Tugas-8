import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    suhu = float(entry_suhu.get())
    unit_awal = combo_unit.get()

    fahrenheit = None
    reamur = None
    kelvin = None

    if unit_awal == "Celcius":
        fahrenheit = (9/5 * suhu) + 32
        reamur = 4/5 * suhu
        kelvin = suhu + 273
    elif unit_awal == "Fahrenheit":
        suhu_celcius = (suhu - 32) * 5/9
        fahrenheit = suhu
        reamur = 4/5 * suhu_celcius
        kelvin = suhu_celcius + 273
    elif unit_awal == "Reamur":
        suhu_celcius = 5/4 * suhu
        fahrenheit = (9/5 * suhu_celcius) + 32
        reamur = suhu
        kelvin = suhu_celcius + 273
    elif unit_awal == "Kelvin":
        suhu_celcius = suhu - 273
        fahrenheit = (9/5 * suhu_celcius) + 32
        reamur = 4/5 * suhu_celcius
        kelvin = suhu

    result_label.config(text=f"{suhu:.2f} {unit_awal} sama dengan:\n"
                             f"{fahrenheit:.2f} Fahrenheit\n"
                             f"{reamur:.2f} Reamur\n"
                             f"{kelvin:.2f} Kelvin")

# Membuat GUI
root = tk.Tk()
root.title("Konversi Suhu")

# Label dan Entry untuk input suhu
label_suhu = tk.Label(root, text="Masukkan suhu:")
label_suhu.grid(row=0, column=0, padx=10, pady=10, sticky="E")

entry_suhu = tk.Entry(root)
entry_suhu.grid(row=0, column=1, padx=10, pady=10)

# Combobox untuk memilih unit suhu
label_unit = tk.Label(root, text="Pilih unit suhu:")
label_unit.grid(row=1, column=0, padx=10, pady=10, sticky="E")

unit_options = ["Celcius", "Fahrenheit", "Reamur", "Kelvin"]
combo_unit = ttk.Combobox(root, values=unit_options)
combo_unit.set("Celcius")
combo_unit.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk konversi
konversi_button = tk.Button(root, text="Konversi", command=konversi_suhu)
konversi_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label untuk menampilkan hasil konversi
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Menjalankan loop GUI
root.mainloop()
