from datetime import *
from sorted_months_weekdays import *

def Day(x):
   
    b=[]
    c=[]

    for key in x.keys():
        c.append(x[key])
        c.sort()

    for i in x:
        a = date.fromisoformat(i)  
        b.append(a.strftime("%a"))

    zipped = dict(zip(Weekday_Sorted_Week(b),c))

    print(zipped)
y = {"2021-01-25":2,"2020-12-31":8,"2020-12-01":4,"2020-12-02":6,"2021-01-30":12,"2021-01-29":10,"2021-01-31":14}   
 
Day(y)



    