import time
import datetime

from requests_html import HTMLSession
from playsound import playsound


def find_in_availability(availability):
    if "No disponible por el momento" in availability:
        return False
    elif "No sabemos si este producto volverá a estar disponible, ni cuándo" in availability:
        return False
    else:
        while(1):
            playsound('sirena.mp3')
            print("Disponible..........")

            time.sleep(40)

        return True

def notify_availability():
    # Xbox Halo infinite
    URL = "https://www.amazon.com.mx/dp/B09F2B7VDM"

    session = HTMLSession()
    response = session.get(URL)
    response.html.render(sleep=1)

    availability = response.html.xpath('//*[@id="availability"]')

    if type(availability) == list:
        valid = find_in_availability(availability[0].text)
    else:
        valid = find_in_availability(availability.text)

    if valid == False:
        find_in_availability(response.html.text)


if __name__ == "__main__":
    while(1):
        # Dormir 5 minutos
        time.sleep(300)

        notify_availability()
