from flask import Flask,render_template,redirect,request
import requests
url='https://api.npoint.io/05ed93b3954a315624a2'
response=requests.get(url)
posts=response.json()

app = Flask(__name__)

@app.route("/")
def index_page():
    context={
        'allposts':posts
    }
    return render_template('index.html',context=context)

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/post/<int:id>")
def post_page(id=0):
    
    request_post=''
    if id==0:
        message='No Post Found'
        context={
            'message':message
        }
    else:
        for post in posts:
            if post['id']==id:
                request_post=post
        context={
            'message':request_post
        }
    return render_template('post.html',context=context)

@app.route("/contact",methods=["POST","GET"])
def contact_page():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        print(name,email,phone,message)
    return render_template('contact.html')


if __name__=="__main__":
    app.run(debug=True)