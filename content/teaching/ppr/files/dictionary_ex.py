#!/usr/bin/env python3

def main():
    # inicjalizacja słownika, inaczej hash map
    slownik = {}
    slownik = dict()
    slownik['Kowalski'] = '123-345-678'
    slownik['NoName'] = '123-345-678'
    del slownik['NoName'] # usunięcie klucza 'NoName' i jej wartości z 'slownik'

    slownik_2 = {'key_1': 'wartosc', 'key_2': 'wartosc'}

    print(slownik['Kowalski']) # ---> '123-345-678'

    # przechodzenie po kluczach i wartościach
    for key, value in slownik.items():
        print(f'Klucz: {key}, wartość: {value}')

    # przechodzenie po kluczach
    for key in slownik_2.keys():
        print(f'klucz: {key}')

    
    # przechodzenie po wartościach
    for value in slownik_2.values():
        print(f'wartość: {value}')


    # inicjalizacja zbioru
    zbior = set()
    zbior = {'Marek'}

    zbior.add('Ala')
    zbior.add('Ala')
    zbior.add('Robert')
    zbior.add(3)

    if 'Ala' in zbior:
        print('Ala jest w zbiorze')
    else:
        print("Nie ma 'Ala' w zbiorze")




if __name__ == '__main__':
    main()
