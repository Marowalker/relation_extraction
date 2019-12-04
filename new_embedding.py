import numpy as np
from data_utils import load_vocab
import constants
import os
from collections import defaultdict
import dill
import pickle

# NLPLAB_W2V = 'data/w2v_model/wikipedia-pubmed-and-PMC-w2v.bin'
NLPLAB_W2V = 'data/w2v_model/BioWordVec_PubMed_MIMICIII_d200.vec.bin'
path = "data"
# datasets = ['train', 'dev', 'test']
datasets = ['full']


def export_dict(vocab, dim=200, bin=NLPLAB_W2V):
    res = defaultdict(lambda: np.zeros(dim))
    embeddings = np.zeros([len(vocab) + 1, dim])
    with open(bin, 'rb') as f:
        header = f.readline()
        vocab_size, layer1_size = map(int, header.split())
        print('nlplab vocab size', vocab_size)
        binary_len = np.dtype('float32').itemsize * layer1_size

        count = 0
        m_size = len(vocab)
        for line in range(vocab_size):
            word = []
            while True:
                ch = f.read(1)
                if ch == b' ':
                    word = b''.join(word)
                    break
                if ch != b'\n':
                    word.append(ch)
            word = word.decode("utf8", errors="ignore")

            if word in vocab:
                count += 1
                embedding = np.fromstring(f.read(binary_len), dtype='float32')
                # word_idx = vocab[word]
                # embeddings[word_idx] = embedding
                # print(word)
                res[word] = embedding
            else:
                f.read(binary_len)

    print('Missing rate {}'.format(1.0 * (m_size - count)/m_size))
    return res


def export_trimmed_nlplab_vectors(vocab, trimmed_filename, dim=200, bin=NLPLAB_W2V):
    """
    Saves glove vectors in numpy array

    Args:
        vocab: dictionary vocab[word] = index
        trimmed_filename: a path where to store a matrix in npy
        dim: (int) dimension of embeddings
        :param bin:
    """
    # embeddings contains embedding for the pad_tok as well
    embeddings = np.zeros([len(vocab) + 1, dim])
    with open(bin, 'rb') as f:
        header = f.readline()
        vocab_size, layer1_size = map(int, header.split())
        print('nlplab vocab size', vocab_size)
        binary_len = np.dtype('float32').itemsize * layer1_size

        count = 0
        m_size = len(vocab)
        for line in range(vocab_size):
            word = []
            while True:
                ch = f.read(1)
                if ch == b' ':
                    word = b''.join(word)
                    break
                if ch != b'\n':
                    word.append(ch)
            word = word.decode("utf-8")

            if word in vocab:
                count += 1
                embedding = np.fromstring(f.read(binary_len), dtype='float32')
                word_idx = vocab[word]
                embeddings[word_idx] = embedding
            else:
                f.read(binary_len)

    print('Missing rate {}'.format(1.0 * (m_size - count)/m_size))
    np.savez_compressed(trimmed_filename, embeddings=embeddings)


#for dataset in datasets:
#    vocab_words = load_vocab(os.path.join(path, "filtered_words." + dataset + ".txt"))
#    if not os.path.exists("data/w2v_model/embedding_dict.pkl"):
#        res = export_dict(vocab_words)
#        with open("data/w2v_model/embedding_dict.pkl", "wb") as file:
#            dill.dump(res, file)
#    else:
#        with open("data/w2v_model/embedding_dict.pkl", "rb") as file:
#            res = dill.load(file)

    # if not os.path.exists("data/w2v_model/dict_biowordvec.npz"):
    #    embeddings = np.zeros([len(res) + 1, 200])
    #    count = 0
    #    for d in res:
    #        embeddings[count] = res[d]
    #        count += 1
    #    np.savez_compressed("data/w2v_model/dict_biowordvec.npz", embeddings=embeddings)

#    if not os.path.exists("data/w2v_model/dict_w2v.npz"):
#        embeddings = np.zeros([len(res) + 1, 200])
#        count = 0
#        for d in res:
#            embeddings[count] = res[d]
#            count += 1
#        np.savez_compressed("data/w2v_model/dict_w2v.npz", embeddings=embeddings)

#    with open(os.path.join(path, "vocab.full.txt"), "w") as f:
#        for d in sorted(res):
#            f.write(d + "\n")

vocab_words = load_vocab(constants.ALL_WORDS)
export_trimmed_nlplab_vectors(vocab_words, 'biowordvec_nlplab.npz')
