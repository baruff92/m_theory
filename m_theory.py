import random as rd
import sys
import numpy as np

def guess_note():
    string = rd.randint(1, 6)
    fret = rd.randint(0, 22)
    print('Which note is:')
    print(' String:', string, 'fret:', fret)

def find_notes():
    note = rd.choice(['A', 'A♯', 'B♭', 'B', 'C', 'C♯', 'D♭', 'D', 'D♯', 'E♭', 'E', 'F', 'F♯', 'G♭', 'G', 'G♯', 'A♭',
                    'La', 'La♯', 'Si♭', 'Si', 'Do', 'Do♯', 'Re♭', 'Re', 'Re♯', 'Mi♭', 'Mi', 'Fa', 'Fa♯', 'Sol♭', 'Sol', 'Sol♯', 'La♭'])
    string = rd.randint(1, 6)
    print('Find the note:')
    print('', note, 'on the string', string)

print('𝄞 Welcome to the music theory exercize for guitar ♪ ♫')

for i in np.arange(0,int(sys.argv[1])):
    test = rd.randint(0, 1)
    if(test==0): guess_note()
    if(test==1): find_notes()
    input()
