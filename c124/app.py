from pydoc import describe
from flask import Flask,jsonify,request

app=Flask(__name__)

#creating a array of tasks

tasks=[
    {'id':1,
    'title':"Buy groceries",
    'description':"milk,cheese,pizz",
    'done':False
    },
    { 'id':2,
    'title':'Learn Python',
    'description':" Need A Good Python Tutorial",
    'done':False
    },

]


@app.route("/")
def hello_world():
    return "how are you"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

        task = {
            'id':tasks[-1]['id'] + 1,
             'title':request.json['title'],
             'description':request.json.get('description',""),
             'done':False               
        }
        tasks.append(task)
        return jsonify({
            "status":"success",
            "message":"Task added sucessfully"
        })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })        

if __name__=='__main__':
    app.run(debug=True)


