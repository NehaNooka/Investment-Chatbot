# Application of Chatbot to Investment Advising with DialogFlow
## Author: Jhancy Amarsingh, Jin Hui Xu, Shikha C. Patel
### DATA 690 - NLP Project

## Presentation
  - Presentation Slides
    - <a href="https://github.com/JinHuiXu1991/DATA690NLP_Project_InvestmentChatbot/blob/b6e91197ac825288689e431bd0df793938431bf3/presentation/NLP%20investment%20chatbot%20presetation.pptx">PPT</a>
    - <a href="https://github.com/JinHuiXu1991/DATA690NLP_Project_InvestmentChatbot/blob/b6e91197ac825288689e431bd0df793938431bf3/presentation/NLP%20investment%20chatbot%20presetation.pdf">PDF</a>
  - Video presentation 
    - <a href="https://www.youtube.com/watch?v=vCKJ0jrXTGo">Youtube Presentation Link</a>


## Paper
  - <a href="https://github.com/JinHuiXu1991/DATA690NLP_Project_InvestmentChatbot/blob/a44047e77e8a1410bf41c19e7fe744d874e6fdf7/paper/Investment_chatbot_paper.docx">Word</a>
  - <a href="https://github.com/JinHuiXu1991/DATA690NLP_Project_InvestmentChatbot/blob/a44047e77e8a1410bf41c19e7fe744d874e6fdf7/paper/Investment_chatbot_paper.pdf">PDF</a>
    
## Table of Contents
- Introduction
- Why are Chatbots a More Significant Presence in Today’s Financial Environment?
- Features
  - Investment Education
  - Information Retrieval
  - Stock Price Forecasting
  - Stock Recommendation
- Methodology
  - Chatbot Development 
  - Chatbot Fulfillment and Webhook
  - Text Summarization
  - Stock Price Forecasting
  - Stock Recommendation
- Results
- Limitations
- Future Scope
- References

## Introduction
A chatbot is a communication software application that can store appropriate answers to questions on a server, create models that continuously develop correct answers through conversations with customers, control exceptions, and provide accurate answers (Hwang, S.; Kim, J., 2021). Chatbot, an interactive AI (where the user influences the system and the system influences the user), has been widely deployed in finance, retail, public, and manufacturing industries. Appleʹs Siri, Amazonʹs Alexa, Googleʹs OKgoogle, and Samsung Electronicsʹ Bixby are good examples of voice conversion personal assistant services (Karnam, M.,2019). A Chatbot for investing purposes is an interface that communicates with financial services to give information and advice to users. Chatbots are dominating the financial industry as a method of customer interaction. Established financial organizations are experimenting with chatbots, mainly in the retail banking, investment management, and wealth management sectors. Financial institutions have embraced this trend and experts predict that, within five years, bots will replace conventional online interfaces such as websites or mobile apps (Dasagrandhi, C. S., 2022). 

Investment Chatbot creates a dedicated relationship serving the investors with their investment management. The chatbot will crunch the numbers and do all the heavy lifting so that investors can focus their efforts on their investment (Botbot.AI, 2018). This service for the investor’s investments is tailored to the needs at any time of the day without worrying more about opening hours or having to consult investment personnel and enduring long waiting times.

## Why are Chatbots a More Significant Presence in Today’s Financial Environment?

Users sometimes have to invest a lot of time on the Internet to find relevant information regarding the investments in mutual funds, bonds, cryptocurrency, stocks, and portfolio management. To alleviate these problems, our Investment Chatbot is an innovative idea built on Dialogflow to provide personalized assistance in discovering important information about any type of investment, as well as help invest, forecast stock prices, and recommend the best investment strategies based on current market stock prices. It can be challenging for investors to maintain track of every stock, especially the ones they just want to monitor. There are potential chances that sometimes investors could miss out on a buy or a sell. So, it is important to build an Investment Chatbot to ensure proper management of their investment portfolio. Eventually, any investor can take advantage of such a multifunctional investment system to grow their wealth.

## Features
The objective of this project is to develop an Investment Chatbot that can assist users to learn how to invest wisely and provide a convenient approach to gather the necessary information and make proper financial investment decisions. The chatbot is task-oriented, which focuses on the pre-defined investment tasks and responds to very specific investment commands. The Investment Chatbot consists of four main components:

* Investment Education
  
  One of the most essential features of the investment chatbot is to provide definitions and tutorials for different investment options to users since not everyone has the financial knowledge and experience to make investment decisions. This chatbot can help users to learn different types of investment and provide them with plenty of additional resources for further learning. Whether it is mutual funds, bonds, stocks, or cryptocurrency, the Investment Chatbot can provide all aspects of information to assist users to make the right financial moves and planning for the future.

