# Created by Rafael Galiev at 07.11.18
def sieve_of_eratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""

    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def write_primes_to_file(n, path):
    with open(path, 'w') as f:
        print('\n'.join(map(str, sieve_of_eratosthenes(n))), file=f, sep='\n')


def main(*args):
    for i in range(1, 11):

        # for i in range(1, 11):
        with open('eroto_primes.txt', 'r') as f:
            primes = []
            # for line in f:
            #     if (int(line.strip()) < i * 1000000) and\
            #             (int(line.strip()) > (i - 1) * 1000000):
            #         primes.append(int(line.strip()))

            [
                primes.append(int(line.strip()))
                for line in f
                if (int(line.strip()) < i * 1000000) and
                   (int(line.strip()) > ((i - 1) * 1000000))
            ]
            path = 'dif_primes/primes_in_{}_{}'.format(
                str((i - 1) * 1000000),
                str(i * 1000000),
            )
            with open(path, 'w') as f_dif:
                print('\n'.join(map(str, primes)), file=f_dif, sep='\n')


if __name__ == "__main__":
    import sys

    main(sys.argv)
