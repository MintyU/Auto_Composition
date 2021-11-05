import music21


us = music21.environment.UserSettings()
us.delete()
us.create()

# for key in sorted(us.keys()):
#     print(key)

print(us['midiPath'])
us['midiPath'] = '/Applications/APPlayMIDI.app'
print(us['midiPath'])

f = music21.note.Note("F4")

# Notes
c = music21.note.Note("C4")
csh = music21.note.Note("C#4")
d = music21.note.Note("D4")
dsh = music21.note.Note("D#4")
e = music21.note.Note("E4")
f = music21.note.Note("F4")
fsh = music21.note.Note("F#4")
g = music21.note.Note("G4")
gsh = music21.note.Note("G#4")
a = music21.note.Note("A4")
ash = music21.note.Note("A#4")
b = music21.note.Note("B4")

# Chords
cMaj = ["C", "E", "G"]
cMin = ["C", "E-", "G"]
aSev = ["A", "C#", "E", "G"]
dSev = ["D", "F#", "A", "C"]
eSev = ["E", "G#", "B", "D"]
gSev = ["G", "B", "D", "F"]
dMinSev = ["D", "F", "A", "C"]


score = music21.stream.Stream()

# score.append(music21.chord.Chord(cMaj, quarterLength=4))
# score.append(music21.chord.Chord(aSev, quarterLength=4))
# score.append(music21.chord.Chord(dSev, quarterLength=4))
# score.append(music21.chord.Chord(dSev, quarterLength=2))
# score.append(music21.chord.Chord(gSev, quarterLength=2))
# score.append(music21.chord.Chord(cMaj, quarterLength=4))
# score.append(music21.chord.Chord(cMaj, quarterLength=2))
# score.append(music21.chord.Chord(gSev, quarterLength=2))
# score.append(music21.chord.Chord(cMaj, quarterLength=4))
# score.append(music21.chord.Chord(eSev, quarterLength=2))
# score.append(music21.chord.Chord(aSev, quarterLength=2))
# score.append(music21.chord.Chord(dMinSev, quarterLength=4))
# score.append(music21.chord.Chord(cMaj, quarterLength=2))
# score.append(music21.chord.Chord(dMinSev, quarterLength=2))
# score.append(music21.chord.Chord(cMaj, quarterLength=4))
'''
--------------------------------------------------------------
'''
# score.append(music21.chord.Chord("E G B D", quarterLength=4))
# score.append(music21.chord.Chord("D# F# A", quarterLength=4))
# score.append(music21.chord.Chord("D F A C", quarterLength=4))
# score.append(music21.chord.Chord("G B D F A", quarterLength=1))
# score.append(music21.chord.Chord("E G B D", quarterLength=1))
# score.append(music21.chord.Chord("A# D F G#", quarterLength=1))
# score.append(music21.chord.Chord("A C# E G", quarterLength=1))
# score.append(music21.chord.Chord("D F A C", quarterLength=4))
# score.append(music21.chord.Chord("G B D F", quarterLength=4))
# score.append(music21.chord.Chord("D F A C", quarterLength=2))
# score.append(music21.chord.Chord("A C# E G", quarterLength=2))
'''
--------------------------------------------------------------
'''
score.append(music21.chord.Chord(cMaj, quarterLength=2))
score.append(music21.chord.Chord("F A C E-", quarterLength=2))
score.append(music21.chord.Chord(cMaj, quarterLength=2))
score.append(music21.chord.Chord("A C E G", quarterLength=2))
score.append(music21.chord.Chord(dMinSev, quarterLength=2))
score.append(music21.chord.Chord(gSev, quarterLength=2))
score.append(music21.chord.Chord(cMaj, quarterLength=2))
score.append(music21.chord.Chord("D# G A# C", quarterLength=2))
score.append(music21.chord.Chord("F A C E", quarterLength=2))
score.append(music21.chord.Chord("D F A-", quarterLength=2))
score.append(music21.chord.Chord(cMaj, quarterLength=2))
score.append(music21.chord.Chord("A C# E G", quarterLength=2))
score.append(music21.chord.Chord(dMinSev, quarterLength=2))
score.append(music21.chord.Chord(gSev, quarterLength=2))
score.append(music21.chord.Chord(cMaj, quarterLength=2))
score.append(music21.chord.Chord("F A C E-", quarterLength=2))
score.append(music21.chord.Chord("D# G A#", quarterLength=2))
score.append(music21.chord.Chord("D# G A# C#", quarterLength=2))
score.append(music21.chord.Chord("G# C D# F#", quarterLength=2))
score.append(music21.chord.Chord("A C E-", quarterLength=2))
score.append(music21.chord.Chord(dMinSev, quarterLength=2))
score.append(music21.chord.Chord("A# D F G#", quarterLength=2))
score.append(music21.chord.Chord("D# G A#", quarterLength=2))
score.append(music21.chord.Chord("A C# E G", quarterLength=2))

# score.show('midi')
# score.write("midi", "result_iter_39(div_1.00).mid")
# score.write("midi", "result_iter_16(div_1.20).mid")
score.write("midi", "result_iter_35(div_1.20).mid")
