import random
import time


# PATH_TO_FILE = 'prime.txt'
PATH_TO_FILE = 'dif_primes/primes_in_0_1000000'


def get_control_prime(from_path):
    file = open(from_path)
    control_prime = list()
    for line in file:
        # control_prime.append(int(line.strip().split(' ')[1]))
        control_prime.append(int(line.strip()))
    control_prime.pop(0)
    return tuple(control_prime)


def miller_test(number, count, *a):
    if type(number) != int or (number != 2 and number % 2 == 0):
        return 'Please, use the not even integer!'

    assumption = ''
    a = list(a)

    for check in range(count):
        if len(a) == 0:
            a_num = random.randint(2, number-1)
        else:
            a_num = a.pop()
        uravn = uravnenie(number)
        odd_multiplier = int(uravn[0])
        s = uravn[1]

        b = pow(a_num, odd_multiplier, number)
        if b == 1 or b == number - 1:
            assumption = 'prime'
        else:
            for i in range(s-1):
                b = pow(b, 2, number)
                if b == number - 1:
                    assumption = 'prime'
        if assumption != 'prime':
            return 'complex'
    return assumption


# n-1 = 2^s * t
def uravnenie(number):
    odd_multiplier = number-1
    s = 0
    while odd_multiplier % 2 == 0:
        odd_multiplier /= 2
        s += 1
    return odd_multiplier, s


def get_primes_in_set(a, raw):
    ass_prime = list()

    # futures = [ass_prime.append(numb) for numb in raw if miller_test(numb, 1, a) == 'prime']

    for numb in raw:
        assumption = miller_test(numb, 1, a)
        if assumption == 'prime':
            ass_prime.append(numb)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(futures))

    return tuple(ass_prime)


def prohod(a, raw, control_raw, file=None):
    result_raw = get_primes_in_set(a, raw)

    err_list = list()
    for assump in result_raw:
        if assump not in control_raw:
            err_list.append(assump)

    # err = len(err_list)/len(control_raw)
    err = len(err_list) / len(raw)
    if not file:
        print("\nВ ряду: ", len(raw), " нечетных чисел\n")

        print(u'Чисел после прохода:', len(result_raw))
        print(len(err_list), u' чисел определены ошибочно')
        print(u'Ошибка: ', err)
    else:
        print("\nВ ряду: ", len(raw), " нечетных чисел\n", file=file)
        print(u'Чисел после прохода:', len(result_raw), file=file)
        print(len(err_list), u' чисел определены ошибочно', file=file)
        print(u'Ошибка: ', err, file=file)
    return {'result': result_raw, 'miss_raw': err_list}


# # ------------------------------------------------------------------------------------------
# etalon = get_control_prime(PATH_TO_FILE)
# print(u'Всего ', len(etalon[:78497]), u' контрольных чисел')
#
# start_time = time.time()
#
# # --------------------------       Pervyi prohod       ----------------------------------------
#
# print("--------       Pervyi prohod       ---------")
# # Pizdec dolgaya huynya!!!!!
# mil = prohod(2, range(3, 1000000, 2), etalon)
#
# print('\nВремя первого прохода: ', time.time()-start_time)
#
# second_time = time.time()
#
# # --------------------------       Vtoroy prohod       ----------------------------------------
#
# print("--------       Vtoroy prohod       ---------")
# second_mil = prohod(3, mil['miss_raw'], etalon)
#
# print('\nВремя второго прохода: ', time.time()-second_time)
# print('\nВремя всей программы: ', time.time()-start_time)
