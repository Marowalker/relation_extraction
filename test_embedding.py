import numpy as np
from data_utils import load_vocab
import constants
import os
from collections import defaultdict
import dill
import pickle
import new_embedding as ne

vocab_words = load_vocab("data/filtered_words.mini.txt")
res = ne.export_dict(vocab_words)
with open("data/vocab.mini.txt", "w") as f:
    for d in sorted(res):
        f.write(d + "\n")
