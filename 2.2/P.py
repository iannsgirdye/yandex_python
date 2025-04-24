# Легенды велогонок возвращаются: кто быстрее?

petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    first = 'Петя'
    if vasya > tolya:
        second = 'Вася'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Вася'

elif vasya > petya and vasya > tolya:
    first = 'Вася'
    if petya > tolya:
        second = 'Петя'
        third = 'Толя'
    else:
        second = 'Толя'
        third = 'Петя'
        
else:
    first = 'Толя'
    if vasya > petya:
        second = 'Вася'
        third = 'Петя'
    else:
        second = 'Петя'
        third = 'Вася'

print(f'          {first}          ')
print(f'  {second}   ')
print(f'                  {third}  ')
print('   II      I      III   ')
