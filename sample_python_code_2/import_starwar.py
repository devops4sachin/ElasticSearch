from elasticsearch import Elasticsearch
import json
import requests

def set_conn(uri):
	res = requests.get(uri)
	if res != None:
		print("We can reach to Elasticsearch cluster successfully")
	
	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
	return res, es


def index_people(resp, es):
	i = 1
	while resp.status_code == 200:
		resp = requests.get('http://swapi.co/api/people/'+ str(i))
		es.index(index='sw', doc_type='people', id=i, body=json.loads(resp.content.decode('utf-8')))
		i=i+1

def get_people(i, es):
	print(es.get(index='sw', doc_type='people', id=i))
	print(es)


def get_using_name(es):
	es.search(index='sw', body={"query": {"match": {'name':'Darth Vader'}}})
	print(es)


def get_using_approx(es):
	es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})


if __name__ == '__main__':
	uri = "http://localhost:9200"
	print("setting connection")
	res, es = set_conn(uri)
	
	#index_people(res, es)
	get_people(1, es)

