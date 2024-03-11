#RO_Page032_02

qKWh = float(input("quantitat de KWh= "))
pKWh = float(input("preu per KWh= "))

if qKWh > 700:
    preutotal= (qKWh * pKWh) * 1.05 #càlcul del preu total+5%
    
else:
    preutotal= qKWh * pKWh
    print("preutotal= ", preutotal)
    
print("preutotal= ", preutotal)    

