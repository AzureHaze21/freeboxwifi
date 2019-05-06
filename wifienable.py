import sys
import json
import requests
import browser_cookie3 

for cookie in browser_cookie3.load():
	if 'mafreebox.freebox.fr' in cookie.domain:
		print('Cookie: ' + cookie.name + '=' + cookie.value)
		url = 'http://mafreebox.free.fr/api/v4/wifi/config/'
		print('Shutting down wifi...') if sys.argv[1]=='disable' else print('Turning on wifi...')
		res = requests.put(url, headers={ 'Cookie': cookie.name+'='+cookie.value }, json={ "enabled": False if sys.argv[1]=='disable' else True })
		print(res.json())
