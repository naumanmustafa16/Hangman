# Write your code here
# import random
# print('''H A N G M A N
# The game will be available soon.''')
# word_list = ['python', 'java', 'kotlin', 'javascript']
# random_word = random.choice(word_list)
# print(random_word)
# todisplay = random_word.replace(random_word,'-'*len(random_word[3:len(random_word)]))
# word = input(f'Guess the word {random_word[:3]}{todisplay}:')
# if word == random_word:
#     print('You survived!')
# else:
#     print('You are hanged!')
#
import random
print('H A N G M A N')
word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(word_list)
todisplay = random_word.replace(random_word,'-'*len(random_word))

def character_index(string,char):
    global pos
    pos=[]
    for i in range(len(string)):
        if string[i] == char:
            pos.append(i)
    return pos

# def repeated_words(a):
#     global repeated
#     repeated =[]
#     repeated.extend(a)
#     return repeated
repeated = []
i=0
assci_check= ('abcdefghijklmnopqrstuvwxyz')
while True:
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice == 'play':

        while i <= 7:
            print(f'\n{todisplay}')
            global letter
            letter = input('Input a letter: ')


            if len(letter) > 1:
                print('You should print a single letter')
                continue

            elif letter not in assci_check:
                print('It is not an ASCII lowercase letter')
                continue

            if letter in random_word:
                character_index(random_word, letter)

                for j in range(len(pos)):
                    todisplay_list = list(todisplay) # converts todisplay string to todisplay list
                    todisplay_list[pos[j]] = letter # Make assignment of the list element with the entered letter.
                    todisplay = ''.join(todisplay_list) # converts list to string


            if letter in repeated:
                print('You already typed this letter')
            # i += 1



            elif letter not in random_word:
                print('No such letter in the word')
                i += 1
            repeated.append(letter)
    # print(repeated)
    # print(i)
            if i <= 7 and todisplay ==random_word:
                print('''You guessed the word!
        You survived!''')
                break
            elif i ==8 and todisplay != random_word:
                print('You are hanged!')
# print('''\nThanks for playing!
# We'll see how well you did in the next stage''')
    elif user_choice == 'exit':
        break
    else:
        continue