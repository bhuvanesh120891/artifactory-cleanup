import json
import requests
from requests.structures import CaseInsensitiveDict
f = open('test.json')

# returns JSON object as
# a dictionary
data = json.load(f)
domain = "http://<jfrog_url>/artifactory/"
headers = CaseInsensitiveDict()
headers["Authorization"] = "<Header for Auth>"
complete=[]
filtered=[]
for i in data['results']:
    artifact_name=i['repo']+'/'+i['path']+'/'
    url = domain+artifact_name
    filtered.append(url)
q = open('complete.json')
data1 = json.load(q)
for i in data1['results']:
    artifact_name=i['repo']+'/'+i['path']+'/'
    url = domain+artifact_name
    complete.append(url)
print(len(complete))
print("#################################")
print(len(filtered))
print("#################################")
to_delete=list(set(complete).symmetric_difference(set(filtered)))
print(len(to_delete))

for i in to_delete:
    print("The %s artifact going to get cleaned up"%(i))
resp1 = requests.post(domain+"api/trash/empty", headers=headers)
print(resp1.status_code)
