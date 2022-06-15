# перебор делителей
def div_cycle(n):
    sieve = [_ for _ in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        for j in range(2, i):
            if sieve[i] % j == 0:
                sieve[i] = 0
                break
    return [_ for _ in sieve if _ != 0]
# div_cycle(10000)
# 7 function calls in 0.431 seconds
# div_cycle(1000000)
# 7 function calls in 2740.842 seconds

# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.div_cycle(10)"
# 1000 loops, best of 5: 3.61 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.div_cycle(20)"
# 1000 loops, best of 5: 9.1 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.div_cycle(100)"
# 1000 loops, best of 5: 86.5 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.div_cycle(1000)"
# 1000 loops, best of 5: 4.92 msec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.div_cycle(5000)"
# 1000 loops, best of 5: 108 msec per loop

# Обычное решето Эратосфена
def erato(n):
    sieve = [_ for _ in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    return [_ for _ in sieve if _ != 0]
# erato(10000)
# 7 function calls in 0.003 seconds
# erato(1000000)
# 7 function calls in 0.467 seconds

# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato(10)"
# 1000 loops, best of 5: 2.05 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato(20)"
# 1000 loops, best of 5: 3.86 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato(100)"
# 1000 loops, best of 5: 19.2 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato(1000)"
# 1000 loops, best of 5: 235 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato(5000)"
# 1000 loops, best of 5: 1.27 msec per loop

# Модифицированное решето Эратосфена
def erato_mod(n):
    sieve = [_ for _ in range(n)]
    sieve[1] = 0
    i = 2
    while i ** 2 <= n:
        if sieve[i] != 0:
            j = i ** 2
            while j < n:
                sieve[j] = 0
                j += i
        i += 1
    return [_ for _ in sieve if _ != 0]
# erato_mod(10000)
# 7 function calls in 0.002 seconds
# erato_mod(1000000)
# 7 function calls in 0.304 seconds

# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato_mod(10)"
# 1000 loops, best of 5: 2.38 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato_mod(20)"
# 1000 loops, best of 5: 3.54 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato_mod(100)"
# 1000 loops, best of 5: 14.3 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato_mod(1000)"
# 1000 loops, best of 5: 150 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_2" "lesson4_2.erato_mod(5000)"
# 1000 loops, best of 5: 812 usec per loop

def main():
    print(erato_mod(1000000))


if __name__ == '__main__':
    main()
