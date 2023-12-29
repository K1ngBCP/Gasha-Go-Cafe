import json
import time
import os
import csv

def clean():
    os.system('cls')

#### Login Customer
def readJson():
    try:
        with open("Database1.json", 'r') as output:
            Data = json.load(output)
            return Data
    except FileNotFoundError:
        data_kosong = []
        with open("Database1.json", 'w') as output:
            json.dump(data_kosong, output, indent=4)
            return data_kosong
        
def writeJson(Data):
    with open("Database1.json", 'w') as output:
        json.dump(Data,output, indent=4)

def Daftar() :
    clean()
    Username = input("Masukkan nama: ")
    Password = input ("Masukkan Password: ")
    Password_K = input ("Konfirmasi Password: ")
    Datbes = readJson()

    for row in Datbes:
            if row["Username"] == Username:
                print("Username telah dipakai, silahkan pilih ulang: ")
                time.sleep(2)
                Daftar()

    if Password != Password_K :
        print ("Password Salah, Silahkan masukkan ulang: ")
        time.sleep(2)
        Daftar ()
    elif len(Password)<=5 :
        print ("Password terlalu pendek, Mohon dirubah: ")
        time.sleep(2)
        Daftar()     
    else:
        data_baru = {
        "Username" : Username,
        "Password" : Password}
        Datbes.append(data_baru)
        writeJson(Datbes)
        print ("""
        Selamat akun anda telah tersimpan
        Silahkan masuk kembali""")
        time.sleep(2)
        Masuk()
    
def Masuk():
    clean()
    Username = input("Masukkan nama: ")
    Password = input ("Masukkan Password: ")
    Datbes = readJson()
    
    BagasGanteng = False
    if len(Datbes) != 0:
        for row in Datbes:
            if row["Username"] == Username and row["Password"] == Password:
                BagasGanteng = True
    else:
        print ("Username tidak tersedia, silahkan mendaftar")
        time.sleep(2)
        Daftar()
    

    if BagasGanteng :
        clean()
        print("Selamat datang, selamat beraktivitas")
        cek=int(input("""  
        1.Hapus akun 
        2.Lanjut belanja dong 
        Silahkan memilih 1/2 : """))
        if cek == 1:
            Hapus_akun()
        elif cek == 2:
            lanjut_belanja()
        else:
            print("Error ngab")
    else:
        print ("Password/Username salah, silahkan masukan ulang")
        time.sleep(2)
        Masuk()


def Hapus_akun():
    clean()
    Username = input("Masukkan nama: ")
    Password = input ("Masukkan Password: ")
    Datbes = readJson()
    
    BagasTampan = False
    for row in Datbes:
            if row["Username"] == Username and row["Password"] == Password:
                BagasTampan = True

    if BagasTampan :
        hapus = {
            "Username" : Username,
            "Password" : Password}
        Datbes.remove(hapus)
        writeJson(Datbes)
        print ("""Akun anda telah terhapus, silahkan cek di menu awal""")
        Customer()
    else:
        print("Username tidak tersedia, silahkan masukkan ulang: ")
        time.sleep(2)
        Hapus_akun()

##### Menu Admin
def readcsv():
    try:
        hasil = []
        with open("Database2.csv", 'r') as Bagas:
            Data = csv.DictReader(Bagas)
            for row in Data:
                hasil.append(row)
            return hasil
    except FileNotFoundError:
        data_kosong = []
        with open("Database2.csv", 'w') as Bagas:
            csv.DictWriter(data_kosong, Bagas, indent=4)
            return data_kosong
        
def Tambah_Barang():
    clean()
    with open("Database2.csv", mode ='a',newline='') as Bagas:
        fieldnames = ['kode','Nama','Harga', 'Jumlah']
        writer = csv.DictWriter(Bagas, fieldnames = fieldnames)
        print('='*61)
        print('='*24+'Tambah Barang'+'='*24)
        print('='*61)

        kode = input("kode: ")
        Nama = input("Nama Barang: ")
        Harga = input("Harga: ")
        Jumlah = input("Jumlah: ")

        print('='*60)

        writer.writerow({'kode': kode,'Nama':Nama,'Harga':Harga,'Jumlah':Jumlah})
    
    print("""
    Data Telah berhasil ditambahkan 
    Silahkan ke Menu awal Untuk Mengecek""")
    time.sleep(2)
    MenuAdmin()


