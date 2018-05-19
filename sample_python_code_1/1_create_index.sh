curl -XPOST http://localhost:9200/test/articles/1 -d '{
    "content": "I like super bikes"
}'
curl -XPOST http://localhost:9200/test/articles/2 -d '{
    "content": "Super bikes are faster than cruise bikes"
}'
curl -XPOST http://localhost:9200/test/articles/3 -d '{
    "content": "But for long rides I like cruise bikes"
}'
curl -XPOST http://localhost:9200/test/articles/4 -d '{
    "content": "Honda and Harley are super and cruise bikes"
}'

