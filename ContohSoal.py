while True:
    print("=============================")
    nama = input("Masukkan Nama Anda: ")
    usia = int(input("Masukkan Usia Anda: "))
    kd_paket = input("Masukkan Kode Paket (D/G/S): ").upper()
    jumlah_tahun = int(input("Jumlah Tahun Pembayaran: "))
    print("==============================")

    # proses
    if kd_paket == 'D':
        paket = "Diamond"
        if 5 <= usia <= 15:
            harga = 3000000
        elif 16 <= usia <= 40:
            harga = 4000000
        elif usia > 40:
            harga = 7000000
        else:
            harga = 0
    elif kd_paket == 'G':
        paket = "Gold"
        if 5 <= usia <= 15:
            harga = 2000000
        elif 16 <= usia <= 40:
            harga = 3000000
        elif usia > 40:
            harga = 6000000
        else:
            harga = 0
    elif kd_paket == 'S':
        paket = "Silver"
        if 5 <= usia <= 15:
            harga = 1000000
        elif 16 <= usia <= 40:
            harga = 2000000
        elif usia > 40:
            harga = 3000000
        else:
            harga = 0
    else:
        paket = "Tidak valid"
        harga = 0

    biaya = jumlah_tahun * harga

    if biaya >= 15000000 and biaya < 30000000:
        diskon = biaya * 0.2
    elif biaya >= 30000000:
        diskon = biaya * 0.3
    else:
        diskon = 0

    total_bayar = biaya - diskon

    print(f"Anda Terdaftar Pada Paket {paket}")
    print(f"Jumlah Biaya yang Dibayar Rp.{biaya}")
    print(f"Potongan Pembayaran Sebesar Rp.{diskon}")
    print(f"Total Bayar Rp.{total_bayar}")

    jawab = input("Apakah anda ingin mengulang program (Y/T): ").upper()
    if jawab != 'Y':
        break
print("Thank You")
