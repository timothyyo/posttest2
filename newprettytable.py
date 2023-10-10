from prettytable import PrettyTable

admin = {'name': 'timothy', 'password': '2301', 'role': 1}
user = {'name': 'sammy', 'password': '2005', 'role': 2}

list_kendaraan = [
    {"Code": "A", "jenis kendaraan": "motor", "merek kendaraan": "honda astrea", "harga rental": 300000},
    {"Code": "B", "jenis kendaraan": "motor", "merek kendaraan": "suzuki gsx r150", "harga rental": 500000},
    {"Code": "C", "jenis kendaraan": "motor", "merek kendaraan": "honda astrea", "harga rental": 300000},
    {"Code": "D", "jenis kendaraan": "mobil", "merek kendaraan": "lamborgini huracan", "harga rental": 3000000},
    {"Code": "E", "jenis kendaraan": "mobil", "merek kendaraan": "porche gtr", "harga rental": 3200000},
    {"Code": "F", "jenis kendaraan": "mobil", "merek kendaraan": "mazda rx 8", "harga rental": 2500000},
    {"Code": "G", "jenis kendaraan": "pesawat", "merek kendaraan": "Airbus A380", "harga rental": 10000000},
    {"Code": "H", "jenis kendaraan": "pesawat", "merek kendaraan": "Air Force One", "harga rental": 100000000},
    {"Code": "I", "jenis kendaraan": "pesawat", "merek kendaraan": "Antonov An-225", "harga rental": 100000000},
    {"Code": "J", "jenis kendaraan": "kapal", "merek kendaraan": "Ocean Pearl", "harga rental": 200000000},
    {"Code": "K", "jenis kendaraan": "kapal", "merek kendaraan": "Supreme Elegance", "harga rental": 300000000},
    {"Code": "L", "jenis kendaraan": "kapal", "merek kendaraan": "Harmony of the Seas", "harga rental": 400000000},
]


# read
def show():
    tabel = PrettyTable(["Code", "jenis kendaraan", "merek kendaraan", "harga rental"])
    for produk in list_kendaraan:
        tabel.add_row([produk["Code"], produk["jenis kendaraan"], produk["merek kendaraan"], "Rp" + str(produk["harga rental"])])
    print(tabel)


# create
def create():
    code = input("Masukkan code produk baru: ")
    jeniskendaraan = input("Masukkan jenis kendaraan: ")
    merekkendaraan = input("Masukkan merek kendaraan: ")
    hargarental = int(input("Masukkan harga rental: "))
    for produkt in list_kendaraan:
        if produkt["Code"] == code:
            print("Code produk sudah digunakan.")
            return
    if hargarental <= 0:
        print("Harga produk tidak boleh negatif.")
        return
    list_kendaraan.append({"Code": code, "jenis kendaraan": jeniskendaraan, "merek kendaraan": merekkendaraan,
       "harga rental": hargarental})
    print("Produk berhasil ditambahkan.")


# update
def update():
    code = input("Masukkan Code produk yang akan diupdate: ")
    for produk in list_kendaraan:
        if produk["Code"] == code:
            produk["jenis kendaraan"] = input("Masukkan jenis kendaraan: ")
            produk["merek kendaraan"] = input("Masukkan merek kendaraan: ")
            produk["harga rental"] = int(input("Masukkan harga rental: "))
            print("Produk berhasil diupdate!")
            return
    else:
        print("Code produk tidak ditemukan.")


# delete
def delete():
    code = input("Masukkan Code produk yang akan dihapus: ")
    for produk in list_kendaraan:
        if produk["Code"] == code:
            list_kendaraan.remove(produk)
            print("Produk berhasil dihapus!")
            return
    else:
        print("Code produk tidak ditemukan.")


# transaksi
def transaksi():
    keranjang = []
    total_harga = 0

    while True:
        print("======================================================\n")
        show()
        kode = input("Masukkan Code produk yang ingin dirental (ketik 0 untuk selesai): ")

        if kode == '0':
            break

        # mencari produk berdasarkan kode
        terpilih = None
        for produk in list_kendaraan:
            if produk["Code"] == kode:
                terpilih = produk
                break

        if terpilih:
            jeniskendaraan = terpilih["jenis kendaraan"]
            harga = terpilih["harga rental"]
            jumlah = int(input(f"Masukkan jumlah {jeniskendaraan} yang ingin dirental: "))
            
            if jumlah <= 0:
                print("Jumlah produk tidak boleh negatif.")
                continue
            
            if terpilih["harga rental"] * jumlah <= int(terpilih["harga rental"]):
                terpilih["harga rental"] -= harga * jumlah
                keranjang.append({"merek kendaraan": terpilih["merek kendaraan"], "jenis kendaraan": terpilih["jenis kendaraan"], 
                "harga rental": harga, "jumlah": jumlah})
                total_harga += harga * jumlah
                print("Produk berhasil ditambahkan ke keranjang.")
            else:
                print("Stok tidak mencukupi.")
        else:
            print("Code produk tidak valid. Coba lagi.")

    print("\n======================================================")
    print("Rincian Transaksi")
    tabel_trans = PrettyTable(["jenis kendaraan", "merek kendaraan", "harga rental", "jumlah", "total harga"])
    for item in keranjang:
        nama = item["jenis kendaraan"]
        merek = item["merek kendaraan"]
        harga = item["harga rental"]
        jumlah = item["jumlah"]
        total_item = harga * jumlah
        tabel_trans.add_row([nama, merek, harga, jumlah, total_item])
    print(tabel_trans)
    print(f"Total Harga : Rp{total_harga}")
    print("======================================================")
            

# login
def login():
    while True:
        username = input("Masukkan nama: ")
        password = input("Masukkan password: ")

        if username == admin['name'] and password == admin['password']:
            user_role = admin['role']
            break
        elif username == user['name'] and password == user['password']:
            user_role = user['role']
            break
        else:
            print("Nama atau password salah.")
    return user_role


print("======================================================")
role_user = login()
print("======================================================\n")
show()

#menu admin
if role_user == 1:
    while True:
        print("1. Menambahkan produk")
        print("2. Mengupdate produk")
        print("3. Menghapus produk")
        print("4. Keluar")
        pilih = int(input("Pilih (1-4): "))
        if pilih == 1:
            create()
        elif pilih == 2:
            update()
        elif pilih == 3:
            delete()
        elif pilih == 4:
            break
        else:
            print("Pilihan tidak valid.")
        print("\n======================================================\n")

        show()

#menu user
elif role_user == 2:
    print("SELAMAT DATANG DI RENTAL KAMI", user['name'])
    while True:
        print("1. Mulai Transaksi?")
        print("2. Keluar")
        pilih = int(input("Pilih (1/2): "))

        if pilih == 1:
            transaksi()
            break
        elif pilih == 2:
            print("Terima Kasih!")
            break
        else:
            print("pilihan anda tidak valid.")