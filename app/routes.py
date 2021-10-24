from flask import render_template, redirect, url_for
from app import app, stockapi
from app.forms import SymbolForm


@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    form = SymbolForm()
    if form.validate_on_submit():
        return redirect(url_for("result", symbol=form.symbol.data))
    return render_template('index.html', form=form)

@app.route("/stock/<symbol>", methods=['GET', 'POST'])
def result(symbol):
    form = SymbolForm()
    data = stockapi.GetStockData(symbol)
    
    if form.validate_on_submit():
        return redirect(url_for("result", symbol=form.symbol.data))
    
    if data == None:
        error = "Invalid Stock Symbol"
        return render_template('index.html', form=form, error=error)
        
    else:
        return render_template('index.html', form=form, data=data)
        
