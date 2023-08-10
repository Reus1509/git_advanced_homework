from random import choice

# Это игра виселица с примитивным графическим отображением в 1.0

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

max_wrong = len(HANGMAN) - 1
WORDS = ("python", "игра", "программирование")  # Здесь я заранее добавляю перечень слов для угадывания, в дальнейшем можно подключить большой словарь

word = choice(WORDS)  
so_far = "_" * len(word)  
wrong = 0  
used = [] 

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])  # Вывод висельника по индексу
    print("\nВы использовали следующие буквы:\n", used)
    print("\nНа данный момент слово выглядит так:\n", so_far)

    guess = input("\n\nВведите свое предположение: ")  

    while guess in used:
        print("Вы уже вводили букву", guess)  # Если буква уже вводилась ранее, то выводим соответствующее сообщение
        guess = input("Введите свое предположение: ") 

    used.append(guess)  # В список использованных букв добавляется введённая буква

    if guess in word:  # Если введённая буква есть в загаданном слове, то выводим соответствующее сообщение
        print("\nДа!", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):  # В цикле добавляем найденную букву в нужное место
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nИзвините, буквы \"" + guess + "\" нет в слове.")  # Если буквы нет, то выводим соответствующее сообщение
        wrong += 1

if wrong == max_wrong:  
    print(HANGMAN[wrong])
    print("\nТебя повесили!")
else:  # Если кол-во ошибок не превышено, то игрок выиграл
    print("\nВы угадали слово!")

print("\nЗагаданное слово было \"" + word + '\"')