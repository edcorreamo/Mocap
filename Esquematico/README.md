# Esquemático

## Esquema temporal

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/EsquematicoTempo.JPG "width=100")

## Regulador
En esta seccion se encuentra el regulador de tensión buscando obtener una salida de 3.3V, para este proposito se hizo uso del regulador AMS1117. Por otro lado se implemento un diodo LED que ayuda a verificar el momento en el que el circuito se energice, el diodo schottky 1N5819 nos ayuda a asegurar que la tensión que pase por el regulador en la entrada V1 no se devuelva a la tension de entrada USB, finalmente los condensadores... . 

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/Regulador.JPG "width=70")

### LTspice
Con ayuda del IDE de LTspice diseñamos un pequeño cicuito y de este modo analizar la salida que se espera tener en este sistema, para este se usa un regulador LM317 con el cual se espera obtener un comportamiento similar con el AMS1117.

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/SimRegulador.JPG "width=70")

![](https://github.com/edcorreamo/Mocap/blob/main/imagenes/Regulador.JPG "width=70")

## ESP32

## Conectores

## USB

## MPU

## Esquema temporal
