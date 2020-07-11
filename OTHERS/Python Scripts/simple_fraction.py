x = '5/2 '

divisor, divide = x.split('/')
divisor, divide = int(divisor), int(divide)

main_quotient = divisor // divide
main_remainder = divisor % divide

remainder_quotient = [(main_remainder,main_quotient)]
repeater_remainder_quotient = []

repeater_quotient = []
repeater_remainder = []

i = 0
remainder = 1
quotient = 0
found = ''
repeater_found = ''

while main_remainder != 0:
    y = remainder_quotient[i][0]
    count = 0
    while y < divide:
        y = y * 10
        count += 1
    if count != 1:
        for c in range(count-1):
            pair = (int(y/pow(10,(count-c)-1)),0)
            if pair in remainder_quotient[1:]:
                found = True
                repeater_remainder_quotient.append(pair)
                break
            else:
                remainder_quotient.append(pair)
            i +=1
    if found == True:
        break
    else:
        remainder = y % divide
        quotient = y // divide
        if (remainder,quotient) not in remainder_quotient[1:]:
            pair = (remainder,quotient)
            remainder_quotient.append(pair)
        else:
            pair = (remainder,quotient)
            repeater_remainder_quotient.append(pair)
            break
        i += 1
        if remainder == 0:
            break

i = 0
while remainder != 0:
    y = repeater_remainder_quotient[i][0]
    count = 0
    while y < divide:
        y = y * 10
        count += 1
    if count != 1:
        for c in range(count-1):
            pair = (int(y/pow(10,(count-c)-1)),0)
            if pair in repeater_remainder_quotient:
                repeater_found = True
                break
            else:
                repeater_remainder_quotient.append(pair)
                i += 1
    if repeater_found == True:
        break
    else:
        remainder = y % divide
        quotient = y // divide
        if (remainder,quotient) not in repeater_remainder_quotient:
            pair = (remainder,quotient)
            repeater_remainder_quotient.append(pair)
        else:
            break
        i += 1
        if remainder == 0:
            break

print('remainder_quotient = ',remainder_quotient)
print('Repeater remainder_quotient = ',repeater_remainder_quotient)

string_quotient = list(map(lambda x : str(x[1]), remainder_quotient))
string_repeater_quotient = list(map(lambda x : str(x[1]),repeater_remainder_quotient))

final_quotient = string_quotient[0] + '.'

if repeater_remainder_quotient == []:
    for e in string_quotient[1:]:
        final_quotient += e
else:
    for e in string_quotient[1:-len(string_repeater_quotient)]:
        final_quotient += e

    final_quotient += '('
    for e in string_repeater_quotient:
        final_quotient += e

    final_quotient += ')'
print(final_quotient)
