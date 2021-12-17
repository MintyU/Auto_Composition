# from keras.models import Sequential
# from keras.layers.core import Dense, Activation, Dropout
# from keras.layers.recurrent import LSTM
# from keras.utils.data_utils import get_file
# import numpy as np
# import random
# import sys
# import keras

# new_model = keras.models.load_model('60iter_multi_lstm_dropout.h5')

# from rouge_metric import PyRouge

# # Load summary results
# hypotheses = [
#     'C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj G:7 G:7 G:7 G:7 C:maj C:maj C:maj C:maj A:min7 A:min7 A:min7 A:min7 D:min7 D:min7 D:min7 D:min7 G:7 G:7 G:7 G:7 C:maj C:maj C:maj C:maj D:7 D:7 D:7 D:7 C:maj7 C:maj7 C:maj7 C:maj7 C:maj7 C:maj7 C:maj7 C:maj7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj D:maj D:maj D:maj D:maj E:7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 D:maj D:maj D:maj D:maj A:maj A:maj A:maj A:maj D:maj D:maj D:maj D:maj E:7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj D:maj D:maj E:7 E:7 A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj A:maj D:maj D:maj D:maj D:maj A:maj A:maj A:maj A:maj']
# references = [[
#     "D:min7 D:min7 G:7 G:7 D:min D:min G:7 G:7 C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj D:min7 D:min7 G:7 G:7 D:min D:min G:7 G:7 C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj A:maj A:maj E:7 E:7 A:7 A:7 A:7 A:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 D:7 E:dim G:7 E:dim G:7 G:7 A:dim C:maj B:7 D:min7 D:min7 G:7 G:7 D:min D:min G:7 G:7 C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj D:min7 D:min7 G:7 G:7 D:min D:min G:7 G:7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 E:7 G:min G:min A:7 A:7 G:min6 G:min6 A:9 A:9 D:min D:min A:7 A:7 D:min D:min D:min D:min D:min7 D:min7 G:7 G:7 D:min D:min G:7 G:7 C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj C:maj"
# ]]
# # Evaluate document-wise ROUGE scores
# rouge = PyRouge(rouge_n=(1, 2, 4), rouge_l=True, rouge_w=True,
#                 rouge_w_weight=1.2, rouge_s=True, rouge_su=True, skip_gap=4)
# scores = rouge.evaluate(hypotheses, references)
# print(scores)
import pandas as pd
path = 'chord_sentences.txt'  # the txt data source
text = open(path).read()
chord_seq = text.split(' ')
text = chord_seq
text2 = []
temp = ""

for chord in text:
    if chord == "_START_" or chord == "_END_":
        pass
    elif chord.split(":")[0] == temp:
        pass

    else:
        temp = chord.split(":")[0]
        text2.append(temp)


pd.crosstab(pd.Series(text2[1:], name='To'), pd.Series(
    text2[:-1], name='From'), normalize=1).style.background_gradient(cmap='rainbow')
