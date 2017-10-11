EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R?
U 1 1 59C918D5
P 6050 3300
F 0 "R?" V 6130 3300 50  0000 C CNN
F 1 "R" V 6050 3300 50  0000 C CNN
F 2 "" V 5980 3300 50  0001 C CNN
F 3 "" H 6050 3300 50  0001 C CNN
	1    6050 3300
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 59C9198C
P 6050 3950
F 0 "R?" V 6130 3950 50  0000 C CNN
F 1 "R" V 6050 3950 50  0000 C CNN
F 2 "" V 5980 3950 50  0001 C CNN
F 3 "" H 6050 3950 50  0001 C CNN
	1    6050 3950
	1    0    0    -1  
$EndComp
$Comp
L Battery BT?
U 1 1 59C919D7
P 5400 3600
F 0 "BT?" H 5500 3700 50  0000 L CNN
F 1 "Battery" H 5500 3600 50  0000 L CNN
F 2 "" V 5400 3660 50  0001 C CNN
F 3 "" V 5400 3660 50  0001 C CNN
	1    5400 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 3400 5400 2900
Wire Wire Line
	5400 2900 6050 2900
Wire Wire Line
	6050 2900 6050 3150
Wire Wire Line
	5400 3800 5400 4300
Wire Wire Line
	5400 4300 6050 4300
Wire Wire Line
	6050 4300 6050 4100
$Comp
L Conn_01x01 J?
U 1 1 59C91ACC
P 6600 3600
F 0 "J?" H 6600 3700 50  0000 C CNN
F 1 "Conn_01x01" H 6600 3500 50  0000 C CNN
F 2 "" H 6600 3600 50  0001 C CNN
F 3 "" H 6600 3600 50  0001 C CNN
	1    6600 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	6050 3450 6050 3600
Wire Wire Line
	6050 3600 6050 3800
Wire Wire Line
	6050 3600 6400 3600
Connection ~ 6050 3600
$EndSCHEMATC
