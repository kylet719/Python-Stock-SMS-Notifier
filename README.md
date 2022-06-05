# SMS Stock Watch

A tool to send the 5 highest gainers and the 5 highest falling stocks of the day, once at market open and another at market close. The stocks were pulling from the Yahoo Finance main page but additional info about the company is provided from the Yahoo Finance! API including sector, dividend rates, buy recommendations, etc.

## Installation
You'll need to install the Twilio, yFinance, and pandas packages. 

- `pip install twilio`
- `pip install yfinance`
- `pip install pandas`

After, create a free Twilio account to get your accountSID, authentication Token, and twilio temporary phone number. Cd into id.py and fill all releveant fields and you're all set. Run and get notified the 5 highest gainers and the 5 highest falling stocks of the day!