* Information Retrieval

  The investment chatbot provides information retrieval services such as suggestions for investment tools and real-time stock price querying. Even though the users have never invested a dollar or are already experienced investors, they can take advantage of the information retrieval feature. First-time investors can retrieve information on useful investment tools and start their journey. On the other hand, the stock price checking feature provides traders and active investors with more accurate information reflecting the market such as High Price, Low Price, Open Price, and Close Price of the stocks. The chatbot will display all the necessary information to support their financial decisions in real-time.

* Stock Price Forecasting
  
  The investment chatbot also provides stock price prediction services for S&P500 stocks. Forecasting the stock market's opening moves can be a useful tool. Investors can query about the particular stock they are interested in and get the forecast value for the next five days before making their decision to buy or sell, especially for the swing traders. 


* Stock Recommendation

  On any particular day, when the users want a recommendation for any S&P500 stocks, the chatbot shortlists the stocks to trade based on technical indicators such as ‘Based on Relative Strength Index (RSI)’ and ‘Based on Volume.’ Technical indicators are tools that help analyze the movement in the stock prices and whether the ongoing trend is either going to continue or reverse. It helps the traders make buy or sell a particular stock of interest. 
  
## Methodology
The investment chatbot leverages machine learning and NLP algorithms to meet the expected features mentioned above. The development process consists of five steps:

* Chatbot Development

  The foundation of the system is to build a chatbot agent that can understand natural human language and provide the requested information. Instead of building our own agent from scratch, we decided to utilize Dialogflow, an existing chatbot development platform powered by Google, to build the conversational agent for the system. Similar to building the chatbot by using NLP tools, Dialogflow offers a friendly user interface to define the key components of a Chatbot such as Agent, Intents, Entities, and Fulfillment (D3Vtech, 2021). Besides, it utilizes Google's machine learning models and NLP to train the agent once we predefined the mentioned components. 

  The following NLP techniques are used by Dialogflow to enable the chatbot to process human conversations:
  1.	POS Tagging - to identify entities in the user input sentence.
  2.	Tokenization - to split the text into meaningful words.
  3.	Stemming - to reduce inflected words to their base form.
  4.	Stop Words - to filter out high-frequency words from the user input sentence.
  5.	Term Reinforcement - to give higher weight to certain phrases in a sentence.
  
  For chatbot deployment, because Dialogflow is fully integrated with ‘Google Assistant,’ we decided to take advantage of the voice chat functionality and deploy the investment chatbot to ‘Google Assistant.’ Thus, the chatbot can handle either text-based or voice-based communication.

* Chatbot Fulfillment and Webhook

  The regular chatbot can handle the general rule-based conversion. However, for our project, it cannot answer questions related to real-time stock queries and stock price prediction. For these scenarios, chatbot fulfillment and webhook need to be built. Fulfillment is a key component of a chatbot that allows an agent to take actions based on the user’s expression and send dynamic responses. In our case, we want the chatbot to send dynamic responses regarding stock prices, stock predictions, and recommendations.
  Since Dialogflow supports the fulfillment feature, a webhook application is developed by using Python with Flask Framework. Besides, we set up a cloud environment in ‘Pythonanywhere,’ a web hosting service, and host the webhook application there. Thus, if users request sophisticated responses like real-time stock price and machine learning model results, the chatbot can send a request with user input entities to our webhook, then the webhook will perform necessary actions and send back the result.

* Text Summarization

  In order to train our chatbot to respond and provide the requested knowledge for investment, web scraping and text summarization techniques are applied for developing this chatbot. Web scraping can collect the required content of different investment options from authoritative investment websites. Then, to provide concise investment educational content for the users, the text summarization model can extract the essential information from the scraped content.
  In our project, we have carried out web scraping using BeautifulSoup, text cleaning, and text summarization using Gensim summarization. Gensim summarization works with the TextRank algorithm. This algorithm utilizes the extractive text summarization technique to examine the original text and extract the highest-ranked sentence based on the sentence similarity. Thus, it best conveys the ideas contained in the text without losing too much meaning. If users want to learn more beyond the summary, they can access the original content by redirecting to the external website link provided on the chatbot interface.

* Stock Price Forecasting

  It is important to make the data stationary before we can us the Autoregressive Integrated Moving Average (ARIMA) model. The ARIMA model has been widely utilized in banking and economics since it is recognized to be reliable, efficient, and capable of predicting short-term share market movements (Dhaduk, H., 2021). In our Investment Chatbot, we use the historical data of S&P500 stocks collected from ‘Yahoo Finance API’ to forecast the stock prices. The ARIMA model is trained for S&P500 ‘Close Price’ data for the duration of 2 years. The model forecasts the Close Prices of the stock for the next 5 days and returns the result to the user in the form of a table. 

