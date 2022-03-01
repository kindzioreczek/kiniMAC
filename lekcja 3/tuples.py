'''
tuples = krotka

krotki czyli a'la struktura


'''
tuple1 = (200, "ok")
tuple2 = (200, "error", False, (-1,1), -123.45)
tuple3 = (200, )  #muszą byc nawiasy bo to jest ktotka wtedy

#wypisz ok z tuple2
print( tuple2[1])  #pierwszy element jest pod indeksem zero
#tuple2[1] = "error" #proba zmiany wartosci elementu tuple2
#!!!!! KROTKI NIE DA SIE MODYFIKOWAC pojedynczo, jest niemutowalna!!!
print(tuple2[3][0])
var1, var2, var3, var4, var5 = tuple2 #musza byc wszystkie elementy wypisane
print(var1, var2, var3, var4, var5)

var1, var2, var3, var4, _ = tuple2 # _  to ślepa zmienna, odbiera zmienne
x, y, z = 10, 20, 30
x = 10; y =10; z=10 #tak tez mozna robic bo ; srednik rozgranicza dzialania

print(var1, var2, var3, var4)