from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Kullanıcı verilerini depolamak için basit bir sözlük kullanalım
users = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Kullanıcı kaydı işlemini gerçekleştir
        username = request.form["username"]
        password = request.form["password"]
        demographic_info = {
            "age": request.form["age"],
            "gender": request.form["gender"],
            "academic_interests": request.form.getlist("academic_interests")
        }
        users[username] = {"password": password, "demographic_info": demographic_info}
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Kullanıcı girişi işlemini gerçekleştir
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
             return redirect("/recommendations")
        else:
            return "Kullanıcı adı veya şifre yanlış!"
    return render_template("login.html")

@app.route("/recommendations")
def recommendations():
    # Kullanıcıya öneriler göstermek için kullanılacak verileri hazırlayın
    # Örneğin, makale önerileri burada olabilir
    # Örnek olarak bir liste oluşturalım:
    recommended_articles = ["Makale 1", "Makale 2", "Makale 3"]

    # HTML şablonunu render ederek öneri sayfasını göster
    return render_template("recommendations.html", recommended_articles=recommended_articles)



if __name__ == "__main__":
    app.run(debug=True)
