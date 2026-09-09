from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json, os

app = Flask(__name__)
LOG_FILE = "click_log.json"

# Define realistic phishing campaigns - only three as requested
CAMPAIGNS = {
    "fake_invoice": {
        "name": "Invoice Payment Required",
        "subject": "Invoice #INV-2026-08942 - Payment Overdue",
        "template": "fake_invoice.html",
        "landing": "fake_invoice_landing.html"
    },
    "hr_policy": {
        "name": "HR Policy Update - Action Required",
        "subject": "Important: New Work-From-House Policy Effective Today",
        "template": "hr_policy.html",
        "landing": "hr_policy_landing.html"
    },
    "sample_email_1": {
        "name": "Password Reset Required",
        "subject": "Verify Your Identity to Avoid Account Suspension",
        "template": "sample_email_1.html",
        "landing": "landing.html"
    }
}

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE) as f:
            return json.load(f)
    return []

def save_click(campaign):
    log = load_log()

    click_data = {
        "campaign": campaign,
        "campaign_name": CAMPAIGNS.get(campaign, {}).get("name", "Unknown"),
        "timestamp": datetime.now().isoformat(),
        "ip": request.remote_addr
    }

    log.append(click_data)
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

@app.route("/")
def home():
    return render_template("index.html", campaigns=CAMPAIGNS)

@app.route("/preview/<campaign>")
def preview(campaign):
    if campaign not in CAMPAIGNS:
        return "Campaign not found", 404
    return render_template(f"{CAMPAIGNS[campaign]['template']}", campaign=campaign)

@app.route("/landing/<campaign>")
def landing(campaign):
    if campaign not in CAMPAIGNS:
        return "Campaign not found", 404
    save_click(campaign)
    return render_template(f"{CAMPAIGNS[campaign]['landing']}", campaign=campaign)

@app.route("/dashboard")
def dashboard():
    log = load_log()
    # Return only the raw click data for logging - no statistics displayed on page
    return jsonify(clicks=log)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, debug=True)