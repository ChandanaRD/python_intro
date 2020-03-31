# https://www.hackerrank.com/challenges/the-minion-game/problem
# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# can be further optimised
def minion_game(string):
    # your code goes here
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    stuart = []
    kevin = []
    for i in range(0, len(string)):
        if vowels.__contains__(string[i]):
            for j in range(i+1, len(string)+1 ):
                kevin.append(string[i:j])
        else:
            for j in range(i+1, len(string)+1):
                stuart.append(string[i:j])
    if(len(kevin) == len(stuart)):
        print('Draw')
    elif len(kevin) < len(stuart):
        print('Stuart ' + str(len(stuart)))
    else:
        print('Kevin ' + str(len(kevin)))

if __name__ == '__main__':
    s = input()
    minion_game(s)