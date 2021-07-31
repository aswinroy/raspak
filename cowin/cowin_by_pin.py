import requests
import json
import datetime
import winsound
import time

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 10000  # Set Duration To 1000 ms == 1 second

while(1):
    try:
        pin = ['673603','673604','673580']
        for p in pin:
            #print('pin:',p)
            d = datetime.date.today().strftime("%d-%m-%y")
            param = {"pincode":p,"date":d}
            resp = requests.get(url, params=param, headers=headers)
            #print('resp',resp)
            data = resp.json()
            for center in data["centers"]:
                #print(center['address'])
                for session in center["sessions"]:
                    #print(session["available_capacity"])
                    if(int(session["available_capacity"])>2 and int(session["min_age_limit"]) >=45):
                        print(center['address'])
                        print('available capacity',session["available_capacity"])
                        winsound.Beep(frequency, duration)

    except:
        print("Something went wrong")

    time.sleep(10)
