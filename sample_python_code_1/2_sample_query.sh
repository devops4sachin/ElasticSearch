curl -XPOST http://localhost:9200/test/articles/_search?pretty=true -d '{
    "query": {
        "match": {
            "content": "cruise"
        }
    }
}'
