#ECE 2305 Course Project
#Authors: Emma Williams, Adam Yang, Tom Nurse, Sami Saif
#Wrapper Module

#import light_sensor
import CP_Raspberry_Pi_Code as CPC
import setup
#import reg
import smtp
import time
import event

circuitPin = 7

def wrapper():
    print('Welcome to your smart mailbox! You may need to run this with sudo permissions for setup.')
    setup_needed = input('Do you want to set up your device? (Y/N): ')
    if (setup_needed == 'Y'):
        setup.setup_phone()
        
    while(True):      
        if (CPC.isLight(CPC.rc_time(circuitPin)) == True):
            smtp.send()
            print('Mail has arrived!')
            event.clear()
            time.sleep(300)
        
if __name__=='__main__':
    wrapper()

