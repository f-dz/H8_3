# CONDITIONAL
print('=====CONDITIONAL=====')
if 10 < 20:
    print('Yes')

if 'rek' in 'mereka':
    print('Yes')

if 'Kita' in ['Saya', 'Kamu', 'Dia']:
    print('Kita saling kenal')
    print('Kita berteman')
print('Endif statement')

nilai = 70
grade = ''
if nilai > 50:
    if nilai > 90: grade = 'A'
    elif nilai > 70: grade = 'B'
    elif nilai > 50: grade = 'C'
    print('Lulus dengan nilai', grade)
else:
    print('Tidak Lulus dengan nilai', grade)

if(grade == 'A'): print('Selamat'); print('Nilaimu Sangat Bagus')
elif(grade == 'B'): print('Selamat!!'); print('Nilaimu Bagus')
elif(grade == 'C'): print('Selamat!!'); print('Nilaimu Cukup Bagus')
elif(grade == 'D'): print('Selamat!!'); print('Nilaimu Buruk')

raining = True
print('Ayo', 'liburan' if not raining else 'tidur')

age = 22
print('Kamu masih kecil!' if age < 17 else 'Kamu sudah besar!')

if(True):
    pass


# LOOPING
print('=====LOOPING=====')

# Indefinite
n = 3
while n >= 1: print(n); n -= 1

i = 0
key = 'Kamu'
keywords = ['Saya', 'Kamu', 'Dia', 'Mereka']
while i < len(keywords):
    if key == keywords[i]:
        print('Menemukan', key, 'di indeks', i)
        break
    i += 1

# Definite
for i in range(3):
    print(i+1)

words = {
    'Saya': 'I',
    'Kamu': 'You',
    'Dia': 'She',
    'Mereka': 'They'
}
for i, j in words.items():
    print(i, ':', j)