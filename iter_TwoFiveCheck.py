for iteration in range(1, 40):
    path = ('result_iter/result_iter_%02d.txt' % iteration)
    text = open(path).read()
    print(iteration)
    chord_seq = text.split(' ')
    chars = set(chord_seq)
    text = chord_seq
    count = 0
    endcount = 0
    for i in range(len(text)-1):
        if text[i].split(":")[0] == "C" and (text[i+1].split(":")[0] == "F" or "D:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "G#" and (text[i+1].split(":")[0] == "C#" or "A#:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "C#" and (text[i+1].split(":")[0] == "F#" or "D#:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "F#" and (text[i+1].split(":")[0] == "B" or "G#:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "B" and (text[i+1].split(":")[0] == "E" or "C#:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "E" and (text[i+1].split(":")[0] == "A" or "F#:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "A" and (text[i+1].split(":")[0] == "D" or "B:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "D" and (text[i+1].split(":")[0] == "G" or "E:min" in text[i+1]):
            count += 1

        elif text[i].split(":")[0] == "G" and (text[i+1].split(":")[0] == "C" or "A:min" in text[i+1]):
            count += 1

        elif text[i] == "_END_":
            endcount += 1

    print(count/(len(text)-1) * 100)
    print(text)
