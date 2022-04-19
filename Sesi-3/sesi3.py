# FUNCTION
print('=====FUNCTION=====')

def hitung_volume_tabung(r, t):
    if r % 7 == 0:
        result = (22/7) * r * r * t
    else:
        result = 3.14 * r * r * t
    print('Volume tabung :', round(result, 2))

hitung_volume_tabung(6, 10)
hitung_volume_tabung(7, 10)

# Required (Function Arguments)
def hello(name):
    print('Hello', name)
hello('Saya')
hello('Kamu')

# Keyword (Function Arguments)
def profile(name, age):
    print('Nama\t:', name)
    print('Umur\t:', age)
    print('--------------')
profile(age=20, name='Saya')

# Default (Function Arguments)
def profile2(name, gender='Perempuan'):
    print('Nama\t:', name)
    print('Gender\t:', gender)
    print('--------------')
profile2(name='Kamu')    

# Variable-length (Function Arguments)
def profile3(name, *hoby):
    print('Nama\t:', name)
    print('Hobi\t:', hoby)
    print('--------------')
profile3('Dia', 'Makan', 'Ngoding', 'Tidur')
# Non-keywords variable
def profile4(name, **friends):
    print('Nama\t:', name)
    for k, v in friends.items():
        print('Friend\t:' , k, '---', v)
    print('--------------')
profile4('Kita', first='Saya', second='Dia')

# Anonymous Functions
luas_persegi = lambda s : s * s
luas_persegi_panjang = lambda p, l : p * l
print('Luas persegi\t\t:', luas_persegi(10))
print('Luas persegi panjang\t:', luas_persegi_panjang(10, 5))

# Return Statement
def keliling_persegi(s):
    return 4 * s
print('Keliling persegi\t:', keliling_persegi(8))

# Docstring
def docstring():
    '''
    Selamat tinggal
    Hati-hati di jalan
    '''
print(docstring.__doc__)


# MODULES
print('=====MODULES=====')

# Import Module
import person
print(person.name)
person.display('Ini fungsi dari modul person')

# Import Module dengan Menambahkan Path
import sys
# Tambah Path
sys.path.append(r'D:\OCBC NISP\Coding\Sesi-34\module')
# Import Module
import person_copy
from person_copy import name as pc_name
from person_copy import display as pc_display
print(pc_name)
pc_display('Ini fungsi dari modul person_copy')
# Hapus Path
sys.path.remove(r'D:\OCBC NISP\Coding\Sesi-34\module')

# dir() Functions
print(dir())
my_list= [1, 2, 3]
print('--------------------------')
print(dir())

# Reload Module
# import importlib
# importlib.reload(nama_modul)


# PACKAGE
print('=====PACKAGE=====')

# Import Package
import package.modul1 as md1
import package.modul2 as md2
print(md1.my_list)
print(md2.my_list)

# Pip
# pip list
# pip help
# pip install requests
# Package            Version
# ------------------ ---------
# certifi            2021.10.8
# charset-normalizer 2.0.12
# idna               3.3
# pip                20.2.3
# requests           2.27.1
# setuptools         49.2.1
# urllib3            1.26.9
# create file using_request.py
# run file using_request.py