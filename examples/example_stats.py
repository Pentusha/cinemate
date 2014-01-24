# coding=utf-8
from cinemate import Cinemate


if __name__ == '__main__':
    cin = Cinemate(
        'username',
        'password',
        'passkey',
        'apikey'
    )
    print(cin.stats.new())
