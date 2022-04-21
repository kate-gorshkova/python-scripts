from copy import deepcopy


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def new_item(any_site, any_item):
    for key, value in any_site.items():
        if isinstance(value, dict):
            new_item(value, any_item)
        elif isinstance(value, str):
            any_site[key] = value.replace("телефон", any_item)

    return any_site


def pretty(any_site, space=1):
    for i_key, i_value in any_site.items():
        if isinstance(i_value, dict):
            print("\t" * space, i_key + ": {")
            pretty(i_value, space + 1)
        else:
            print("\t" * (space + 1), i_key + ":", i_value)
    print("\t" * space, "}")


site_count = int(input("Сколько сайтов: "))
for _ in range(site_count):
    my_site = deepcopy(site)
    my_item = input("\nВведите название продукта для нового сайта: ")
    print("Сайт для {}:".format(my_item))
    print("site = {")
    my_site = new_item(my_site, my_item)
    pretty(my_site)