def Lihat_Barang():
    clean()
    Cahyo=readcsv()
    Count = len(Cahyo)

    print("-"*57)
    print("\t\tStock Barang Di GaSha GoCafe")
    print("-"*57)

    print("|Kode \t\tNama\t\tHargaa\t\tJumlah \t|")
    print("-"*57)

    for data in Cahyo:
        print(f"| {data['kode']} \t\t{data['Nama']}    \t{data['Harga']}   \t{data['Jumlah']}\t|")
    print("-"*57)
    print("Total Data: ",Count)
    print("-"*57)

    ABC = int(input("Tekan 0 untuk kembali ke menu awal: "))
    if ABC == 0:
        MenuAdmin()
    else:
        print("Error")
        time.sleep(2)
        Lihat_Barang()

def Hapus_Barang():
    clean()
    Purnomo=readcsv()
    print("-"*57)
    print("\t\tStock Barang Di GaSha GoCafe")
    print("-"*57)

    print("|Kode \t\tNama\t\tHargaa\t\tJumlah \t|")
    print("-"*57)

    for data in Purnomo:
        print(f"| {data['kode']} \t\t{data['Nama']}    \t{data['Harga']}   \t{data['Jumlah']}\t|")
    print("-"*57)
    kode= input("Masukkan kode barang yang akan dihapus: ")

    indeks = 0
    for data in Purnomo:
        if(data["kode"]== kode):
            Purnomo.remove(Purnomo[indeks])
        indeks +=1

    with open("Database2.csv", mode ='w') as Bagas:
        fieldnames = ['kode','Nama','Harga', 'Jumlah']
        writer = csv.DictWriter(Bagas, fieldnames = fieldnames)
        writer.writeheader()
        for new in Purnomo:
            writer.writerow({'kode': new['kode'],'Nama':new['Nama'],'Harga':new['Harga'],'Jumlah':new['Jumlah']})
    
    print("""
    Data Telah Terhapus 
    Silahkan ke Menu awal Untuk Mengecek""")
    time.sleep(2)
    MenuAdmin()


def Edit_Barang():
    clean()
    Bagas2=readcsv()
    Count = len(Bagas2)
    print("-"*57)
    print("\t\tStock Barang Di GaSha GoCafe")
    print("-"*57)
    print("|Kode \t\tNama\t\tHargaa\t\tJumlah \t|")
    print("-"*57)

    for data in Bagas2:
        print(f"| {data['kode']} \t\t{data['Nama']}    \t{data['Harga']}   \t{data['Jumlah']}\t|")
    print("-"*57)
    print("Total Data: ",Count)
    print("-"*57)
    kode = input("kode: ")
    Nama = input("Nama Barang: ")
    Harga = input("Harga: ")
    Jumlah = input("Jumlah: ")
    indeks = 0
    for data in Bagas2:
        if(data["kode"]== kode):
            Bagas2[indeks]['Nama']= Nama
            Bagas2[indeks]['Harga']= Harga
            Bagas2[indeks]['Jumlah']= Jumlah
        indeks +=1
    with open("Database2.csv", mode ='w') as Bagas:
        fieldnames = ['kode','Nama','Harga', 'Jumlah']
        writer = csv.DictWriter(Bagas, fieldnames = fieldnames)
        writer.writeheader()
        for new in Bagas2:
            writer.writerow({'kode': new['kode'],'Nama':new['Nama'],'Harga':new['Harga'],'Jumlah':new['Jumlah']})
    print("Data telah terproses, silahkan ke menu awal untuk mengecek")
    time.sleep(3)
    MenuAdmin()

