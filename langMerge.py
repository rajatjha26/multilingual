# -*- coding: utf-8 -*-
import pandas as pd
import re

inputName="Itanagar"
inputCsv=inputName+".csv"
fhbg=inputName+"_hin2ban_gmt.txt"
fhbb=inputName+"_hin2ban_bmt.txt"
febg=inputName+"_eng2ban_gmt.txt"
fhmg=inputName+"_hin2mar_gmt.txt"
fhmb=inputName+"_hin2mar_bmt.txt"
femg=inputName+"_eng2mar_gmt.txt"
fhkg=inputName+"_hin2kan_gmt.txt"
fhkb=inputName+"_hin2kan_bmt.txt"
fekg=inputName+"_eng2kan_gmt.txt"
fhtg=inputName+"_hin2tel_gmt.txt"
fhtb=inputName+"_hin2tel_bmt.txt"
fetg=inputName+"_eng2tel_gmt.txt"

file_fhbg=open(fhbg,'r')
file_fhbb=open(fhbb,'r')
file_febg=open(febg,'r')
file_fhmg=open(fhmg,'r')
file_fhmb=open(fhmb,'r')
file_femg=open(femg,'r')
file_fhkg=open(fhkg,'r')
file_fhkb=open(fhkb,'r')
file_fekg=open(fekg,'r')
file_fhtg=open(fhtg,'r')
file_fhtb=open(fhtb,'r')
file_fetg=open(fetg,'r')
df = pd.read_csv (inputCsv,sep="|",index_col=[0],na_filter=False)

ban=[]
mar=[]
kan=[]
tel=[]

for d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15 in zip(df.index.tolist(),df["English"],df["Hindi"],file_fhbg,file_fhbb,file_febg,file_fhmg,file_fhmb,file_femg,file_fhkg,file_fhkb,file_fekg,file_fhtg,file_fhtb,file_fetg):
    if(re.search(r"[#](SEG)\d",d4)):
        ban.append(d4.strip()+"|"+d4.strip()+"|"+d4.strip()+"|"+d4.strip()+"|"+d5.strip()+"|"+d6.strip())
        mar.append(d4.strip()+"|"+d4.strip()+"|"+d4.strip()+"|"+d7.strip()+"|"+d8.strip()+"|"+d9.strip())
        kan.append(d4.strip()+"|"+d4.strip()+"|"+d4.strip()+"|"+d10.strip()+"|"+d11.strip()+"|"+d12.strip())
        tel.append(d4.strip()+"|"+d4.strip()+"|"+d4.strip()+"|"+d13.strip()+"|"+d14.strip()+"|"+d15.strip())
    else:
        ban.append(d1.strip()+"|"+d2.strip()+"|"+d3.strip()+"|"+d4.strip()+"|"+d5.strip()+"|"+d6.strip())
        mar.append(d1.strip()+"|"+d2.strip()+"|"+d3.strip()+"|"+d7.strip()+"|"+d8.strip()+"|"+d9.strip())
        kan.append(d1.strip()+"|"+d2.strip()+"|"+d3.strip()+"|"+d10.strip()+"|"+d11.strip()+"|"+d12.strip())
        tel.append(d1.strip()+"|"+d2.strip()+"|"+d3.strip()+"|"+d13.strip()+"|"+d14.strip()+"|"+d15.strip())

fban=open("banglaMulti.csv",'w')
fmar=open("marathiMulti.csv",'w')
fkan=open("kannadaMulti.csv",'w')
ftel=open("teluguMulti.csv",'w')

for ban1,mar1,kan1,tel1 in zip(ban,mar,kan,tel):
    fban.write(ban1)
    fban.write("\n")
    fmar.write(mar1)
    fmar.write("\n")
    fkan.write(kan1)
    fkan.write("\n")
    ftel.write(tel1)
    ftel.write("\n")
