import pandas as pd
import math
df=pd.read_csv("main.csv")
mass=df["Mass"].tolist()
radius=df["Radius"].tolist()
newMass=[]
newRadius=[]
gravity=[]
for i in range(1,50,2):
    r=float(radius[i])*6.957e+8
    m=float(mass[i])*1.989e+30
    newRadius.append(r)
    newMass.append(m)
    g=6.67*pow(10,-11)*(m/pow(r,2))
    gravity.append(g)
newdf=pd.DataFrame({"radius":newRadius,"mass":newMass,"gravity":gravity})
newdf.to_csv("calculated.csv")
