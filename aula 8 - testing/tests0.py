from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f'ERROR on is_prime({n}), expected {expected}, but got {is_prime(n)}')
        return False
    return True
