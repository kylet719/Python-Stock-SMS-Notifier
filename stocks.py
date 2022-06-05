from twilio.rest import Client
import yfinance as yf
import pandas as pd
import time
import timeit
import threading
import schedule
from datetime import date
import id


accountSID = id.accountSID
authToken = id.authToken
twilioPhoneNo = id.twilioPhoneNo
phoneNo = id.phoneNo

# Now just run and you're all set!

client = Client(accountSID, authToken)
def market_check(market_time, trend):
    output = market_time + " "+ str(date.today()) + "\n"
    stocklist = pd.read_html('https://finance.yahoo.com/'+ trend +'/')[0].head()
    x = 0
    output += "====BIG "+trend.upper()+"====\n" 
    while x < 5:
        output += "Name:" + " " + str(stocklist["Name"][x]) + "\n"
        output += "Ticker:" + " " + str(stocklist['Symbol'][x]) + " " + str(stocklist["% Change"][x]) + "\n"
        output += "Intraday Price:" + " " + str(stocklist['Price (Intraday)'][x]) + "\n"
        output += "Volume Change:" + " " + str(stocklist['Avg Vol (3 month)'][x]) + " to " +  str(stocklist['Volume'][x]) + "\n"
        test = yf.Ticker(stocklist['Symbol'][x])
        testingdict  = test.info
        output += "Sector:" + " " + testingdict["sector"] + "\n"
        output += "Country:" + " " + testingdict["country"] + "\n"
        output += "Website:" + " " + testingdict["website"] + "\n"
        output += "Market Cap:" + " " + str(stocklist["Market Cap"][x]) + "\n"
        output += "Recommendation:" + " " + str(testingdict["recommendationKey"]) + "\n"
        output += "\n"
        x += 1
    client.messages.create(to= phoneNo, from_= twilioPhoneNo, body = output)

def start_threading(var):
    print("Starting")
    t1 = threading.Thread(target=market_check, args=(var,"gainers"))
    t2 = threading.Thread(target=market_check, args=(var,"losers"))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    start = timeit.default_timer()
    schedule.every().day.at(id.marketOpen).do(lambda: start_threading("Market Open"))
    schedule.every().day.at(id.marketClose).do(lambda: start_threading("Market Close"))
    while True:
        print("In Loop")
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
    stop = timeit.default_timer()
    print('Time: ', stop - start)   












