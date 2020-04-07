from requests import post, get

print(get('http://127.0.0.1:5000/api/jobs/4').json())
print(post('http://127.0.0.1:5000/api/jobs/4', json={
    'team_leader': 3,
    'job': '___________',
    'work_size': 0,
    'collaborators': '',
    'is_finished': True}).json())

print(get('http://127.0.0.1:5000/api/jobs/4').json())
