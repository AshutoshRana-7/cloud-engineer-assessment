from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1 style="color: #2E86C1;">Cloud Engineer Assessment</h1>
        <h2>Hi, I am Ashutosh 👋</h2>
        <p>Here is my assessment project.</p>
        <p style="color: green;"><b>Successfully running and deployed on AWS EC2.</b></p>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)