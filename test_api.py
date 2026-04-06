import json
import urllib.request

# Login
try:
    login_data = json.dumps({'username': 'teacher', 'password': 'teacher123'}).encode()
    req = urllib.request.Request('http://localhost:3001/api/auth/login', data=login_data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req)
    login_resp = json.loads(resp.read())
    token = login_resp['data']['token']
    print(f'Token obtained: {token[:50]}...')
    
    # Get users
    req2 = urllib.request.Request('http://localhost:3001/api/users', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    resp2 = urllib.request.urlopen(req2)
    users_resp = json.loads(resp2.read())
    print(f"Success: {users_resp['success']}, Total users: {len(users_resp['data'])}")
    
    # Show students
    students = [u for u in users_resp['data'] if u.get('role') == 'student']
    print(f"Students found: {len(students)}")
    for s in students:
        print(f"  - {s['name']} (Grade {s.get('grade', '?')})")
        
    # Show all users with roles
    print("\nAll users by role:")
    for role in ['student', 'teacher', 'parent']:
        role_users = [u for u in users_resp['data'] if u.get('role') == role]
        print(f"  {role}: {len(role_users)}")
        
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
