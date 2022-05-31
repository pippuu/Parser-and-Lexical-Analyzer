print("Selamat datang pada aplikasi parser bahasa jepang sederhana.")
print("Aplikasi ini dibuat untuk mendeteksi grammar yang sesuai dengan kamus yang telah ada.")
print("")
print("Subjek yang diterima: ")
print("yuuji, aoi, riko, dan tanaka")
print("")
print("Kata kerja yang diterima: ")
print("tabemasu(Makan), nomimasu(Minum), mimasu(Nonton), yomimasu(Baca)")
print("")
print("Objek yang diterima: ")
print("ringo(Apel), sushi, juusu(Jus), soda, eiga(Film), terebi(TV), hon(Buku), jisho(Kamus)")
print("")
print("Bentuk kalimat umum yang diterima:")
print("X wa Y o Z")
print("X sebagai Subjek, Y sebagai Objek, dan Z sebagai Kata Kerja")
print("")
print("Silakan masukkan input:")

# input example
sentence = input()
tokens = sentence.lower().split()
tokens.append('EOS') 
print("")

# symbols definition
non_terminals = ['S', 'SB', 'P', 'V', 'O', 'OV']
terminals = ['yuuji', 'aoi','riko', 'tanaka','tabemasu', 'nomimasu','yomimasu','mimasu', 'sushi', 'ringo', 'juusu', 'soda', 'eiga', 'terebi', 'hon', 'jisho', 'wa','o']


# parse table definition
parse_table = {}

# parse_table [('', '')] = ['', '', '']

parse_table [('S', 'yuuji')] = ['SB', 'P', 'OV']
parse_table [('S', 'aoi')] = ['SB', 'P', 'OV']
parse_table [('S', 'riko')] = ['SB', 'P', 'OV']
parse_table [('S', 'tanaka')] = ['SB', 'P', 'OV']
parse_table [('S', 'tabemasu')] = ['error']
parse_table [('S', 'nomimasu')] = ['error']
parse_table [('S', 'yomimasu')] = ['error']
parse_table [('S', 'mimasu')] = ['error']
parse_table [('S', 'sushi')] = ['error']
parse_table [('S', 'ringo')] = ['error']
parse_table [('S', 'juusu')] = ['error']
parse_table [('S', 'soda')] = ['error']
parse_table [('S', 'eiga')] = ['error']
parse_table [('S', 'terebi')] = ['error']
parse_table [('S', 'hon')] = ['error']
parse_table [('S', 'jisho')] = ['error']
parse_table [('S', 'wa')] = ['error']
parse_table [('S', 'o')] = ['error']
parse_table [('S', 'EOS')] = ['error']

parse_table [('SB', 'yuuji')] = ['yuuji']
parse_table [('SB', 'aoi')] = ['aoi']
parse_table [('SB', 'riko')] = ['riko']
parse_table [('SB', 'tanaka')] = ['tanaka']
parse_table [('SB', 'tabemasu')] = ['error']
parse_table [('SB', 'nomimasu')] = ['error']
parse_table [('SB', 'yomimasu')] = ['error']
parse_table [('SB', 'mimasu')] = ['error']
parse_table [('SB', 'sushi')] = ['error']
parse_table [('SB', 'ringo')] = ['error']
parse_table [('SB', 'juusu')] = ['error']
parse_table [('SB', 'soda')] = ['error']
parse_table [('SB', 'eiga')] = ['error']
parse_table [('SB', 'terebi')] = ['error']
parse_table [('SB', 'hon')] = ['error']
parse_table [('SB', 'jisho')] = ['error']
parse_table [('SB', 'wa')] = ['error']
parse_table [('SB', 'o')] = ['error']
parse_table [('SB', 'EOS')] = ['error']

parse_table [('OV', 'yuuji')] = ['error']
parse_table [('OV', 'aoi')] = ['error']
parse_table [('OV', 'riko')] = ['error']
parse_table [('OV', 'tanaka')] = ['error']
parse_table [('OV', 'tabemasu')] = ['error']
parse_table [('OV', 'nomimasu')] = ['error']
parse_table [('OV', 'yomimasu')] = ['error']
parse_table [('OV', 'mimasu')] = ['error']
parse_table [('OV', 'sushi')] = ['O', 'P', 'V']
parse_table [('OV', 'ringo')] = ['O', 'P', 'V']
parse_table [('OV', 'juusu')] = ['O', 'P', 'V']
parse_table [('OV', 'soda')] = ['O', 'P', 'V']
parse_table [('OV', 'eiga')] = ['O', 'P', 'V']
parse_table [('OV', 'terebi')] = ['O', 'P', 'V']
parse_table [('OV', 'hon')] = ['O', 'P', 'V']
parse_table [('OV', 'jisho')] = ['O', 'P', 'V']
parse_table [('OV', 'wa')] = ['error']
parse_table [('OV', 'o')] = ['error']
parse_table [('OV', 'EOS')] = ['error']

