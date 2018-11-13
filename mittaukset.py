import RPi.GPIO as GPIO
from gopigo import *
import time
#import liikkuminen


def mittaus():

    pulse_start = 0
    while True:
        import liikkuminen
        
        GPIO.setmode(GPIO.BCM)
        TRIG = 14 
        ECHO = 15

        #print "Distance Measurement In Progress"

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG, False)
        #print "Waiting For Sensor To Settle"
        #time.sleep(0.5)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        """print "Eteen:",distance,"cm"
        sleep(0.5)
        print "Oikea: ",us_dist(10),"cm"
        sleep(0.5)
        print "Vasen: ",us_dist(15), "cm"
        sleep(0.5)"""

        GPIO.cleanup()


        eteen = distance
        vasen = us_dist(15)
        oikea = us_dist(10)

        # poistetaan mahdolliset virhelukemat
        if vasen == 0 or vasen > 3000:
            vasen = 26

        if oikea == 0 or oikea > 3000:
            oikea = 26

        print "Eteen: ", eteen, "cm", "Vasen:", vasen, "cm","Oikea",oikea, "cm"
        
        """print "Vasen:", vasen, "cm"
       
        print "Oikea",oikea, "cm","""

        if vasen < 5:
            # vasen seina liian lahella
            liikkuminen.korjausvasen()

        if oikea < 5:
            # oikea seina liian lahella
            liikkuminen.korjausoikea()
        
        
        if vasen > 30:
            # jos voi kaantya vasemmalle
            liikkuminen.vasen()
            
        elif eteen < 25 and oikea > 40:
            # jos ei voi kaantya vasemmalle tai jatkaa suoraan
            liikkuminen.oikea()

        elif eteen < 18 and vasen < 25 and oikea < 25:
            # jos saavutaan umpikujaan
            liikkuminen.ukaannos()

        else:
            liikkuminen.eteen()

#mittaus()        
