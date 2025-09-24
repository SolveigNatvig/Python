#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:41:51 2023

@author: solveig

Dette progammet tar inn en string av reaktanter på dette formatet 'H2 + O2' og en string med produkter på dette formatet 'H2O' og balanserer likningen
"""

from bib import *



def balanser_likning(r, p):
    
    # bruker funksjonen lag_list_dict() til å gjøre om listene til lister med dictionarys for eksempel gjøres ['H2', 'O2'] om til [{'H': 2}, {'O': 2}]
    R = lag_list_dict(r) 
    P = lag_list_dict(p)
    
    # kaller funksjonen balanser_likning_kieffisienter() som regner ut Koeffisientene til den balanserte reaksjonslikningen og legger de i en liste 
    koeff = balanser_likning_koeffisienter(R, P)



    # sørger for at elementene ikke er lik 1 fordi det da er unødvendig å skrive
    if koeff[0] != 1:
        likning = f'{koeff[0]}{r[0]}'

    else:
        likning = f'{r[0]}'



    for i in range(1, len(r)):
        if koeff[i] != 1:
            l_del = f'{koeff[i]}{r[i]}'
            likning = likning + '+' + l_del
        else:
            l_del = f'{r[i]}'
            likning = likning + '+' + l_del
            
    flytt = len(r)
    
    
    
    
    if koeff[flytt] != 1:
        likning = likning + '-->' + f'{koeff[flytt]}{p[0]}'

    else:
        likning = likning + '-->' + f'{p[0]}'
          
    
    
    
    
    for i in range(1, len(p)):
        if koeff[flytt + i] != 1:
            l_del = f'{koeff[flytt+ i]}{p[i]}'
            likning = likning + '+' + l_del
        else:
            l_del = f'{p[i]}'
            likning = likning + '+' + l_del
            
    return(likning)
    




r = input('Skriv inn reaktantene på formen: H2 + O2 + ... : ') 
p = input('Skriv inn reaktantene på formen: H2O + ... : ')


# denne Funksjonen tar inn en string som bruker har skrevet som input og formaterer stringen om til en liste
def balanser_likning_input(x):
    b = x.split('+') # gjør om stringen til en liste der elementene er splittet ved '+'
    test_list = []
    
    for e in b:
         d = liste_til_string(e)
         test_list.append(d.strip(' ')) 
    #print(test_list)    
    return test_list
         

R = balanser_likning_input(r)
P = balanser_likning_input(p)

print(f'Du ga oss disse reaktantene: {R} og disse produktene: {P}')
print(f'Den balanserte likningen er: {balanser_likning(R, P)}')
