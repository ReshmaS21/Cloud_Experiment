import os
import yaml

from flask import Flask, request, render_template

app = Flask(__name__)

# Load configuration from the config.yaml file
config_env = os.environ.get("FLASK_ENV", "development")
with open("config.yaml", "r") as config_file:
    config = yaml.safe_load(config_file)[config_env]

app.config.update(config)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user's name from the form
        user_name = request.form["name"]
        
        # Generate a personalized greeting
        greeting = f"Hello, {user_name}!"
        
        return render_template("index.html", greeting=greeting)
    
    # If it's a GET request or the form hasn't been submitted yet, just render the form
    return render_template("index.html", greeting=None)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
