countries_count = int(input("Кол-во стран: "))
countries_dict = dict()

for i_country in range(1, countries_count + 1):
    print(i_country, "страна:", end=" ")
    country = input()
    country_list = country.split()
    for i_city in country_list[1:]:
        countries_dict[i_city] = country_list[0]

for i_city in range(1, 4):
    print(i_city, "город:", end=" ")
    my_city = input()
    my_country = countries_dict.get(my_city, 0)
    if my_country == 0:
        print("По городу", my_city, "данных нет.")
    else:
        print("Город", my_city, "расположен в стране", my_country)

# зачёт!
