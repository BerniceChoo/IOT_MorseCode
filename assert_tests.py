import morse
    
    
def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."
    assert morse.encode('FY') == '..-. -.--', "Should be ..-"
    assert morse.encode('UWE') == '..- .-- .', "Should be ..-"
    assert morse.encode('FAIL') == '-..-. .- .. .-..', "Should be ..-"
    assert morse.encode('FAIL2') == '-..-. .- .. .-.. ..---', "Should be ..-"

    assert morse.decode('..- ...') == 'US', "Should be ..-"
    assert morse.decode('.. --- -') == 'IOT', "Should be ..-"
    assert morse.decode('..- .-- .') == 'UWE', "Should be ..-"
    assert morse.decode('.-.. --- .-..') == 'LOL', "Should be ..-"
    assert morse.decode('-..-. .- .. .-..') == 'FAIL', "Should be ..-"

if __name__ == "__main__":
    #assert_tests.test_encode_us()
    print('Everything passed')
