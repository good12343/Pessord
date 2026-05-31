import unittest
from attacks.dictionary import dictionary_attack

class TestDictionary(unittest.TestCase):
def test_dictionary(self):
target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbddc7ee10954f2b3f4b6"
wordlist = ["password", "123456", "123456789", "qwerty"]
dictionary_attack(target_hash, wordlist)

if __name__ == "__main__":
unittest.main()
