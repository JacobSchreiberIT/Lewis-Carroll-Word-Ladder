from convert import convert
from english_words import get_english_words_set

if __name__ == '__main__':
    
    wordset = get_english_words_set(['web2'], lower=True)

    user_word = input("Enter word 1: ")
    user_word2 = input("Enter word 2: ")
    print(convert(user_word, user_word2, wordset))

    