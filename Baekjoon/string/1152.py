import sys

string1 = "The Curious Case of Benjamin Button"
string2 = " Mazatneunde Wae Teullyeoyo "
string3 = "Teullinika Teullyeotzi "


def wordcount(word):
    word_cnt = word.strip()
    if len(word_cnt) == 0:
        return 0
    return word_cnt.count(' ') + 1

word = sys.stdin.readline()
print(wordcount(word))