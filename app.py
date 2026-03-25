from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Placeholder login route for testing
@app.route("/login")
def login():
    session["username"] = "Admin"  # auto-login for testing
    return redirect(url_for("dashboard"))

# Dashboard route
@app.route("/dashboard")
def dashboard():
    # Dummy riders
    riders = [
        (1, "John Doe", "Nairobi", "Bajaj", "Active"),
        (2, "Jane Smith", "Kasarani", "TVS", "On-Duty"),
        (3, "Mike Otieno", "Kilimani", "Bajaj", "Inactive"),
    ]
    total_riders = len(riders)
    online_riders = sum(1 for r in riders if r[4] in ["Active", "On-Duty"])
    inactive_riders = sum(1 for r in riders if r[4] == "Inactive")
    
    return render_template(
        "dashboard.html",
        username=session.get("username", "Admin"),
        riders=riders,
        total_riders=total_riders,
        online_riders=online_riders,
        inactive_riders=inactive_riders
    )

# Placeholder routes for edit/delete buttons
@app.route("/edit_rider/<int:rider_id>")
def edit_rider(rider_id):
    return redirect(url_for("dashboard"))

@app.route("/delete_rider/<int:rider_id>")
def delete_rider(rider_id):
    return redirect(url_for("dashboard"))

# Logout route
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)