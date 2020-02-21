def remove_dig(n):
    second_digit = int(n[-2])

    first_digit = int(n[-1])

    if second_digit > first_digit:
        new_n = n[:-2] + n[-1]

    else:
        new_n = n[:-1]

    return new_n


n = input()

if int(n) > 9:
    print(n)

elif n in ['-10', '-20', '-30', '-40', '-50', '-60', '-70', '-80', '-90']:
    print(0)
else:
    print(remove_dig(n))