"Program Manajemen Kontak"

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["Email"]})')
    else:
        print("Kontak masi kosong!")
        return 1

def menambah_kontak():
    # Menambah Kontak
    nama = input("Masukkan nama kontak yang baru: ")
    HP = input("Masukkan nomor kontak yang baru: ")
    email = input("Masukkan email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'Email': email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan!")

def menghapus_kontak():
    # Menghapus Kontak

    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah dihapus!")


kontak1 = {'nama' : 'Angga', 'HP': '08933243', 'Email' : 'angga@gmaiil.com'}
kontak2 = {'nama' : 'rudi', 'HP': '03433defe', 'Email' : 'rudi@gmaiil.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari kontak")

    pilihan = input("Masukkan pilihan menu kontak (1,2,3,4): ")

    if pilihan == '1':
        # melihat semua kontak
        melihat_kontak()


    elif pilihan == '2':
        # Menambah Kontak
        menambah_kontak()

    elif pilihan == '3':
        # Menghapus Kontak
        menghapus_kontak()



    elif pilihan == '4':
        # Keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah")