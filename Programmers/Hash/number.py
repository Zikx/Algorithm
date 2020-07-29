def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
        return True

phone1 = ['119', '97674223', '1195524421'] # False
phone2 = ['123','456','789'] # True

print(solution(phone2))