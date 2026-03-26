from flask import Flask, render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Login route (GET + POST)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Temporary login (replace with DB later)
        if username == "admin" and password == "admin123":
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


# Dashboard (protected)
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

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
        username=session["username"],
        riders=riders,
        total_riders=total_riders,
        online_riders=online_riders,
        inactive_riders=inactive_riders
    )


# Edit rider (placeholder)
@app.route("/edit_rider/<int:rider_id>")
def edit_rider(rider_id):
    return redirect(url_for("dashboard"))


# Delete rider (placeholder)
@app.route("/delete_rider/<int:rider_id>")
def delete_rider(rider_id):
    return redirect(url_for("dashboard"))


# Logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))