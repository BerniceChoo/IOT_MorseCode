import unittest
import morse


class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ...')

class TestMorse(unittest.TestCase):
    def test_encode_fy(self):
        self.assertEqual( morse.encode('FY'), '..-. -.--')

class TestMorse(unittest.TestCase):
    def test_encode_uwe(self):
        self.assertEqual( morse.encode('UWE'), '..- .-- .')

class TestMorse(unittest.TestCase):
    def test_encode_fail(self):
        self.assertEqual( morse.encode('FAIL'), '-..-. .- .. .-..')

class TestMorse(unittest.TestCase):
    def test_encode_fail2(self):
        self.assertEqual( morse.encode('FAIL2'), '-..-. .- .. .-.. ..---')

class TestMorse(unittest.TestCase):
    def test_decode_us(self):
        self.assertEqual( morse.encode('..- ...'), 'US')

class TestMorse(unittest.TestCase):
    def test_decode_us(self):
        self.assertEqual( morse.encode('.. --- -'), 'IOT')

class TestMorse(unittest.TestCase):
    def test_decode_us(self):
        self.assertEqual( morse.encode('..- .-- .'), 'UWE')

class TestMorse(unittest.TestCase):
    def test_decode_us(self):
        self.assertEqual( morse.encode('.-.. --- .-..'), 'LOL')

class TestMorse(unittest.TestCase):
    def test_decode_us(self):
        self.assertEqual( morse.encode('-..-. .- .. .-..'), 'FAIL')
        

if __name__ == '__main__':
    unittest.main()