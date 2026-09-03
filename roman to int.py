def romanToInt(romanInput):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    resultInteger = 0

    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i + 1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]

roman = input("Input roman numeral: ")

print("Integer equivalent : " , romanToInt(roman))