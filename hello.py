from flask import Flask, render_template, request
import os

counter = 0

app = Flask(__name__)

print("aaaa" +str(counter))

@app.route("/")
def hello_world():
    print("bbbbbb")
    liczba = 1 / 0
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    name = request.args.get("name")
    print(name)
    global counter
    counter += 1
    # return sklej_htmla(counter)
    return render_template("example.html", my_counter = counter, name = name)

@app.route("/test2", methods = ['POST'])
def test2():
    name = request.form.get("name")
    print(name)
    global counter
    counter += 1
    # return sklej_htmla(counter)
    return render_template("example.html", my_counter = counter, name = name)


@app.route("/test2", methods = ['GET'])
def test2a():
    return "akuku"

def sklej_htmla(counter):
    wygenerowany_htnl =  "<h1>Hi!</h1> Counter:  " + str(counter)
    print(wygenerowany_htnl)
    return wygenerowany_htnl

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Port is " + str(port))
    print("ccccccc")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
    )