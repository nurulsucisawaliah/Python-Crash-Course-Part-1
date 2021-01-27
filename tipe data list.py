print('='*20,'Tipe data skalar','='*20)
uci = 'ukuran L'
nining = 'ukuran m'
mama = 'ukuran s'
papa = 'ukuran j'

print('baju uci', uci)
print('baju nining', nining)
print('baju mama', mama)
print('baju mama', papa)
print('-'* 20)

print('='*20,'Tipe data list','='*20)

print('\nTipe data list/daftar/array')
    # Bentuk pertama
ukuran = []
ukuran.append('L')
ukuran.append('M')
ukuran.append('S')
ukuran.append('J')
print(ukuran)
    # Bentuk kedua
    # mendefinisikan tipe data list dengan menggunakan kurung siku"[]""
ukuran = ['L', 'M', 'S', 'J']
print(ukuran)
print('-'* 20)

print('\nPerulangan pada tipe data list menggunakan for loop')
print('\nDaftar ukuran baju ditoko sadar:')
for x in ukuran:
    print(f'tersedia ukuran {x}')

print('\ncara ribet for loop')
print('\nDaftar ukuran baju ditoko mekar :')
for u in range(0, len(ukuran)):
    print(f'{u +1}, tersedia ukuran {ukuran [u]}')