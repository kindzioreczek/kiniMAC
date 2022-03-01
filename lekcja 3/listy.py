'''
listy w pythonie

przechowywanie wielu elementow, jest mozliwa modyfikacja dynamiczna, mozna dodawac do listy elementy
mozna usuwac elementy, dortowac dane, zmieniac kolejnosc

'''
list1 = list() #pusta lista
list1 = [] #pusta lista
list1 = [1, "ala ma kota", True, 999.99, (1,), ["A", "B"], None] # deklaracja listy z wartosciami inicjalnymi
#list1.append() #dolaczenie
print(list1)

#dodaj element na koniec listy
list1.append(2)
print(list1)

#dodaj liste na koniec listy
list1.append([9,8,7])
print(list1)

#append to dołącz, a extend to rozszerz
list1.extend([9, 7, 4])
print(list1)
