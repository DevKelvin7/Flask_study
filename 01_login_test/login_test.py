from flask import Flask, jsonify, request, render_template
app=Flask(__name__)

@app.route('/login')
def login():
    username=request.args.get('username')
    pw=request.args.get('pw')
    email=request.args.get('email_address')
    if username=='dave' and pw=='1234':
        return_data={'auth':'success'}
    else:
        return_data={'auth':'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html')

if __name__ =='__main__':
    app.run(debug=True,port=8081)