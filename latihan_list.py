jumlah = int(input("Masukkan Banyak Mahasiswa: "))

npm_list = []
nama_list = []

# Mengumpulkan data mahasiswa
for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    npm = input("Masukkan NPM  : ")
    nama = input("Masukkan Nama : ")
    npm_list.append(npm)
    nama_list.append(nama)

# Menampilkan data mahasiswa
print("\n---------------------")
print("       Results       ")
print("---------------------")

for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    print(f"NPM  : {npm_list[i]}")
    print(f"Nama : {nama_list[i]}")

print("\nTerima Kasih")
