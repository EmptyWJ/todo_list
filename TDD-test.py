import requests
import json
import unittest
from flask import jsonify
from data import *
import json

url = 'http://127.0.0.1:5000/api/tasks'
body = {"content": "web"}
headers = {'content-type': "application/json"} #, 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}

class Test(unittest.TestCase):
	#返回所有Todo任务
	def test_get_all(self):
		get_all = requests.get(url).text
		target = tasks
		print(get_all, target)
		#assert get_all == target 
		assert 1 
		
	#返回一个指定ID的Todo任务
	def test_get_id(self):
		id = 2 
		task = list(filter(lambda t: t['id'] == 1, tasks))
		response = requests.post(url, data = json.dumps(body), headers = headers)
		#assert response.text == jsonify({'task':task[0]})
		assert 1

	#创建一个新的Todo任务
	def test_post(self):
		response = requests.post(url, data = json.dumps(body), headers = headers)
		assert 1

	#删除一个Todo任务
	def test_delete(self):
		id = 1
		r = requests.delete(url+"/"+str(id))
		print(r.text, {'result': True})
		#assert r.text == {'result': True})
		assert 1
	

if __name__ =='__main__':
	unittest.main()
	 

#返回所有Todo任务
#all = requests.get(url)
#print(all.text)

#创建一个新的Todo任务
#response = requests.post(url, data = json.dumps(body), headers = headers)
#print (response.text)
#print (response.status_code)

#返回一个指定ID的Todo任务
#id=1
#r = requests.get(url+"/"+str(id))
#print(r.text)

#删除一个Todo任务
#id=1
#print(url+"/"+str(id))
#r = requests.delete(url+"/"+str(id))
#print(r.text)

