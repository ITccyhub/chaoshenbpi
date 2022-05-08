import RPi.GPIO as GPIO		#引入RPi.GPIO库函数命名为GPIO
import time					#引入计时time函数

trig_pin = 16
echo_pin = 18

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig_pin,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(echo_pin,GPIO.IN)
    time.sleep(2)

def checkdist():
    GPIO.output(trig_pin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(trig_pin,GPIO.LOW)

    while not GPIO.input(echo_pin):
        pass
    t1 = time.time()


    while GPIO.input(echo_pin):
        pass
    t2=time.time()
    return  (t2-t1)*340 / 2
if __name__ == '__main__':
    setup()
    try:
        while True:
            print('distance: %0.2f m' % checkdist())
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
