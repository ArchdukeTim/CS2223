from .gcd import euclid, ms_procedure, consecutive_integer
import pytest


@pytest.mark.parametrize("m,n,res", [
    (13, 13, 13),  # trick case: a = b
    (37, 600, 1),  # first argument is a prime
    (20, 100, 20),  # one is multiplum of other
    (624129, 2061517, 18913), # Random numbers
    (1234567890, 987654321, 9), # Big numbers
    (31415, 14142, 1), # The required test case
    (1234567890, 123, 3), # Big and small number
    (79, 71, 1), # Two Primes
    (33_554_432, 67_108_864, 33_554_432)]) # Powers of 2
def test_gcd(m, n, res):
    assert euclid(m, n) == res
    assert consecutive_integer(m, n) == res
    assert ms_procedure(m, n) == res
