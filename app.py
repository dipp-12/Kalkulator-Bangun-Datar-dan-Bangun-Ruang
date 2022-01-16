from browser import document, console, alert
import math

input1 = document['input1']
input2 = document['input2']
input3 = document['input3']
input4 = document['input4']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

type1 = {'Belah Ketupat': {'Keliling': {'formula': lambda sisi, x,y,z: 4 * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                            'Luas': {'formula': lambda d1, d2, x,y: (1/2) * d1 * d2, 'input1': 'Masukkan Diameter 1', 'input2': 'Masukkan Diameter 2', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Jajar Genjang': {'Keliling': {'formula': lambda a, b, x,y: 2 * (a + b), 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                            'Luas': {'formula': lambda a, t, x,y: a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Layang-Layang': {'Keliling': {'formula': lambda a, c, x,y: 2 * (a + c), 'input1': 'Masukkan Sisi Panjang', 'input2': 'Masukkan Sisi Pendek', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                            'Luas': {'formula': lambda a, t, x,y: a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Lingkaran': {'Keliling': {'formula': lambda r, x,y,z: 2 * math.pi * r, 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                        'Luas': {'formula': lambda r, x,y,z: math.pi * (r ** 2), 'input1': 'Masukkan Jari-Jari', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Persegi Panjang': {'Keliling': {'formula': lambda p, l, x,y: 2 * (p + l), 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                        'Luas': {'formula': lambda p, l, x,y: p * l, 'input1': 'Masukkan Panjang', 'input2': 'Masukkan Lebar', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Persegi': {'Keliling': {'formula': lambda sisi, x,y,z: 4 * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}, 
                    'Luas': {'formula': lambda sisi, x,y,z: sisi * sisi, 'input1': 'Masukkan Sisi', 'input2': 'Kosongkan', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Segitiga': {'Keliling': {'formula': lambda a, b , c, x: a + b + c, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Sisi c', 'input4': 'Kosongkan'}, 
                    'Luas': {'formula': lambda a, t, x,y: (1/2) * a * t, 'input1': 'Masukkan Alas', 'input2': 'Masukkan Tinggi', 'input3': 'Kosongkan', 'input4': 'Kosongkan'}},
        'Trapesium': {'Keliling': {'formula': lambda a, b , c, d: a + b + c + d, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Sisi c', 'input4': 'Masukkan Sisi d'}, 
                    'Luas': {'formula': lambda a, b, t,y: (1/2) * (a + b) * t, 'input1': 'Masukkan Sisi a', 'input2': 'Masukkan Sisi b', 'input3': 'Masukkan Tinggi', 'input4': 'Kosongkan'}}}

type2 = {'Balok': {},
        'Bola': {},
        'Kerucut': {},
        'Kubus': {},
        'Tabung': {}}

def selectTypeAction(x):
    x = selectType.value
    y = selectCalculated.value

    for key in type1.keys():
        if key.find(x) > -1:
            console.log(key.find(x))
            document['select-keliling'].disabled = False
            document['select-luas'].disabled = False
            document['select-luas-permukaan'].disabled = True
            document['select-volume'].disabled = True
            

    for key in type2.keys():
        if key.find(x) > -1:
            console.log(key.find(x))
            document['select-keliling'].disabled = True
            document['select-luas'].disabled = True
            document['select-luas-permukaan'].disabled = False
            document['select-volume'].disabled = False

def selectCalculatedAction(X):
    x = selectType.value
    y = selectCalculated.value

    for key in type1.keys():
        if key.find(x) > -1:
            input1.placeholder = type1[x][y]['input1']
            input2.placeholder = type1[x][y]['input2']
            input3.placeholder = type1[x][y]['input3']
            input4.placeholder = type1[x][y]['input4']
    
    for key in type2.keys():
        if key.find(x) > -1:
            input1.placeholder = type2[x][y]['input1']
            input2.placeholder = type2[x][y]['input2']
            input3.placeholder = type2[x][y]['input3']
            input4.placeholder = type2[x][y]['input4']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input1.value = temp
            return temp
        else:
            return temp

def formula(x, num1, num2, num3, num4):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['formula'](num1, num2, num3, num4)
    

def main(ev):
    num1 = getNum(input1.value)
    num2 = getNum(input2.value)
    num3 = getNum(input3.value)
    num4 = getNum(input4.value)
    result = formula(selectType.value, num1, num2, num3, num4)
    output.textContent = str(result)
    
def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction)
selectCalculated.bind('change', selectCalculatedAction)
button.bind('click', main)
input1.bind("keypress", keyEnter)