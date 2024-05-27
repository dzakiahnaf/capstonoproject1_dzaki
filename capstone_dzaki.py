#  untuk menyimpan informasi kontak
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

# untuk mengelola buku telepon
class PhoneBook:
    def __init__(self):
        self.contacts = []

    # Fungsi untuk menambahkan kontak baru
    def create_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Kontak {name} berhasil ditambahkan.")

    # Fungsi untuk menampilkan semua kontak atau kontak tertentu
    def read_contacts(self, name=None):
        if name:
            found = False
            for contact in self.contacts:
                if contact.name.lower() == name.lower():
                    print(f"Nama: {contact.name}, No. Telepon: {contact.phone}, Email: {contact.email}")
                    found = True
            if not found:
                print(f"Kontak dengan nama {name} tidak ditemukan.")
        else:
            if not self.contacts:
                print("Tidak ada kontak yang disimpan.")
            else:
                print("Daftar Kontak:")
                for contact in self.contacts:
                    print(f"Nama: {contact.name}, No. Telepon: {contact.phone}, Email: {contact.email}")

    # Fungsi untuk memperbarui informasi kontak
    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print(f"Kontak {name} berhasil diperbarui.")
                return
        print(f"Kontak dengan nama {name} tidak ditemukan.")

    # Fungsi untuk menghapus kontak
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Kontak {name} berhasil dihapus.")
                return
        print(f"Kontak dengan nama {name} tidak ditemukan.")

# Fungsi utama untuk mengintegrasikan semua fitur
def main():
    phonebook = PhoneBook()
    while True:
        print("\n====================Menu Kontak Telefon====================")
        print("1. Tambah Kontak")
        print("2. Tampilkan Kontak")
        print("3. Perbarui Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar program")
        print("=============================================================")
        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == '1':
            name = input("Masukkan nama: ")
            phone = input("Masukkan no. telepon: ")
            email = input("Masukkan email: ")
            phonebook.create_contact(name, phone, email)
        elif choice == '2':
            sub_choice = input("Tampilkan semua kontak atau kontak tertentu? (all/name): ").lower()
            if sub_choice == 'name':
                name = input("Masukkan nama kontak yang ingin ditampilkan: ")
                phonebook.read_contacts(name)
            else:
                phonebook.read_contacts()
        elif choice == '3':
            name = input("Masukkan nama kontak yang ingin diperbarui: ")
            new_phone = input("Masukkan no. telepon baru (kosongkan jika tidak ingin mengubah): ")
            new_email = input("Masukkan email baru (kosongkan jika tidak ingin mengubah): ")
            phonebook.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '4':
            name = input("Masukkan nama kontak yang ingin dihapus: ")
            phonebook.delete_contact(name)
        elif choice == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()


   