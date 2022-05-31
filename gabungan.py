import string

print("Selamat datang pada aplikasi lexical analyzer sekaligus parser bahasa jepang sederhana.")
print("Aplikasi ini dibuat untuk mendeteksi kata-kata dan grammar yang sesuai dengan kamus yang sesuai.")
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
print("Program hanya akan lanjut ke tahap parsing apabila valid pada tahap lexical analyzing.")
print("Silakan masukkan input:")

sentence = input()
input_string = sentence.lower()+'#'

alphabet_list = list(string.ascii_lowercase)
state_list = {'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37', 'q38'}

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] = 'error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

transition_table['q0', 'o'] = 'q38'
transition_table['q0', 'h'] = 'q1'
transition_table['q0', 'r'] = 'q3'
transition_table['q0', 'a'] = 'q7'
transition_table['q0', 's'] = 'q9'
transition_table['q0', 'y'] = 'q13'
transition_table['q0', 'j'] = 'q16'
transition_table['q0', 'm'] = 'q21'
transition_table['q0', 'n'] = 'q19'
transition_table['q0', 't'] = 'q22'
transition_table['q0', ' '] = 'q33'
transition_table['q0', 'w'] = 'q32'

transition_table['q1', 'o'] = 'q2'

transition_table['q2', 'n'] = 'q38'

transition_table['q3', 'i'] = 'q4'

transition_table['q4', 'k'] = 'q6'
transition_table['q4', 'n'] = 'q5'

transition_table['q5', 'g'] = 'q6'

transition_table['q6', 'o'] = 'q38'

transition_table['q7', 'o'] = 'q8'

transition_table['q8', 'i'] = 'q38'

transition_table['q9', 'u'] = 'q10'
transition_table['q9', 'o'] = 'q12'

transition_table['q10', 's'] = 'q11'

transition_table['q11', 'h'] = 'q8'

transition_table['q12', 'd'] = 'q32'

transition_table['q13', 'u'] = 'q14'
transition_table['q13', 'o'] = 'q20'

transition_table['q14', 'u'] = 'q15'

transition_table['q15', 'j'] = 'q8'

transition_table['q16', 'i'] = 'q37'
transition_table['q16', 'u'] = 'q17'

transition_table['q17', 'u'] = 'q28'

transition_table['q18', 'b'] = 'q8'

transition_table['q19', 'o'] = 'q20'

transition_table['q20', 'm'] = 'q21'

transition_table['q21', 'i'] = 'q26'

transition_table['q22', 'e'] = 'q23'
transition_table['q22', 'a'] = 'q29'

transition_table['q23', 'r'] = 'q24'

transition_table['q24', 'e'] = 'q18'

transition_table['q25', 'e'] = 'q26'

transition_table['q26', 'm'] = 'q27'

transition_table['q27', 'a'] = 'q28'

transition_table['q28', 's'] = 'q35'

transition_table['q29', 'b'] = 'q25'
transition_table['q29', 'n'] = 'q30'

transition_table['q30', 'a'] = 'q31'

transition_table['q31', 'k'] = 'q32'

transition_table['q32', 'a'] = 'q38'

transition_table['q33', 'j'] = 'q34'

transition_table['q34', 'g'] = 'q32'

transition_table['q35', 'u'] = 'q38'

transition_table['q36', 'h'] = 'q6'

transition_table['q37', 's'] = 'q36'

transition_table['q38', ' '] = 'q0'
transition_table['q38', '#'] = 'accept'

# Lexical Analysis
print("")
idx_char = 0
state = 'q0'
current_token = ''
while state != 'accept':
    current_char = input_string[idx_char]
    if current_char != ' ':
        current_token += current_char
    state = transition_table[(state, current_char)]
    if state == 'q38':
        print('Simbol sekarang: ' + current_token + ', valid.')
        current_token = ''
    if state == 'error':
        print('Ada simbol di input: ' + sentence + ', yang tidak valid.')
        break
    idx_char += 1
    
if state == 'accept':
    print('Semua simbol di input: "' + sentence + '" valid. Kalimat akan dilanjutkan ke tahap parsing.')
    # input example
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
