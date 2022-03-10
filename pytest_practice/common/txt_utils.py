

def read_txt(text_file):
    with open(text_file, 'r') as f:
        value = f.read()
        return value


def write_txt():
    pass

def truncate_txt():
    pass





value = read_txt('/Users/dongshuai/PycharmProject/pytest_practice/aaa.txt').split(',')
district = list(set(value))
print(value)
print(district)


dic = {}
count = []
for i in district:

    dic[i] = value.count(i)
    count.append(value.count(i))

print(sorted(count, reverse=True))


for k, v in dic.items():
    if v == sorted(count, reverse=True)[-1]:
        print(k,v)

