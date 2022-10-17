import random
def detect(temp,humi):
	    if(humi<30):
	        if(temp>30):
	            print("Humidity : ",humi,"Temperature :",temp,"Alarm Turned On")
for i in range(0,15):
	    temp=random.randint(14,50)
	    humi=random.randint(15,50)
	    detect(temp,humi)