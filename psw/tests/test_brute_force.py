import unittest
from attacks.brute_force import brute_force_attack

class TestBruteForce(unittest.TestCase):
def test_brute_force(self):
target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddc7ee10954f2b3f4b6"
brute_force_attack(target_hash, "123456")

if __name__ == "__main__":
unittest.main()
