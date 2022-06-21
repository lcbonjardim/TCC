# Programa: Controle de Acesso RFID com Raspberry Pi
# Autor: Arduino e Cia
# !/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

def cartao():

    leitorRfid = SimpleMFRC522()

    print("Aproxime o cartao da leitora...")
    id, text = leitorRfid.read()
    print("ID do cartao: ", id)
    if id == 1082030234638:
        cartaoconhecido= 'Leandro'
        GPIO.cleanup()

    elif id == 108548897250:
        cartaoconhecido = 'Alextian'
        GPIO.cleanup()

    else:
        cartaoconhecido = 'Cartão não cadastrado.'
        GPIO.cleanup()





    return cartaoconhecido


