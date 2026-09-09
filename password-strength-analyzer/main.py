from flask import Flask, render_template, request, jsonify
import re
import secrets
import string
import math

app = Flask(__name__)

COMMON_PASSWORDS = [
    "password", "123456", "123456789",
    "qwerty", "abc123", "password123",
    "admin", "letmein"
]

def estimate_crack_time(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset += 32
    if charset == 0:
        return "instant"
    combinations = charset ** len(password)
    guesses_per_second = 1e9  # rough offline brute-force estimate
    seconds = combinations / guesses_per_second
    if seconds < 1: return "instant"
    if seconds < 60: return f"{seconds:.0f} seconds"
    if seconds < 3600: return f"{seconds/60:.0f} minutes"
    if seconds < 86400: return f"{seconds/3600:.0f} hours"
    if seconds < 31536000: return f"{seconds/86400:.0f} days"
    return f"{seconds/31536000:.0f} years"

def evaluate_password(password):
    score = 0
    feedback = []

    if not password:
        feedback.append("Password cannot be empty.")
        return score, feedback, "instant"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters required.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a commonly used weak password.")
        score = 0

    crack_time = estimate_crack_time(password)
    return score, feedback, crack_time

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")
    score, feedback, crack_time = evaluate_password(password)
    return jsonify(score=score, feedback=feedback, crack_time=crack_time)

@app.route("/generate_password")
def generate_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = "".join(secrets.choice(alphabet) for _ in range(14))
    return jsonify(password=pwd)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)