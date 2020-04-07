from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())
print(delete('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs').json())

print(delete('http://localhost:5000/api/jobs/re').json())
print(delete('http://localhost:5000/api/jobs/20').json())
