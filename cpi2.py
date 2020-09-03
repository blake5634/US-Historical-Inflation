#!/usr/bin/python3
#
#
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.dates import DayLocator
from decimal import Decimal

fname = 'inflByYr.txt'
#fname = 'inflByYr1971.txt'
base_year = 1977

#
##  Data sample
#Jul 1, 2020 	0.99%
#Jan 1, 2020 	2.49%
#Jan 1, 2019 	1.55%
#Jan 1, 2018 	2.07%
#Jan 1, 2017 	2.50%
#
#  Data Source
#  https://jobs.utah.gov/wi/data/library/wages/uscpihistory.html
#    State of Utah
#


#Year,U,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,Avg,Prior

yrs = []
pct = []    # percent inflation
cumul = []  # cumulative cost of living

with open(fname, mode='r', encoding="UTF-8", newline='') as f:
    for l in f:
        st_yr = l[7:11]
        st_pct = l.split('\t')[1]
        st_pct = st_pct[:-2]
        #print(st_yr, st_pct, '%')
        yrs.append(int(st_yr))
        pct.append(float(st_pct))
        
print('loaded: ',len(yrs), ' data years')

yrs.reverse()
pct.reverse()

cpi = 1.00
for i,y in enumerate(yrs):
    cumul.append(cpi)
    cpi *= 1.0 + pct[i]/100.0
    
yi = yrs.index(base_year)
norm = cumul[yi]

for i,c in enumerate(cumul):
    c /= norm
    cumul[i] = c

plt.figure(1)
#ax=plt.axes()
#ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M %d.%m.%Y'))
#ax.xaxis.set_minor_locator(DayLocator())
p1 = plt.plot(yrs,pct,linestyle='solid')

plt.ylabel('1-yr Inflation (%)')
plt.title('Rate of Inflation')
plt.grid()
#plt.grid(axis='x',which='minor')

plt.figure(2)
p2 = plt.plot(yrs,cumul)
plt.grid()

plt.ylabel('Cost' )
plt.title('Cumulative Cost of Living Relative to '+str(base_year))

plt.show()
