<div align="center">
  <h1>✨ AI Smart Expense Tracker</h1>
  <p>A beautiful, modern, and intelligent expense tracking application with automated AI categorization and rich data visualization.</p>
</div>

<br/>

## 🌟 Features

- **🧠 Smart AI Categorization**: Simply type your expense description, and our algorithm auto-categorizes it (e.g., "Starbucks Coffee" -> *Food*, "Uber to Airport" -> *Transport*).
- **📱 Fully Responsive Design**: Beautiful "glassmorphism" UI built with Tailwind CSS that works seamlessly across desktop, tablet, and mobile devices.
- **📊 Rich Data Visualization**: Interactive doughnut charts and top spending analytics powered by Chart.js.
- **🔐 User Authentication**: Secure login and signup functionality using hashed passwords.
- **💾 Database Viewer**: Built-in raw SQL database viewer directly from the frontend interface for transparency.
- **🚀 Cloud-Ready**: Pre-configured for seamless serverless deployment on Vercel (`vercel.json` included).

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS, Google Fonts (Outfit).
- **Backend / API**: Python 3, Flask, Flask-CORS, Werkzeug Security.
- **Database**: SQLite3 (Local / Dev) *(Note: For true serverless production on Vercel, consider migrating to Supabase or Neon Postgres as SQLite will reset on ephemeral instances)*.
- **Libraries**: Chart.js for data visualization.

---

## � Local Development Setup

Follow these simple steps to run the project on your local machine:

1. **Clone the repository**
   ```bash
   git clone https://github.com/dhangarbhushan026/MyProject.git
   cd MyProject
   ```

2. **Install Python Dependencies**
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask Server**
   ```bash
   python app.py
   ```

4. **Open in Browser**
   Visit `http://127.0.0.1:5000/` in your favorite web browser.

---

## 🚀 Deployment (Vercel)

This project is pre-configured to be deployed natively on Vercel using Serverless Functions.

1. Install the Vercel CLI (`npm i -g vercel`) or connect your GitHub repository to your Vercel Dashboard.
2. Run `vercel` in the root directory.
3. Vercel will automatically detect the `vercel.json` and deploy your `app.py` as a Python Serverless Function, while serving the `frontend` folder statically.

> **⚠️ Important Production Note**: Vercel Serverless Functions have a read-only filesystem (except for `/tmp`). Because this project uses a local `.db` file (SQLite), the database will reset to zero every time the serverless function cold-starts. For a permanent production app, please change the SQLite connection in `app.py` to a remote SQL database URL (like Supabase, Render, or Railway PostgreSQL).

---

## 👨‍💻 Author

Developed by **Bhushan Dhangar**
- 📧 Email: bhushan.dhangar026@gmail.com
- ⭐ Don’t forget to star this repository if you find it helpful!

---

<div align="center">
  <p>Thank you for checking out this project! Your support motivates me to build more amazing applications. 🚀</p>
</div>
