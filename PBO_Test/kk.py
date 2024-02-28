import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        temperature = float(entry.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            result.set(f"{temperature} Celsius = {celsius_to_fahrenheit(temperature):.2f} Fahrenheit")
        elif var.get() == 2:  # Fahrenheit to Celsius
            result.set(f"{temperature} Fahrenheit = {fahrenheit_to_celsius(temperature):.2f} Celsius")
        else:
            result.set("Pilih jenis konversi")
    except ValueError:
        result.set("Masukkan suhu yang valid")

# Membuat GUI
app = tk.Tk()
app.title("Konversi Suhu")

# Label dan Entry untuk input suhu
tk.Label(app, text="Masukkan suhu:").pack(pady=10)
entry = tk.Entry(app)
entry.pack(pady=10)

# Radiobutton untuk memilih jenis konversi
var = tk.IntVar()
var.set(0)
tk.Radiobutton(app, text="Celsius to Fahrenheit", variable=var, value=1).pack()
tk.Radiobutton(app, text="Fahrenheit to Celsius", variable=var, value=2).pack()

# Tombol konversi
tk.Button(app, text="Konversi", command=convert_temperature).pack(pady=10)

# Label untuk menampilkan hasil konversi
result = tk.StringVar()
tk.Label(app, textvariable=result).pack(pady=10)

# Menjalankan aplikasi
app.mainloop()
