# Esquemático

## Esquema temporal

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/EsquematicoTempo.JPG "width=100")

## Regulador
En esta seccion se encuentra el regulador de tensión buscando obtener una salida de 3.3V, para este proposito se hizo uso del regulador AMS1117. Por otro lado se implemento un diodo LED que ayuda a verificar el momento en el que el circuito se energice, el diodo schottky 1N5819 nos ayuda a asegurar que la tensión que pase por el regulador en la entrada V1 no se devuelva a la tension de entrada USB, finalmente los condensadores... . 

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/Regulador.JPG "width=70")
A la salida del regulador se conecto un led que nos indica cuando el circuito se encuentre energizado, ya que la tensión de un led es de 1,6V y su corriente de peración es de 5mA la resistencia necesaria para su funcionamiento es de 330.

### LTspice
Con ayuda del IDE de LTspice diseñamos un pequeño cicuito y de este modo analizar la salida que se espera tener en este sistema, para este se usa un regulador LM317 con el cual se espera obtener un comportamiento similar con el AMS1117.

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/SimRegulador.JPG "width=40")

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/SimResultRegulador.JPG "width=70")

## ENABLE/BOOT
La tensión en el enable y el boot en un caso ideal se considera con valores de 0 y 1, sin embargo esta se encuentra en un umbral de funcionamiento, en donde el valor de cero puede tomar hasta un valor de 0.124 mientras que para el funcionamiento del enable se tomo desde un valor de 0.7 el cual se va representar con ayuda de un diodo led.
### Ltspice
La tensión de caida de un diodo esta dado por 0.7V y la corriente en el led es de 5mA, por otro lado la corriente en el enable del ESP32 es de 264uA.
![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/ResistenciaEn.JPG "width=40")
![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/CircEnable.JPG "width=40")



## ESP32
![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/esp32-wroom-pinout.png)

Para el desarrollo de este proyecto se hizo uso de un Soc ESP32-WROOM, debido a que representa una solucion ideal para suplir las necesidades de este proyecto. El Soc ESP32-WROOM entre otras cosas, posee un chip capaz de controlar multiplez sensores a la vez por medio de software y ademas cuenta tanto con modulo bluetooth como WIFI integrados, perimitiendo de esta manera la conxion inalambrica con otros dispositivos sin necesidad de un modulo complementario. 

Ahora, el proyecto se realizo teniendo en cuenta las condiciones de operacion y las limitaciones del ESP32-WROOM, este dispositivo debe ser alimentado idealmente con un voltaje de 3,3V o como maximo con un voltaje de 3,6V y puede entregar por sus pines de salida una corriente maxima de 1200mA. Ahora con respecto a sus diferesntes pines, la imagen anterior ilustra cada uno d ellos y sus particularidades.    

## Conectores

## USB

## MPU


