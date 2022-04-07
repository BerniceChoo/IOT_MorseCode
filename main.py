import morse

if __name__ == "__main__":
    e = morse.encode('us')
    print('%s' % e)
    d = morse.decode(e)

    assert morse.encode('us') == '..- ...', "Should be ..-"
    assert morse.encode('FY') == '..-. -.--', "Should be ..-"
    assert morse.encode('UWE') == '..- .-- .', "Should be ..-"
    assert morse.encode('FAIL') == '-..-. .- .. .-..', "Should be ..-"
    assert morse.encode('FAIL2') == '-..-. .- .. .-.. ..---', "Should be ..-"

    assert morse.decode('..- ...') == 'US', "Should be ..-"
    assert morse.decode('.. --- -') == 'IOT', "Should be ..-"
    assert morse.decode('..- .-- .') == 'UWE', "Should be ..-"
    assert morse.decode('.-.. --- .-..') == 'LOL', "Should be ..-"
    assert morse.decode('-..-. .- .. .-..') == 'FAIL', "Should be ..-"