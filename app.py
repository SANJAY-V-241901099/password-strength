from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 5:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions

@app.route("/", methods=["GET", "POST"])
def home():
    strength = ""
    suggestions = []

    if request.method == "POST":
        password = request.form["password"]
        strength, suggestions = check_strength(password)

    return render_template(
        "index.html",
        strength=strength,
        suggestions=suggestions
    )

if __name__ == "__main__":
    app.run(debug=True)