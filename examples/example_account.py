# coding=utf-8
""" Пример показывает как использовать следующие методы api:
    * account.auth
    * account.profile
    * account.updatelist
    * account.watchlist
"""
from cinemate import Cinemate


if __name__ == '__main__':
    cin = Cinemate(
        'username',
        'password',
        'passkey',
        'apikey'
    )
    passkey = cin.account.auth()
    profile = cin.account.profile()
    updatelist = cin.account.updatelist()
    watchlist = cin.account.watchlist()
    print(passkey)
    print(profile['username'])
    for update in updatelist:
        if update['new']:
            print(update['date'])
            print(update['date'], update['for_object'])
    for interesting_person in watchlist['person']:
        print(interesting_person)
    for interesting_movie in watchlist['movie']:
        print(interesting_movie)
