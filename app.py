from flask import Flask, request, jsonify, render_template
from db import create_users_table, insert_user, get_all_data, insert_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        insert_data(name, email)
    data = get_all_data()
    return render_template("index.html", data=data)

@app.route("/create-table", methods=["GET"])
def create_table_route():
    try:
        create_users_table()
        return "Таблиця users створена або вже існує.", 200
    except Exception as e:
        return f"Помилка при створенні таблиці: {e}", 500

# @app.route("/add-user", methods=["POST"])
# def add_user_route():
#     try:
#         data = request.get_json()
#         name = data["name"]
#         email = data["email"]
#         insert_user(name, email)
#         return jsonify({"status": "успішно додано", "name": name, "email": email}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # беремо порт з Render
    app.run(host="0.0.0.0", port=port)
