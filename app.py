from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Remote',
        'salary' : 'N 2,000,000'
    },
    {
        'id' : 2,
        'title' : 'Data Engineer',
        'location' : 'Abuja, Nigeria',
        'salary' : 'N 5,000,000'
    },
    {
        'id' : 3,
        'title' : 'Chief of Operations',
        'location' : 'Abuja, Nigeria',
        'salary' : 'N 10,000,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name = 'Enoch')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)