from flask import Flask, render_template, jsonify

app = Flask(__name__) 

JOBS = [
  {
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'Salary': 'Rs.10,00,000'
},
  {
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'Salary': 'Rs.8,00,000'
},
  {
    'title': 'Frontend Engineer',
    'location': 'Dubai,UAE',
    'Salary': '$10,000'
},
  {
    'title': 'Backend Engineer',
    'location': 'Chennai, India',
    'Salary': 'Rs.15,00,000'
},
  {
    'title': 'Software Engineer',
    'location': 'Chennai, India',
    'Salary': 'Rs.15,00,000'
}


  
]


@app.route('/')
def hello():
  return render_template('home.html',
                          jobs=JOBS)

@app.route('/api/jobs')
def API():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)