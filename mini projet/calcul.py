from heure import *


### Calcul du temps ###
print('Calcul du temps')
def CalculDuTemps(distance):
    d = distance
    duree = 0
    nbrPause =int(d / 168)
    duree += float(nbrPause * 2.0) + float(nbrPause* 0.25)
    print(nbrPause)
    dist = float(d) - float(nbrPause) * 168
    if(dist < 15):  
        dist -= 15
        duree += 0.3
        duree += dist / 90
    else:
        duree += 0.9
    
    DecimalToHeure(duree)

