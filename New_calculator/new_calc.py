from new_oper import my_sum, my_red, my_mult, my_div, my_pow
fid = open("history.py", "at")
a = float(input("Введите число 'a'"))
oper =(input("Введите операцию"))
b = float(input("Введите число 'b'"))
fid.write("Enter number 'a'\n")
fid.write(str(a))
fid.write("\n")
fid.write("Enter the operation\n")
fid.write(oper)
fid.write("\n")
fid.write("Enter number 'b'\n")
fid.write(str(b))
fid.write("\n")

if oper == '+':
    result = my_sum(a, b)
    print(result)
elif oper == '-':
    result = my_red(a, b)
    print(result)
elif oper == '*':
    result = my_mult(a, b)
    print(result)
elif oper == '/':
    result = my_div(a, b)
    print(result)
elif oper == '**':
    result = my_pow(a, b)
    print(result)

fid.write(str(result))
fid.write('\n')

while True:
    oper = (input("Выберите любую операцию, если хотите продолжить, или 'terminate', если вычисления окончены"))
    if oper == ('terminate'):
        fid.write('terminate')
        break
    b = float(input("Введите следующее число"))
    a = result

    fid.write("Enter any operation, if you want to continue, or enter 'terminate' if you are done\n")
    fid.write(oper)
    fid.write("\n")
    fid.write("Enter number 'b'\n")
    fid.write(str(b))
    fid.write("\n")

    if oper == '+':
        result = my_sum(a, b)
        print(result)
    elif oper == '-':
        result = my_red(a, b)
        print(result)
    elif oper == '*':
        result = my_mult(a, b)
        print(result)
    elif oper == '/':
        result = my_div(a, b)
        print(result)
    elif oper == '**':
        result = my_pow(a, b)
        print(result)

    fid.write(str(result))
    fid.write('\n')

fid.close()


