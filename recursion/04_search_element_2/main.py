site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h1': 'Здесь будет мой заголовок',
            'div': {
                'aside': {
                    'section': {
                        'h2': 'Здесь будет заголовок секции',
                        'span': 'Тут, наверное, какой-то текст'
                    }
                }
            },
            'p': 'А вот здесь новый абзац'
        }
    }
}


def key_search(any_dict, any_key, depth):
    if depth < 1:
        return

    if any_key in any_dict:
        return any_dict[any_key]

    for any_dict in any_dict.values():
        if isinstance(any_dict, dict):
            result = key_search(any_dict, any_key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


key = input("Искомый ключ: ")
answer = input("Хотите ввести максимальную глубину? (да или нет) ").lower()
lev = 0
if answer == "да":
    lev = int(input("Введите максимальную глубину: "))
elif answer == "нет":
    lev = 6

value = key_search(site, key, lev)
if value:
    print("Значение:", value)
else:
    print("Такого ключа в структуре сайта нет.")

# зачёт!
