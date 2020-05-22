def merge_sort(a:list):
    """
    Возвращает отсортированный (слиянием) список
    """
    if len(a) <= 1:
        return
    middle = len(a)//2
    l = a[0:middle]
    r = a[middle:]
    merge_sort(l)
    merge_sort(r)
    c = []
    while len(l) > 0 and len(r) > 0:
        if l[0] <= r[0]:
            c.append(l.pop(0))
        else:
            c.append(r.pop(0))
    c.extend(l) if l else c.extend(r)
    for j in range(len(c)):
        a[j] = c[j]


def test_merge_sort():
    a = [5,4,7,2,0,5,9,6,3,5]
    print('Дано:', a)
    merge_sort(a)
    print('Итог:', a)
    if a == sorted([5,4,7,2,0,5,9,6,3,5]):
        print(merge_sort.__doc__, "...OK!")
    else:
        print(merge_sort.__doc__, "...FAILED!")


if __name__ == '__main__':
    print('Запускаем тест')
    test_merge_sort()
