import random

terendah = 0
tertinggi = 100
jawaban = random.randint(terendah, tertinggi)
tebakan = 0
berjalan = True

while berjalan:
    tebak = input(f"Masukkan angka antara {terendah} hingga {tertinggi}: ")

    if tebak.isdigit():
        tebak = int(tebak)
        tebakan += 1
        if tebak < terendah or tebak > tertinggi:
            print("Angka Diluar Batas")
        elif tebak > jawaban:
            print("Angka Tebakan Terlalu Tinggi")
        elif tebak < jawaban:
            print("Angka Tebakan Terlalu Rendah")
        else:
            print(f"Tebakan Kamu benar. {jawaban} adalah angka yang sama")
            berjalan = False
    else:
        print("Hanya Angka")
        print(f"Masukkan angka antara {terendah} hingga {tertinggi}")
