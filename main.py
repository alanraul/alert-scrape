#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

from requests_html import HTMLSession
from playsound import playsound


def find_in_availability(availability):
    if "No disponible por el momento" in availability:
        return False
    elif "No sabemos si este producto volverá a estar disponible, ni cuándo" in availability:
        return False
    elif "Necesitamos asegurarnos de que no eres un robot" in availability:
        print("Detectado como robot ........")
        playsound('sirena.mp3')
        return True
    else:
        while(1):
            playsound('sirena.mp3')
            print("Disponible..........")

            time.sleep(40)

        return True

def notify_availability(url, valid):
    # Xbox Halo infinite
    #URL = "https://www.amazon.com.mx/dp/B09F2B7VDM"

    session = HTMLSession()
    session.delete(url)
    response = session.get(url, headers={'Cache-Control': 'no-cache'})
    response.html.render(sleep=10)

    availability = response.html.xpath('//*[@id="availability"]')

    if type(availability) == list:
        if len(availability) > 0:
            valid = find_in_availability(availability[0].text)
    else:
        valid = find_in_availability(availability.text)

    if valid == False:
        valid = find_in_availability(response.html.text)


    session.close()

    return valid

if __name__ == "__main__":
    valid = False

    while(valid == False):
        valid = notify_availability(sys.argv[2], valid)

        # Dormir 5 minutos
        time.sleep(300)
