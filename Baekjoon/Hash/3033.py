# 가장 긴 수
# 라빈-카프 알고리즘 활용

s_input ="sabcabcfabc"

def f_3033(s):
    rtn = list()
    cnt = 0
    for i in range(len(s)):
        for j in range(len(s) + 1):
            if s.count(s[i:j]) > 1 and len(s[i:j]) >= 2 and s[i:j] != "":
                rtn.append(s[i:j])
    
    return rtn

print(set(f_3033(s_input)))