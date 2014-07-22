import requests

# Request 1.
data = {
    'task_id': 3,
    'key': "something",
    'system_id': "my system 1",
    'data': "hey!"
}

res = requests.post("http://localhost:8080/run", data=data)
data = res.json()
if data['status'] == 0:
    print "ERROR1", res.text
    exit(1)
dialog_key = data['dialog_key']
print data


# Request 2.
data = {
    'dialog_key': dialog_key,
    'data': "ho!"
}

res = requests.post("http://localhost:8080/run", data=data)
data = res.json()
if data['status'] == 0:
    print "ERROR2", res.text
    exit(2)
print data
