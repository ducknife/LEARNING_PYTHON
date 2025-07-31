#import ...

DUCKNIFE = '__main__'

def val(x):
    return x * x

if __name__ == DUCKNIFE:
    #ducknife
    h_dict = {}
    h_dict['hello'] = 'world'
    h_dict.setdefault('Hung', 99) # thêm vào với giá trị key, value nếu key chưa có trong dict
    h_dict['Hung'] += 1
    print(h_dict)

    h_dict.update({'Hoho' : 10})
    print(h_dict.get('Hoho'))

    h_dict.update({'Haha': 10, 'Hihi': 10})
    print(h_dict)

    h_dict.pop('Haha')
    h_dict.popitem()

    print(h_dict)

    a = [1, 2, 3, 4, 5]
    a2 = [1, 4, 9, 16, 25]

    h2_dict = dict(zip(a, a2))
    print(h2_dict)

    h3_dict = dict.fromkeys(a, 0)
    print(h3_dict)

    del h2_dict[1]
    print(h2_dict)

