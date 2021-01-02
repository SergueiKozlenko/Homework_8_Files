def get_ingredient_dict(ingredient_line):
    """Примет строку, разобьет ее по разделителю ' | ' и возвратит словарь."""
    ingredient_dict = {}
    ingredient_record = ingredient_line.strip().split(' | ')
    ingredient_dict['ingredient_name'] = ingredient_record[0]
    ingredient_dict['quantity'] = int(ingredient_record[1])
    ingredient_dict['measure'] = ingredient_record[2]
    return ingredient_dict


def get_shop_list_by_dishes(dishes, person_count):
    """Примет список блюд, количество персон, возвратит словарь с названием ингредиентов
    и их необходимого количества"""
    shop_list = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            if ingredients['ingredient_name'] not in shop_list.keys():
                shop_list[ingredients['ingredient_name']] = dict(measure=ingredients['measure'],
                                                                 quantity=ingredients['quantity'] * person_count)
            else:
                shop_list[ingredients['ingredient_name']] = dict(measure=ingredients['measure'],
                                                                 quantity=shop_list[ingredients['ingredient_name']][
                                                                              'quantity'] + ingredients[
                                                                              'quantity'] * person_count)
    sorted_shop_list = {k: shop_list[k] for k in sorted(shop_list)}
    return sorted_shop_list


cook_book = {}

with open('recipes.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    recipe_name = ''
    ingredients_list = []
    ingredients_number = 0
    counter = 0
    for i in range(len(lines)):
        if i == 0 or lines[i - 1] == '\n':
            recipe_name = lines[i].strip()
            ingredients_number = int(lines[i + 1].strip())
        elif lines[i] != '\n' and not (i == 1 or lines[i - 2] == '\n'):
            ingredients_list.append(get_ingredient_dict(lines[i]))
            counter += 1
        if counter == ingredients_number:
            cook_book[recipe_name] = ingredients_list.copy()
            ingredients_list.clear()
            counter = 0

# print(cook_book)
# print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
