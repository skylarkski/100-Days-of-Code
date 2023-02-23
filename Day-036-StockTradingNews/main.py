import requests
import os
from twilio.rest import Client
import datetime

#Using my system's enviroment variables stored  
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

pho_num = os.environ['PHO_NUM']

#Stock Symbol
stock_symbol = "TLSA"
#Stock API
stock_api = os.environ['ALPHAVANTAGE_API']
#Stock URL
stock_url = 'https://www.alphavantage.co/query'
#Stock Parameters
stock_params = {
    "apikey": stock_api,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA"
}

#News Topic
news_topic = 'Tesla'
#News API
news_api = os.environ['NEWS_API']
#News URL
news_url = 'https://newsapi.org/v2/top-headlines'
#News Parameters
news_params = {
    "apiKey": news_api,
    "q": news_topic,
    "country": "us",
    "category": "business",
    "pageSize": 3
}

#Getting previous weekday
def get_previous_day(my_date):
    my_date -= datetime.timedelta(days=1)
    while my_date.weekday() > 4:
        my_date -= datetime.timedelta(days=1)
    return my_date

#Getting Stock Delta by comparing yesterday's stock close value to stock close value from two days ago
def get_stock_delta():
    response = requests.get(stock_url, params=stock_params)
    response.raise_for_status()
    data = response.json()

    date_today = datetime.date.today()
    date_last_weekday = get_previous_day(date_today)
    date_weekday_two_days_ago = get_previous_day(get_previous_day(date_today))

    #close_today = data["Time Series (Daily)"][str(date_today)]['4. close']
    close_yesterday = float(data["Time Series (Daily)"][str(date_last_weekday)]['4. close'])
    close_two_days_ago = float(data["Time Series (Daily)"][str(date_weekday_two_days_ago)]['4. close'])

    delta = round((1 - (close_two_days_ago / close_yesterday)) * 100, 2)

    return delta


def get_news():
    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    data = response.json()
    articles = data['articles']

    delta = get_stock_delta()

    if delta < 0:
        delta_trend = "🔻"
    else:
        delta_trend = "🔺"

    text_body = "\n" + news_topic + f" {delta_trend} {delta}% \n" + "\n\n".join(["Headline: " + article['title'] + '\n' + "Brief: " + article['description'] + '\n' + article['url'] for article in articles])
    return text_body

def send_sms(text_body):

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text_body,
        from_="+18449133385",
        to=pho_num
    )

    print(message.status)

if abs(get_stock_delta()) > 5:
    text_body = get_news()

    send_sms(text_body)
else:
    print("Delta too small. No alerts sent.")


