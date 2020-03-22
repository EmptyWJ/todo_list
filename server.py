from flask import Flask,jsonify,abort,request
import datetime
from data import *
app = Flask(__name__)



@app.route('/api/tasks', methods=['GET'])
def get_tasks():
	return jsonify({'tasks':tasks})

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
	task = list(filter(lambda t: t['id'] == id, tasks))
	if len(task) == 0:
		abort(404)
	return jsonify({'task':task[0]})


@app.route('/api/tasks', methods=['POST'])
def create_task():
	if not request.json or not 'content' in request.json:
		abort(400)
	task = {
	    'id': tasks[-1]['id']+1,
	    'content':request.json['content'],
	    'createdTime':request.json.get('createdTime',datetime.datetime.now()),
	}
	tasks.append(task)
	return jsonify({'task':task}), 201

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
	task = list(filter(lambda t: t['id'] == id, tasks))
	if len(task) == 0:
		abort(404)
	tasks.remove(task[0])
	return jsonify({'result': True})
if __name__ == '__main__':
	app.run(host='127.0.0.1',debug=True)

