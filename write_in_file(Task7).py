from pprint import pprint


# Подсчёт количества строк в файле, т.к. мы предерживаемся определённой логики в ведении recipes.txt
# От этого и формируем дальше list. Что бы знать когда файл закончился.
def line_count(file):
    with open(file, 'r', encoding='utf-8') as f:
        numb_len = f.readlines()
        numb_len = len(numb_len)
        return numb_len


# формируем list с помощью полученных данных из файла recipes.txt
# аргумент на входе, файл с данными(рецептами)
def dict_menu(file):
    numb_len = line_count(file)
    cook_book = {}
    write_menu = True
    write_pod_menu = False
    count = 1
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        while write_menu:
            write_pod_menu = True
            while write_pod_menu:
                count +=1
                key = f.readline().strip()
                if key == '' and count < numb_len:
                    count +=1
                    continue
                numb = int(f.readline().strip())
                list_add_ingred = []
                for i in range(0, numb):
                    count +=1
                    a = (f.readline().strip().split(' | '))
                    a = {'ingredient_name':a[0], 'quantity':int(a[1]), 'measure':a[2]}
                    list_add_ingred.append(a)
                cook_book[key] = list_add_ingred
                list_add_ingred = []
                write_pod_menu = False
            if count == numb_len:
                write_menu = False
    return cook_book

# Выводит dict продуктов, которые надо купить. Принимает либо одно блюдо(str), либо список блюд, и кол-во персон(порций)
def get_shop_list_by_dishes(disher, person_count=1):
    cook_book = dict_menu('recipes.txt')
    shop_dict = {}
    if isinstance(disher, str):
        if disher in cook_book:
            for dict_ingrid in cook_book.get(disher):
                add_shop = {dict_ingrid.get('ingredient_name') : {'measure':dict_ingrid.get('measure'),
                                                                  'quantity':f"{dict_ingrid.get('quantity')*person_count}"}}
                print(add_shop)
# Тут обрабатывает list блюд.
    elif isinstance(disher, list):
        for dish in disher:
            if dish in cook_book:
                for dict_ingrid in cook_book.get(dish):
                    add_shop = {dict_ingrid.get('ingredient_name') : {'measure': dict_ingrid.get('measure'),
                                                                      'quantity':f"{dict_ingrid.get('quantity')*person_count}"}}
                    if list(add_shop.keys())[0] in shop_dict:
                        add_shop = {dict_ingrid.get('ingredient_name'): {'measure': dict_ingrid.get('measure'),
                                                                         'quantity': f"{(dict_ingrid.get('quantity') * person_count) + int(shop_dict.get(list(add_shop.keys())[0]).get('quantity'))}"}}
                        shop_dict.update(add_shop)
                    else:
                        shop_dict.update(add_shop)
    return shop_dict



pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))





