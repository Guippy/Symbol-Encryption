import string
import random
print("welcome to the ECC 2.0")
types = input("encrypt:1\ndecrypt:2\n")
word = input("enter a word ")

def encode_decode(words, typess):
    alphabet = string.printable
    new_word = []
    positive_symbols = ["@", "$", "/", ",", "+", "~"]
    negative_symbols = ["#", "?", "*", "(", ")", "=", "["]
    equal_symbols = ["&", "%", "<", ">", "!", "]"]
    index = 0
    match typess:
        case 1:
            for letters in words:
                target_index = alphabet.index(letters)
                while target_index != index:
                    if target_index > index:
                        index += 1
                        new_word.append(positive_symbols[random.randint(0, (len(positive_symbols) - 1))])
                    else:
                        index -= 1
                        new_word.append(negative_symbols[random.randint(0, (len(negative_symbols) - 1))])
                new_word.append(equal_symbols[random.randint(0, (len(equal_symbols) - 1))])
            return "".join(new_word)
        case 2:
            for letters in words:
                if letters in positive_symbols:
                    index += 1
                elif letters in negative_symbols:
                    index -= 1
                else:
                    new_word.append(alphabet[index])
            return "".join(new_word)


print(encode_decode(word, int(types)))
