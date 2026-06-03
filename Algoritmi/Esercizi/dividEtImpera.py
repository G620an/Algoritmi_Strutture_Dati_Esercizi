#Preso un algoritmo divide et Impera che a ogni passo divide il problema in tre sottoistanze dello stesso problema, ciascuna di dimensione n/2;
#si ricavi la complessità dell'algoritmo supponendo che al netto delle chiamate ricorsive, la singola chiamata ha complessitò b*n con b const

#T(n) = bn + 3T(n/2)

#a = 3
#c = 2
#d = 1

#a/c^d == 3/2 > 1 e quindi siamo nel caso tetha(n^logc(a)) cioè tetha(n^log_2(3))