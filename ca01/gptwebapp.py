'''

'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
# app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def home():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>CA 01</h1>
        <a href="/about">About page</a><br>
        <a href="/team">Team page</a><br>
        <a href="/index">Index page</a><br>
    '''

@app.route('/about')
def about():
    return "<h1>About Page</h1>This is a program that can do lots of useful things"

@app.route('/team')
def team():
    return f'''
        <h1>Team Page</h1>
        <ul>
        <li>Shichao He: Sophomore, CS major, author of factorization function</li><br>
        <li>Xu (Charles) Cai: Sophomore, CS and Math major, author of fibonacci_sequence function</li>
        <li></li>
        </ul>
    '''

@app.route('/index')
def index():
    return f'''
        <h1>Index Page</h1>
        <a href="/index/factorization">Factorizing a polynomial</a><br>
        <a href="/index/fibonacci">Generate a fibnoacci sequence</a><br>
    '''


#The factorization funciton will get a polynomial and give the result after the factorization
@app.route('/index/factorization', methods=['GET', 'POST'])
def factorization():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the result of polynomial factorization:
        <div style="border:thin solid black">{answer}</div>
        <a href=/factorizing> do another factorization</a>
        '''
    else:
        return '''
        <h1>Shichao He factorizing app</h1>
        Enter your polynomial that needs to be factorized(start with factorizing)
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''
#The factorization funciton will get a polynomial and give the result after the factorization
@app.route('/index/fibonacci', methods=['GET', 'POST'])
def fibonacci_sequence():
    ''' generate a fibonacci sequence with the specified length 
    from user
    '''

    if request.method == 'GET':
        
        return '''
        <h1>Fibonacci Sequence Generator</h1>
         <form method="post">
            Enter the length of fibonacci sequence you wish to generate: <input type="text" name="length"><br>
            <p><input type=submit value="generate">
        </form>
        <br>
        <a href=/index> Back to Home Page</a>

        
        '''
    elif request.method == 'POST':
        length = request.form['length']
        answer = gptAPI.fibonacci_sequence(length)
        return f'''
        <h1>Fibonacci Sequence Generator</h1>
        <pre style="bgcolor:yellow">length: {length}</pre>
        <hr>
        Here is the result fibonacci sequence:
        <pre style="border:thin solid black">{answer}</pre>
        <a href=index/fibonacci> Generate another sequence</a>
        <br>
        <a href=/index> Back to Home Page</a>
        '''
    
    
    

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5000)