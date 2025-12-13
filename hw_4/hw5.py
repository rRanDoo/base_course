def exponentiation_without_exponentiation(a,n):
    resultat = 1
    kolvo_a = 0
    while kolvo_a < n:
        resultat *= a
        kolvo_a += 1
    return resultat
me = exponentiation_without_exponentiation(11,2)
print(me)