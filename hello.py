from flask import Flask, request
app = Flask(__name__)


page="""
Hello to Dummy Container

To edit the content, go to <a href='./update' > Update Home Page </a> <br/>
<h1> <center> <font color=red> 
<marquee  scrollamount=20 > <pre>
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
"""

@app.route("/")
def hello():
    return page


@app.route("/update", methods=['GET','POST'])
def uploadfile():
    global page
    if request.method == 'POST' and 'value' in request.form:
        page= request.form['value']
        return page
    else:
        return """
        <html>
        <h1> Enter Content of File to be shown on Index Page</h1>
        <form method='post' action='./update'>
        <textarea id="value" name="value" rows="20" cols="100">"""+page+"""</textarea>
        <input type="submit">
        </form>
        </html>
        """

if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')