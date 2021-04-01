# string to hexadecimal converter

def string_hex(string):
    return ':'.join(format(ord(c), 'x') for c in string)

# hexadecimal to string converter.

def hex_string(hexa):
    if ':' in hexa:
        a = hexa.split(':')
        hexa = ''.join(a)
    hexgen = (hexa[i:i+2] for i in range(0, len(hexa), 2))
    return ''.join(chr(eval('0x'+n)) for n in hexgen)

# string to binary converter

def string_bin(string):
    return ':'.join(format(ord(c), 'b') for c in string)

# binary to string converter

def bin_string(binary):
    if ':' in binary:
        a = binary.split(':')
        binary = ''.join(a)
    bingen = (binary[i:i+7] for i in range(0, len(binary), 7))
    return ''.join(chr(eval('0b'+n)) for n in bingen)

# string to ascii converter

def string_ascii(string):
    return ':'.join(str(ord(c)) for c in string)

# ascii to string converter

def ascii_string(asciii):
    if ':' in asciii:
        b = asciii.split(':')
        asciii = ''.join(b)
    b = ''
    c = ''
    i = 0
    while i < len(asciii):
        b += asciii[i]
        if chr(int(b)).isalpha():
            c+=chr(int(b))
            b = ''
            i+=1
        else:
            i+=1
    return c

# string to octal converter

def string_oct(string):
    return ':'.join(format(ord(c), 'o') for c in string)

# octal to string converter

def oct_string(octa):
    if ':' in octa:
        a = octa.split(':')
        octa = ''.join(a)
    octgen = (octa[i:i+3] for i in range(0, len(octa), 3))
    return ''.join(chr(eval('0o'+n)) for n in octgen)