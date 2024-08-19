import random

word_list = ['book']
chosen_word = random.choice(word_list)
end_game = False

print('THE WORD IS')
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

while end_game == False:
    user_guess = input('Guess a letter: ').lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    print(display)
    
    if '_' not in display:
        end_game = True
        print('You Won')