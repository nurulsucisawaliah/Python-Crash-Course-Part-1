"""
tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = key value pair
dictionary = kamus 
dictionary juga bisa diartikan sebagai penerjemah
"""

# mendefinisikan tipe data dictionary dengan kurung kurawal"{}"
print('cara 1')
kamus = {}
kamus['buku'] = 'book'
kamus['kursi'] = 'chair'
kamus['mobil'] = 'car'
kamus['meja'] = 'table'

    # menerjemahkan bahasa inggris dari kursi
print(kamus['kursi'])
    # menerjemahkan bahasa inggris dari mobil
print(kamus['mobil'])
print(f'Berikut terjehamannya : \n{kamus}')

print('\ncara 2 ; ringkas')
kamus = {'buku': 'book', 'kursi': 'chair', 'mobil': 'car', 'meja': 'table'}
print(kamus)

"""
misalnya pengguna ingin memesan gojek dengan jarak lokasi 
driver terdekat, maka yang dibutuhkan adalah "tanggal 
pemesanan, nama driver, jarak driver, dan DN motor"
"""
print('\nmengirimkan data info driver ojol ke pengguna aplikasi gojek')
data_dari_server = {
    'tanggal' : '2021-01-27',
    'driver_list':[
        {'nama':'nurul', 'jarak':100, 'DN MOTOR': 14324},
        {'nama': 'suci', 'jarak':10, 'DN MOTOR': 90001},
        {'nama': 'sawaliah', 'jarak':1000, 'DN MOTOR': 10001}]
}

print(f"driver 3 : {data_dari_server['driver_list'][2]}")
print(f"driver terdekat berjarak {data_dari_server['driver_list'][1] ['jarak']} meter")
print(f"driver terjauh berjarak {data_dari_server['driver_list'][2] ['jarak']} meter")