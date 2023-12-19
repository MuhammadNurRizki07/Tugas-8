import tkinter as tk
from tkinter import ttk

class KonversiSuhuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")

        self.suhu_var = tk.DoubleVar()
        self.unit_awal_var = tk.StringVar(value="")

        self.buat_gui()

    def buat_gui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Masukkan suhu:").grid(column=0, row=0, sticky=tk.W)
        suhu_entry = ttk.Entry(frame, textvariable=self.suhu_var)
        suhu_entry.grid(column=1, row=0)

        ttk.Label(frame, text="Pilih unit konversi:").grid(column=0, row=1, sticky=tk.W)
        unit_combobox = ttk.Combobox(frame, textvariable=self.unit_awal_var, values=["Celcius", "Fahrenheit", "Reamur", "Kelvin"])
        unit_combobox.grid(column=1, row=1)

        hasil_label = ttk.Label(frame, text="")
        hasil_label.grid(column=0, row=2, columnspan=2)

        ttk.Button(frame, text="Konversi", command=self.tampilkan_hasil).grid(column=0, row=3, columnspan=2)

        self.hasil_label = hasil_label

    def to_fahrenheit(self):
        if self.unit_awal_var.get() == "Celcius":
            return (9/5 * self.suhu_var.get()) + 32
        elif self.unit_awal_var.get() == "Fahrenheit":
            return self.suhu_var.get()
        elif self.unit_awal_var.get() == "Reamur":
            return (9/5 * self.suhu_var.get()) + 32
        elif self.unit_awal_var.get() == "Kelvin":
            return (9/5 * (self.suhu_var.get() - 273)) + 32

    def to_reamur(self):
        if self.unit_awal_var.get() == "Celcius":
            return 4/5 * self.suhu_var.get()
        elif self.unit_awal_var.get() == "Fahrenheit":
            return 4/9 * (self.suhu_var.get() - 32)
        elif self.unit_awal_var.get() == "Reamur":
            return self.suhu_var.get()
        elif self.unit_awal_var.get() == "Kelvin":
            return 4/5 * (self.suhu_var.get() - 273)

    def to_kelvin(self):
        if self.unit_awal_var.get() == "Celcius":
            return self.suhu_var.get() + 273
        elif self.unit_awal_var.get() == "Fahrenheit":
            return 5/9 * (self.suhu_var.get() - 32) + 273
        elif self.unit_awal_var.get() == "Reamur":
            return self.suhu_var.get() + 273
        elif self.unit_awal_var.get() == "Kelvin":
            return self.suhu_var.get()

    def tampilkan_hasil(self):
        hasil = f"{self.suhu_var.get()} {self.unit_awal_var.get()} sama dengan:\n"
        hasil += f"{self.to_fahrenheit():.2f} Fahrenheit\n"
        hasil += f"{self.to_reamur():.2f} Reamur\n"
        hasil += f"{self.to_kelvin():.2f} Kelvin"
        self.hasil_label.config(text=hasil)

def main():
    root = tk.Tk()
    app = KonversiSuhuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
