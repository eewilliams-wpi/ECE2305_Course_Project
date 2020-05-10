#ECE 2305 Course Project
#Authors: Emma Williams, Adam Yang, Tom Nurse, Sami Saif
#Wrapper Module

#import light_sensor
import CP_Raspberry_Pi_Code as CPC
import setup
#import reg
import smtp
import time
import asyncio

circuitPin = 7

def wrapper():
    #Display a welcome message
    print('Welcome to your smart mailbox! You may need to run this with root permissions for setup.')

    #Prompt user to input setup information only if the user has not already done setup
    setup_needed = input('Do you want to set up your device? (Y/N): ')
    if (setup_needed == 'Y'):
        setup.setup_phone() #Prompt user for setup information (Phone, WiFi)

    #Loop checking the light sensor and sending message when light is detected
    async def checkLightSensor():
        while True:
            await asyncio.sleep(1)
            if (CPC.isLight(CPC.rc_time(circuitPin)) == True): #Light is detected
                #event.set()
                smtp.send() #Send the "You've got mail!" text to user's phone
                print('Mail has arrived!')
                #event.clear()
                time.sleep(300) #Wait 5 minutes
        
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(checkLightSensor())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

        
if __name__=='__main__':
    wrapper()

