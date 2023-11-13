import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['banana', 'apple', 'mango', 'grapes', 'papaya', 'good', 'bad', 'sleep', 
'weep', 'hello', 'god', 'system', 'computer']


chosen_words = random.choice(word_list)

word_len = len(chosen_words)

display=[]
for i in range(0,word_len):
    display.append("_")
l=[]
for j in range(0,(len(chosen_words))//2):
    r = random.randrange(0,len(chosen_words))
    if r not in l:
        l.append(r)
        display[r]=chosen_words[r]

print(display)


s=7

while(s!=0):
    guess = input("guess a letter:-")
    f=0
    for i in range(0,word_len):
        if chosen_words[i] == guess:
            display[i]=guess
        else:
            f=f+1
    print(display)
    if(list(chosen_words)==display):
        print("you win")
        break

    if(f==word_len):
        print(f"try again! you have only {s-1} chance ")
        s=s-1
        print(stages[s])
    if(s==0):
        print("you loose")
    


