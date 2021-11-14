# C   F   Bb  Eb  G#  C#  F#  B   E   A   D   G   C
# Am  Dm  Gm  Cm  Fm  A#m D#m G#m C#m F#m Bm  Em  Am


path = 'chord_sentences.txt'  # the txt data source
text = open(path).read()

# print(text)
chord_seq = text.split(' ')
chars = set(chord_seq)
text = chord_seq
count = 0
endcount = 0
for i in range(len(text)):
    if text[i].split(":")[0] == "C" and (text[i+1].split(":")[0] == "F" or "D:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "G#" and (text[i+1].split(":")[0] == "C#" or "A#:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "C#" and (text[i+1].split(":")[0] == "F#" or "D#:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "F#" and (text[i+1].split(":")[0] == "B" or "G#:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "B" and (text[i+1].split(":")[0] == "E" or "C#:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "E" and (text[i+1].split(":")[0] == "A" or "F#:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "A" and (text[i+1].split(":")[0] == "D" or "B:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "D" and (text[i+1].split(":")[0] == "G" or "E:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i].split(":")[0] == "G" and (text[i+1].split(":")[0] == "C" or "A:min" in text[i+1]):
        count += 1
        print(text[i], text[i+1])
    elif text[i] == "_END_":
        endcount += 1

print(count/(len(text)-1) * 100)
print(count/(len(text) - endcount*3 + 1) * 100)
