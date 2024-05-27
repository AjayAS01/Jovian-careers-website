from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Bangaluru, India',
    'salary' : 'RS. 15,00,000'
  },
  {
    'id' : 2,
    'title' : 'App Developer',
    'location' : 'Tokyo, Japan',
    'salary' : 'Yen. 34,00,000'
  },
  {
    'id' : 3,
    'title' : 'Data Scientist',
    'location' : 'New York, America',
    'salary' : '$. 1,55,062'
  },
  {
    'id' : 4,
    'title' : 'AI Engineer',
    'location' : 'Remote',
    'salary' : 'RS. 25,00,000'
  }
]

@app.route("/")
def home():
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def job_list():
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug = True)
