import flask
import pandas as pd
from datetime import datetime

app = flask.Flask(__name__)

df = pd.DataFrame(columns=["Time", "Humidity", "Temperature"])

@app.post("/")
def main_post():
    global df
    try: 
        df = df.append({"Time": datetime.now(),
                        "Humidity": flask.request.form["Humidity"],
                        "Temperature": flask.request.form["Temperature"]}, 
                   ignore_index=True)
        print(df)
    except Exception as e: 
        print(e)
    return main_get()

@app.get("/")
def main_get():
    return flask.render_template("main.html", data=df.to_html())