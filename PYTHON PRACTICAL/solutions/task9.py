
import re


def create_account(user_name, password, secret_words):
    tempDict = {'up': 0, 'low': 0, 'dig': 0, 'spec': 0}
    tempDict['up'] = len(re.findall(r'[A-Z]', password)) != 0
    tempDict['low'] = len(re.findall(r'[a-z]', password)) != 0
    tempDict['dig'] = len(re.findall(r'\d{1}', password)) != 0
    tempDict['spec'] = len(re.findall(
        r'[|!|@|#|$|%|^|&|*|(|)|_|+|=]', password)) != 0
    for key in tempDict:
        if not tempDict[key]:
            raise ValueError

    def check(own_password, checklist):
        if own_password == password and len(checklist) == len(secret_words):
            temp = [] + secret_words
            for item in checklist:
                if item in temp:
                    temp.pop(temp.index(item))
            return len(temp) <= 1
        else:
            return False

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])

# print(check1,check2,check3,check4)