def Cari_Barang():
    clean()
    print("Cari Barangberdasarkan kode!")
    CB=input("Masukkan Kode: ")
    clean()
    Bagas3 = readcsv()

    Ketemu=[]
    indeks = 0
    for A in Bagas3:
        if (A['kode']==CB):
            Ketemu = Bagas3[indeks]
        indeks +=1

    if len(Ketemu)>0:
        print("Data Telah Ditemukan")
        print(f"Nama: {Ketemu['Nama']}")
        print(f"Harga: {Ketemu['Harga']}")
        print(f"Jumlah: {Ketemu['Jumlah']}")
    else:
        print("Data Anda tidak tersedia")

    Aku = int(input("Tekan 0 untuk kembali ke menu: "))
    if Aku == 0:
        MenuAdmin()
    else:
        print("Error")


def Keluar():
    clean()
    print("Sampai Jumpa "+Id)  


#### Menu Awal Banget
def Customer():
    clean()
    Bagas=int(input(""" 
    1. Masuk 
    2. Daftar 
    pilih [1, 2] : """))
    if Bagas == 1:
        Masuk()
    elif Bagas == 2:
        Daftar()
    else :
        print("Error!!!")

#Admin
def Admin():
    clean()
    Username = input("Masukkan nama: ")
    Password = input ("Masukkan Password: ")
    if Username == "admin" and Password == "admin":
        MenuAdmin()
    else:
        print("Username atau Password salah, silahkan masukkan ulang!")
        Admin()

def MenuAdmin():
    clean()
    print("Selamat datang "+ Id)
    Bagas=int(input(""" 
    Silahkan pilih [1, 2, 3, 4, 5, 6] :
    1. Lihat Barang 
    2. Tambah Barang 
    3. Hapus Barang
    4. Edit Barang
    5. Cari Barang
    6. Keluar 
    Pilihan Anda : """))
    if Bagas == 1:
        Lihat_Barang()
    elif Bagas == 2:
        Tambah_Barang()
    elif Bagas == 3:
        Hapus_Barang() 
    elif Bagas == 4:
        Edit_Barang()
    elif Bagas == 5:
        Cari_Barang()
    elif Bagas == 6:
        Keluar()
    else :
        print("Error!!!")

#### Awal
clean()
Id = input("Selamat datang di GaSha Gocafe, Masukkan Nama anda: ")
def Awal():
    clean()
    print("Selamat datang "+ Id)
    Bagas=int(input(""" 
    Silahkan pilih [1, 2] :
    1. Admin 
    2. Customer 
    Siapakah Anda : """))
    if Bagas == 1:
        Admin()
    elif Bagas == 2:
        Customer()
    else :
        print("Error!!!")

def lanjut_belanja():
    clean()
    pesan = (int(input("""
    1. Take Away
    2. Dine In
    \nSilahkan pilih [1, 2] : """)))
    if pesan == 1:
        take_away()
    elif pesan == 2:
        dine_in()
    else:
        print("Tidak ada di pilihan!")
        time.sleep(2)
        lanjut_belanja()

