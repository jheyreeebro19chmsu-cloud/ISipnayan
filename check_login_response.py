import json
import urllib.request

try:
    login_data = json.dumps({'username': 'teacher', 'password': 'teacher123'}).encode()
    req = urllib.request.Request('http://localhost:3001/api/auth/login', data=login_data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req)
    login_resp = json.loads(resp.read())
    
    print("Login response structure:")
    print(json.dumps(login_resp, indent=2))
    
except Exception as e:
    print(f'Error: {e}')
