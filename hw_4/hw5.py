def exponentiation_without_exponentiation(a,n):
    resultat = 1
    kolvo = 0
    while kolvo < n:
        resultat *= a
        kolvo += 1
    return resultat
me = exponentiation_without_exponentiation(3,3)
print(me)