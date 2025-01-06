first = input('Введите, пожалуйста, параметр first: ')
second = input('Введите, пожалуйста, параметр second: ')
third = input('Введите, пожалуйста, параметр third: ')
if first==second and second==third and third==first:
    print ('3')
elif first == second or second == third or third == first:
    print ('2')
else:
    print ('0')