import sys
cyptext = sys.stdin.readline()

plaintext = [chr(ord(i) + 23) if i < 'D' else chr(ord(i) - 3) for i in cyptext]
print(''.join(plaintext[:len(plaintext) - 1]))

#
# plaintext = list()
# for i in cyptext:
#     if i < 'D':
#         plaintext.append(chr(ord(i) + 23))
#     else:
#         plaintext.append(chr(ord(i) - 3))

# print(''.join(plaintext[:len(plaintext) - 1]))