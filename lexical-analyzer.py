import string

print("Selamat datang pada aplikasi lexical analyzer bahasa jepang sederhana.")
print("Aplikasi ini dibuat untuk mendeteksi kata-kata yang sesuai dengan kamus yang sesuai.")
print("Kata yang diterima: ")
print("yuuji, aoi, riko, tanaka, wa, ringo(Apel), sushi, juusu(Jus), soda, eiga(Film), terebi(TV), hon(Buku), jisho(Kamus), o, tabemasu(Makan), nomimasu(Minum), mimasu(Nonton), yomimasu(Baca)")
print("")
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
    print('Semua simbol di input: "' + sentence + '" valid.')
print("Klik enter untuk keluar program.")
input()
