# coding=utf-8

# input: array with multiple strings expected output: rank of the 3 most often repeated words in given set of strings
# and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

removed_characters = ".,?/!;:-()[]*-+"
response_list = []
words_list = []
stop = 0

for i in range(len(sentences)):
    for character in removed_characters:
        sentences[i] = sentences[i].replace(character, "")
    for j in range(len(sentences[i].split())):
        words_list.append(sentences[i].split()[j].lower())

for word in set(words_list):
    number = 0
    for element in range(len(words_list)):
        if word == words_list[element]:
            number += 1
    response_list.append([word, number])

response = sorted(response_list, key=lambda x: x[1], reverse=True)

print("\nResult:")
for elements in response:
    stop += 1
    print(str(stop) + "." + ' "' + str(elements[0]) + '" ' + "- " + str(elements[1]))
    if stop == 3:
        break


# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
