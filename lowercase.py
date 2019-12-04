import re
import os


def replacement(match):
    return match.group(0).lower()


def to_lowercase(file):
    lines = file.readlines()
    res = []
    for line in lines:
        temp = []
        for token in line.split():
            # reg = r".*\\"
            # tok = re.sub(reg, replacement, token)
            # reg2 = r"\|.*"
            # tok = re.sub(reg2, replacement, tok)
            # reg = r"[A-Z]+.*[a-z]+.*/"
            # tok = re.sub(reg, replacement, token)
            # temp.append(tok)
            if token.find('/') != -1:
                w, p, s = token.rsplit('/', 2)
                w = w.lower()
                temp.append(w + '/' + p + '/' + s)
            else:
                temp.append(token)
        sent = ' '.join(temp)
        res.append(sent)
    return res


datasets = ["train", "dev", "test"]
path = "data/raw_data"
for dataset in datasets:
    print("Process dataset: " + dataset)
    with open(os.path.join(path, "sdp_data_acentors_pos_synset." + dataset + ".txt")) as f:
        res = to_lowercase(f)
    with open(os.path.join(path, "sdp_data_acentors_pos_synset_lower." + dataset + ".txt"), "w") as save:
        for sent in res:
            save.write(sent)
            save.write('\n')
print("Done.")

print("Build new vocab...")
file = open("data/vocab.txt")
lines = file.readlines()
save = open("data/vocab_lower.txt", "w")
temp = []
for line in lines:
    if line.lower() not in temp:
        temp.append(line.lower())
for line in temp:
    save.write(line)
save.close()
print("Done.")



