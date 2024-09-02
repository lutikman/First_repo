# one_line_text = ("Textual data in Python is handled with str objects,"
#                  " or strings. Strings are immutable sequences of Unicode"
#                  " code points. String literals are written in a variety "
#                  " of ways: single quotes, double quotes, triple quoted.")

# print(one_line_text)


# url_search = '<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>'
# _, query = url_search.split('?')
# print(query)

# my_dict = {} # пустого словника

# for param in query.removesuffix('>').split('&',):
#     p_name, p_value = param.split('=')
#     # my_dict[p_name] = p_value.replace('+', ' ')
#     my_dict.update({p_name: p_value.replace('+', ' ')})

# print(my_dict)


# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str)
# print(str.translate(trantab))

# trantab = str.maketrans('t', 'T', intab)
# print(str)
# print(str.translate(trantab))
# print(trantab)


# symbols = "0123456789ABCDEF"
# code = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)


# morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
#               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#               '8': '---..', '9': '----.'}

# table_morze_dict = {}
# for k, v in morze_dict.items():
#     table_morze_dict[ord(k)] = v

# string = "Hello world"

# result = ""

# print(morze_dict)
# print(table_morze_dict)

# for ch in string:
#     print(ch, end=' ')
#     result = result + ch.upper().translate(table_morze_dict)

# print('\r\n', result)


# for i in range(10):
#     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#     print(s)


width = 20
for num in range(12):
    print(f'{num:^{width}} {num**2:^{width}} {num**3:^{width}}')