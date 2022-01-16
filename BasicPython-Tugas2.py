Nama = ['Fawwaz', 'John']
Nomor = ['08123456789', '08987654321']

def daftar(): 
    print('Daftar kontak:')
    for i in range(len(Nama)):
        print('Nama: {}'.format(Nama[i]))
        print('No Telepon: {}'.format(Nomor[i]))


def tambah():  
    Nama.append(input('Nama: '))
    Nomor.append(input('No telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        daftar()
    elif menu == 2:
        tambah()
    elif menu == 3:
        print('Sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')