import random
n = random.randrange(3, 21)


def get_password(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password = password + str(i) + str(j)
    return password


print(n, '- Число из первой вставки\n', get_password(n), '- Нужный пароль')
