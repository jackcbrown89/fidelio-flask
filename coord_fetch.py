import requests, geoip2, json

def ipinfo(ip):
    r = requests.get('http://freegeoip.net/json/%s' % ip)
    j = json.loads(r.content)
    jlat = j['latitude']
    jlon = j['longitude']
    jcoord = [jlat, jlon]
    return jcoord
