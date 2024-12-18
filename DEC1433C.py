def inppt():
    strs = input()
    wd = strs.split('-')
    return strs, wd

def Violationword(keyword):
    banword = {'FUC', 'FUG', 'FUQ', 'FUT', 'GPU', 'KGB', 'KKK', 'KMT', 'DPP', 'PUG', 'PUP', 'CAT', 'ANT', 'APE', 'MAD', 'NUN', 'SEX', 'SLY', 'BAD', 'GAY', 'ASS', 'BUM', 'BRA', 'CRY'}
    if len(keyword) != 3 or keyword in banword or any(c in keyword for c in "IO"):
        return True
    else:
        return False

def numsize(numword):
    if len(numword) != 4 or '4' in numword:
        return True
    else:
        return False

def main():
    strs, words = inppt()
    if len(words) != 2:  # Check if the input has the correct format (two parts separated by '-')
        print(strs + ' is Invalid license plate number.')
        return

    keyword = words[0]
    numword = words[1]
    if Violationword(keyword) or numsize(numword):
        print(strs + ' is Invalid license plate number.')
    else:
        print(strs + ' is Valid license plate number.')

main()