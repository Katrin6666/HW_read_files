from pprint import pprint
def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', encoding='utf-8') as menu:
        cook_book = {}
        for line in menu:
            for dish in dishes:
                if dish in line:
                    number = int(menu.readline())
                    for item in range(number):
                        data = menu.readline().strip().split('|')
                        ingred = {}
                        ingred['quantity'] = (int(data[1]) * int(person_count))
                        ingred['measure'] = data[2]
                        cook_book[data[0]] = ingred
                    menu.readline()
        pprint(cook_book)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
