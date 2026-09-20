
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.context_processor
def inject_demo():
    return {
        "app_name": "CivicClean AI",
        "tagline": "Cleaner Today • Greener Tomorrow"
    }

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html", title="Create Account")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("login.html", title="Login")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Citizen Dashboard")

@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        return redirect(url_for("ai_preview"))
    return render_template("report.html", title="Report Waste")

@app.route("/ai-preview")
def ai_preview():
    return render_template("ai_preview.html", title="AI Detection Preview")

@app.route("/rewards")
def rewards():
    return render_template("rewards.html", title="My Rewards")

@app.route("/reports")
def reports():
    return render_template("reports.html", title="My Reports")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/community")
def community():
    return render_template("community.html", title="Community")

@app.route("/admin")
def admin():
    return render_template("admin.html", title="Admin Dashboard")

@app.route("/mobile")
def mobile():
    return render_template("mobile.html", title="Mobile Preview")

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
