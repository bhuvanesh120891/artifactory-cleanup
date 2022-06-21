#!/bin/bash

product=${1}
echo "$product"

RESULTS=`curl -s -X POST -u <username>:<password> "http://<jfrog_url>/artifactory/api/search/aql" -H "content-type: text/plain" -d 'items.find({"repo":{"$eq":"<Repo_name>"}},{"path": {"$match" : "'"*${product}*"'"}}).sort({"$desc" : ["created"]}).limit(10)'`

COMPLETE_RESULTS=`curl -s -X POST -u <username>:<password> "http://<jfrog_url>/artifactory/api/search/aql" -H "content-type: text/plain" -d 'items.find({"repo":{"$eq":"<Repo_name>"}},{"path": {"$match" : "'"*${product}*"'"}})'`

echo "$RESULTS" > test.json

echo "$COMPLETE_RESULTS" > complete.json
