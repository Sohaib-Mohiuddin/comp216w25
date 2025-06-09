'''
Created by Narendra for COMP216 June 2020
wk05_9a_handling_requests.py

A flask application to handle request for lab05.
Not meant for code inspection
Might contain advanced coding
'''

import urllib
from flask import Flask, url_for, request

users = {
    'ilia': {
        'fname': 'Ilia',
        'lname': 'Nika',
        'age': 56
    },
    'narendra': {
        'fname': 'Narendra',
        'lname': 'Pershad',
        'age': 45
    },
    'hao': {
        'fname': 'Hao',
        'lname': 'Lac',
        'age': 40
    }
}

app = Flask(__name__)

def process_docstring(docs):
    raw = docs.splitlines()              #split into lines
    tok = [x.strip() for x in raw]       #remove leading and trailing spaces
    tok = [x for x in tok if len(x) > 0] #remove empty tokens
    result = tok[0] + '</a><br/>'        #first token will the part of the hyper link
    for x in range(1, len(tok)):         #skip the first token
        result += tok[x] + '<br/>'       #just add text to the result
    return result +'</br>'

@app.route('/')
def index():
    '''
    The main landing page
    Builds a lisk of all the routes published by this flask application
    Appends the doc string to each route. The result is what you are seeing now!
    '''
    result = '<ol>'
    for route in app.url_map.iter_rules():
        if  route.endpoint != 'static':
            result += f'<li> <a href="{route}">{process_docstring(eval(route.endpoint).__doc__)}' + '</li>'
    return result + '</ol>'
    
@app.route('/test0')
def test0():
    '''
    Returns some static text to the client
    Check the server terminal for the request headers
    '''
    print(f'\nHeaders: \n{request.headers}') 
    return 'the home page'

@app.route('/test1') 
def test1():                                
    '''
    returns a single json object (dictionary) to the client<br/>[browser sup]
    '''
    return {'name': 'Narendra', 'course': 'COMP216', 'semester': 'Fall 2020'}

@app.route('/test2')
def test2():
    '''
    Returns the arguments that was sent by the request<br/>[browser sup only if query string supplied]
    '''
    return request.args

@app.route('/profs/')
def show_profs():
    '''
    Returns all the users in the collection<br/>[browser sup]
    '''
    return users

@app.route('/cookies/')
def show_cookies():
    '''
    Returns the cookies that was sent to this server
    '''
    return request.cookies

@app.route('/uploads', methods=['POST'])
def upload_file():
    '''
    Provides the means for a client to upload a file
    to this server.
    It will append a .bak extension the file when 
    saving and return this new name to the client.
    '''
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(f'{uploaded_file.filename}.bak')
    return f'{uploaded_file.filename}.bak successfully uploaded'


@app.route('/admin/add', methods = ['POST'])
def add_prof(): 
    '''
    Adds a user to the data store
    A message is returned to the client
    This end point can only be accessed via a POST command
    '''     
    prof = request.get_json() 
    users.update(prof)
    return f' {prof} was added to the list of registered users'

@app.route('/admin-form', methods=['GET', 'POST']) 
def form_example():
    '''
    The endpoint is able to process both GET and POST requests<br/>[browser sup]
    GET returns a table of the form data submitted
    POST returns an input form to capture data
    '''
    if request.method == 'POST':
        print(request.args)                      #returns a table to the client
        return f'''
        <table>
        <tr><td>First name</td><td>-- {request.form.get('fname')} --</td></tr>
        <tr><td>Last name</td><td>-- {request.form.get('lname')} --</td></tr>
        <tr><td>Age</td><td>-- {request.form.get('age')} --</td></tr>
        <tr><td colspan="2"><input type="submit" value="Submit"></td></tr>
        </table>
        '''
    else:                                        #HTTP GET command, returns an html form 
        return '''
        <form method="POST">
        <table>
        <tr><td>First name</td><td><input type="text" name="fname"></td></tr>
        <tr><td>Last name</td><td><input type="text" name="lname"></td></tr>
        <tr><td>Age</td><td><input type="text" name="age"></td></tr>
        <tr><td colspan="2"><input type="submit" value="Submit"></td></tr>
        </table>
        </form>
        '''


@app.route('/blog/<int:postID>')      #using converter type
def show_blog(postID):
    '''
    Returns some text prepended to your parameter<br/>[browser sup only if argument is supplied]
    '''
    return f'Blog Number: {postID}'

if __name__ == '__main__':
	app.run(debug=True, port=5444)      #app.run(host, port, debug, options)


#curl --request GET --url http://127.0.0.1:5000/

# GET /people reads all the people
# POST /people creates a person and adds to list
# DELETE /people/{key} deletes a person
# GET /people/{key} reads a person
# PUT /people/{key} updates a person

'''
<li> <a href="/admin/add">Adds a user to the collection</a><li/><li> <a href="/admin-form">
    GET returns a table of the form submitted<br/>
    POST returns an input form
    </a><li/>
<li> <a href="/test0">
    Returns some static text<br/>
    Check the server terminal for the request headers
    </a><li/>
<li> <a href="/test1">returns a static json object (dictionary)</a><li/>
<li> <a href="/test2">Returns the arguments that was sent by the request</a><li/>
<li> <a href="/profs/">Returns all the users in the collection </a><li/><li> <a href="/">The main landing page</a><li/><li> <a href="/blog/<int:postID>">Returns some text prepended to your parameter</a><li/>
'''