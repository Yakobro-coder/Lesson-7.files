import glob

# Создаём лист с именнами всех файлов *.txt в директории, и удаляем файл с результатами если он есть.
list_files= glob.glob('./*.txt')
list_files.remove('.\\result.txt')

# Покажет ко-во строк каждого файла и создаст dict { имя файла : кол-во строк}
dict_len_files = {}
for files in list_files:
    with open(files, 'r', encoding='utf-8') as f:
        numb_len = f.readlines()
        numb_len = len(numb_len)
    dict_len_files[files] = numb_len

# Проходимся по отсартированному списку значений словоря {name_file:line_count}
# Список отсортирован от 0 до n, далее идёт сравнение значений по ключу словоря {name_file:line_count}
# Если значения равны, то записываем этот файл в результат по ключу(имя файла)
for i in range(len(sorted(dict_len_files.values()))):
    for key, val in dict_len_files.items():
        if val == sorted(dict_len_files.values())[i]:
            with open(key,'r', encoding='utf-8') as f:
                text_in_file = f.read()
            with open('result.txt', 'a', encoding='utf-8') as f:
                f.write(f'{key}\n{val}\n{text_in_file}\n')