
from flask import Flask, render_template, request

app = Flask(__name__)

def ai_tahmin_ev_skor(xg_ev):
    if xg_ev > 1.6:
        return "EV SAHİBİ ÜST (2.5)"
    elif xg_ev < 0.8:
        return "EV SAHİBİ ALT (2.5)"
    else:
        return "KARARSIZ"

def ai_tahmin_deplasman_skor(xg_dep):
    if xg_dep > 1.6:
        return "DEPLASMAN ÜST (2.5)"
    elif xg_dep < 0.8:
        return "DEPLASMAN ALT (2.5)"
    else:
        return "KARARSIZ"

@app.route("/", methods=["GET", "POST"])
def index():
    tahmin_ev = None
    tahmin_dep = None

    if request.method == "POST":
        try:
            xg_ev = float(request.form["xg_ev"])
            xg_dep = float(request.form["xg_dep"])
            tahmin_ev = ai_tahmin_ev_skor(xg_ev)
            tahmin_dep = ai_tahmin_deplasman_skor(xg_dep)
        except:
            tahmin_ev = "Hatalı giriş"
            tahmin_dep = "Hatalı giriş"

    return render_template("index.html", tahmin_ev=tahmin_ev, tahmin_dep=tahmin_dep)

if __name__ == "__main__":
    app.run(debug=True)
