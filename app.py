import requests
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS


app=Flask(__name__)

cors=CORS(app)


query="django api"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method =="POST":
        data=request.get_json()

        query=data.get('searchterm')

        url=f"http://openlibrary.org/search.json?q={query}"

        response=requests.get(url)

        data=response.json()

        count=0

        docs=data.get('docs')



        print(type(docs))

        for i in docs:
            print(i.get('title'))
            print(i.keys())
            print("======================")
            print("\n")
        print(f"count: {count}")


        return jsonify(docs)
        

    
    
    return render_template('index.html')



if __name__ =="__main__":
    app.run(debug=True)