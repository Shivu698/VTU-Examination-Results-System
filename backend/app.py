from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded sample results (NO DATABASE)
RESULTS = {
    "1RV22CS001": [
        {"subject": "Programming", "marks": 85},
        {"subject": "Maths", "marks": 78},
        {"subject": "Data Structures", "marks": 69}
    ],
    "1RV22CS002": [
        {"subject": "Programming", "marks": 72},
        {"subject": "Maths", "marks": 66}
    ]
}

@app.route("/api/results/<usn>")
def get_results(usn):
    usn = usn.upper()
    data = RESULTS.get(usn, [])
    return jsonify({"usn": usn, "results": data})

if __name__ == "__main__":
    app.run(debug=True)
