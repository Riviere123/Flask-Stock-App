To use this flask app you need an "https://marketstack.com/" API Key. They offer a free key.
You need to either set a couple environmental variables as defined in config.py(Your API key and your Cookies encryption key) or you can change the variables within config.py directly.

This project is the result of the following requirements.

## Goal ##
The goal for this project is to create a simple single-page web application
that allows a user to input a New York Stock Exchange stock symbol and receive
a listing of the current stock price for that stock.
## Requirements ##
* Written in Python
* Must use `flask` as a micro-framework
* Program must be able to run in development mode via `flask run`
* Project must utilize a virtual Python environment via `venv`
* Project files must include a `requirements.txt` file defining the python
  modules used by the application
* When started, the application must present a form for user input
 * The form should accept a string value as input and include a button to
 process the form.
 * If the value is a valid stock symbol
    * The application should retrieve stock symbol data from a
    third-party service (specified below) and display the following
    values on the web page.
    * Date (as returned by the service)
    * Symbol
    * Trade Volume
    * High price
    * Low price
    * Opening price
    * Closing price
    * Current price
  * If the value is NOT a valid stock symbol, an appropriate error message
  should be displayed to the user and the form reset.
