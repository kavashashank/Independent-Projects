#import urllib.request
from urllib2 import urlopen
from instagram.client import InstagramAPI

access_token="YOUR ACCESS TOKEN&q"
api=InstagramAPI(client_id= 'dd22a1d9196f44ac86027420bca4ba8b', client_secret='YOUR CLIENT SECRET')
scope='public_content'
url='https://api.instagram.com/v1/users/search?q=selenagomez&access_token=256684569.1677ed0.1d70988552744d388c6dea639f6fd078'
a=urlopen(url)
print(a.read())