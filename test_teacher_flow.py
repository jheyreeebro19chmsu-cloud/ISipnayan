import json
import urllib.request

# Simulate teacher login and data fetch
try:
    # Step 1: Login as teacher
    login_data = json.dumps({'username': 'teacher', 'password': 'teacher123'}).encode()
    req = urllib.request.Request('http://localhost:3001/api/auth/login', data=login_data, headers={'Content-Type': 'application/json'})
    resp = urllib.request.urlopen(req)
    login_resp = json.loads(resp.read())
    
    token = login_resp['data']['token']
    teacher_id = login_resp['data']['user']['id']
    teacher_name = login_resp['data']['user']['name']
    print(f'Logged in as: {teacher_name} (ID: {teacher_id})')
    print(f'Token: {token[:50]}...\n')
    
    # Step 2: Get all users (like TeacherDashboard does)
    print('Step 1: Fetching all users...')
    req2 = urllib.request.Request('http://localhost:3001/api/users', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    resp2 = urllib.request.urlopen(req2)
    users_resp = json.loads(resp2.read())
    all_users = users_resp['data']
    print(f'  Total users: {len(all_users)}')
    
    # Step 3: Filter students (like TeacherDashboard filterting)
    students = [u for u in all_users if u.get('role') == 'student']
    print(f'  Students: {len(students)}')
    for s in students:
        print(f'    - {s["name"]} (ID: {s["id"]}, Grade: {s.get("grade", "?")})')
    
    # Step 4: Get assignments (like TeacherDashboard does)
    print('\nStep 2: Fetching assignments...')
    req3 = urllib.request.Request('http://localhost:3001/api/assignments', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    resp3 = urllib.request.urlopen(req3)
    assign_resp = json.loads(resp3.read())
    all_assignments = assign_resp['data']
    print(f'  Total assignments: {len(all_assignments)}')
    for a in all_assignments[:3]:
        print(f'    - {a["title"]} (ID: {a["id"]})')
    if len(all_assignments) > 3:
        print(f'    ... and {len(all_assignments) - 3} more')
    
    # Step 5: Get assignments for teacher (monitoring)
    print('\nStep 3: Fetching assignments for teacher...')
    req4 = urllib.request.Request(f'http://localhost:3001/api/assignments?teacherId={teacher_id}', headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'})
    resp4 = urllib.request.urlopen(req4)
    teach_assign_resp = json.loads(resp4.read())
    teacher_assignments = teach_assign_resp['data']
    print(f'  Teacher assignments: {len(teacher_assignments)}')
    
    print(f'\n✅ All data loading works correctly!')
    
except Exception as e:
    print(f'❌ Error: {e}')
    import traceback
    traceback.print_exc()
