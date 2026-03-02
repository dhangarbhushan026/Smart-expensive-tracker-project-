

# # app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash
# import os

# DB_PATH = "expenses.db"

# def get_conn():
#     return sqlite3.connect(DB_PATH)

# def init_db():
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL,
#                     password TEXT NOT NULL
#                 )""")
#     c.execute("""CREATE TABLE IF NOT EXISTS expenses (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id INTEGER NOT NULL,
#                     amount REAL NOT NULL,
#                     description TEXT,
#                     date TEXT NOT NULL,
#                     category TEXT,
#                     FOREIGN KEY(user_id) REFERENCES users(id)
#                 )""")
#     conn.commit()
#     conn.close()

# # initial categories (frontend expects names/colors/keywords)
# CATEGORIES = [
#     {"id":1,"name":"Food","color":"#6366F1"},
#     {"id":2,"name":"Transport","color":"#10B981"},
#     {"id":3,"name":"Entertainment","color":"#F59E0B"},
#     {"id":4,"name":"Shopping","color":"#EC4899"},
#     {"id":5,"name":"Utilities","color":"#3B82F6"},
#     {"id":6,"name":"Health","color":"#EF4444"},
#     {"id":7,"name":"Other","color":"#64748B"}
# ]

# app = Flask(__name__, static_folder='../frontend', static_url_path='/')
# CORS(app)  # allow frontend to call backend (for local dev)

# # Initialize DB file
# if not os.path.exists(DB_PATH):
#     init_db()
# else:
#     # still ensure tables exist when app restarts
#     init_db()

# @app.route("/")
# def root():
#     return app.send_static_file("index.html")

# @app.route("/categories", methods=["GET"])
# def categories():
#     return jsonify(CATEGORIES)

# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.json
#     name = data.get("name")
#     email = data.get("email")
#     password = data.get("password")
#     if not (name and email and password):
#         return jsonify({"error":"Name, email and password required"}), 400
#     hashed = generate_password_hash(password)
#     try:
#         conn = get_conn()
#         c = conn.cursor()
#         c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
#                   (name, email, hashed))
#         conn.commit()
#         user_id = c.lastrowid
#         conn.close()
#         return jsonify({"message":"Signup successful", "user_id": user_id})
#     except sqlite3.IntegrityError:
#         return jsonify({"error":"Email already exists"}), 400

# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     email = data.get("email")
#     password = data.get("password")
#     if not (email and password):
#         return jsonify({"error":"Email and password required"}), 400
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("SELECT id, password, name FROM users WHERE email = ?", (email,))
#     row = c.fetchone()
#     conn.close()
#     if row and check_password_hash(row[1], password):
#         return jsonify({"message":"Login successful", "user_id": row[0], "name": row[2]})
#     return jsonify({"error":"Invalid credentials"}), 400

