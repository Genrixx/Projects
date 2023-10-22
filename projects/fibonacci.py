def fibonacci(num):
    rav = [0, 1]
    for i in range(2, num):
        prev_num = rav[i - 1]
        prev_num2 = rav[i - 2]
        rav.append(prev_num + prev_num2)
    return rav


print(fibonacci(15))