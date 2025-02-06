import unittest
import ceaser as ce
import vigenere as vi

class TestMethods(unittest.TestCase):
    def test_crypting(self):
        self.assertEqual('whvw', ce.crypting('test'))

    def test_decrypting(self):
        self.assertEqual('test', ce.decrypt('whvw'))

    def test_bruceforce(self):
        array = ce.bruteforce('whvw', ce.crypting)

        result = array[22]

        self.assertEqual('test', result)
    
    def test_ceaser_encrypt_decrypt(self):
        text = "hello"
        encrypted = ce.crypting(text, 3)
        decrypted = ce.decrypt(encrypted, 3)
        self.assertEqual(decrypted, text)
    
    def test_vigenere_encrypt_decrypt(self):
        text = "hello"
        key = "key"
        encrypted = vi.encrypt_vigenere(text, key)
        decrypted = vi.decrypt_vigenere(encrypted, key)
        self.assertEqual(decrypted, text)

if __name__ == '__main__':
    unittest.main()