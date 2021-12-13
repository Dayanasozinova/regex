from pprint import pprint
import csv
import re

data = []

with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f)
    contacts_list = list(rows)

#--------------lastname-----------------------
lastname_raw = []
lastname = []
for contact in contacts_list:
  pattern_last_name = r'([А-Я]\w+)'
  find_last_name = re.findall(pattern_last_name, contact[0])
  lastname_raw.append(find_last_name)

lastname_filter = list(filter(None, lastname_raw))
for ln in lastname_filter:
  lastname.append(ln[0])
#------------name-----------------------
name_raw = []
name = []
for contact in contacts_list:
  pattern_name = r'([А-Я]\w+)\s([А-Я]\w+)'
  find_name = re.findall(pattern_name, contact[0])
  name_raw.append(find_name)

name_filter = list(filter(None, name_raw))
for n in name_filter:
  name.append(n[0][1])
#-----------surname---------------
surname_raw = []
surname = []
for contact in contacts_list:
  pattern_surname = r'([А-Я]\w+)\s([А-Я]\w+)'
  find_surname = re.findall(pattern_surname, contact[0])
  surname_raw.append(find_surname)

# surname_filter = list(filter(None, surname_raw))
# for n in surname_filter:
#   surname.append(n[0][1])
print(name)














# pprint(contacts_list)
# data_1 = []
# for contact in contacts_list:
#   cont = list(filter(None, contact))
#   data_1.append(cont)
# print(data_1)
#
# for c in data_1:
#   for n in c:
#     file_new = re.sub(r'([А-Я]\w+)\s([А-Я]\w+)\s', r'\1,\2,', fi)
#     data.append(file_new)
# data = []




# print(data)
# sub_2 = re.sub(pattern_3, pattern_4, contact[0])
  # sub_3 = re.sub(pattern_5, pattern_6, contact[0])
# pattern_1 = r'([А-Я]\w+)\s([А-Я]\w+)\s([А-Я][а-я]+)'
  # pattern_2 = r'\1,\2,\3'
  # pattern_3 = r'([А-Я]\w+)\s([А-Я]\w+)'
  # pattern_4 = r'\1,\2'
  # pattern_5 = r'([А-Я]\w+)\s([А-Я]\w+)'
  # pattern_6 = r'\1,\2'

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)
