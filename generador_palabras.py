import os
import random

def run():
    new_words = ""
    os.system("clear")
    letters = input("\nIntroduzca las letras con las que desea generar combinaciones: ")
    letters = letters.replace(" " , "")
    letters = letters.upper()
    letter_list = []
    for letter in letters:
        letter_list.append(letter)
    os.system("clear")
    mostrar = int(input("\nCuantas Palabras desea mostrar: "))
    os.system("clear")
    while new_words != "n":
        i = 0
        while i < mostrar:
            random.shuffle(letter_list)
            word = "".join(letter_list)
            print(word)
            i += 1
        question = "\nSi desea generar " + str(mostrar) + " palabras nuevas presione ENTER, de lo contrario presione N y luego enter: "
        new_words = input(question)
        new_words = new_words.lower()
        os.system("clear")

if __name__ == "__main__":
    run()