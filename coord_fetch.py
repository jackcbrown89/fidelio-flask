import requests

def ipinfo(ip):
    r = requests.get('http://ipinfo.io/%s/loc' % ip)
    return r.text