"""
Введите три слова через пробел. Преобразуйте их таким образом, чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы.

Например:  --> В-С-Т-А-В-А-Й Н-А Л-Ы-Ж-И
"""
strg = ('Вставай на лыжи')
strg = strg.upper()
print(strg)
new_strg = ''
counter = 1
# print(len(strg))

for i in strg:
    if counter < len(strg):
        if strg[counter] != ' ':
            if strg[counter - 1] != ' ':
                new_strg += i + '-'
        else:
            new_strg += i + ' '
        counter += 1
new_strg += strg[-1]

print(new_strg)

# lst=strg.split(' ')
#
# print(lst)
# for i in lst:
#     strg.join(i,'-')
#
# print(strg)
