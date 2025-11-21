from flask import Flask,flash,redirect,url_for, render_template
from forms import RegistrationForm

app=Flask(__name__)

app.secret_key = "my_secret_key"

@app.route("/", methods=["POST", "GET"])
def register():
    form=RegistrationForm() #object

    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"Thankyou, {name}! for Registring")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run()
