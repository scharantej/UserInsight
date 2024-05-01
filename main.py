
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/findings')
def findings():
    findings = ['Finding 1', 'Finding 2', 'Finding 3']  # Placeholder data, retrieve from database or file
    return render_template('findings.html', findings=findings)

if __name__ == '__main__':
    app.run()
