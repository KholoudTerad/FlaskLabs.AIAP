from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/hello/<blog_no>', methods=['GET', 'POST'])
def blog(blog_no):
    return 'blog NO. %s!' % blog_no

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# to get "Hello John!" visit the route http://127.0.0.1:5000/hello/John . but move the route to top
# to get "blog NO. 121!" visit the route http://127.0.0.1:5000/hello/121 . but move the route to top