parse_table [('V', 'yuuji')] = ['error']
parse_table [('V', 'aoi')] = ['error']
parse_table [('V', 'riko')] = ['error']
parse_table [('V', 'tanaka')] = ['error']
parse_table [('V', 'tabemasu')] = ['tabemasu']
parse_table [('V', 'nomimasu')] = ['nomimasu']
parse_table [('V', 'yomimasu')] = ['yomimasu']
parse_table [('V', 'mimasu')] = ['mimasu']
parse_table [('V', 'sushi')] = ['error']
parse_table [('V', 'ringo')] = ['error']
parse_table [('V', 'juusu')] = ['error']
parse_table [('V', 'soda')] = ['error']
parse_table [('V', 'eiga')] = ['error']
parse_table [('V', 'terebi')] = ['error']
parse_table [('V', 'hon')] = ['error']
parse_table [('V', 'jisho')] = ['error']
parse_table [('V', 'wa')] = ['error']
parse_table [('V', 'o')] = ['error']
parse_table [('V', 'EOS')] = ['error']

parse_table [('O', 'yuuji')] = ['error']
parse_table [('O', 'aoi')] = ['error']
parse_table [('O', 'riko')] = ['error']
parse_table [('O', 'tanaka')] = ['error']
parse_table [('O', 'tabemasu')] = ['error']
parse_table [('O', 'nomimasu')] = ['error']
parse_table [('O', 'yomimasu')] = ['error']
parse_table [('O', 'mimasu')] = ['error']
parse_table [('O', 'sushi')] = ['sushi']
parse_table [('O', 'ringo')] = ['ringo']
parse_table [('O', 'juusu')] = ['juusu']
parse_table [('O', 'soda')] = ['soda']
parse_table [('O', 'eiga')] = ['eiga']
parse_table [('O', 'terebi')] = ['terebi']
parse_table [('O', 'hon')] = ['hon']
parse_table [('O', 'jisho')] = ['jisho']
parse_table [('O', 'wa')] = ['error']
parse_table [('O', 'o')] = ['error']
parse_table [('O', 'EOS')] = ['error']

parse_table [('P', 'yuuji')] = ['error']
parse_table [('P', 'aoi')] = ['error']
parse_table [('P', 'riko')] = ['error']
parse_table [('P', 'tanaka')] = ['error']
parse_table [('P', 'tabemasu')] = ['error']
parse_table [('P', 'nomimasu')] = ['error']
parse_table [('P', 'yomimasu')] = ['error']
parse_table [('P', 'mimasu')] = ['error']
parse_table [('P', 'sushi')] = ['error']
parse_table [('P', 'ringo')] = ['error']
parse_table [('P', 'juusu')] = ['error']
parse_table [('P', 'soda')] = ['error']
parse_table [('P', 'eiga')] = ['error']
parse_table [('P', 'terebi')] = ['error']
parse_table [('P', 'hon')] = ['error']
parse_table [('P', 'jisho')] = ['error']
parse_table [('P', 'wa')] = ['wa']
parse_table [('P', 'o')] = ['o']
parse_table [('P', 'EOS')] = ['error']

stack = []
stack.append('#')
stack.append('S')

idx_token = 0
symbol = tokens[idx_token]

# Parsing process
while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ',top)
    print('symbol = ',symbol)
    if top in terminals:
        print('top adalah simbol terminal')
        if top == symbol:
            stack.pop()
            idx_token += 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack:',stack)
                stack.pop()
        else:
            print('error')
            break
    elif top in non_terminals:
        print('top adalah simbol non-terminal')
        if parse_table[(top,symbol)][0] != 'error':
            stack.pop()
            symbols_to_be_pushed = parse_table[(top,symbol)]
            for i in range(len(symbols_to_be_pushed)-1,-1,-1):
                stack.append(symbols_to_be_pushed[i])
        else:
            print('error')
            break
    else:
        print('error')
        break
    print('isi stack:',stack)
    print()
if symbol == 'EOS' and len(stack) == 0:
    print('Input string: ' + sentence + ' DITERIMA karena sesuai Grammar')
else:
    print('Input string: "' + sentence + '" TIDAK DITERIMA karena tidak sesuai Grammar')
print("Klik enter untuk keluar program.")
input()