* Stock Recommendation

  The Stock Recommendation feature is designed so that the investor can make an informed decision after getting the recommended stocks and their close price/volume (based on a selected indicator). It shows the present movement of stocks in the stock market. In our Investment Chatbot, we used the historical data of S&P500 stocks collected from ‘Yahoo Finance API’ to recommend the stocks based on technical indicators RSI and Volume. RSI is a Relative Strength Indicator essentially used as a momentum indicator.  It measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock (Fernando, 2022). The RSI is displayed as an oscillator and can have a magnitude of momentum from 0 to 100. Trading volume is a measure of how much a given financial asset has traded in a period of time (Mitchell, C., 2022). For stocks, volume is measured in the number of shares traded. 
  In our Investment Chatbot, we recommend stocks with RSI less than 30 (Oversold stocks) and the stocks with a higher average volume over the last 2 years in the sampled data.
 
## Results

  The Investment chatbot is a novel platform for users who have little experience or knowledge about investment and the stock market. It is a platform that enables the education of investors about different types of investments through the ‘Learn about investment’ feature. The retrieved information on the types of investment options is summarized by leveraging the ‘Text Summarization’ technique of Natural Language Processing. After educating the user on various investment types, the ‘Invest’ feature provides options for top investment websites where users can log in and start investing. In order to invest, the user can check the ‘Low Price,’ ‘High Price,’ ‘Open Price’, and ‘Close Price’ of the specific stock of their interest under the ‘Check the prices of stocks’ feature. Additionally, the platform has a very significant feature of ‘Forecasting the stock prices’ of a particular stock for the next five days. As recommendation is an important tool that any investor can need in their investment, this platform also provides ‘Recommendation of stocks’ based on the factors like ‘Relative Strength Index (RSI)’ and ‘Volume’. Presently, this chatbot has predefined buttons for the users to select for maintaining the flow of the conversation. Once users are familiar with the conversational flow, they can type the predefined queries without using the buttons, and the chatbot returns the corresponding information to the user.  

## Limitations

  This Investment Chatbot can be helpful for investors, portfolio management companies, entrepreneurs, and other stock market stakeholder who looks forward to benefiting and earning money in this competitive stock market era. However, this Investment Chatbot is only implemented on ‘Google Assistant’, it does not allow to present graphs or charts for better visualization of the forecasted stock prices. Another shortcoming of deploying with Google Assistant is that it does not allow the developers to provide an alternate/attractive UI to our chatbot, but it can be implemented by using another platform in a revised version of this chatbot. 

## Future Scope

  This chatbot can also be deployed on other platforms and applications with more enhanced features to be compatible with other languages than English. This integration of compatibility with other languages will give a broader scope and can be useful to the wider public of the world speaking other languages than English. This Chatbot can also leverage more features to help invest in the mutual funds, bonds and crypto-by-crypto price predictions and recommendations. We can also leverage more on stock prediction and recommendation based on Fundamental Metrics like EPS, Price-to-Earnings Ratio, Price-to-Book Ratio and Return on Equity (ROE) and Technical Indicators like Money Flow Index (MFI), Simple Moving Average (SMA), and Bollinger Bands. We can leverage the latest Neural Network models to forecast stock prices.  It can have more conversations and give insightful responses to the investor/user about the risk percentage, return percentage, and the duration of the investment before recommending the stocks. This chatbot can be connected with Trading APIs to help place the trading orders after the conversation. 

## References

Dasagrandhi, C. S., 2022). 22 reasons why investing in Chatbots is no longer an option. Blog. Retrieved May 1, 2022, from https://blog.vsoftconsulting.com/blog/22-reasons-why-investing-in-chatbots-is-no-longer-an-option 

Karnam, M. (2019, September 24). How to build an investment management chatbot. IBM. https://www.ibm.com/cloud/blog/announcements/build-investment-management-chatbot

Hwang, Sewoong & Kim, Jonghyuk. (2021). Toward a Chatbot for Financial Sustainability. Sustainability. 13. 3173. 10.3390/su13063173.

D3VTech. (2021, August 2). The AI Behind Google Dialogflow - How it Differs from Other Conversational AI | Cloud Insights | D3V Technology Solutions. https://www.d3vtech.com/insights/the-ai-behind-google-dialogflow-how-it-differs-from-other-conversational-ai

Mitchell, C. (2022, February 10). How to Use Volume to Improve Your Trading. Investopedia. https://www.investopedia.com/articles/technical/02/010702.asp

Hwang, S.; Kim, J. Toward a Chatbot for Financial Sustainability. Sustainability 2021, 13, 3173. https://doi.org/10.3390/su13063173

Botbot.AI. (2018, February 2). Banking & Investment - Chatbot for Enterprise Productivity. Botbot.AI. https://botbot.ai/solutions/banking-investment-chatbot/

Dhaduk, H. (2021, July 18). Stock market forecasting using Time Series analysis With ARIMA model. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/07/stock-market-forecasting-using-time-series-analysis-with-arima-model/

Fernando, J. (2022, February 19). Relative Strength Index (RSI). Investopedia. 

Finra. (n.d.). Learn to Invest | FINRA.org. https://www.finra.org/investors/learn-to-invest

