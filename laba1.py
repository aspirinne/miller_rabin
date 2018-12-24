import time

import miller


OTCHET_FILE_PATH = 'otchety/otchet_7.txt'

ETALON_FILES_PATHS = (
    'dif_primes/primes_in_0_1000000',
    'dif_primes/primes_in_1000000_2000000',
    'dif_primes/primes_in_2000000_3000000',
    'dif_primes/primes_in_3000000_4000000',
    'dif_primes/primes_in_4000000_5000000',
    'dif_primes/primes_in_5000000_6000000',
    'dif_primes/primes_in_6000000_7000000',
    'dif_primes/primes_in_7000000_8000000',
    'dif_primes/primes_in_8000000_9000000',
    'dif_primes/primes_in_9000000_10000000',
)


# etalon = miller.get_control_prime(ETALON_FILES_PATHS[0])
#
# with open(OTCHET_FILE_PATH, 'w') as f_dif:
#     # print('\n'.join(map(str, primes)), file=f_dif, sep='\n')
#
#     print('\n', '--------       10^6       ---------------------------------------------------', '\n', file=f_dif)
#
#     print(u'Всего ', len(etalon[:78497]), u' контрольных чисел', '\n', file=f_dif)
#
#     start_time = time.time()
#
#     print("--------       Prohod dlya a=2       ---------", file=f_dif)
#     # Pizdec dolgaya huynya!!!!!
#     mil = miller.prohod(2, range(3, 1000000, 2), etalon, file=f_dif)
#
#     print('\nВремя прохода: ', time.time()-start_time, file=f_dif)
#     print('\n', '-----------------------------------------------------------------------------', '\n\n', file=f_dif)


start_time = time.time()
start_begin = 3
start_end = 1000000
err_list = list()
result_list = list()
nech = 0
etalon_len = 0
for ETALON_FILE in ETALON_FILES_PATHS:
    etalon = miller.get_control_prime(ETALON_FILE)
    mil = miller.prohod(2, range(start_begin, start_end, 2), etalon)

    etalon_len += len(etalon)
    nech += len(range(start_begin, start_end, 2))
    err_list.extend(mil['miss_raw'])
    result_list.extend(mil['result'])

    start_begin = start_end + 1
    start_end = start_end + 1000000

err = len(err_list) / nech
with open(OTCHET_FILE_PATH, 'w') as f_dif:
    print('\n', '--------       10^7       ---------------------------------------------------', '\n', file=f_dif)
    print(u'Всего ', etalon_len, u' контрольных чисел', '\n', file=f_dif)
    print("\nВ ряду: ", nech, " нечетных чисел\n", file=f_dif)

    print(u'Чисел после прохода:', len(result_list), file=f_dif)
    print(len(err_list), u' чисел определены ошибочно', file=f_dif)
    print(u'Ошибка: ', err, file=f_dif)
    print('\nВремя прохода: ', time.time()-start_time, file=f_dif)
