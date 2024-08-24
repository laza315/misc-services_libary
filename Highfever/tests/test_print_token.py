from pyotp import *


def test_token():
        totp = TOTP("eyo6v7bip4e7av2nbiqekgdysmbgjuso")
        token = totp.now()
        print(token)


