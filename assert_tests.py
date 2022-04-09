import morse
    
def test_encode_us():
    assert morse.encode('us') == '..- ...', "Should be ..- ..."

def test_encode_fy():
    assert morse.encode('FY') == '..-. -.--', "Should be ..-"

def test_encode_uwe():
    assert morse.encode('UWE') == '..- .-- .', "Should be ..-"

    #fail testing
def test_encode_fail():
    assert morse.encode('FAIL') == '..... ---', "Should be ..-"

def test_encode_fail2():
    assert morse.encode('FAIL2') == '..... ---', "Should be ..-"

def test_decode_us():
    assert morse.decode('..- ...') == 'US', "Should be ..-"

def test_decode_iot():
    assert morse.decode('.. --- -') == 'IOT', "Should be ..-"

def test_decode_uwe():
    assert morse.decode('..- .-- .') == 'UWE', "Should be ..-"

def test_decode_lol():
    assert morse.decode('.-.. --- .-..') == 'LOL', "Should be ..-"
    #fail testing
def test_decode_fail3():
    assert morse.decode('..... .. .. ....') == 'FAIL3', "Should be ..-"

if __name__ == "__main__":
    print('Everything passed')
