from browser import document, alert  # Import Library Brython 
import math

# Deklarasi Variable
input1 = document['input1']
input2 = document['input2']
input3 = document['input3']
input4 = document['input4']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

# Dictionary untuk menyimapan variabel input1, input2, input3, dan input4
# untuk memudahkan saat pemanggilan keempat variabel secara berurut
input = {'1': input1,
         '2': input2,
         '3': input3,
         '4': input4}

# Setiap bangun datar dan bangun ruang memiliki key 'Keliling' dan 'Luas' 
# yang masing-masing value-nya berisi key 'formula' dan informasi input yang diperlukan (input1, input2, input3, input4).
# Parameter x, y, atau z pada lambda formula adalah parameter yang tidak terpakai, 
# karena pada fungsi formula (dibawah) secara default diberikan empat argumen dari setiap input (input1, input2, input3, input4).

# Dictionary Bangun Datar
type1 = {'Belah Ketupat': {'Keliling': {'formula': lambda sisi, x, y, z: 4 * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                           'Luas': {'formula': lambda d1, d2, x, y: (1/2) * d1 * d2, 'input1': 'Masukkan Diameter 1', 'input2': 'Masukkan Diameter 2', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Jajar Genjang': {'Keliling': {'formula': lambda a, b, x, y: 2 * (a + b), 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                           'Luas': {'formula': lambda a, t, x, y: a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Layang-Layang': {'Keliling': {'formula': lambda a, c, x, y: 2 * (a + c), 'input1': 'Masukkan Sisi Panjang', 'input2': 'Masukkan Sisi Pendek', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                           'Luas': {'formula': lambda a, t, x, y: a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Lingkaran': {'Keliling': {'formula': lambda r, x, y, z: 2 * math.pi * r, 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                       'Luas': {'formula': lambda r, x, y, z: math.pi * (r ** 2), 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Persegi Panjang': {'Keliling': {'formula': lambda p, l, x, y: 2 * (p + l), 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                             'Luas': {'formula': lambda p, l, x, y: p * l, 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Persegi': {'Keliling': {'formula': lambda sisi, x, y, z: 4 * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                     'Luas': {'formula': lambda sisi, x, y, z: sisi * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Segitiga': {'Keliling': {'formula': lambda a, b, c, x: a + b + c, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Sisi c', 'input4': 'Kosongkan'},
                      'Luas': {'formula': lambda a, t, x, y: (1/2) * a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Trapesium': {'Keliling': {'formula': lambda a, b, c, d: a + b + c + d, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Sisi c', 'input4': 'Masukkan Sisi d'},
                       'Luas': {'formula': lambda a, b, t, y: (1/2) * (a + b) * t, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Tinggi', 'input4': 'Kosongkan'}}}

# Dictionary Bangun Ruang
type2 = {'Balok': {'Luas Permukaan': {'formula': lambda p, l, t, x: 2 * (p * l + p * t + l * t), 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Masukkan Tinggi', 'input4': 'Kosongkan'},
                   'Volume': {'formula': lambda p, l, t, x: p * l * t, 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Masukkan Tinggi', 'input4': 'Kosongkan'}},
         'Bola': {'Luas Permukaan': {'formula': lambda r, x, y, z: 4 * math.pi * (r ** 2), 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                  'Volume': {'formula': lambda r, x, y, z: (4/3) * math.pi * (r ** 3), 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Kerucut': {'Luas Permukaan': {'formula': lambda r, s, x, y: math.pi * r * (r + s), 'input1': 'Masukkan Jari-Jari', 'input2': 'Masukkan Garis Pelukis', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                     'Volume': {'formula': lambda r, t, x, y: (1/3) * math.pi * (r ** 2) * t, 'input1': 'Masukkan Jari-Jari', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Kubus': {'Luas Permukaan': {'formula': lambda sisi, x, y, z: 6 * (sisi ** 2), 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                   'Volume': {'formula': lambda sisi, x, y, z: (sisi ** 3), 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
         'Tabung': {'Luas Permukaan': {'formula': lambda r, t, x, y: 2 * math.pi * r * (r + t), 'input1': 'Masukkan Jari-Jari', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'},
                    'Volume': {'formula': lambda r, t, x, y: math.pi * (r ** 2) * t, 'input1': 'Masukkan Jari-Jari', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}}}

# Fungsi yang akan dijalankan ketika pilihan bangun datar dan ruang diubah
def selectTypeAction(ev):
    x = selectType.value
    # Reset Input Field
    for i in range(1, 5):
        input[str(i)].placeholder = 'Input ' + str(i)
        input[str(i)].value = ''
        input[str(i)].disabled = True
    # Ketika bangun dari type1 (bangun datar) terpilih, pilihan 'Luas Permukaan' dan 'Volume' akan di-disabled
    for key in type1.keys():
        if key.find(x) > -1:
            document['select-keliling'].disabled = False
            document['select-luas'].disabled = False
            document['select-luas-permukaan'].disabled = True
            document['select-volume'].disabled = True
    # Ketika bangun dari type2 (bangun ruang) terpilih, pilihan 'Keliling' dan 'Luas' akan di-disabled
    for key in type2.keys():
        if key.find(x) > -1:
            document['select-keliling'].disabled = True
            document['select-luas'].disabled = True
            document['select-luas-permukaan'].disabled = False
            document['select-volume'].disabled = False

# Fungsi yang akan dijalankan ketika pilihan 'yang akan dihitung' diubah
def selectCalculatedAction(ev):
    x = selectType.value
    y = selectCalculated.value
    # Reset Input Field
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False
    # Mengubah input placeholder (keterangan) pada setiap input, menyesuikan pada setiap bangun datar dan ruang yang dipilih
    # Jika input placeholder == 'Kosongkan', maka akan di-disabled
    for key in type1.keys():
        if key.find(x) > -1:
            for i in range(1, 5):
                input[str(i)].placeholder = type1[x][y]['input' + str(i)]
                if input[str(i)].placeholder == 'Kosongkan':
                    input[str(i)].disabled = True

    for key in type2.keys():
        if key.find(x) > -1:
            for i in range(1, 5):
                input[str(i)].placeholder = type2[x][y]['input' + str(i)]
                if input[str(i)].placeholder == 'Kosongkan':
                    input[str(i)].disabled = True

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float), 
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input1.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil formula pada dictionary
def formula(x, num1, num2, num3, num4):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['formula'](num1, num2, num3, num4)
            
    for key in type2.keys():
        if key.find(x) > -1:
            return type2[x][y]['formula'](num1, num2, num3, num4)

# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def main(ev):
    num1 = getNum(input1.value)
    num2 = getNum(input2.value)
    num3 = getNum(input3.value)
    num4 = getNum(input4.value)
    result = formula(selectType.value, num1, num2, num3, num4)
    output.textContent = str(result)

# Fugnsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction) # Ketika pilihan bangun datar dan ruang berubah, maka akan menjalankan fungsinya
selectCalculated.bind('change', selectCalculatedAction) # Ketika pilihan 'yang akan dihitung' berubah, maka akan menjalankan fungsinya
button.bind('click', main) # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketika 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter)
input2.bind("keypress", keyEnter)
input3.bind("keypress", keyEnter)
input4.bind("keypress", keyEnter)
