# E Сломай меня.
from random import choices
import string


def polynomial_hash(a, m, s):
    h_s = 0
    for i in range(len(s)):
        h_s = (h_s * a + ord(s[i])) % m
    return h_s


def generate_string(n):
    return ''.join(choices(string.ascii_letters, k=n))

a = 1000
m = 123987123

hashes = {}
for i in range(100000):
    s = generate_string(8)
    hash = polynomial_hash(a, m, s)
    if hash in hashes:
        print(hashes[hash], s)
        break
    else:
        hashes[hash] = s

assert polynomial_hash(a, m, 'begxpgurlt') == polynomial_hash(a, m, 'qxaxlurkoy')
assert polynomial_hash(a, m, hashes[hash]) == polynomial_hash(a, m, s)