def home():
    pass
print("              <<========== Pembelian Tiket BUS ===========>>")
print()
print("                <<========== Terminal INTR ===========>>     ")
print()
print("                  <<========== Kota Tujuan ===========>>     ")

def cetak():
    
    print("              ===============================================")

cetak()
def rute_keberangkatan():
    routes = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 200000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
        4: {"route": "Jakarta - Lampung", "price": 250000},
        5: {"route": "Jakarta - Padang", "price": 500000},
        6: {"route": "Jakarta - Bandung", "price": 150000},
    }
    print("Rute yang Tersedia: ")
    for key, value in routes.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return routes
    
def jadwal_keberangkatan(route_id):
    jadwal = {
        1: ["08:00", "12:00", "16:00"],
        2: ["09:00", "13:00", "17:00"],
        3: ["07:00", "11:00", "15:00"],
        4: ['08:15', '22:48', '04:27'],
        5: ['00:09', '17:05', '20:18'],
        6: ['03:44', '12:50', '15:00'],
    }
    print("Jadwal Tersedia: ")
    for i, schedule in enumerate(jadwal[route_id], start=1):
        print(f"{i}. {schedule}")
    return jadwal[route_id]

def data_penumpang(jumlah_tiket):
    data = []
    for i in range(jumlah_tiket):
        print(f"\nMasukkan data penumpang ke-{i+1}:")
        nama = str(input("Nama Penumpang: "))
        nik = int(input("NIK: "))
        telepon = int(input("Nomor Telepon: "))
        email = input("Alamat Email: ")
        if "@" not in email :
            raise ValueError("Email harus menggunakan '@'.")
        else:
            print("Email tidak valid!")
        data.append({
            "nama": nama,
            "nik": nik,
            "telepon": telepon,
            "email": email
        })
    return data

def pemesanan():
    routes = rute_keberangkatan()
    try:
        route_id = int(input("Pilih rute berdasarkan nomor: "))
        if route_id not in routes:
            print("Pilihan rute tidak valid.")
            return
        
        waktu_keberangkatan = jadwal_keberangkatan(route_id)
        pilih_waktu_keberangkatan = int(input("Pilih jadwal berdasarkan nomor: "))
        if pilih_waktu_keberangkatan not in range(1, len(waktu_keberangkatan)+ 1):
            print("Pilihan jadwal tidak valid.")
            return
        
        jumlah_tiket = int(input("Masukkan jumlah tiket: "))
        if jumlah_tiket <= 0:
            print("Jumlah tiket tidak valid.")
            return
        
        total = routes[route_id]["price"] * jumlah_tiket
        penumpang = data_penumpang(jumlah_tiket)

        print("\n Ringkasan pemesanan: ")
        print(f"Rute: {routes[route_id]['route']}")
        print(f"Jadwal: {waktu_keberangkatan[pilih_waktu_keberangkatan -1]}")
        print(f"Jumlah Tiket: {jumlah_tiket}")
        print(f"Total Harga: IDR {total}")
        for i, penumpang in enumerate(penumpang, start=1):
            print(f"\n Data Penumpang {i}: ")
            print(f"Nama: {penumpang['nama']}")
            print(f"NIK: {penumpang['nik']}")
            print(f"Nomor Telepon: {penumpang['telepon']}")
            print(f"Alamat Email: {penumpang['email']}")


        konfirmasi_pemesanan = input("Konfirmasi Pemesanan ? (ya/tidak): ").lower()
        if konfirmasi_pemesanan == "ya":
            print("Pemesanan anda telah di konfirmasi. Terimakasih atas pembelian Anda!!")
        elif konfirmasi_pemesanan == "tidak":
            print("Pemesanan Tiket Dibatalkan.")
        else:
            print("Maaf, Pilihan anda tidak valid")
    except ValueError:
        print("Input tidak valid silahkan coba lagi.")

if __name__ == "__main__":
    pemesanan()





    