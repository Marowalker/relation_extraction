import re


def numbers_only(sent):
    m = re.match(r'.*[A-z]+', sent)
    if m:
        return False
    return True


def replace_parentheses(sent):
    fixed = re.sub(r'\(.*\) ', '', sent)
    return fixed


def count_ids(lines):
    count = 0
    for line in lines:
        if numbers_only(line):
            count += 1
    return count


def count_keyword(keyword, lines):
    count = 0
    for line in lines:
        if keyword in line:
            count += 1
    return count


def find_longest_path(lines):
    lengths = []
    for line in lines:
        temp = replace_parentheses(line)
        lengths.append(len(temp.split()))
    placebo = 0
    for i in range(len(lengths)):
        if lengths[i] == max(lengths):
            placebo = i
    return lines[placebo]


old = open('data/raw_data/sdp_data_acentors.dev.txt').readlines()
new = open('data/raw_data/sdp_data_acentors_test.dev.txt').readlines()
print('old numbers: ' + str(count_ids(old)))
print('new numbers: ' + str(count_ids(new)))
print('old CIDs: ' + str(count_keyword('CID', old)))
print('new CIDs: ' + str(count_keyword('CID', new)))
print('old NONEs: ' + str(count_keyword('NONE', old)))
print('new NONEs: ' + str(count_keyword('NONE', new)))
print('longest path in old: ', find_longest_path(old))
print('longest path in new: ', find_longest_path(new))
