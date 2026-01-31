from flask import Flask, render_template, request
import numpy as np
from wellbeing_predictor import predict_wellbeing

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        sleep = float(request.form["sleep"])
        screen = float(request.form["screen"])
        exercise = float(request.form["exercise"])
        food = float(request.form["food"])
        stress = float(request.form["stress"])
        # Must match training feature order
        features = np.array([[sleep, screen, exercise, food, stress]])

        result = predict_wellbeing(features)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
