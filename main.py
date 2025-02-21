import math
import cmath  # Untuk bilangan kompleks
import os
from tabulate import tabulate  # Untuk tampilan riwayat lebih rapi

# File untuk menyimpan riwayat perhitungan
RIWAYAT_FILE = "riwayat_perhitungan.txt"


# Fungsi operasi matematika
def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    return a / b if b != 0 else "Error: Pembagian dengan nol tidak diperbolehkan"


def modulus(a, b):
    return a % b


def pangkat(a, b):
    return a**b


def akar(a):
    return math.sqrt(a) if a >= 0 else cmath.sqrt(
        a)  # Support bilangan kompleks


def sin_rad(a):
    return math.sin(math.radians(a))


def cos_rad(a):
    return math.cos(math.radians(a))


def tan_rad(a):
    return math.tan(math.radians(a))


def log(a):
    return math.log10(
        a
    ) if a > 0 else "Error: Log tidak terdefinisi untuk nilai negatif atau nol"


def derajat_ke_radian(a):
    return math.radians(a)


def radian_ke_derajat(a):
    return math.degrees(a)


# Fungsi input validasi angka
def get_number(prompt, allow_complex=False):
    while True:
        try:
            user_input = input(prompt).strip()
            if allow_complex and 'j' in user_input:
                return complex(user_input)  # Bilangan kompleks
            return float(user_input)
        except ValueError:
            print("Input tidak valid! Harap masukkan angka yang benar.")


# Fungsi menampilkan menu
def tampilkan_menu():
    print("\n===== KALKULATOR LENGKAP =====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Modulus")
    print("6. Pangkat")
    print("7. Akar Kuadrat")
    print("8. Trigonometri (sin, cos, tan)")
    print("9. Logaritma")
    print("10. Konversi Satuan (Derajat <-> Radian)")
    print("11. Lihat Riwayat Perhitungan")
    print("12. Reset Riwayat")
    print("13. Keluar")
    print("================================")


# Fungsi menyimpan dan membaca riwayat
def simpan_riwayat(riwayat):
    with open(RIWAYAT_FILE, "w") as file:
        for item in riwayat:
            file.write(item + "\n")


def baca_riwayat():
    if os.path.exists(RIWAYAT_FILE):
        with open(RIWAYAT_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


riwayat = baca_riwayat()

print("🎉 Selamat datang di Kalkulator Lengkap!")

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan (1-13): ").strip()

    if pilihan == "13":
        print("Terima kasih telah menggunakan kalkulator ini! 😊")
        simpan_riwayat(riwayat)
        break
    elif pilihan in ("1", "2", "3", "4", "5", "6"):
        angka1 = get_number("Masukkan angka pertama: ")
        angka2 = get_number("Masukkan angka kedua: ")
        operasi = {
            "1": ("Penjumlahan", tambah),
            "2": ("Pengurangan", kurang),
            "3": ("Perkalian", kali),
            "4": ("Pembagian", bagi),
            "5": ("Modulus", modulus),
            "6": ("Pangkat", pangkat),
        }
        nama_operasi, fungsi = operasi[pilihan]
        hasil = fungsi(angka1, angka2)
        riwayat.append(f"{nama_operasi}: {angka1} dan {angka2} = {hasil}")
        print(f"✅ Hasil {nama_operasi.lower()}: {hasil}")
    elif pilihan == "7":
        angka = get_number("Masukkan angka: ", allow_complex=True)
        hasil = akar(angka)
        riwayat.append(f"Akar Kuadrat: {angka} = {hasil}")
        print(f"✅ Hasil akar kuadrat: {hasil}")
    elif pilihan == "8":
        angka = get_number("Masukkan sudut (derajat): ")
        print(f"Sin({angka}) = {sin_rad(angka)}")
        print(f"Cos({angka}) = {cos_rad(angka)}")
        print(f"Tan({angka}) = {tan_rad(angka)}")
        riwayat.append(
            f"Trigonometri: sin({angka}) = {sin_rad(angka)}, cos({angka}) = {cos_rad(angka)}, tan({angka}) = {tan_rad(angka)}"
        )
    elif pilihan == "9":
        angka = get_number("Masukkan angka untuk logaritma: ")
        hasil = log(angka)
        riwayat.append(f"Logaritma: log({angka}) = {hasil}")
        print(f"✅ Hasil log: {hasil}")
    elif pilihan == "10":
        angka = get_number("Masukkan nilai: ")
        print(f"{angka} derajat = {derajat_ke_radian(angka)} radian")
        print(f"{angka} radian = {radian_ke_derajat(angka)} derajat")
        riwayat.append(
            f"Konversi: {angka}° = {derajat_ke_radian(angka)} rad, {angka} rad = {radian_ke_derajat(angka)}°"
        )
    elif pilihan == "11":
        if riwayat:
            print("\n===== Riwayat Perhitungan =====")
            print(
                tabulate([[i + 1, item] for i, item in enumerate(riwayat)],
                         headers=["No", "Perhitungan"],
                         tablefmt="grid"))
        else:
            print("⛔ Riwayat masih kosong.")
    elif pilihan == "12":
        if input("Yakin ingin menghapus riwayat? (y/n): ").strip().lower(
        ) == "y":
            riwayat.clear()
            if os.path.exists(RIWAYAT_FILE):
                os.remove(RIWAYAT_FILE)
            print("✅ Riwayat telah dihapus.")
    else:
        print("⚠️ Pilihan tidak valid! Silakan pilih lagi.")
