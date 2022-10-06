import requests
#https://youtu.be/DqtlR0y0suo  Testing out this method
url = "https://api.recollect.net/api/areas/Austin/services/waste/pages/en-US/place_calendar.json"

querystring = {"widget_config":"{\"js_host\":\"https://api.recollect.net\",\"version\":\"0.11.1664211408\",\"api_host\":\"https://api.recollect.net\",\"third_party_cookie_enabled\":1,\"name\":\"calendar\",\"base\":\"https://recollect.net\",\"area\":\"Austin\",\"schedule_view\":1}","_":"1664844148485"}

headers = {
    "cookie": "recollect-locale=en-US; temp-client-id=D3291396-3BFC-11ED-A651-949AB7EA60BB",
    "authority": "api.recollect.net",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "dnt": "1",
    "referer": "https://api.recollect.net/w/areas/Austin/services/323/pages/place_calendar",

    "sec-ch-ua-mobile": "?0",

    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "x-recollect-locale": "en-US",
    "x-recollect-place": "77916FA4-DF69-11E8-8A3F-5432682931C6:323:Austin",
    "x-requested-with": "XMLHttpRequest",
    "x-widget-instance": "D3291396-3BFC-11ED-A651-949AB7EA60BB",
    "x-widget-version": "0.11.1664211408"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response['sections'][1]['rows'][0]['html'])
print(response['sections'][1]['rows'][1]['html'])
print(response['sections'][1]['rows'][2]['html'])
print(response['sections'][1]['rows'][3]['html']) #this one is the recycling, but i'll have to test it next week

#success! gives me the date and the bins that need to go out, all in
#simple json file that i can then pass to variables!  This makes
#my life so much easier.