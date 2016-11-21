# import json
import requests
#
# r = requests.get("https://private-anon-42901ac37d-timdorr.apiary-mock.com/api/1/vehicles/1234567890/data_request/drive_state")
# print r.content
# json.loads(r.content)
#
from urllib2 import Request, urlopen
import json

headers = {
  'Authorization': 'Bearer {access_token}'
}
#request = Request('https://private-anon-32c2b4f262-timdorr.apiary-mock.com/api/1/vehicles/1/data_request/drive_state', headers=headers)
response_body = requests.get("https://private-anon-32c2b4f262-timdorr.apiary-mock.com/api/1/vehicles/1/data_request/drive_state")
t = response_body.content
print t
#print t['latitude']
#print j