from keras.models import load_model
import numpy as np
import sys

model = load_model('60iter_single_lstm_dropout.h5')
testtext = open('testset.txt').read()
testtext = testtext.split(' ')

path = 'chord_sentences.txt'
text = open(path).read()
chord_seq = text.split(' ')
chars = set(chord_seq)
text = chord_seq
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))
num_chars = len(char_indices)

maxlen = 20
step = 3
sentences = []
next_chars = []


def sample(a, temperature=1.0):
    # helper function to sample an index from a probability array
    a = np.log(a) / temperature
    dist = np.exp(a) / np.sum(np.exp(a))
    choices = range(len(a))
    return np.random.choice(choices, p=dist)


with open(('60iter_single_lstm_dropout_generated.txt'), 'w') as f_write:
    print('----- diversity:', 1.0)

    generated = []
    start_index = 1

    sentence = testtext[start_index: start_index + maxlen]
    seed_sentence = testtext[start_index: start_index + maxlen]

    generated = generated + sentence

    print('----- Generating with seed:')

    print(' '.join(sentence))

    num_char_pred = 3000

    for i in range(num_char_pred):
        x = np.zeros((1, maxlen, num_chars))

        for t, char in enumerate(sentence):
            x[0, t, char_indices[char]] = 1.

        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, 1.0)
        next_char = indices_char[next_index]

        generated.append(next_char)
        sentence = sentence[1:]
        sentence.append(next_char)

        sys.stdout.flush()
    print()
    f_write.write(' ' .join(generated))
