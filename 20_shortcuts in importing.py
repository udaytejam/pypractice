#module is just another python script

#you can find them at C://Python34/Lib --> all of your modules

import statistics as s
from statistics import variance as v, mean as m

listt = [1,2,3,4,3,2,2,3]
print(s.mean(listt))

x = v(listt) #don't even need to reference to module. Directly use the method
y = m(listt)

print(x,y)


#from statistics import * --> don't have to reference to statistics
