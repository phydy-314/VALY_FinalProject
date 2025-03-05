from flask import Flask, render_template
import os

# Chỉ định thư mục chứa template (frontend)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")  # Kiểm tra lại tên file có đúng không

if __name__ == "__main__":
    app.run(debug=True)
#python -m flask --app backend.app run