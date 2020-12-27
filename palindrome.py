def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    inverted_word = word[::-1]
    if word == inverted_word:
        return True
    else:
        return False


def run():
    word = input("Escribe una palabra, verificaré si es palindroma: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Sí es un palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    run()
