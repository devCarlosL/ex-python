get_phrase = input('Digite uma frase: ')
word_list = get_phrase.split(' ')
list_with_two_letters = []
list_rest_letters = []

def to_string(list):
    return ' '.join(list)

def remove_space(phrase):
    return ' '.join(phrase).split()

for word in word_list:
    list_with_two_letters.append(word[:2])
    list_rest_letters.append(word[2:])
    list_with_two_letters = remove_space(list_with_two_letters)
    list_rest_letters = remove_space(list_rest_letters)

phrase_two_letters = to_string(list_with_two_letters)
phrase_rest_letters = to_string(list_rest_letters)

print(phrase_two_letters)
print(phrase_rest_letters)
