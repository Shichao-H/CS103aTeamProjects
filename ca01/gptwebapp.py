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
        <h1>CA 01 - Team 31</h1>
        <a href="/about">About page</a><br>
        <a href="/team">Team page</a><br>
        <a href="/index">Index page</a><br>
    '''

@app.route('/about')
def about():
    '''
    This is the about page of our team which explains the main theme 
    of our team's web project
    Author: Xu (Charles) Cai
    '''
    return '''
    <h1>About Page</h1><br><h4>Welcome to our math enthusiast's web page! Our site is designed to help you 
    solve a variety of mathematical problems quickly and easily. Whether you need to factor a polynomial, g
    enerate a Fibonacci series, or find the greatest common divisor of two numbers, our site has got you covered.</h4>
    <br>
    <h4>Whether you're a beginner looking to learn more about math, or an experienced mathematician looking for powerful 
    tools to help you solve complex problems, our site has something to offer. So why not give us a try today and see
    how we can help you master the world of mathematics?</h4>
    '''


@app.route('/team')
def team():
    '''
    This method gives introduction of each team member
    '''
    return f'''
        <h1>Team Page</h1>
        <ul>
        <li>Shichao He: Sophomore, CS major, author of factorization function</li><br>
        <li>Xu (Charles) Cai: Sophomore, CS and Math major, author of fibonacci_sequence function</li><br>
        <li>Yukun Zhang: Sophomore, CS and Math major, author of greatest_common_divisor</li><br>
        <li>Xiaoyang Zhang: Sophomore, CS and Econ major, author of is_prime</li><br>
        </ul>
        <a href=/> Back to Home Page</a>
    '''

@app.route('/index')
def index():
    '''
    This page links to each member's program page
    '''
    return f'''
        <h1>Index Page</h1>
        <a href="/index/factorization">Factorizing a polynomial</a><br>
        <a href="/index/fibonacci">Generate a fibnoacci sequence</a><br>
        <a href="/index/greatestcommondivisor">Find the greatest common divisor of the two numbers</a><br>
        <a href="/index/isPrime">Check if a number is prime</a><br><br>
        <a href=/> Back to Home Page</a>
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
        <h1>Result of factorization</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the result of polynomial factorization:
        <div style="border:thin solid black">{answer}</div>
        <a href=/index/factorization> do another factorization</a>
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

    
#This function will generate a fibonacci series with given length 
@app.route('/index/fibonacci', methods=['GET', 'POST'])
def fibonacci_sequence():
    ''' 
    generate a fibonacci sequence with the specified length from user
    @Author: Xu (Charles) Cai
    '''

    if request.method == 'GET':
        return '''
        <h1>Fibonacci Sequence Generator</h1><h5>Author: Xu (Charles) Cai</h5>
         <form method="post">
            Enter the length of fibonacci sequence you wish to generate: <input type="text" name="length"><br>
            <p><input type=submit value="generate">
        </form>
        <br>
        <a href=/> Back to Home Page</a>
        '''
    
    elif request.method == 'POST':
        length = request.form['length']
        answer = gptAPI.fibonacci_sequence(length)
        return f'''
        <h1>Fibonacci Sequence Generator11</h1>
        <pre style="bgcolor:yellow"> {length}</pre>
        <hr>
        Here is the result fibonacci sequence:
        <pre style="border:thin solid black">{answer}</pre>
        <hr>
        <a href=/index/fibonacci> Generate another sequence</a>
        <br>
        <a href=/index> Back to Index Page</a>
        <br>
        <a href=/> Back to Home Page</a>
        '''


@app.route('/index/greatestcommondivisor', methods=['GET', 'POST'])    
def greatest_common_divisor():   
    ''' find the greatest common divisor of the two numbers
        provided from the user
    '''

    if request.method == 'GET':
        return f'''
        <h1>Yukun Zhang Find Greatest Common Divisor</h1>
        <form method="post">
            Enter the two numbers which you would like to calculate the greatest common divisor (number 1): <input type="text" name="num1"><br>
            Enter the two numbers which you would like to calculate the greatest common divisor (number 2): <input type="text" name="num2"><br>
            <p><input type=submit value="get response">
        </form>
        <br>
        <a href=/index> Back to Home Page</a>
        '''
    
    else:
        num1 = request.form['num1']
        num2 = request.form['num2']
        answer = gptAPI.greatest_common_divisor(num1, num2)
        return f'''
        <h1>Greatest Common Divisor</h1>
        <pre style="bgcolor:yellow">num1: {num1}</pre>
        <pre style="bgcolor:yellow">num2: {num2}</pre>
        <hr>
        This is the greatest common divisor:
        <pre style="border:thin solid black">{answer}</pre>
        <a href=/index/greatestcommondivisor> Enter another two numbers</a>
        <br>
        <a href=/index> Back to Home Page</a>
        '''
   
@app.route('/index/isPrime', methods=['GET', 'POST'])
def is_prime():
    ''' check if a given number is a prime number '''

    if request.method == 'GET':

        return '''
        <h1>Prime Number Checker</h1>
         <form method="post">
            Enter the number you wish to check: <input type="text" name="number"><br>
            <p><input type=submit value="check">
        </form>
        <br>
        <a href=/index> Back to Home Page</a>

        
        '''
    elif request.method == 'POST':
        number = request.form['number']
        answer = gptAPI.is_prime(number)
        return f'''
        <h1>Prime Number Checker</h1>
        <pre style="bgcolor:yellow">number: {number}</pre>
        <hr>
        Here is the result of the prime check:
        <pre style="border:thin solid black">{answer}</pre>
        <a href=/index/isPrime> Check another number</a>
        <br>
        <a href=/index> Back to Home Page</a>
        '''           
        
        

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
