import string

some = "*****это пASDFрdимеВА  фыва ФЫАВЖр строки....wow!!!****"
some_list = list(some)
some_len = len(some)
new_some = ''

for i in range(some_len):
    if some_list[i] not in string.punctuation and some_list[i] != ' ':
        new_some += some_list[i]

print(new_some.lower())
