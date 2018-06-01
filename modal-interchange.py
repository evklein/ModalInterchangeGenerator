# Chord finder

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
modes = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian']

majorIntervals = [2, 2, 1, 2, 2, 2, 1]
majorChordTypes = ['', 'min', 'min', '', '', 'min', 'dim']
dorianIntervals = [2, 1, 2, 2, 2, 1, 2]
dorianChordTypes = ['min', 'min', '', '', 'min', 'dim', '']
phrygianIntervals = [1, 2, 2, 2, 1, 2, 2]
phrygianChordTypes = ['min', '', '', 'min', 'dim', '', 'min']
lydianIntervals = [2, 2, 2, 1, 2, 2, 1]
lydianChordTypes = ['', '', 'min', 'dim', '', 'min', 'min']
mixolydianIntervals = [2, 2, 1, 2, 2, 1, 2]
mixolydianChordTypes = ['', 'min', 'dim', '', 'min', 'min', '']
minorIntervals = [2, 1, 2, 2, 1, 2, 2]
minorChordTypes = ['min', 'dim', '', 'min', 'min', '', '']
locrianIntervals = [1, 2, 2, 1, 2, 2, 2]
locrianChordTypes = ['dim', '', 'min', 'min', '', '', 'min']

modeIntervals = [majorIntervals, dorianIntervals, phrygianIntervals, lydianIntervals, mixolydianIntervals, minorIntervals, locrianIntervals]
modeChordTypes = [majorChordTypes, dorianChordTypes, phrygianChordTypes, lydianChordTypes, mixolydianChordTypes, minorChordTypes, locrianChordTypes]

def getMajorChords(key):
    keyIndex = 0
    for i in range(0, len(notes)):
        if (notes[i] == key):
            keyIndex = i

    print(' + ' + key)
    for i in range(0, len(majorIntervals) - 1):
        keyIndex += majorIntervals[i]
        if (keyIndex >= len(notes)):
            keyIndex -= len(notes)
        print(' + ' + notes[keyIndex] + majorChordTypes[i + 1])

def getMinorChords(key):
    keyIndex = 0
    for i in range(0, len(notes)):
        if (notes[i] == key):
            keyIndex = i

    print(' + ' + key + 'min')
    for i in range(0, len(majorIntervals) - 1):
        keyIndex += minorIntervals[i]
        if (keyIndex >= len(notes)):
            keyIndex -= len(notes)
        print(' + ' + notes[keyIndex] + minorChordTypes[i + 1])

def getAllChordsInKey(key):
    print('Warning: Make sure the current key has been transposed to Ionian for correct results')
    originalKeyIndex = 0
    keyIndex = 0
    for i in range(0, len(notes)):
        if (notes[i] == key):
            keyIndex = i
            originalKeyIndex = i

    chords = []
    rawChords = []
    for i in range(0, len(modes)):
        mode = modes[i]
        intervals = modeIntervals[i]
        chordTypes = modeChordTypes[i]
        
        for j in range(0, len(intervals)):
            # Search for duplicates and mark
            chordToAdd = notes[keyIndex] + chordTypes[j]
            chordIsNew = True
            for k in range(0, len(rawChords)):
                if (rawChords[k] == chordToAdd):
                    # Same chord, new mode
                    for l in range(0, len(chords)):
                        if (chordToAdd == chords[l][0:len(chordToAdd)]):
                            chords[l] = chords[l] + ' | ' + mode
                            chordIsNew = False
                            break
                    break
                    
            if chordIsNew:
                chords.append(chordToAdd + getFormattingSpace(len(chordToAdd)) + ' | ' + mode)
                rawChords.append(chordToAdd)

            keyIndex += intervals[j]
            if (keyIndex >= len(notes)):
                keyIndex -= len(notes)
            
        keyIndex = originalKeyIndex

    return chords


def getAllChordsForKey(key, mode):
    print('Getting all possible chords in all possible modes for the key of ' + key + ' ' + mode + '.')
    if mode == 'major':
        return getAllChordsInKey(key)
    elif mode == 'minor':
        keyIndex = 0
        for i in range(0, len(notes)):
            if (notes[i] == key):
                keyIndex = i
                break
        keyIndex += 3
        if (keyIndex >= len(notes)):
            keyIndex -= len(notes)
        return getAllChordsInKey(notes[keyIndex])
                    
def getFormattingSpace(strLength):
    string = ''
    for i in range(0, 5 - strLength):
        string = string + ' '
    return string


while True:
    note = input("Please enter the note: ")
    mode = input("Please enter minor or major: ")
    chords = getAllChordsForKey(note, mode)
    chords.sort()
    for i in range(0, len(chords)):
        print(chords[i])
    print('\n')
