# Stock Market News Alert
Using the API from:
- https://www.alphavantage.co/ - My source of Stock API data
- https://newsapi.org/ - My source of News data

When ran, the program checks for the delta of stock value, comparing yesterday's price to the price two days ago.

I then pool top 3 most popular news articles pertaining to the stock I have chosen (in this case it is Tesla stock).

The Twilio phone number I aquired in a free trial allows for SMS sending via the twilio python package.

I am hosting the main.py on https://www.pythonanywhere.com/, which runs daily at 8am local to me, letting me know whether there was a large stock value change yesterday.