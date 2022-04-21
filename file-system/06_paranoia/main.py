def caesar_cipher(my_message):
    alphabet_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_message = ""
    i = 1
    for letter in my_message:
        if letter == "\n":
            i += 1

        if letter.isalpha():
            new_message += alphabet_letters[(alphabet_letters.index(letter) + i) % 52]
        else:
            new_message += letter

    return new_message


message = "Good Bay\nGood Bay\nHello\nHello"
file = open("text.txt", "w")
file.write(message)
file.close()

new_file = open("cipher_text.txt", "w")
new_file.write(caesar_cipher(message))
new_file.close()

# зачёт!
