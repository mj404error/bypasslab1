from flask import Flask,render_template,url_for,redirect,request,abort

app = Flask(__name__)


@app.route('/')
# @app.route('/home')
def home():
    name='Lab 1'
    return render_template('index.html',title='Lab1 MJ Script',username=name) 

@app.route('/admin/login')
def admin_login():
    user = request.headers.get('Host')
    if 'localhost' in user.lower():
        return render_template('admin.html')
    else:
        return abort(403)
    

@app.route('/admin')
def check_http_headers():
    # Get the Host header from the request
    host = request.headers.get('Host')

    if 'localhost' in host.lower():
        return redirect(url_for('admin_login'))

    else:
        return abort(403)
    

if __name__=='__main__':
    app.run(debug=True)
