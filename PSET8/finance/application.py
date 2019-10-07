import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # look up the current user
    stocks = db.execute("SELECT symbol, shares, price FROM History WHERE id = :id", id=session['user_id'])

    result = db.execute("SELECT cash FROM users WHERE id = :id", id=session['user_id'])

    totalCash = float(result[0]['cash'])

    grandTotal = totalCash

    totalValueShare = 0
    # Pull from database and send to table
    for stock in stocks:
        symbol = str(stock["symbol"])
        shares = int(stock["shares"])
        price = float(stock["price"])
        totalValueShare = shares * price
        grandTotal += totalValueShare

    return render_template("index.html", stocks=stocks, cash=totalCash, totalValueShare=totalValueShare, grandTotal=grandTotal)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":
        symbol = request.form.get("symbol")
        # Error handling when forms are not filled correctly
        try:
            shares = int(request.form.get("shares"))
        except ValueError:
            return apology("you can only supply an integer", 400)

        if not symbol:
            return apology("must provide symbol", 400)

        quote = lookup(symbol)

        if not quote:
            return apology("Enter a valid symbol plix", 400)

        if not shares:
            return apology("must provide shares", 400)

        if shares < 1:
            return apology("shares should be a positive integer", 400)
        # Check user's money to see if purchase is affordable
        price = shares * quote["price"]
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        cash = rows[0]['cash']

        if cash < price:
            return apology("Sorry ... You can't afford this", 400)

        balance = cash - price
        symbol = quote['symbol']
        # update databases to reflect BUY
        db.execute("INSERT INTO History (id, symbol, shares, price, date, histSymbol, histShares) VALUES (:user, :symbol, :shares, :price, :date, :histSymbol, :histShares)",
                   user=session["user_id"], symbol=symbol, shares=shares, price=quote["price"], date=datetime.now(), histSymbol=symbol, histShares=shares)

        db.execute("UPDATE users SET cash=:balance WHERE id=:id", balance=balance, id=session["user_id"])

        grandTotal = shares + cash

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""

    username = request.args["username"]

    if len(username) == 0:
        return jsonify(False)

    rows = db.execute("SELECT * FROM users WHERE username = :username",
                      username=username)
    if rows:
        return jsonify(False)

    return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # look up the current user
    stocks = db.execute("SELECT symbol, shares, price, date FROM History WHERE id = :id", id=session['user_id'])

    for stock in stocks:
        symbol = str(stock["symbol"])
        shares = int(stock["shares"])
        price = float(stock["price"])
        date = stock["date"]

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Cover errors
        if not request.form.get("symbol"):
            return apology("must enter symbol", 400)

        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Stock not found or invalid", 400)
        # Send user to next page if successful
        return render_template("quoted.html", stock=stock)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Read user's form input
    if request.method == "POST":
        # Errors covered for all fields
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must re-enter password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        rows = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get(
            "username"), hash=generate_password_hash(request.form.get("password")))
        if not rows:
            return apology("Username already exists")

        # Turns newly-inputted account into the current session
        session["user_id"] = rows

        # Redirect user to login form
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        # Form errors
        if not symbol:
            return apology("No stock entered", 400)

        quote = lookup(symbol)

        if not quote:
            return apology("Invalid company", 400)

        if not shares:
            return apology("No shares entered", 400)

        if shares <= 0:
            return apology("Please enter a positive number", 400)

        symbol = quote['symbol']
        rows = db.execute("SELECT SUM(shares) FROM History WHERE id = :id AND symbol = :symbol",
                          id=session["user_id"], symbol=symbol)

        stock = rows[0]['SUM(shares)']
        if not stock:
            return apology("No stocks found for this company", 400)

        if stock < shares:
            return apology("Not enough shares! Buy more!", 400)

        price = shares * quote['price']
        shares = - shares
        # Update tables after SELL
        db.execute("INSERT INTO History (id, symbol, shares, price, date, histSymbol, histShares) VALUES (:user, :symbol, :shares, :price, :date, :histSymbol, :histShares)",
                   user=session["user_id"], symbol=symbol, shares=shares, price=quote["price"], date=datetime.now(), histSymbol=symbol, histShares=shares)

        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        cash = rows[0]['cash']
        balance = cash + price
        db.execute("UPDATE users SET cash=:balance WHERE id=:id", balance=balance, id=session["user_id"])

        # Redirect user to home page
        return redirect("/")
    else:
        # Render table if no SELL
        rows = db.execute("SELECT symbol FROM History WHERE id=:id", id=session["user_id"])
        symbols = []

        for row in rows:
            symbols.append(row['symbol'])

        symbols = list(set(symbols))
        data = []

        for symbol in symbols:
            rows = db.execute("SELECT symbol, SUM(shares) FROM History WHERE id=:id AND symbol=:symbol",
                              id=session["user_id"], symbol=symbol)
            if rows[0]['SUM(shares)'] > 0:
                data.append(rows[0]['symbol'])

        return render_template("sell.html", data=data)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
