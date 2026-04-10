# home work L3 3.1

hat_list = [1,2,3,4,5]
print(hat_list, " - первоначальный список")

len(hat_list)
print(len(hat_list), " - кол-во элементов в списке")

# Write a line of code that prompts the user
your_number = int(input("Введите ваше число для замены: "))

# To replace the middle number with an integer number entered by the user
hat_list[2] = your_number
print(hat_list, " - измененный список ")

# Write a line of code that removes the last element from the list
hat_list.pop(-1)
print(hat_list, " - удаленно последнее знач.")

# Write a line of code that prints the length of the existing list
print(len(hat_list), " - длина списка после изменений")

# home work 3.3

li = []
n = int(input("Сколько значений? : "))

for i in range(n):
    numbers = int(input("Введите значения: "))
    li.append(numbers)

print(li)

swapped = True

while swapped:
    swapped = False 
    for i in range(len(li) - 1):
        if li[i] > li[i+1]:
            li[i], li[i+1] = li[i+1], li[i] 
            swapped = True

print(li)          

# home work 3.4 

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(my_list)

new_list = list(set(my_list))
print(new_list)

# home work 3.5

li = input("Введите числа через пробел:")
li.split()
li = [int(value) for value in li.split()]

summa = sum(li)
print("Сумма чисел - ", summa)


