
### Conversion de la durée ###

def DecimalToHeure(duration):
     duration = str(duration)
     print(duration)
     h,m = duration.split('.')
     print(m)
     m = int(m)*60
     if m < 1000 :
         hm = str(h) + 'h' +'0'+ str(m)[0:1]
     else :
          hm = str(h) , 'h' , str(m)[0:2]
     print(hm)

