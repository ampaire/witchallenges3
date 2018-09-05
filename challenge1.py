def sorted_list(mylist):
    mydictionary = dict()
    even = []
    odd = []
    char = []

    for x in mylist:
        if isinstance(x, int):
            if (x % 2 == 1):
                odd.append(x)

            else:
                even.append(x)
        else:

            char.append(x)

    mydictionary['odds'] = odd
    mydictionary['evens'] = even
    mydictionary['chars'] = char

    return mydictionary


print(sorted_list([2, 0, 6, 5, 1, 7, 'z', 'a']))
