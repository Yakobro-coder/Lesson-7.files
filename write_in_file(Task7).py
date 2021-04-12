from pprint import pprint

menu = {}
write_menu = True
write_pod_menu = False
count = 1

with open('recipes.txt', 'r', encoding='utf-8') as f:
    numb_len = f.readlines()
    numb_len = len(numb_len)
    print(numb_len)

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
                a = {'ingredient_name':a[0], 'quantity':a[1], 'measure':a[2]}
                print(a)
                list_add_ingred.append(a)
            menu[key] = list_add_ingred
            list_add_ingred = []
            write_pod_menu = False
        if count == numb_len:
            write_menu = False

pprint(menu)




