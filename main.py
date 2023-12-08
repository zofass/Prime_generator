from inspect import isgenerator

def prime_generator(end):
    numbers = list(range(2, end + 1))

    while numbers:
        prime = numbers[0]
        if prime <= int(end ** 0.5):
            yield prime
            numbers = [x for x in numbers if x % prime != 0]
        else:
            yield from numbers
            break


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('OK')
