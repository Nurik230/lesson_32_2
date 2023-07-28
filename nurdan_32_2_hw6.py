def bubble_sort():
    # n=len(int(input()))
    mas = list(map(int, input().split()))
    for i in range(len(mas) - 1):
        for j in range(len(mas) - 1 - i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    print(f'bubble_sort: {mas}')


def binarry_search(number, list):
    list.sort()

    med = len(list) // 2
    lec = 0
    first = len(list) - 1

    while list[med] != number and lec <= first:
        if number > list[med]:
            lec = med + 1
        else:
            first = med - 1
        med = (lec + first) // 2

        if lec > first:
            print('Not found')
        else:
            print(f'index = {med}')


binarry_search(6,[0,4,3,8,2,6,8])

bubble_sort()