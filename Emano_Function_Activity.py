def sum(first_num, second_num, third_num):
    total_sum = first_num + second_num + third_num

    if first_num == second_num == third_num:
        result = first_num * second_num * third_num
    elif first_num == second_num:
        result = (first_num * second_num) + third_num
    elif first_num == third_num:
        result = (first_num * third_num) + second_num
    elif second_num == third_num:
        result = (second_num * third_num) + first_num
    else:
        result = total_sum

    return result

first_num = eval(input("Enter first number: "))
second_num = eval(input("Enter second number: "))
third_num = eval(input("Enter third number: "))

result = sum(first_num, second_num, third_num)
print("Result is", result)


