# FILES
print('=====FILE=====')

# Open File
try:
    files = open('sample_text.txt', encoding = 'utf-8')
    print(files.read())
except FileNotFoundError:
    print('File not found')
finally:
    files.close()

# Create File
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write("Nama\t: Saya\n")
    f.write("Umur\t: 22 tahun")
try:
    f = open('sample.txt','r', encoding = 'utf-8')
    print(f.readline())
    print(f.readline())
except:
    print('File not found')
finally:
    f.close()


# EXCEPTION
print('=====EXCEPTION=====')

# Raise Exception
x = 4
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# Exception on OS Interaction
import sys
def os_interaction():
    assert ('win' in sys.platform), "This code runs on Windows only."
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
try:
    os_interaction()
except AssertionError as error:
    print(error)
    print('os_interaction() function was not executed')