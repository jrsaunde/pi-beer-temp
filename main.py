#!/usr/bin/env python
import time
import eeml
from temp import Temp

# COSM variables. API_KEY and FEED are specific
API_KEY = 'SCf8E2SZG3W68pbyUuf1qzg9umMWy6VCkHoeVuuDPEjI2SPN'
FEED = '2053937525'
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)

#replace 28-00000449ef31 below with the id of your temperature probe
sensor1=Temp(fileName='28-000004d93f9d')
sensor2=Temp(fileName='28-000004d9ad58')
sensor1.start()
sensor2.start()

#the rest of your code is below.
# The Temp class will be updating on its own thread which will allow you to do
#  anything you want on the main thread.
while True:

        temp1 =  sensor1.getCurrentTemp()
        temp2 = sensor2.getCurrentTemp()

        print temp1
        print temp2

        #open cosm feed
        pac = eeml.Pachube(API_URL, API_KEY)

        #send fahrenheit data
        pac.update([eeml.Data('Fermenter_Temp', temp1, unit=eeml.Fahrenheit())])
        pac.update([eeml.Data('Closet_Temp', temp2, unit=eeml.Fahrenheit())])

        #send data to cosm
       # if((temp1 > 55 and temp1 < 110) and (temp2 >50 and temp2 <110)):
        if( (temp1 > 40) and (temp1 < 110) and (temp2 > 40) and (temp2 < 110)):
                pac.put()

        #hang out and do nothing for 30 seconds, dont flood cosm
        time.sleep(30)