def take_away():
    clean()
    putri = readcsv()
    print("="*50)
    print("="*16 , "SELAMAT BELANJA" , "="*17)
    print("="*50 + "\n")
    print("-"*50)
    print("| Kode\t\t Nama \t\tHarga  \t\t |")
    print("-"*50)
    for data in putri:
        print(f"|{data['kode']}  \t\t{data['Nama']}   \t{data['Harga']}     \t |")
    print("-"*50)

    print("nb: maksimal 2 jenis barang.\n")
    with open("Database3.csv", mode ='a',newline='') as dini:
        fieldnames = ['kode', 'Jumlah']
        writer = csv.DictWriter(dini, fieldnames = fieldnames)
        p = input("\nkode : ")
        s = int(input("pcs  : "))
        writer.writerow({'kode': p, 'Jumlah':s})

    for hitung in putri:
        if hitung['kode'] == p:
            harga = s*int(hitung['Harga'])
            print(harga) 
            tambah = input("ada yang ingin dipesan lagi[y/n]? : ")
            if tambah == "y":
                with open("Database3.csv", mode ='a',newline='') as dini:
                    fieldnames = ['kode', 'Jumlah']
                    writer = csv.DictWriter(dini, fieldnames = fieldnames)
                    b = input("\nkode : ")
                    g = int(input("pcs  : "))
                    writer.writerow({'kode': b, 'Jumlah':g})
                    for hitung1 in putri:
                        if hitung1['kode'] == b:
                            harga1 = g*int(hitung1['Harga'])
                            print(harga1, "\n")
                    total = harga + harga1
                    if total >= 100000:
                        total1 = total * 0.05
                        if total1 >= 15000:
                            total1 = 15000
                    elif total < 100000:
                        total1 = 0
                    
                    print("-"*41)
                    print("|{:^39}|".format("BON PEMBAYARAN"))
                    print("-"*41)

                    print("-"*41)
                    print("| Total  : Rp", total, "\t\t\t|")
                    print("| Diskon : Rp", total1, "\t\t\t|")
                    print("-"*41)
                    print("| Total Akhir : Rp", total-total1,"\t\t|")
                    print("-"*41)
                                                      
            elif tambah == "n":
                total = harga
                if total >= 100000:
                    total1 = total * 0.05
                    if total1 >= 15000:
                        total1 = 15000
                elif total < 100000:
                    total1 = 0
                
                print("-"*41)
                print("|{:^39}|".format("BON PEMBAYARAN"))
                print("-"*41)

                print("-"*41)
                print("| Total  : Rp", total, "\t\t\t|")
                print("| Diskon : Rp", total1, "\t\t\t|")
                print("-"*41)
                print("| Total Akhir : Rp", total-total1,"\t\t|")
                print("-"*41)
                
            else:
                print("ERROR. Silahkan masukan ulang")
                time.sleep(2)
                take_away()
    

def dine_in():
    clean()
    putri = readcsv()
    print("="*50)
    print("="*16 , "SELAMAT BELANJA" , "="*17)
    print("="*50 + "\n")
    print("-"*50)
    print("| Kode\t\t Nama \t\tHarga  \t\t |")
    print("-"*50)
    for data in putri:
        print(f"|{data['kode']}  \t\t{data['Nama']}   \t{data['Harga']}     \t |")
    print("-"*50)
    
    print("nb: maksimal 2 jenis barang.\n")
    with open("Database3.csv", mode ='a',newline='') as dini:
        fieldnames = ['kode', 'Jumlah']
        writer = csv.DictWriter(dini, fieldnames = fieldnames)
        p = input("\nkode : ")
        s = int(input("pcs  : "))
        writer.writerow({'kode': p, 'Jumlah':s})

    for hitung in putri:
        if hitung['kode'] == p:
            harga = s*int(hitung['Harga'])
            print(harga) 
            tambah = input("ada yang ingin dipesan lagi[y/n]? : ")
            if tambah == "y":
                with open("Database3.csv", mode ='a',newline='') as dini:
                    fieldnames = ['kode', 'Jumlah']
                    writer = csv.DictWriter(dini, fieldnames = fieldnames)
                    b = input("\nkode : ")
                    g = int(input("pcs  : "))
                    writer.writerow({'kode': b, 'Jumlah':g})
                    for hitung1 in putri:
                        if hitung1['kode'] == b:
                            harga1 = g*int(hitung1['Harga'])
                            print(harga1, "\n")
                    total = harga + harga1
                    total1 = 0
                    print("-"*41)
                    print("|{:^39}|".format("BON PEMBAYARAN"))
                    print("-"*41)

                    print("-"*41)
                    print("| Total  : Rp", total, "\t\t\t|")
                    print("| Diskon : Rp", total1, "\t\t\t|")
                    print("-"*41)
                    print("| Total Akhir : Rp", total-total1,"\t\t|")
                    print("-"*41)
            elif tambah == "n":
                total = harga 
                total1 = 0
                print("-"*41)
                print("|{:^39}|".format("BON PEMBAYARAN"))
                print("-"*41)

                print("-"*41)
                print("| Total  : Rp", total, "\t\t\t|")
                print("| Diskon : Rp", total1, "\t\t\t|")
                print("-"*41)
                print("| Total Akhir : Rp", total-total1,"\t\t|")
                print("-"*41)
            else :
                print("Pilihan yang anda masukan salah, Cobalah kemali")
                time.sleep(2)
                dine_in()

Awal()