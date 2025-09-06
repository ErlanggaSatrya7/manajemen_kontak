"Program Manajemen Kontak"
import kontak
def main:
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

    # kontak1 = {'nama' : 'Angga', 'HP': '08933243', 'Email' : 'angga@gmaiil.com'}
    # kontak2 = {'nama' : 'rudi', 'HP': '03433defe', 'Email' : 'rudi@gmaiil.com'}
    # kontak = [kontak1, kontak2]

    while True:
        print("\nMenu Kontak")
        print("1. Melihat Semua Kontak")
        print("2. Menambahkan Kontak Baru")
        print("3. Menghapus Kontak")
        print("4. Keluar dari kontak")

        pilihan = input("Masukkan pilihan menu kontak (1,2,3,4): ")

        if pilihan == '1':
            # melihat semua kontak

            kontak_keluarga.melihat_kontak()


        elif pilihan == '2':
            # Menambah Kontak

            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            # Menghapus Kontak

            kontak_keluarga.menghapus_kontak()


        elif pilihan == '4':
            # Keluar dari kontak
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("Anda memasukkan pilihan yang salah")

if __name__ == "__main__":
    main()