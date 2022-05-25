# SMS Stock Watch

A tool to send the 5 highest gainers and the 5 highest falling stocks of the day, once at market open and another at market close. The stocks were pulling from the Yahoo Finance main page but additional info about the company is provided from the Yahoo Finance! API including sector, dividend rates, buy recommendations, etc.

## Installation
You'll need to install the Twilio, yFinance, and pandas packages. After, go to lines 47 and 48 and change the respective Market Open and Market Close times to your local 24:00 time. Run and get notified the 5 highest gainers and the 5 highest falling stocks of the day!
