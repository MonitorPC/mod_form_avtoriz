from requests import get, post

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/2').json())
print(get('http://localhost:5000/api/jobs/99999').json())
print(get('http://localhost:5000/api/jobs/ter').json())

print(post('http://localhost:5000/api/jobs', json={
    'team_leader': 3,
    'job': 'РАБОТА РАБОТА НИЧЕГО КРОМЕ РАБОТЫ',
    'work_size': 3,
    'collaborators': '1, 2',
    'is_finished': True}).json())