# @app.route("/add_expense", methods=["POST"])
# def add_expense():
#     data = request.json
#     user_id = data.get("user_id")
#     amount = data.get("amount")
#     description = data.get("description", "")
#     date = data.get("date")
#     category = data.get("category", None)
#     if not (user_id and amount is not None and date):
#         return jsonify({"error":"Missing fields"}), 400
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("INSERT INTO expenses (user_id, amount, description, date, category) VALUES (?, ?, ?, ?, ?)",
#               (user_id, amount, description, date, category))
#     conn.commit()
#     conn.close()
#     return jsonify({"message":"Expense added"})

# @app.route("/get_expenses/<int:user_id>", methods=["GET"])
# def get_expenses(user_id):
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("SELECT id, amount, description, date, category FROM expenses WHERE user_id = ?", (user_id,))
#     rows = c.fetchall()
#     conn.close()
#     expenses = [{"id": r[0], "amount": r[1], "description": r[2], "date": r[3], "category": r[4]} for r in rows]
#     return jsonify(expenses)

# if __name__ == "__main__":
#     print("Starting Flask on http://127.0.0.1:5000")
#     app.run(debug=True)


















# # app.py (upgraded - drop-in for your original backend)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sqlite3
# from werkzeug.security import generate_password_hash, check_password_hash
# import os
# from datetime import datetime, timedelta

# DB_PATH = "expenses.db"

# def get_conn():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# def init_db():
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     name TEXT NOT NULL,
#                     email TEXT UNIQUE NOT NULL,
#                     password TEXT NOT NULL
#                 )""")
#     c.execute("""CREATE TABLE IF NOT EXISTS expenses (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id INTEGER NOT NULL,
#                     amount REAL NOT NULL,
#                     description TEXT,
#                     date TEXT NOT NULL,
#                     category TEXT,
#                     FOREIGN KEY(user_id) REFERENCES users(id)
#                 )""")
#     conn.commit()
#     conn.close()

# CATEGORIES = [
#     {"id":1,"name":"Food","color":"#6366F1"},
#     {"id":2,"name":"Transport","color":"#10B981"},
#     {"id":3,"name":"Entertainment","color":"#F59E0B"},
#     {"id":4,"name":"Shopping","color":"#EC4899"},
#     {"id":5,"name":"Utilities","color":"#3B82F6"},
#     {"id":6,"name":"Health","color":"#EF4444"},
#     {"id":7,"name":"Other","color":"#64748B"}
# ]

# app = Flask(__name__, static_folder='../frontend', static_url_path='/')
# CORS(app)

# # ensure DB & tables exist
# init_db()

# @app.route("/")
# def root():
#     return app.send_static_file("index.html")

# @app.route("/categories", methods=["GET"])
# def categories():
#     return jsonify(CATEGORIES)

# @app.route("/signup", methods=["POST"])
# def signup():
#     data = request.json
#     name = data.get("name")
#     email = data.get("email")
#     password = data.get("password")
#     if not (name and email and password):
#         return jsonify({"error":"Name, email and password required"}), 400
#     hashed = generate_password_hash(password)
#     try:
#         conn = get_conn()
#         c = conn.cursor()
#         c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
#                   (name, email, hashed))
#         conn.commit()
#         user_id = c.lastrowid
#         conn.close()
#         return jsonify({"message":"Signup successful", "user_id": user_id})
#     except sqlite3.IntegrityError:
#         return jsonify({"error":"Email already exists"}), 400

# @app.route("/login", methods=["POST"])
# def login():
#     data = request.json
#     email = data.get("email")
#     password = data.get("password")
#     if not (email and password):
#         return jsonify({"error":"Email and password required"}), 400
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("SELECT id, password, name FROM users WHERE email = ?", (email,))
#     row = c.fetchone()
#     conn.close()
#     if row and check_password_hash(row["password"], password):
#         return jsonify({"message":"Login successful", "user_id": row["id"], "name": row["name"]})
#     return jsonify({"error":"Invalid credentials"}), 400

# @app.route("/add_expense", methods=["POST"])
# def add_expense():
#     data = request.json
#     user_id = data.get("user_id")
#     amount = data.get("amount")
#     description = data.get("description", "")
#     date = data.get("date")
#     category = data.get("category", None)
#     if not (user_id and amount is not None and date):
#         return jsonify({"error":"Missing fields"}), 400
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("INSERT INTO expenses (user_id, amount, description, date, category) VALUES (?, ?, ?, ?, ?)",
#               (user_id, amount, description, date, category))
#     conn.commit()
#     conn.close()
#     return jsonify({"message":"Expense added"})

# # DELETE expense (new)
# @app.route("/delete_expense/<int:expense_id>", methods=["DELETE"])
# def delete_expense(expense_id):
#     conn = get_conn()
#     c = conn.cursor()
#     c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
#     conn.commit()
#     conn.close()
#     return jsonify({"message":"Expense deleted"})

# # GET expenses, with optional filter via ?filter=month|year|6months|all (default all)
# @app.route("/get_expenses/<int:user_id>", methods=["GET"])
# def get_expenses(user_id):
#     filter_type = request.args.get("filter", None)  # e.g. "month", "year", "6months"
#     conn = get_conn()
#     c = conn.cursor()

#     query = "SELECT id, amount, description, date, category FROM expenses WHERE user_id = ?"
#     params = [user_id]

#     now = datetime.now()
#     if filter_type == "month":
#         start_date = now.replace(day=1).strftime("%Y-%m-%d")
#         query += " AND date >= ?"
#         params.append(start_date)
#     elif filter_type == "year":
#         start_date = now.replace(month=1, day=1).strftime("%Y-%m-%d")
#         query += " AND date >= ?"
#         params.append(start_date)
#     elif filter_type == "6months":
#         start_date = (now - timedelta(days=182)).strftime("%Y-%m-%d")
#         query += " AND date >= ?"
#         params.append(start_date)
#     elif filter_type == "2years":
#         start_date = (now - timedelta(days=730)).strftime("%Y-%m-%d")
#         query += " AND date >= ?"
#         params.append(start_date)
#     # else no filter (all)

#     c.execute(query + " ORDER BY date DESC", tuple(params))
#     rows = c.fetchall()
#     conn.close()
#     expenses = []
#     for r in rows:
#         expenses.append({
#             "id": r["id"],
#             "amount": float(r["amount"]),
#             "description": r["description"],
#             "date": r["date"],
#             "category": r["category"]
#         })
#     return jsonify(expenses)

# if __name__ == "__main__":
#     print("Starting Flask on http://127.0.0.1:5000")
#     app.run(debug=True)




























# app.py - fixed (keeps your original structure, minimal safe fixes)

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

# keep the original DB name but resolve to absolute path so DB always created next to this file
DB_PATH = "expenses.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if not os.path.isabs(DB_PATH):
    DB_PATH = os.path.join(BASE_DIR, DB_PATH)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()
    # Create users table
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )""")
    # Create expenses table
    c.execute("""CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL,
                    category TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )""")
    # optional index to speed up queries
    c.execute("CREATE INDEX IF NOT EXISTS idx_expenses_user_date ON expenses(user_id, date)")
    conn.commit()
    conn.close()

# Predefined categories for frontend sync (unchanged)
CATEGORIES = [
    {"id":1,"name":"Food","color":"#6366F1"},
    {"id":2,"name":"Transport","color":"#10B981"},
    {"id":3,"name":"Entertainment","color":"#F59E0B"},
    {"id":4,"name":"Shopping","color":"#EC4899"},
    {"id":5,"name":"Utilities","color":"#3B82F6"},
    {"id":6,"name":"Health","color":"#EF4444"},
    {"id":7,"name":"Other","color":"#64748B"}
]

# KEEP YOUR ORIGINAL static_folder path (you used ../frontend). Change only if your frontend folder sits elsewhere.
app = Flask(__name__, static_folder='frontend', static_url_path='/')
CORS(app)

# Initialize DB & tables
init_db()
print("Using DB at:", DB_PATH)

@app.route("/")
def root():
    try:
        return app.send_static_file("index.html")
    except Exception:
        return jsonify({"message":"Index not found. Put your index.html into the frontend folder and verify static_folder path."}), 200

@app.route("/categories", methods=["GET"])
def categories():
    return jsonify(CATEGORIES), 200

def parse_json_request():
    """
    Robust parsing: prefer JSON; if missing, fall back to form data.
    """
    data = request.get_json(silent=True)
    if data is None:
        if request.form:
            data = request.form.to_dict()
        else:
            data = {}
    return data

@app.route("/signup", methods=["POST"])
def signup():
    data = parse_json_request()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # If frontend didn't send name, derive from email so old frontend works unchanged
    if not name and email:
        name = email.split("@")[0]

    if not (name and email and password):
        return jsonify({"error":"Name, email and password required"}), 400

    hashed = generate_password_hash(password)

    try:
        conn = get_conn()
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed))
        conn.commit()
        user_id = c.lastrowid
        conn.close()
        print(f"[signup] created user {email} id={user_id}")
        return jsonify({"message":"Signup successful", "user_id": user_id}), 201
    except sqlite3.IntegrityError as e:
        print(f"[signup] IntegrityError: {e}")
        return jsonify({"error":"Email already exists"}), 409
    except Exception as e:
        print(f"[signup] Exception: {e}")
        return jsonify({"error":"Server error", "detail": str(e)}), 500

@app.route("/login", methods=["POST"])
def login():
    data = parse_json_request()
    email = data.get("email")
    password = data.get("password")

    if not (email and password):
        return jsonify({"error":"Email and password required"}), 400

    try:
        conn = get_conn()
        c = conn.cursor()
        c.execute("SELECT id, password, name FROM users WHERE email = ?", (email,))
        row = c.fetchone()
        conn.close()
    except Exception as e:
        print(f"[login] DB error: {e}")
        return jsonify({"error":"Server error", "detail": str(e)}), 500

    if row and check_password_hash(row["password"], password):
        print(f"[login] success for {email}")
        return jsonify({"message":"Login successful", "user_id": row["id"], "name": row["name"]}), 200

    print(f"[login] failed for {email}")
    return jsonify({"error":"Invalid credentials"}), 401

@app.route("/add_expense", methods=["POST"])
def add_expense():
    data = parse_json_request()
    user_id = data.get("user_id")
    amount = data.get("amount")
    description = data.get("description", "")
    date = data.get("date")
    category = data.get("category", None)

    if user_id is None or amount is None or not date:
        return jsonify({"error":"Missing fields"}), 400

    try:
        amount = float(amount)
    except Exception:
        return jsonify({"error":"Amount must be a number"}), 400

    # try to normalize date
    try:
        parsed = datetime.fromisoformat(date)
        date_str = parsed.date().isoformat()
    except Exception:
        date_str = date

    try:
        conn = get_conn()
        c = conn.cursor()
        c.execute("INSERT INTO expenses (user_id, amount, description, date, category) VALUES (?, ?, ?, ?, ?)",
                  (user_id, amount, description, date_str, category))
        conn.commit()
        conn.close()
        return jsonify({"message":"Expense added"}), 201
    except Exception as e:
        print(f"[add_expense] Exception: {e}")
        return jsonify({"error":"Server error", "detail": str(e)}), 500

@app.route("/delete_expense/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    try:
        conn = get_conn()
        c = conn.cursor()
        c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        deleted = c.rowcount
        conn.close()
        if deleted:
            return jsonify({"message":"Expense deleted"}), 200
        else:
            return jsonify({"error":"Expense not found"}), 404
    except Exception as e:
        print(f"[delete_expense] Exception: {e}")
        return jsonify({"error":"Server error", "detail": str(e)}), 500

@app.route("/get_expenses/<int:user_id>", methods=["GET"])
def get_expenses(user_id):
    filter_type = request.args.get("filter", None)
    try:
        conn = get_conn()
        c = conn.cursor()
        query = "SELECT id, amount, description, date, category FROM expenses WHERE user_id = ?"
        params = [user_id]
        now = datetime.now()
        if filter_type == "month":
            start_date = now.replace(day=1).strftime("%Y-%m-%d")
            query += " AND date >= ?"
            params.append(start_date)
        elif filter_type == "year":
            start_date = now.replace(month=1, day=1).strftime("%Y-%m-%d")
            query += " AND date >= ?"
            params.append(start_date)
        elif filter_type == "6months":
            start_date = (now - timedelta(days=182)).strftime("%Y-%m-%d")
            query += " AND date >= ?"
            params.append(start_date)
        elif filter_type == "2years":
            start_date = (now - timedelta(days=730)).strftime("%Y-%m-%d")
            query += " AND date >= ?"
            params.append(start_date)
        query += " ORDER BY date DESC"
        c.execute(query, tuple(params))
        rows = c.fetchall()
        conn.close()
        expenses = []
        for r in rows:
            expenses.append({
                "id": r["id"],
                "amount": float(r["amount"]),
                "description": r["description"],
                "date": r["date"],
                "category": r["category"]
            })
        return jsonify(expenses), 200
    except Exception as e:
        print(f"[get_expenses] Exception: {e}")
        return jsonify({"error":"Server error", "detail": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask server at http://127.0.0.1:5000")
    app.run(debug=True)
