from gopigo import *
import time
import mittaukset



def eteen():
    #import mittaukset
    set_speed(100)
    fwd()
    mittaukset.mittaus()




def vasen():

    enc_tgt(1,1,6)
    fwd()
    time.sleep(2)
    stop()
    set_speed(75)
    time.sleep(0.5)
                       
    enc_tgt(0,1,18)
    left()
    time.sleep(3)
    stop()
    enc_tgt(1,1,15)
    fwd()
    time.sleep(2.5)
    mittaukset.mittaus()

def oikea():
    
    enc_tgt(1,1,6)
    fwd()
    time.sleep(2)
    stop()
    set_speed(75)
    time.sleep(0.5)
                                 
    enc_tgt(1,0,18)
    right()
    time.sleep(3)
    stop()
    enc_tgt(1,1,15)
    fwd()
    time.sleep(2)   
    mittaukset.mittaus()

def ukaannos():

    stop()
    set_speed(50)
    time.sleep(0.2)
                        
    enc_tgt(1,1,18)
    right_rot()
    time.sleep(4)
    stop()
    mittaukset.mittaus()

def korjausvasen():

    fwd()
    set_right_speed(50)
    time.sleep(1)
    set_right_speed(100)
    set_left_speed(70)
    time.sleep(1)
    set_left_speed(100)
    mittaukset.mittaus()
    
def korjausoikea():

    fwd()
    set_left_speed(50)
    time.sleep(1)
    set_left_speed(100)
    set_right_speed(70)
    time.sleep(1)
    set_right_speed(100)
    mittaukset.mittaus()

eteen()
    
