from bs4 import BeautifulSoup
import requests


def find_current_cap_hit(player_found=True):
    input_player = input("Please input players name with a hyphen for a space. \nEX: Auston Matthews: 'auston-matthews': ")
    url = "https://www.capfriendly.com/players/" + input_player
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    try:
        name = doc.select('h1.c')[0].text.strip().title()
        team = doc.select('h3.c')[0].text.strip().title()
        sal = doc.find_all(['td'],class_="b")
    except:
        print("Player not found.")
        player_found = False
    if player_found != False:
        try:
            print("Player:", name, "\nTeam: ", team, "\nYear:", sal[0].string, "\nCap Hit:", sal[2].string)
        except:
            print("Player does not have an active contract for current season")
    request_another_player = input("Would you like to search for another player? ('Y/N') : ")
    if request_another_player.upper() == "Y":
        find_current_cap_hit()

if __name__ == "__main__":
    find_current_cap_hit()