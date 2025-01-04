grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_s = list(students)
#print(list_s)
a = len(list_s)
#print(a)
dict = {}
list_s = sorted(list_s)
#print(list_s)
if a == len(grades):
    i = 0
    while i < a:
        m = grades[i]
        ma = sum(m) / len(m)
        #print(ma)
        dict.update({list_s[i]: ma})
        i += 1
    print(dict)
else: print('Списки разной длины')
