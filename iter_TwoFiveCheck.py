import csv

div08 = 0
div10 = 0
div12 = 0
arr1 = []
arr2 = []
arr3 = []
for iteration in range(1, 81):
    arr1.append(iteration)
    path = ('result_iter_%02d.txt' % iteration)
    text = open(path).read()
    print(iteration)
    text = text.replace('\n', ' ')
    chord_seq = text.split(' ')
    chars = set(chord_seq)
    text = chord_seq
    count1 = 0
    count2 = 0
    count3 = 0
    div = 0
    i = 1
    while not "diversity" in text[i]:
        if text[i].split(":")[0] == "C" and (text[i+1].split(":")[0] == "F" or "D:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "G#" and (text[i+1].split(":")[0] == "C#" or "A#:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "C#" and (text[i+1].split(":")[0] == "F#" or "D#:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "F#" and (text[i+1].split(":")[0] == "B" or "G#:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "B" and (text[i+1].split(":")[0] == "E" or "C#:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "E" and (text[i+1].split(":")[0] == "A" or "F#:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "A" and (text[i+1].split(":")[0] == "D" or "B:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "D" and (text[i+1].split(":")[0] == "G" or "E:min" in text[i+1]):
            count1 += 1

        elif text[i].split(":")[0] == "G" and (text[i+1].split(":")[0] == "C" or "A:min" in text[i+1]):
            count1 += 1
        i += 1
    i += 1
    while not "diversity" in text[i]:
        if text[i].split(":")[0] == "C" and (text[i+1].split(":")[0] == "F" or "D:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "G#" and (text[i+1].split(":")[0] == "C#" or "A#:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "C#" and (text[i+1].split(":")[0] == "F#" or "D#:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "F#" and (text[i+1].split(":")[0] == "B" or "G#:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "B" and (text[i+1].split(":")[0] == "E" or "C#:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "E" and (text[i+1].split(":")[0] == "A" or "F#:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "A" and (text[i+1].split(":")[0] == "D" or "B:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "D" and (text[i+1].split(":")[0] == "G" or "E:min" in text[i+1]):
            count2 += 1

        elif text[i].split(":")[0] == "G" and (text[i+1].split(":")[0] == "C" or "A:min" in text[i+1]):
            count2 += 1
        i += 1
    i += 1
    while i != len(text):
        if text[i].split(":")[0] == "C" and (text[i+1].split(":")[0] == "F" or "D:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "G#" and (text[i+1].split(":")[0] == "C#" or "A#:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "C#" and (text[i+1].split(":")[0] == "F#" or "D#:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "F#" and (text[i+1].split(":")[0] == "B" or "G#:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "B" and (text[i+1].split(":")[0] == "E" or "C#:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "E" and (text[i+1].split(":")[0] == "A" or "F#:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "A" and (text[i+1].split(":")[0] == "D" or "B:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "D" and (text[i+1].split(":")[0] == "G" or "E:min" in text[i+1]):
            count3 += 1

        elif text[i].split(":")[0] == "G" and (text[i+1].split(":")[0] == "C" or "A:min" in text[i+1]):
            count3 += 1
        i += 1
    div08 += count1/270 * 100
    div10 += count2/270 * 100
    div12 += count3/270 * 100
    print(count1/270 * 100)
    print(count2/270 * 100)
    print(count3/270 * 100)
    print((count1 + count2 + count3)/810 * 100)
    arr2.append((count1 + count2 + count3)/810 * 100)
    arr3.append((count2 + count3)/540 * 100)
print(arr1)
print(arr2)

f = open('twofive.csv', 'w', newline='')
wr = csv.writer(f)
wr.writerow(arr1)
wr.writerow(arr3)

f.close()
