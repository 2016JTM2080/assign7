###### this is the second .py file ###########

import random    #importing radom from the python library
  
count=0     
#count denotes the no of users in the unit circle

for u in range(1,101):
	(X,Y)=(random.random()*2- 1, random.random()*2-1)
	u=u+1
	
	if((X**2+Y**2)<=1):
		count+=1

perc=(float(count)/100)*100

print "Percentage of users in the unit circle around the MSC is" ,perc
