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
list1.append([9,8,7, 1])
print(list1)

#append to dołącz, a extend to rozszerz
list1.extend([9, 7, 4, 1])
print(list1)

#wstawianie elemenrow w liste
list1.insert(1, 5678) #na drugie (bo 0 jest oierwsze) miejsce leci ta liczba
print(list1)

#usuwanie elementow z listy
list1.remove("ala ma kota") #trzeba podac cala wartosc
print(list1)

list1.remove(1) #remove usuwa pierwsza podana wattosc, gdy jest wievej to tylko ten pierwszy
print(list1)

# detekcja liczby elelentow o podanej wartosci w liscie
print(list1.count(1)) #liczy ile razy podana wartosc wystepuje w liscie
# true liczy sie jako 1 wiec tez jest liczona

#przed usunieciem sprawdzam czy sa wartosci do usuniecia
#if list1.count("ala ma kota":
#list1.remove("ala ma kota")
if "ala ma kota" in list1:
    list1.remove("ala ma kota")

#ile jest elementow
print(f"liczba elementów = {len(list1)}")

print(f"pozycja liczby 999.99 to {list1.index(999.99)}") #ta wartosc musi istniec w liscie

#usuwanie pierwszego elementu w liscie
del(list1[0])

#modyfikacja wartosci elementu listy
list1[0] = "ABC"
print(list1)

#kopiowanie listy
list2 = list1.copy() #trzeba dodac to copy bo inaczej beda takie same i sie beda tak samo zmieniac za kazdym razem, to samo id maja
list2[0] = "xyz"
print(f"List1 = {list1}")
print(f"List2 = {list2}")
print(f"list1 = {id(list1)}, list2 = {id(list2)}")
