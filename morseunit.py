import unittest
import morse

#unit testing for 5 encode
class TestMorse(unittest.TestCase):
    def test_encode_us(self):
        self.assertEqual( morse.encode('us'), '..- ...')

    def test_encode_fy(self):
        self.assertEqual( morse.encode('FY'), '..-. -.--')

    def test_encode_uwe(self):
        self.assertEqual( morse.encode('UWE'), '..- .-- .')

    #fail test 1
    def test_encode_fail(self):
        self.assertEqual( morse.encode('FAIL'), '..... ---')

    #fail test 2
    def test_encode_fail2(self):
        self.assertEqual( morse.encode('FAIL2'), '..... ---')

    #unit testing for 5 decode
    def test_decode_us(self):
        self.assertEqual( morse.encode('..- ...'), 'US')

    def test_decode_us(self):
        self.assertEqual( morse.encode('.. --- -'), 'IOT')

    def test_decode_us(self):
        self.assertEqual( morse.encode('..- .-- .'), 'UWE')

    def test_decode_us(self):
        self.assertEqual( morse.encode('.-.. --- .-..'), 'LOL')

    #fail test 3
    def test_decode_us(self):
        self.assertEqual( morse.encode('..... .. .. ....'), 'FAIL3')

    # Task 4 Testing
    def test_encode_task4(self):
        self.assertEqual(morse.encode('(+&,:"!)'), '-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-')

    def test_decode_task4(self):
        self.assertEqual(morse.decode('-.--. .-.-. .-... --..-- ---... .-..-. -.-.-- -.--.-'), '(+&,:"!)')
        

if __name__ == '__main__':
    unittest.main()