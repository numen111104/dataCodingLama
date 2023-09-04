import tkinter as tk

# Buat jendela utama
root = tk.Tk()
root.title("Kartu Ulang Tahun")

# Buat label dengan teks "Selamat Ulang Tahun"
label = tk.Label(root, text="Selamat Ulang Tahun!", font=("Helvetica", 20))
label.pack(pady=20)

# Buat gambar dengan photoimage
image = tk.PhotoImage(file="nide.png")
gambar = tk.Label(root, image=image)
gambar.pack()

# Jalankan jendela utama
root.mainloop()
