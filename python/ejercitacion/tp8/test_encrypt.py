import unittest
from tp8 import encrypt_with_char, encrypt

class TestEncrypt(unittest.TestCase):
    def test_empty_with_char(self):
        self.assertEqual("", encrypt_with_char("", "x"))

    def test_empty_with_password(self):
        self.assertEqual("", encrypt("", "secret"))

    def test_example_with_char(self):
        self.assertEqual("0\x1d\x14\x14\x17", encrypt_with_char("Hello", "x"))

    def test_example_with_password(self):
        self.assertEqual("5\t\x05\x1fE\x18B\x16\x0b\x05\x01\x1c\x10\x07\x11\x07E.\r\x13\x08\x0fD",
                         encrypt("What a wonderful World!", "badkey"))

    def test_encrypt_decrypt(self):
        self.encrypt_decrypt("A long message with a short Key", "1289")
        self.encrypt_decrypt("Short", "A quite long Key. 12e-0as;'")
        self.encrypt_decrypt("129", "129")

    def encrypt_decrypt(self, message: str, key: str): # (msg xor key) xor msg = msg => 0001 xor 1000 = 1001 xor 1000 = 0001
        encrypted_message = encrypt(message, key)
        decrypted_message = encrypt(encrypted_message, key)
        self.assertEqual(message, decrypted_message)

if __name__ == '__main__':
    unittest.main()
