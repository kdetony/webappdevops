from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
 
 
@app.route('/test/<name>')
def success(name):
    return 'welcome %s' % name
 
 
@app.route('/login')
def login():
     return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run(debug=True, port=8888, host='0.0.0.0')

