import pandas as pd
import matplotlib.pyplot as plt

a = [
    2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
    2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020, 2021
]

s = [
    151, 180, 200, 240, 260, 300, 350,
    380, 415, 465, 510, 540, 622, 678, 
    724, 788, 880, 937, 954, 998, 1039, 
    1100
]

plt.xlabel(u'Ano') 
plt.ylabel(u'Salário') 

plt.plot(a, s, 'r--o')

plt.show()