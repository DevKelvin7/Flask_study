from flask import Flask, jsonify
app=Flask(__name__)

@app.route("/json_test")
def hello_json():
    data={'name':'김대리','family':'byun'}
    return jsonify(data)

@app.route("/server_info")
def sever_info():
    data={'server_name':'0.0.0.0','server_port':'8081'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8081")