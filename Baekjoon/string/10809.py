import sys

word_S = sys.stdin.readline()
rtnList = [ str(word_S.find(chr(i))) for i in range(97,123)]

print(' '.join(rtnList))