from machine import SoftI2C
from machine import I2C
from machine import Pin
from machine import sleep
import mpu6050

##FUNCIONA###

import bluetooth
from ble_advertising import advertising_payload
import ble_uart_peripheral

from micropython import const
import time
addr=0x68

ble = bluetooth.BLE()
uart = ble_uart_peripheral.BLEUART(ble)

def on_rx():
    print("rx: ", uart.read().decode().strip())

uart.irq(handler=on_rx)

try:
    while True:
        if addr==0x68:
            #Mder_1
            i2c11 = SoftI2C(scl=Pin(16), sda=Pin(5))     #initializing the I2C method for ESP32
            mpu11= mpu6050.accel(i2c11,addr)
            AC11=mpu11.get_values()
            print(str(AC11[1]),str(AC11[2]),str(AC11[3]),'i2c11')
            uart.write(str(AC11[1]) + str(AC11[2])+ str(AC11[3])+ 'i2c11' +"\n")
            #P_der1
#             i2c21 = SoftI2C(scl=Pin(17), sda=Pin(18))     #initializing the I2C method for ESP32
#             mpu21= mpu6050.accel(i2c21,addr)
#             AC21=mpu21.get_values()
#             print(str(AC21[1]),str(AC21[2]),str(AC21[3]),'i2c21')
#             uart.write(str(AC21[1]) + str(AC21[2])+ str(AC21[3])+ 'i2c21' +"\n")
# # 
            i2c31 = SoftI2C(scl=Pin(13), sda=Pin(15))     #initializing the I2C method for ESP32
            mpu31= mpu6050.accel(i2c31,addr)
            AC31=mpu31.get_values()
            print(str(AC31[1]),str(AC31[2]),str(AC31[3]),'i2c31')
            uart.write(str(AC31[1]) + str(AC31[2])+ str(AC31[3])+ 'i2c31' +"\n")
            
            i2c41 = SoftI2C(scl=Pin(2), sda=Pin(4))     #initializing the I2C method for ESP32
            mpu41= mpu6050.accel(i2c41,addr)
            AC41=mpu41.get_values()
            print(str(AC41[1]),str(AC41[2]),str(AC41[3]),'i2c41')
            uart.write(str(AC41[1]) + str(AC41[2])+ str(AC41[3])+ 'i2c41' +"\n")
            
            i2c51 = SoftI2C(scl=Pin(25), sda=Pin(26))     #initializing the I2C method for ESP32
            mpu51= mpu6050.accel(i2c51,addr)
            AC51=mpu51.get_values()
            print(str(AC51[1]),str(AC51[2]),str(AC51[3]),'i2c51')
            uart.write(str(AC51[1]) + str(AC51[2])+ str(AC51[3])+ 'i2c51' +"\n")
            
            i2c61 = SoftI2C(scl=Pin(27), sda=Pin(14))     #initializing the I2C method for ESP32
            mpu61= mpu6050.accel(i2c61,addr)
            AC61=mpu61.get_values()
            print(str(AC61[1]),str(AC61[2]),str(AC61[3]),'i2c61')
            uart.write(str(AC61[1]) + str(AC61[2])+ str(AC61[3])+ 'i2c61' +"\n")
          
            i2c71 = SoftI2C(scl=Pin(32), sda=Pin(33))     #initializing the I2C method for ESP32
            mpu71= mpu6050.accel(i2c71,addr)
            AC71=mpu71.get_values()
            print(str(AC71[1]),str(AC71[2]),str(AC71[3]),'i2c71')
            uart.write(str(AC71[1]) + str(AC71[2])+ str(AC71[3])+ 'i2c71' +"\n")
          
            
            
            addr=0x69;
        
        else:
            #M_der1
            i2c12 = SoftI2C(scl=Pin(16), sda=Pin(5))     #initializing the I2C method for ESP32
            mpu12= mpu6050.accel(i2c12,addr)
            AC12=mpu11.get_values()
            print(str(AC12[1]),str(AC12[2]),str(AC12[3]),'i2c12')
            uart.write(str(AC12[1]) + str(AC12[2])+ str(AC12[3])+ 'i2c12' +"\n")
            #P_der1
            
#             i2c22 = SoftI2C(scl=Pin(17), sda=Pin(18))     #initializing the I2C method for ESP32
#             mpu22= mpu6050.accel(i2c22,addr)
#             AC22=mpu21.get_values()
#             print(str(AC22[1]),str(AC22[2]),str(AC22[3]),'i2c22')
#             uart.write(str(AC22[1]) + str(AC22[2])+ str(AC22[3])+ 'i2c22' +"\n")

            i2c32 = SoftI2C(scl=Pin(13), sda=Pin(15))     #initializing the I2C method for ESP32
            mpu32= mpu6050.accel(i2c32,addr)
            AC32=mpu32.get_values()
            print(str(AC32[1]),str(AC32[2]),str(AC32[3]),'i2c32')
            uart.write(str(AC32[1]) + str(AC32[2])+ str(AC32[3])+ 'i2c32' +"\n")
            
            i2c42 = SoftI2C(scl=Pin(2), sda=Pin(4))     #initializing the I2C method for ESP32
            mpu42= mpu6050.accel(i2c42,addr)
            AC42=mpu42.get_values()
            print(str(AC42[1]),str(AC42[2]),str(AC42[3]),'i2c42')
            uart.write(str(AC42[1]) + str(AC42[2])+ str(AC42[3])+ 'i2c42' +"\n")
            
            i2c52 = SoftI2C(scl=Pin(25), sda=Pin(26))     #initializing the I2C method for ESP32
            mpu52= mpu6050.accel(i2c51,addr)
            AC52=mpu52.get_values()
            print(str(AC52[1]),str(AC52[2]),str(AC52[3]),'i2c52')
            uart.write(str(AC52[1]) + str(AC52[2])+ str(AC52[3])+ 'i2c52' +"\n")
            
            i2c62 = SoftI2C(scl=Pin(27), sda=Pin(14))     #initializing the I2C method for ESP32
            mpu62= mpu6050.accel(i2c62,addr)
            AC62=mpu62.get_values()
            print(str(AC62[1]),str(AC62[2]),str(AC62[3]),'i2c62')
            uart.write(str(AC62[1]) + str(AC62[2])+ str(AC62[3])+ 'i2c62' +"\n")
            
#             
#             
            addr=0x68;
            
        #########33#############3
        ######################

        
        
        time.sleep_ms(100)

except KeyboardInterrupt:
    pass

uart.close()



