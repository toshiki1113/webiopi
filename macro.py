# coding: utf-8

## inport文
import webiopi
import RPi.GPIO as GPIO

##　初期化
GPIO.setmode(GPIO.BCM)
MOTOR_A1 = 26;
MOTOR_A2 = 19;
MOTOR_B1 = 13;
MOTOR_B2 = 12;



def setup():
    GPIO.setup(MOTOR_A1, GPIO.OUT)
    GPIO.setup(MOTOR_A2, GPIO.OUT)
    GPIO.setup(MOTOR_B1, GPIO.OUT)
    GPIO.setup(MOTOR_B2, GPIO.OUT)



## 以下マクロ　前進　
@webiopi.macro
def FW():
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)

## 後退
@webiopi.macro
def BK():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)

## 左旋回
@webiopi.macro
def LT():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.HIGH)
    GPIO.output(MOTOR_B1,GPIO.HIGH)
    GPIO.output(MOTOR_B2,GPIO.LOW)
    
## 右旋回
@webiopi.macro
def RT():
    GPIO.output(MOTOR_A1,GPIO.HIGH)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.HIGH)

## 停止
@webiopi.macro
def ST():
    GPIO.output(MOTOR_A1,GPIO.LOW)
    GPIO.output(MOTOR_A2,GPIO.LOW)
    GPIO.output(MOTOR_B1,GPIO.LOW)
    GPIO.output(MOTOR_B2,GPIO.LOW)
