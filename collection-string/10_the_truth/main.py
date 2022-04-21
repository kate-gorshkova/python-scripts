def caesar_cipher(my_message):
    alphabet_letters_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_letters_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    for letter in my_message:
        if letter == " " or letter == "/":
            new_message += letter
        elif letter.islower():
            new_message += alphabet_letters_lower[(alphabet_letters_lower.index(letter) - 1) % 26]
        elif letter.isupper():
            new_message += alphabet_letters_upper[(alphabet_letters_upper.index(letter) - 1) % 26]
        else:
            new_message += letter
    my_str = "".join(new_message)
    return my_str


def shift(my_list):
    i = 3
    new_list = []
    for word in my_list:
        for _ in range(i):
            word = word[-1] + word
            word = word[:-1]
        for letter in word:
            if letter == "/":
                i += 1
        new_list.append(word)
    new_list = " ".join(new_list)
    total_list = new_list.replace("/ ", ".\n")
    total_list = total_list.replace("(", "`")
    total_list = total_list.replace("-", ",")
    total_list = total_list.replace("+", "")
    total_list = total_list.replace(" ..", "")
    total_list = total_list.replace("'", "!")
    return total_list


message = "vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf " \
          "jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp " \
          "djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst " \
          "tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq " \
          "up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn " \
          "puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs " \
          "boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt " \
          "fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf'uip"
new_str = caesar_cipher(message)
list_str = new_str.split()
my_new_message = shift(list_str)
print(my_new_message)

# зачёт!
