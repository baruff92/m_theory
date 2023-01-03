import random as rd
import sys
import numpy as np
import musicalbeeps

player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)

notes_engl = ['A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab']
notes_it = ['La', 'La#', 'Sib', 'Si', 'Do', 'Do#', 'Reb', 'Re', 'Re#', 'Mib', 'Mi', 'Fa', 'Fa#', 'Solb', 'Sol', 'Sol#', 'Lab']

def guess_note():
    string = rd.randint(1, 6)
    fret = rd.randint(0, 22)
    print('Which note is:')
    print(' String:', string, 'fret:', fret)

def find_notes():
    note_i = rd.randint(0, len(notes_engl)-1)
    if(rd.randint(0,1)): note = notes_it[note_i]
    else: note = notes_engl[note_i]
    string = rd.randint(1, 6)
    note = note.replace("b", "♭")
    note = note.replace("#", "♯")
    print('Find the note:')
    print('', note, 'on the string', string)
    player.play_note(notes_engl[note_i],2)

print('𝄞 Welcome to the music theory exercize for guitar ♪ ♫')

for i in np.arange(0,int(sys.argv[1])):
    test = rd.randint(0, 1)
    if(test==0): guess_note()
    if(test==1): find_notes()
    input()
