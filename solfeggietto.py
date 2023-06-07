#Solfeggietto
m=['E3 C3 E3 G3 C4 E4 D4 C4 B3nG3 B3nD4 G4 F4 E4 D4 ',
   'E4 C4 E4 G4 C5 E5 D5 C5 D5 C5 B4nA4nG4 F4 E4 D4 ',
   'E4 C4 E4 G4 C5 E5 D5 C5 B4nG4 B4nD5 G5 F5 E5 D5 ',
   'E5 C5 E5 G5 C6 E6 D6 C6 D6 C6 B5nA5nG5 F5 E5 D5 ',

   'E5 C5 G4 E4 C4 C6 G5 E5 A5 F3 A3 C4 F4 A4 C5 E5 ',
   'D5 B4 F4 D4 B3 B5 F5 D5 G5 E3 G3 B3 E4 G4 B4 D5 ',
   'C5 A4nG4#A4nC5 A4nG4#A4nE5 C5 G4nA4nE5 C5 G4 A4n',
   'D5 C5 F4#A4nA5nC5 F4#A4nF5#C5 D4 A4nC5 A4nF4#D4 ',
   
   'B4 G2 B2 D3 G3 B3 A3nG3 F3#D3 F3#A3nD4 C4 B3 A3n',
   'B3 G3 B3 D4 G4 B4 A4nG4 A4nG4 F4#E4nD4 C4 B3 A3n',
   'B3 G3 B3 D4 G4 B4 A4nG4 F4#D4 F4#A4nD5 C5 B4 A4n',
   'B4 G4 B4 D5 G5 B5 A5nG5 A5nG5 F5#E5nD5 C5 B4 A4n',
   
   'B4 G4 B4 D5 G5 D5 B4 G4 F3 G5 D5 B4nG4 B4nD5 G5 ',
   'C5 G4 G5 G4 C5 G4 G5 G4 B4nG4 F5 G4 B4nG4 F5 G4 ',
   'E5 C5 E5 G5 C6 G5 E5 C5 B3 C6 G5 E5nC5 E5nG5 C5 ',
   'F5 C5 C6 C5 F5 C5 C6 C5 E5nC5 B5 C5 E5nC5 B5 C5 ',
   
   'A5 F2 A2 C3 F3 A3 G3 F3 E3nC3 E3nG3 C4 B3 A3 G3 ',
   'A3 F3 A3 C4 F4 A4 G4 F4 G4 F4 E4nD4 C4 B3 A3 G3 ',
   'A3 F3 A3 C4 F4 A4 G4 F4 E4nC4 E4nG4 C5 B4 A4 G4 ',
   'A4 F4 A4 C5 F5 A5 G5 F5 G5 F5 E5nD5 C5 B4 A4 G4 ',
   
   'A4 F5 C5 A4 F4 C5 A4 F4 C4 A4 F4 C4 A3 F4 C4 A3 ',
   'D3bD3bD3bD3bD3bD3bD3bD3bA5 F5 E5nF5 G5 F5 E5nF5 ',
   'C3 C3 C3 C3 C3 C3 C3 C3 A4 F4 E4nF4 G4 F4 E4nF4 ',
   'B2nB2nB2nB2nB2nB2nB2nB2nD6 F5 G5 A5 G5 F5 E5bD5 ',

   'E5 G5 C6 G5 B5 A5 G5 F5 E5 E5 E5 E5 D5 D5 D5 D5 ',
   'C5 G4 G5 G4 C5 G4 G5 G4 B4nG4 F5 G4 B4nG4 F5 G4 ',
   'B4 G4 E5nG4 B4 G4 E5nG4 A4nE5 C6 E5 A4nE5 C6 E5 ',
   'A4bF4 D5 F4 A4 F4 D5 F4 G4 D5bB5 D5bG4 D5bB5 D5b',

   'F4#E4 C5 E4 F4#E4 C5 E4 E4 C5 C6 C5 E4 C5 C6 C5 ',
   'E4 C5 E5 G5 C6 G5 E5 C5 G5 E5 C5 G4 F5 D5 B4nF4 ',
   'E4 C3nE3 G3 C4 E4 D4 C4 B3nG3 B3nD4 G4 F4 E4 D4 ',
   'E4 C4 E4 G4 C5 E5 D5 C5 D5 C5 B4nA4nG4 F4 E4 D4 ',

   'E4 C4 E4 G4 C5 E5 D5 C5 B4nG4 B4nD5 G5 F5 E5 D5 ',
   'E5 C5 E5 G5 C6 E6 D6 B5nC6 G5 E5 D5 C5 G4 E4 D4 ',

   'C4 ']
   
key = {'A':'b',
       'B':'b',
       'C':' ',
       'D':' ',
       'E':'b',
       'F':' ',
       'G':' '}

string = [40,45,50,55,59,64]    #Standard Tuning
top_fret = [19,19,20,21,22,24]  #Highest reachable fret per string
shift = -1                      #Offset the score by this amount

def midi_value(n):
    ''' returns the midi note of a 3 character note and key '''
    midi_offset = {'A':9,'B':11,'C':0,'D':2,'E':4,'F':5,'G':7}
    # start with the value of the octave and note
    val = 12+int(n[1])*12 + midi_offset[n[0]]
    # adjust for incidentals or key signature
    if n[2] == '#':
        val = val + 1
    elif n[2] == 'b':
        val = val - 1
    elif n[2] == 'n':
        val = val + 0 #natural - cancels key sig
    elif key[n[0]] == '#':
        val = val + 1
    elif key[n[0]] == 'b':
        val = val -1
    val = val + shift
    return val

def prep_music():
    music = []
    bar = []
    for measure in m:
        z = []
        for n in range(len(measure)//3):
            z.append(measure[n*3:n*3+3])
        bar.append(z)
#    print bar
    for n in bar:
        notes = [midi_value(x) for x in n]
        music.append(notes)
    return music

def print_tab(notes):
    for s in [5,4,3,2,1,0]:
        tab = '|'
        for n in range(len(notes)):
            tab = tab + '-'
            fret = notes[n]-string[s]
            if (fret < 10) or (fret>top_fret[s]):
                tab = tab + '-'
            if (fret < 0) or (fret>top_fret[s]):
                tab = tab + '-'
            else:
                tab = tab + str(notes[n]-string[s])
            if (n & 15)==15:
                tab = tab + '-|'
        print(tab)
    print('')

def go():
    z = prep_music()
    for x in range(len(m)//2):
        notes = z[x*2]+z[x*2+1]
        print_tab(notes)

go()
