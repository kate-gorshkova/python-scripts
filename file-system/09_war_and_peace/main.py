import collections
import zipfile


def unzip(archive):
    zip_file = zipfile.ZipFile(archive, "r")
    for i_file_name in zip_file.namelist():
        zip_file.extract(i_file_name)
    zip_file.close()


def statistic_letter(any_file_name):
    any_dict = dict()
    if any_file_name.endswith(".zip"):
        unzip(any_file_name)
        any_file_name = "".join((any_file_name[:-3], "txt"))
    text_file = open(any_file_name, "r", encoding="utf-8")
    for i_line in text_file:
        for i_sym in i_line:
            if i_sym.isalpha():
                if i_sym not in any_dict:
                    any_dict[i_sym] = 0
                any_dict[i_sym] += 1
    text_file.close()

    return any_dict


def sorted_statistic(any_statistic_dict):
    sorted_values = sorted(any_statistic_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for i_key in any_statistic_dict.keys():
            if any_statistic_dict[i_key] == i_value:
                sorted_dict[i_key] = i_value

    return sorted_dict


def print_statistic(any_sorted_statistic):
    print("{:-^21}".format("+"))
    print("|{: ^9}|{: ^9}|".format("буква", "частота"))
    print("{:-^21}".format("+"))
    for letter, count in any_sorted_statistic.items():
        print("|{: ^9}|{: ^9}|".format(letter, count))
    print("{:-^21}".format("+"))


file_name = "voyna-i-mir.zip"
statistic = statistic_letter(file_name)
sorted_statistic = sorted_statistic(statistic)
print_statistic(sorted_statistic)

# зачёт!
