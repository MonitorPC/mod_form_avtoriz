from requests import get, post, delete

print(get('http://localhost:5000/api/jobs'))
print(delete('http://localhost:5000/api/jobs/1'))
print(get('http://localhost:5000/api/jobs'))

print(delete('http://localhost:5000/api/jobs/re'))
print(delete('http://localhost:5000/api/jobs/20'))
