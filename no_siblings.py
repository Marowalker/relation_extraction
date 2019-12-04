import re
import os
from nltk.corpus import wordnet as wn


datasets = ['train', 'dev', 'test']
# datasets = ['test']

input_path = 'data/raw_data'


def numbers_only(sent):
    m = re.match(r'.*[A-z]+', sent)
    if m:
        return False
    return True


def replace_pos(word):
    res = word
    # if not check_parentheses(line):
    if res.find('|') != -1:
        w = res.split('|')[0]
        res = w.replace('\\', '/')
        # print(w1)
        # res = w1.lower() + '/' + p + "/" + replace
        # res = w1 + '|' + p
    # res = re.sub(reg, replace + "|", word)
    return res


for dataset in datasets:
    print("Process dataset: " + dataset)
    with open(os.path.join(input_path, "sdp_data_acentors." + dataset + ".txt"), 'r') as f:
        lines = f.readlines()
    with open(os.path.join(input_path, "sdp_data_acentors_original." + dataset + ".txt"), 'w') as f2:
        for line in lines:
            if numbers_only(line):
                f2.write(line)
            else:
                temp = line.split()[:2]
                # print(temp)
                for token in line.split()[2:]:
                    # print(token)
                    t = replace_pos(token)
                    temp.append(t)
                sent = ' '.join(temp)
                f2.write(sent)
                f2.write('\n')