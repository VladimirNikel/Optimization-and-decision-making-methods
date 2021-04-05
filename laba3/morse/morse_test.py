import morse
import pytest


@pytest.mark.parametrize('s,exp', [
    ('... --- ...', 'SOS'),
    ('... . -.-. --- -. -..', 'SECOND'),
    ('--. --- --- -.. -....- .--- --- -...', 'GOOD-JOB'),
    ('--.- .-- . .-. - -.-- -....- -. .. -.- . .-.. -....- --... .---- -.... -....- -- .- .. -....- .---- .---- --...',
     'QWERTY-NIKEL-716-MAI-117')
])
def test_decode(s, exp):
    assert morse.decode(s) == exp