import os
import re
from nltk.corpus import wordnet as wn


datasets = ['full']
# NLPLAB_W2V = 'data/w2v_model/BioWordVec_PubMed_MIMICIII_d200.vec.bin'
NLPLAB_W2V = 'data/w2v_model/wikipedia-pubmed-and-PMC-w2v.bin'
path = "data"


def filter_words(filename=''):
    for dataset in datasets:
        res = []
        with open(os.path.join(path, "all_words" + filename + "." + dataset + ".txt")) as f:
            for line in f.readlines():
                # temp = re.sub(r'[!@#$%^&*().?":{},|<>;\']$', '', line)
                # temp = re.sub(r'^[!@#$%^&*().?":{},|<>;\']', '', temp)
                if line not in res:
                    res.append(line)
            # lemma_list = []
            # [lemma_list.append(lemma.lemmatize(word)) for word in res if lemma.lemmatize(word) not in lemma_list]
            save = open(os.path.join(path, "filtered_words" + filename + "." + dataset + ".txt"), "w")
            for token in sorted(res, key=str.lower):
                save.write(token)


def concat_words(filename):
    train = open(os.path.join(path, filename + "train.txt")).readlines()
    dev = open(os.path.join(path, filename + "dev.txt")).readlines()
    test = open(os.path.join(path, filename + "test.txt")).readlines()
    train.extend(test)
    train.extend(dev)
    all = train
    vocab = []
    for w in all:
        if w not in vocab:
            vocab.append(w)
    with open(os.path.join(path, filename + "full.txt"), "w") as f:
        for token in sorted(vocab, key=str.lower):
            f.write(token)


def save_all_synsets():
    with open('all_synsets.txt', 'w') as f:
        for ss in wn.all_synsets():
            f.write(str(ss.offset()))
            f.write('\n')
        f.close()


# concat_words("all_words.")
# filter_words()

# file = open("data/all_words_test.txt")
# lines = file.readlines()
# res = []
# for line in lines:
    # if line not in res:
        # res.append(line)
# save = open("data/filtered_words.mini.txt", "w")
# for line in sorted(res, key=str.lower):
    # save.write(line)
# save.close()

save_all_synsets()
