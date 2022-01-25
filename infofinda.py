import requests
import time

def outer_func(color):
    def inner_function(msg):
        print(f"{color}{msg}")

    return inner_function


GREEN  = outer_func("\033[92m")
YELLOW = outer_func("\033[93m")
RED    = outer_func("\033[91m")


username = input("\033[92m/+/ Enter username to search from: ")


# Links 

instagram = f"https://www.instagram.com/{username}"

facebook = f"https://www.facebook.com/{username}"

cashapp = f"https://cash.app/"

twitter = f"https://www.twitter.com/{username}"

aboutme = f"https://about.me/{username}"

imgur = f"https://imgur.com/user/{username}"

flipboard = f"https://flipboard.com/@{username}"

slideshare = f"https://slideshare.net/{username}"

fotolog = f"https://fotolog.com/{username}"

spotify = f"https://open.spotify.com/user/{username}"

mixcloud = f"https://www.mixcloud.com/{username}"

patreon = f"https://www.patreon.com/{username}"

bitbucket = f"https://bitbucket.org/{username}"

etsy = f"https://www.etsy.com/shop/{username}"

cashme = f"https://cash.me/{username}"

keybase = f"https://keybase.io/{username}"

codecademy = f"https://www.codecademy.com/{username}"

pastebin = f"https://pastebin.com/u/{username}"

youtube = f"https://www.youtube.com/{username}"

reddit = f"https://www.reddit.com/user/{username}"

wordpress = f"https://{username}.wordpress.com"

pinterest = f"https://www.pinterest.com/{username}"

github = f"https://www.github.com/{username}"

tumblr = f"https://{username}.tumblr.com"

steam = f"https://steamcommunity.com/id/{username}"

vimeo = f"https://vimeo.com/{username}"

soundcloud = f"https://soundcloud.com/{username}"

medium = f"https://medium.com/@{username}"

roblox = f"https://www.roblox.com/user.aspx?username={username}"

wattpad = f"https://www.wattpad.com/user/{username}"

buzzfeed = f"https://buzzfeed.com/{username}"

tripadvisor = f"https://tripadvisor.com/members/{username}"

wikipedia = f"https://www.wikipedia.org/wiki/User:{username}"

hackernews = f"https://news.ycombinator.com/user?id={username}"

ebay = f"https://www.ebay.com/usr/{username}"

slack = f"https://{username}.slack.com"


''' WEBSITE LIST - USE FOR SEARCHING OF USERNAME '''

LINKS = [
instagram, facebook, twitter, youtube, reddit,
wordpress, pinterest, github, tumblr, steam, vimeo, soundcloud, 
medium, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
mixcloud, patreon, bitbucket, etsy, cashme, keybase, codecademy, pastebin, roblox,
wattpad, buzzfeed, tripadvisor, wikipedia, hackernews, ebay, slack, ]



def search():
    YELLOW(r"""
    ｉｎｆｏ ｆｉｎｄａ 

    Ｖ１．２

    ｂｙ ｓｉｍ－ｂｙｔｅ""")

    time.sleep(2)
    print("")
    GREEN(f"// Searching for {username} //")
    print("")
    time.sleep(2)

    GREEN(f"/+/ {username} found! /+/")
    print("")
    time.sleep(1)

    valid = 0
    match = True

    for url in LINKS:

        r = requests.get(url)

        if r.status_code == 200:

            if match == True:
                GREEN("/+/ FOUND VALIDS /+/")
                print("")
                match = False

            YELLOW(f"\n{url} ")

            if username in r.text:
                GREEN(f"/+/ {username} Found! /+/")

            else:
                RED(f"/-/ {username} NOT found /-/")
        valid += 1

    total_valid = len(LINKS)

    GREEN (f"// DONE! //")
    GREEN (f"//{valid} matches found out of {total_valid} links//")



if __name__=="__main__":
    search()
