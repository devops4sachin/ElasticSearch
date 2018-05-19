'''
Querying Elasticsearch using REST requests
'''
import requests
import json

def search(uri, term):
	""" Querying Elastic Search """
	""" json.dumps is to encode in the JSON """
	query = json.dumps({
		"query": {
			"match": {
				"content": term
			 }
		}
	})
	
	response = requests.get(uri, data=query)
	results = json.loads(response.text) # to decode the JSON format in string. We will get the result in JSON format.
	return results

def format_results(results):
	""" Prints formatted results:
	doc_id:) content """
	data = [doc for doc in results['hits']['hits']]
	for doc in data:
		print("{}:) {}".format(doc['_id'], doc['_source']['content']))

def create_doc(uri, doc_data={}):
	""" Creating a new document """
	query = json.dumps(doc_data)
	response = requests.post(uri, data=query)
	print(response)


if __name__ == '__main__':
	uri_search = 'http://localhost:9200/test/articles/_search'
	uri_create = 'http://localhost:9200/test/articles'

	print("Sending the search query for cruise bikes")
	results = search(uri_search, "cruise")

	format_results(results)
	
	create_doc(uri_create, {"content": "I also like City bikes"})
	results = search(uri_search, "city")
	format_results(results)
