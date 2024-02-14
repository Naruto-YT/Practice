# FUNCIONA PARA HACER SPAM EN WHATSAPP

import pyautogui as pt
import time 

limit =  input("cantidad de mensajes: ")
message = input("mensaje: ")
i = 0

time.sleep(3)

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")

    i += 1
