from flask import Flask, render_template

app = Flask(__name__)

# Sample student data (you can replace this with your own data)
students = [
    {"name": "John Doe", "major": "Computer Science"},
    {"name": "Jane Smith", "major": "Engineering"},
    {"name": "Alice Johnson", "major": "Biology"},
]

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
