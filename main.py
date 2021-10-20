# 5
def transformare_stirng(lista):
    result_list = []
    for element in range(len(lista)):
        result_list.append(lista[element])
    return result_list


# 4
def extract_parte_fractionara(numar):
    """
    Functia pregateste partea fractionara a numarului de tip Float.
    :param numar: numarul de tip float
    :return: partea fractionara a numarului
    """
    return str(numar).split('.')[1]

'''
def test_extract_parte_fractionara():
    assert extract_parte_fractionara([1.2]) == [2]
    assert extract_parte_fractionara([3.5]) == [5]
'''

def int_div_frac(lista):
    """
    Functia returneaza lista numerelor de tip float in care partea fractionara este divizibila cu partea intreaga
    :param lista: lista de float-uri
    :return: lista de numere de tip float cuproprietatea precizata
    """
    result_list = []
    for element in range(len(lista)):
        a = int(extract_parte_fractionara(lista[element]))
        b = int(extract_parte_intreaga(lista[element]))
        if a % b == 0:
            result_list.append(lista[element])
    return result_list

'''
def test_int_div_frac():
    assert int_div_frac([1.2, 4.8, 3.4]) == [1.2, 4.8]
'''

# 3
def interval(lista, a, b):
    """
    Functia va returna lista cu numerele de timp float care se afla in intervalul specificat
    :param lista: lista din care vom extrage numerele
    :param a: capat al intervalului
    :param b: capat al intervalului
    :return: returneaza lista obtinuta, cu numerele din interiorul intervalului deschis
    """
    result_list = []
    if a > b:
        auxiliar = a
        a = b
        b = auxiliar
    for element in range(len(lista)):
        if lista[element] > a and lista[element] < b:
            result_list.append(lista[element])
    return result_list

'''
def test_interval():
    assert test_interval([1,2,3,4], 0, 4) == [1,2,3]
    assert test_interval([-3, -1, 3, 4], -2, 4) == [-1,3]
'''

# 2
def extract_parte_intreaga(numar):
    """
    Functia pregateste partea intreaga a numarului de tip Float.
    :param numar: numarul de tip float
    :return: partea intreaga a numarului
    """
    return str(numar).split('.')[0]

'''
def test_extract_parte_intreaga():
    assert extract_parte_intreaga(1.2) == [1]
    assert extract_parte_intreaga(2.3) == [2]
'''


def partea_intreaga(lista):
    """
    functia creeaza o lista cu partea intreaga a numerelor fractionare din lista.
    :param lista: lista de float-uri
    :return: lista de nurere intregi
    """
    result_list = []
    for element in range(len(lista)):
        result_list.append(extract_parte_intreaga(lista[element]))

    return result_list

'''
def test_partea_intreaga():
    assert partea_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
'''

# 1
def citire_lista():
    """
    Functia citeste lista de float-uri de la tastatura.
    :return: lista de float-uri citita
    """
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)

    return result_list


def main():
    lista = []
    while True:
        print('1. Citirea unei liste de numere float. ')
        print('2. Afișarea părții întregi a tuturor numerelor din listă.')
        print('3. Intersectia multimilor.')
        print('4. c.')
        print('x. Iesire din program - exit.')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            lista = citire_lista()
            print(lista)
            print("\n")
        elif optiune == '2':
            print(partea_intreaga(lista))
            print("\n")
        elif optiune == '3':
            st = float(input("Dati capatul din stanga al intervalului: "))
            dr = float(input("dati capatul din dreapta al intervalului: "))
            print(interval(lista, st, dr))
            print("\n")
        elif optiune == '4':
            print(int_div_frac(lista))
            print("\n")
        elif optiune == '5':
            print(transformare_stirng(lista))
            print("\n")
        elif optiune == '6':
            break
        else:
            print('Optiune invalida!')
            print("\n")


# test_extract_parte_fractionara()
# test_int_div_frac()
# test_interval()
# test_partea_intreaga()
# test_extract_parte_intreaga()
main()
