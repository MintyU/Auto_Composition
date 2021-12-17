from collections import Counter
import matplotlib.pyplot as plt

for iteration in range(1, 81):
    path = ('result_iter_%02d.txt' % iteration)
    text = open(path).read()
    print(iteration)
    text = text.replace('\n', ' ')
    chord_seq = text.split(' ')
    chars = set(chord_seq)
    text = chord_seq
    cnt = Counter(text)
    print(cnt.most_common())
    plt.bar(cnt.keys(), cnt.values())
    plt.show()

# path = ("chord_sentences.txt")
# text = open(path).read()
# chord_seq = text.split(' ')
# chars = set(chord_seq)
# text = chord_seq
# cnt = Counter(text)
# print(cnt.most_common())
# plt.bar(cnt.keys(), cnt.values())
# plt.show()
