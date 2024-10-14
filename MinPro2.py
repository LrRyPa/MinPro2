import random
from prettytable import PrettyTable

skor_user = {}

"""
nama admin: larry
ID admin  : 026
"""

def login_admin(admin, no_admin):
    if admin == "larry" and no_admin == "026":
        return True
    else:
        return False

def data_user():
    table = PrettyTable()
    table.field_names = ["  Username  ", "Skor"]
    for username, skor_list in skor_user.items():
        total_skor = sum(skor_list)
        table.add_row([username, total_skor])
    print("\n=======DATA USER=======")
    print(table)
    print("=======================")
    return  

def tambah_user():
    while True:
        username = input("\nMasukkan username baru: ")
        if username in skor_user:
            print(f"User {username} sudah ada\n")
            return
        else:
            try:
                skor = int(input("Masukkan skor user: "))
                skor_user[username] = [skor]
                print(f"User {username} berhasil ditambahkan, dengan skor {skor}!\n")
                break
            except ValueError:
                print("Skor harus berupa angka!")

def ubah_user():
    data_user()
    username = input("\nMasukkan username yang ingin anda ubah: ")
    username_baru = input("Masukkan username baru: ")

    if username in skor_user:
        skor_user[username_baru] = skor_user.pop(username)
        print(f"Username telah berubah dari {username} menjadi {username_baru}\n")
    else:
        print(f"Username {username} tidak ditemukan.\n")
    return 

def hapus_user():
    data_user()
    username = input("\nMasukkan username yang ingin dihapus: ")

    if username in skor_user:
        del skor_user[username]
        print(f"Username {username} berhasil dihapus!\n")
    else:
        print(f"Username {username} tidak ditemukan!\n")
    return 

def menu_admin():
    while True:
        table_admin = PrettyTable()
        table_admin.field_names = ["Menu Admin"]
        table_admin.add_rows(
            [
                ["1. Tambah user   "],
                ["2. Lihat skor user"],
                ["3. Ubah nama user"],
                ["4. Delete user    "],
                ["5. Keluar         "],
            ]
        )
        print(table_admin)
        pilih_menu = int(input("Pilih menu: "))
        try:
            if pilih_menu == 1:
                tambah_user()
            elif pilih_menu == 2:
                data_user()
            elif pilih_menu == 3:
                ubah_user()
            elif pilih_menu == 4:
                hapus_user()
            elif pilih_menu == 5:
                print("Anda telah log out dari role Admin!\n")
                return
            else:
                print("\nMaaf pilihan tidak tersedia, silahkan pilih kembali")
        except ValueError:
            print("\ninput harus berupa angka, silahkan memilih kembali")


def get_range():
    min_value = 1
    max_value = 100
    return min_value, max_value

def game(username):
    min_value, max_value = get_range()
    angka_random = random.randint(min_value, max_value)
    percobaan = 0

    if username not in skor_user:
        skor_user[username] = []

    while True:
        try:
            tebakan = int(input("Tebak angka antara {} dan {}: ".format(min_value, max_value)))
            percobaan += 1
            if tebakan < angka_random:
                print("Terlalu rendah!")
            elif tebakan > angka_random:
                print("Terlalu tinggi!")
            else:
                skor = 100 - (percobaan * 5)
                print(f"Selamat {username}, tebakan anda benar! Anda menebak sebanyak {percobaan} kali, dengan skor {skor}!\n")
                skor_user[username].append(skor)
                break
        except ValueError:
            print("\nInput harus berupa angka, Silahkan dicoba kembali")
    return

def main():
    while True:
        print("=====Selamat datang=====")
        table = PrettyTable()
        table.field_names = ["        LOGIN       "]
        table.add_rows(
            [
            ["1. User"],
            ["2. Admin"],
            [" 3. Keluar"],
            ]
        )
        
        print(table)
        try:
            pilih = int(input("Silahkan login: "))
            if pilih == 1:
                username = input("\nMasukkan username anda: ")
                game(username)
            elif pilih == 2:
                admin = input("\nMasukkan nama anda: ")
                no_admin = input("Masukkan no anda: ")
                if login_admin(admin, no_admin):
                    print(f"\nSelamat datang kembali {admin}!")
                    menu_admin()
                else:
                    print("Maaf nama atau nomor anda salah!\n")
            elif pilih == 3:
                print("Silahkan datang kembali di lain waktu!")
                break
            else:
                print("Pilihan tidak tersedia")
                print("Silahkan memilih kembali!\n")
        except ValueError:
            print("Input harus berupa angka")
            break

if __name__ == "__main__":
    main()