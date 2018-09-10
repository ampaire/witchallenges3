def list_sort(lista):
    evens = []
    odds = []
    chars = []
    if not isinstance(lista,list):
        return 'Invalid Input'

    for x in lista:
        if isinstance(x, int):

            if (x % 2 == 1):
                odds.append(x)

            else:
                (x % 2 == 0)
                evens.append(x)

        else:
            if (type(lista) != str) and (type(lista) != int):
                chars.append(x)
            else:
                return 'Invalid Input'

    odds = sorted(odds)
    evens = sorted(evens)
    chars = sorted (chars)
    return {'evens':evens,'odds':odds,'chars':chars}


if __name__ == '__main__':
    print(list_sort([4, 3, 2, 'b']))
