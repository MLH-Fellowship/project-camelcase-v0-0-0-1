# !/bin/bash

# create new post
curl -X POST http://localhost:5000/api/v1/timeline_post -d 'name=Dario&email=test1@gmail.com&content=Just testing my end points!' 2> stderr > stdout
cat stdout

#deleting post
ID=$(jq '.id' stdout)
curl -X DELETE "http://localhost:5000/api/v1/timeline_post/$ID"

#remove the output files
rm stderr stdout
