from elasticsearch import Elasticsearch

if __name__ == '__main__':
	es = Elasticsearch()
	res = es.search(index="test", doc_type="articles", body={"query": {"match": {"content": "cruise"}} })
	print("{} documents found:".format(res['hits']['total']))
	for doc in res['hits']['hits']:
		print("{} )  content:{}".format(doc['_id'], doc['_source']['content']))
	#	print("%s) %s" % (doc['_id'], doc['_source']['content']))


'''
res contents are as below

{  
   'took':6,
   'timed_out':False,
   '_shards':{  
      'successful':5,
      'total':5,
      'failed':0
   },
   'hits':{  
      'max_score':0.11506981,
      'hits':[  
         {  
            '_id':'2',
            '_source':{  
               'content':'Super bikes are faster than cruise bikes'
            },
            '_index':'test',
            '_score':0.11506981,
            '_type':'articles'
         },
         {  
            '_id':'3',
            '_source':{  
               'content':'But for long rides I like cruise bikes'
            },
            '_index':'test',
            '_score':0.095891505,
            '_type':'articles'
         },
         {  
            '_id':'4',
            '_source':{  
               'content':'Honda and Harley are super and cruise bikes'
            },
            '_index':'test',
            '_score':0.095891505,
            '_type':'articles'
         }
      ],
      'total':3
   }
}
'''
