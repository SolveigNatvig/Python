#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 08:21:07 2023

@author: solveig

Dette programmet ber om et molekyl fra brukeren på dette formatet 'H2O' som det regnes molar masse av. Programmet plotter også atomradius mot atomnummer og elektronegativitet mot atomnummer
"""

#importerer biblioteker
import csv
import matplotlib.pyplot as plt
import numpy as np
from bib import *

#lager tomme lister som senere skal fylles
atomMasse = []
navn = []
symbol = []
elektronegativitet = []
atomRadius = []
atomNummer = []


#åpner csv fila for lesing med utf8
with open("kjemi.csv", "r", encoding="utf-8-sig") as f:
    
    #henter ut innhold delt av kolon
    innhold = csv.reader(f, delimiter=",")
    
    overskrift = next(innhold)
    
    #for hver rad i fila skal det legges til info i listene
    for rad in innhold:
        atomMasse.append(float(rad[3]))
        atomRadius.append(None if rad[16] == "" else float(rad[16]))
        navn.append(str(rad[1]))
        atomNummer.append(int(rad[0]))
        symbol.append(str(rad[2]))
        elektronegativitet.append(None if rad[17]=="" else float(rad[17])) 
        #inline if-test for å forhindre trøbbel med hull i datasettet. setter inn None hvis det er et hull 
              

    
#Lager en klasse  
class Grunnstoffer:
    """
    Parametere:
        navn(str) = Grunnstoffets navn
        symbol(str) = Grunnstoffets symbol
        atmMasse(float) = massen til atomene i u
        elektronegativitet(float) = elektronegativiteten til grunnstoffene
        
    """
    
    
    def __init__(self, navn, symbol, atomMasse, elektronegativitet):
        self.navn = navn
        self.symbol = symbol
        self.atomMasse = atomMasse
        self.elektronegativitet = elektronegativitet
     
    #en metode i klassen som printer ut informasjonen vi har om grunnstofet når den kalles
    def visInfo(self):
        
        #Printer infoen i en string
        print(self.navn, 'har symbol', self.symbol, 'atommasse', self.atomMasse, 'i u, og elektronegativiteten', self.elektronegativitet)
        

        
        
#Lager en tom dictionary
grunnstoffer = {}

#legger til objekter i dictionaryen med grunnstoffets symbol som key
for i in range(len(atomMasse)):
    grunnstoffer[symbol[i]] = Grunnstoffer(navn[i], symbol[i], atomMasse[i], elektronegativitet[i])






#Funksjon som finner molar masse
def molarMasse(glist):
    Mmasse = 0 #tellevariabel
    
    #for hvert av elementene i grunnstoff-lista hentes atommassen ut og og 
    #legges sammen med de andre atommassene for å få den molare massen
    for g in glist:
        Mmasse = Mmasse + grunnstoffer[g].atomMasse
        
    return Mmasse



#funksjon som regner ut konsentrasjonen ved å ta inn den molare massen, massen i gram, og volumet i L
def regn_ut_konsentrasjon(m, V, Mm):
    
    #formelen for konsentrasjon
    c = (Mm/m)/V 
    return c


    
#Definerer funksjonen plotElektroN
def plotElektronegativitet():
    
    #En liste med anntall atomer per periode i periodesystemet
    perioder =[2,8,8,18,18,32,32]
    
    #setter startpunktet der periodene starter til 0
    startpkt = [0]
    
    for p in perioder:
        startpkt.append(startpkt[-1]+p)
     
    #lager et subplot med to plot
    fig, (plot1, plot2) = plt.subplots(2,1,figsize=(8,12)) #skriv 1, 2 inne i parentesen for å få plottene ved siden av hverandre
    
    #tittel til subplottet
    fig.suptitle('Elektronegativitet i perioder i periodesystemet')
    serier=[] #Tom liste
    for i in range(len(perioder)):
        e = np.array(elektronegativitet[startpkt[i]:startpkt[i+1]])
        x2 = np.linspace(0,1,perioder[i])
        
        #Legger til string i den tomme lista serier
        serier.append(f"Atomnr. fra {startpkt[i]} til {startpkt[i+1]}")
        
        plot2.plot(x2,e,'-o')
        plt.legend(serier)
        
        x1 = np.array(atomNummer[startpkt[i]:startpkt[i+1]])
        plot1.plot(x1,e, '-o', markersize=3)
    
    #setter egne aksetitler for hvert av de to plottene    
    plot2.set_xlabel('Fra høyre til venstre i periodesystemet')
    plot2.set_ylabel('Elektronegativitet')
    plot1.set_xlabel('Atomnummer')
    plot1.set_ylabel('Elektronegativitet')
    
    plt.show() #viser grafene
    
  
          

plt.plot(atomNummer, atomRadius,'-o', markersize = 3) # I periodesystemet avtar atomradius mot høyre og øker nedover i hver gruppe
plt.xlabel('Atomnummer') #Navn på x-akse 
plt.ylabel('Atomradius') #Navn på y-akse
plt.show() #viser grafen


#Kaller funksjon som plotter elektronegativitet
plotElektronegativitet() #elektronegativiteten øker mot høyre i periodesystemet, og avtar nedover
    
    
# ber om et stoff fta bruker
stoff = input('Skriv inn molekylet du vil finne den molare massen og konsentrasjonen av på formen H2O. Vær påpasselig med store og små bokstaver ')  


Mm = molarMasse(finn_grunnstoffer(stoff))
print(f'Den molare massen av {stoff} er {Mm:.3} g/mol')

# Ber bruker skrive inn volumet av stoffet i liter
volum = float(input('Hva er volumet av væsken stoffet er løst i L? ')) 

# Ber bruker skrive inn massen til stoffet i gram
masse = float(input('Hvor mange gram har du av stoffet? ')) 


c = regn_ut_konsentrasjon(masse, volum, Mm) # Bruker funksjonen regn_ut_Konsentrasjon til å finne konsentrasjonen

print(f'Konstentrasjonen av {masse} g {stoff} i {volum} L væske er {c:.3} mol/L')


info_symbol = input('Vil du ha litt info om et grunnstoff? skriv inn et symbol ')
grunnstoffer[info_symbol].visInfo()

        
    

