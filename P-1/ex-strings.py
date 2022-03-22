def manipulate_string():
    vowels = 'AEIOU'
    
    word_1 = input("Digite a primeira palavra: ").upper()
    word_2 = input("Digite a segunda palavra: ").lower()
    word_3 = input("Digite a terceira palavra: ")
    
    for i in vowels:
        word_3 = word_3.upper().replace(i, '')

    print(f'{word_1}, {word_2}, {word_3}')

manipulate_string()
