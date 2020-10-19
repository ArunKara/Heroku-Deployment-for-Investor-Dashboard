from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
from config import cxnstring
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask_sqlalchemy import sqlalchemy
import json
import leaflet

app = Flask(__name__)

engine = create_engine(cxnstring, pool_recycle=3600)
con=engine.connect()

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/maps.html')
def map_func():
	return render_template('maps.html')

@app.route("/investors2")
def investors2():
    investors2 = pd.read_sql("SELECT * FROM investors2", con=engine)
    investors2_dict=investors2.to_dict(orient = "records")
    return jsonify(investors2_dict)

@app.route("/angel")
def angel():
    angel = pd.read_sql("SELECT * FROM api1 WHERE type = 'angel'", con=engine)
    angel_dict=angel.to_dict(orient = "records")
    return jsonify(angel_dict)

@app.route("/strategic")
def strategic():
    strategic = pd.read_sql("SELECT * FROM api1 WHERE type = 'strategic'", con=engine)
    strategic_dict=strategic.to_dict(orient = "records")
    return jsonify(strategic_dict)

@app.route("/venture_capital")
def venture_capital():
    venture_capital = pd.read_sql("SELECT * FROM api1 WHERE type = 'vc'", con=engine)
    venture_capital_dict=venture_capital.to_dict(orient = "records")
    return jsonify(venture_capital_dict)

@app.route("/private_equity")
def private_equity():
    private_equity = pd.read_sql("SELECT * FROM api1 WHERE type = 'pe'", con=engine)
    private_equity_dict=private_equity.to_dict(orient = "records")
    return jsonify(private_equity_dict)

@app.route("/other")
def other():
    other = pd.read_sql("SELECT * FROM api1 WHERE type = 'accelerator'", con=engine)
    other_dict=other.to_dict(orient = "records")
    return jsonify(other_dict)

#learn how to get integers greater than zero
@app.route("/portfolio_size")
def portfolio_size():
    portfolio_size = pd.read_sql("SELCT * FROM api1 WHERE portfolio_size > 0", con=engine)
    portfolio_size_dict = portfolio_size.to_dict(orient="records")
    return jsonify(portfolio_size_dict)

@app.route("/api1")
def api1():
    response9 = pd.read_sql("SELECT * FROM api1", con=engine)
    response9_dict = response9.to_dict(orient = "records")
    return jsonify(response9_dict)

@app.route("/billionaires")
def billionaires():
    response8 = pd.read_sql("SELECT * FROM billionaires", con=engine)
    response8_dict = response8.to_dict(orient = "records")
    return jsonify(response8_dict)

@app.route("/forbes")
def forbes():
    response7 = pd.read_sql("SELECT * FROM Forbes_Billionaires", con=engine)
    response7_dict = response7.to_dict(orient = "records")
    return jsonify(response7_dict)

@app.route("/sharktank")
def sharktank():
    response5 = pd.read_sql("SELECT * FROM sharktank", con=engine)
    response5_dict = response5.to_dict(orient = "records")
    return jsonify(response5_dict)

@app.route("/the worlds billionaires")
def The_Worlds_Billionaires():
    response4 = pd.read_sql("SELECT * FROM investors_copy", con=engine)
    response4_dict = response4.to_dict(orient = "records")
    return jsonify(response4_dict)

@app.route("/investors_copy2")
def investorscopy2():
    investorscopy2 = pd.read_sql("SELECT * FROM investors_copy2", con=engine)
    investorscopy_dict2 = investorscopy2.to_dict(orient = "records")
    return jsonify(investorscopy_dict2)

if __name__ == "__main__":
    app.run()