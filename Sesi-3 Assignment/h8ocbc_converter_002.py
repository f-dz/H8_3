import temp_converter as tc

main_menu = {
    '1' : 'Celcius ke Kelvin',
    '2' : 'Celcius ke Fahrenheit',
    '3' : 'Kelvin ke Celcius',
    '4' : 'Kelvin ke Fahrenheit',
    '5' : 'Fahrenheit ke Celcius',
    '6' : 'Fahrenheit ke Kelvin',
}

def back_menu():
    input('Kembali ke menu utama, tekan enter..')
    print('----------------')

while(True):
    print('MENU CONVERTER')
    for k, v in main_menu.items():
        print(k, v)
    print('7 Keluar')

    menu = input('Pilih menu : ')
    if menu in main_menu:
        print('----------------')
        print('Program Konversi', main_menu[menu])
        while(True):
            try:
                value = int(input('Masukkan derajat suhu : '))
                break
            except:
                input('Input salah, masukkan kembali..')

    if menu == '1':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert(value, 'C'))
        back_menu()
    elif menu == '2':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert_to_fahrenheit(value,'C'))
        back_menu()
    elif menu == '3':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert(value, 'K'))
        back_menu()
    elif menu == '4':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert_to_fahrenheit(value, 'K'))
        back_menu()
    elif menu == '5':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert_from_fahrenheit(value, 'C'))
        back_menu()
    elif menu == '6':
        print('Hasil Konversi', main_menu[menu], ':', tc.convert_from_fahrenheit(value, 'K'))
        back_menu()
    elif menu == '7':
        print('Program berakhir..')
        break
    else:
        input('Input salah, masukkan kembali..')
