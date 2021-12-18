from flask import Flask, request, render_template, redirect, url_for
from ProcessData import Data

app = Flask(__name__)

# Key
app.secret_key = "adbfnkg"


@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home() -> None:

    draw = False
    if request.method == "POST":
        if request.form:
            if request.form["res"] == "ok":
                draw = True

    return render_template("home.html", the_title="Home", draw=draw, yes=True)



# Just give the client the chance to review the data again

@app.route("/approve", methods=["POST", "GET"])
def approve():

    
    if request.method == "POST":
        
        # Create an instance of Data and than check if the data given by the client is right
        data = Data()

        res = data.isCorrect(request.form["book"], request.form["cd"], request.form["date"], 
        request.form["name"], request.form["lastname"], request.form["country"], request.form["city"], 
        request.form["street"], request.form["zip"], request.form["phone"], )

        
        # If everything was right than get the tuple from the data's object
        if res:
            
            content = ("Number of books:", "CD extra:", "Arrive date:", "Name:", "Last name:",
            "Country:", "City:", "Street:", "Zip:", "Phone:", )

            return render_template('approve.html', the_title="Approve", d_data=data.getTuple(), content=content)
            


    return redirect(url_for("home"))





# Run the app
if __name__ == "__main__":
    app.run(debug=True)
