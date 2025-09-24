#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:22:27 2023

@author: solveig

Dette er et bibliotek med funksjoner som benyttes i filene molar_masse.py og balansere_likning.py
"""

from sympy import Matrix, lcm



# Funksjon som konverterer fra liste til string uten mellomrom
def liste_til_string(s):
   
    # lager en tom string
    string = ""
   
    # return string uten mellomrom 
    return (string.join(s)) # gjør om listen til en string der '' skiller elementene



# tar inn en liste ['H','2','O','1'] og gjør denne lista om til en dictionary {'H':2,'O':1}
def lag_dict(Symboler):
    dictionary  = {} #lager en tom dictionary
    
    for i in range(0, len(Symboler), 2): # fra og med 0 til men ikke med len(Symboler), hopper to av gangen fordi listen som tas inn har annenhver bokstav og tall
        dictionary[Symboler[i]] = int(Symboler[i+1]) #setter bokstaven som key og tallet som value
        
    return dictionary #Returnerer en divtionary med atomer og anntall atomer i molekylet
                    




# ['H2O','H3O','NH4'] ->[{'H':2,'O':1}, ...]
#
# (1) 'H20' -> ['H','2','O','1']
# (2) ['H','2','O','1'] ->{'H':2,'O':1}

# Tar inn en liste på formatet ['H2O','H3O','NH4'] og bruker funksjonen list_dict() til å lage en liste med dictionarys
def lag_list_dict(L):
    listDict = []
    for e in L:
        sym = finn_symboler(e)
        listDict.append(lag_dict(sym))
     
    return listDict








# R=[{'H':2,'O':1}, ...]
# P=[{'Br':2,'F':1}, ...]
#
# returner koeffisienter som balanserer H2O +... => Br2F + ...

# Tar inn to lister med dictionarys, en for reaktanter og en for produkter
def balanser_likning_koeffisienter(R, P):
    #finn grunnstoffene
    G = set()
    for r in R+P:
        for v in r:
            G.add(v)
     
    # Sett opp koiffisientlikningene
    M = []
    for g in G:
        rad = []
        for r in R:
            rad.append(r.get(g, 0))
        for p in P:
            rad.append(-p.get(g, 0))
            
        M.append(rad)
        

    
    # oppskrift fra nettet
    M=Matrix(M) # lager en matrise
    result = M.nullspace()[0] # finner en eller annen x, y, z.. som løser koiffisientlikningene siden det er færre likninger enn ukjente finnes det mange løsninger
    multiple = lcm([val.q for val in result]) # finn minste felles multiplum #en faktor man kan gange med brøkene slik at man får heltall 
    result = result*multiple #sørger for at koeffisientene er heltall
    
    # Legger resultatet inn i en liste
    factors = []
    for i in range(len(R+P)):
        factors.append(result[i,0])
        
    return factors #returnerer lista med koeffisientene







# funksjon som finner symboler fra input, deler opp og legger til i en liste
# inn CaSO4
# ut [Ca,1,S,1,O,4] 
def finn_symboler(x):
    symboler = []
    
    #for hvert av tegnene i x
    for i in x:
        if i.isspace():
            continue
        
        #Hvis c er en liten bokstav
        if i.islower() == True:
            
            #Erstatter siste element i lista med siste element + c
            symboler[-1] += i
        
        #Hvis c er et tall og siste element i lista symboler er et tall, sørger for at vi kan skrive inn flersiffrede tall 
        elif i.isnumeric() == True and symboler[-1].isnumeric() == True:
            
            #Erstatter siste element i lista med siste element + c
            symboler[-1] += i
        
        else:
            #legger til c i lista symboler
            symboler.append(i)
            
    sym = [symboler[0]]        
    for i in range(1, len(symboler)):
        if symboler[i].isnumeric() == False and sym[-1].isnumeric() == False: 
            sym.append('1')
        sym.append(symboler[i])
        
    if sym[-1].isnumeric() == False:
        sym.append('1')
    
    return sym #returnerer en liste son ser slik ut [Ca,1,S,1,O,4] 







#funksjon som bruker funksjonen finn_symboler(), finner alle grunnstoffer og legger de etter hverandre i en liste
# inn [Ca,1,S,1,O,4]
# ut [Ca,S,O,O,O,O]    
def finn_grunnstoffer(x):
    symboler = finn_symboler(x)
    grunnstoffer = []
    
    #for hvert element i lista
    for s in symboler:
        
        #hvis elementet er et tall, legger til forrige element ganger tallet-1
        if s.isnumeric() == True:
            a = grunnstoffer[-1]
            n = int(s)
            for i in range(n-1):
                grunnstoffer.append(a)
        
        else:
            grunnstoffer.append(s)
            
    return grunnstoffer # Returnerer en liste som ser slik ut [Ca,S,O,O,O,O]



    
if __name__=='__main__': #hvis denne fila kjøres gjelder dette og denne koden kjøres
    H2 = {
        'H': 2
        }

    O2 = {
        'O': 2
          }

    H2O = {
        'H': 2,
        'O': 1
        }

    R=[H2, O2]
    P=[H2O]


     
    r = balanser_likning_koeffisienter(R, P)
    #print (r)
    
    #print(finn_symboler('H2O13C5LiCa'))
    
    #print(lag_dict(['H','2','O','1']))
    
    #print(lag_list_dict(['H2O','H3O','NH4']))