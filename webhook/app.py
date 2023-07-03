# /index.py
from __future__ import print_function
from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
import json
import random
import pandas as pd

from flask import Flask
from flask import request
from flask import make_response
import yfinance as yf
import datetime
from datetime import datetime as dt
import requests

app = Flask(__name__)

os.environ["DIALOGFLOW_PROJECT_ID"]="investmentassistant-setk"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/nlpproject690webhook/mysite/investmentassistant-setk-53554122c639.json"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult')
    if query_result.get('action') == 'query':
        res = processRequest(req)
    elif query_result.get('action') == 'recommendRSI':
        res = recommendRSI(req)
    elif query_result.get('action') == 'recommendVolume':
        res = recommendVolume(req)
    elif query_result.get('action') == 'forecast':
        res = forecast(req)

    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



def forecast(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    stockname = parameters['Stock_name']
    if stockname == "":
     return {
            "fulfillmentMessages": [
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                  "simpleResponses": [
                    {
                      "textToSpeech": "Can't find this stock, please try another one."
                    }
                  ]
                }
              }
            ]
        }

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    data_url = os.path.join(SITE_ROOT, "static/data", "Arima_prediction.csv")
    stock_df = pd.read_csv(data_url, index_col=0)
    stock_df.columns = ['a', 'b']

    stock_price_df = stock_df[stock_df['a']==stockname]['b'].item().replace('[', '').replace(']', '').split()

    return {
    "fulfillmentMessages": [
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
              "simpleResponses": [
                {
                  "textToSpeech": "Hey, here you go, this is the forecast results for stock " +str(stockname)
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "tableCard": {
              "title": "Forecast results for stock " +str(stockname),
              "columnProperties": [
                {
                  "header": "Next n trading days",
                  "horizontalAlignment": "LEADING"
                },
                {
                  "header": "Price",
                  "horizontalAlignment": "LEADING"
                }
              ],
              "rows": [
                {
                  "cells": [
                    {
                      "text": "1"
                    },
                    {
                      "text": "${:.2f}".format(float(stock_price_df[0]))
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": "2"
                    },
                    {
                      "text": "${:.2f}".format(float(stock_price_df[1]))
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": "3"
                    },
                    {
                      "text": "${:.2f}".format(float(stock_price_df[2]))
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": "4"
                    },
                    {
                      "text": "${:.2f}".format(float(stock_price_df[3]))
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": "5"
                    },
                    {
                      "text": "${:.2f}".format(float(stock_price_df[4]))
                    }
                  ]
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "suggestions": {
              "suggestions": [
                {
                  "title": "Get more forecast"
                },
                {
                  "title": "Back To Main Menu"
                }
              ]
            }
          }
        ]
    }

def recommendRSI(req):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    data_url = os.path.join(SITE_ROOT, "static/data", "stock_oversold.csv")
    stock_df = pd.read_csv(data_url)

    return {
    "fulfillmentMessages": [
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
              "simpleResponses": [
                {
                  "textToSpeech": "Hey, here you go, this is the recommendation results based on the stock RSI:"
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "tableCard": {
              "title": "Recommendation results based on the stock RSI",
              "columnProperties": [
                {
                  "header": "Stock",
                  "horizontalAlignment": "LEADING"
                },
                {
                  "header": "RSI",
                  "horizontalAlignment": "LEADING"
                }
              ],
              "rows": [
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[0].Stock
                    },
                    {
                      "text": stock_df.iloc[0].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[1].Stock
                    },
                    {
                      "text": stock_df.iloc[1].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[2].Stock
                    },
                    {
                      "text": stock_df.iloc[2].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[3].Stock
                    },
                    {
                      "text": stock_df.iloc[3].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[4].Stock
                    },
                    {
                      "text": stock_df.iloc[4].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[5].Stock
                    },
                    {
                      "text": stock_df.iloc[5].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[6].Stock
                    },
                    {
                      "text": stock_df.iloc[6].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[7].Stock
                    },
                    {
                      "text": stock_df.iloc[7].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[8].Stock
                    },
                    {
                      "text": stock_df.iloc[8].rsi
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_df.iloc[9].Stock
                    },
                    {
                      "text": stock_df.iloc[9].rsi
                    }
                  ]
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "suggestions": {
              "suggestions": [
                {
                  "title": "Get more recommendation"
                },
                {
                  "title": "Back To Main Menu"
                }
              ]
            }
          }
        ]
    }


def recommendVolume(req):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    data_url = os.path.join(SITE_ROOT, "static/data", "stock_high_volume.csv")
    stock_volume = pd.read_csv(data_url)

    return {
    "fulfillmentMessages": [
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "simpleResponses": {
              "simpleResponses": [
                {
                  "textToSpeech": "Hey, here you go, this is the recommendation results based on the stock volume:"
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "tableCard": {
              "title": "Recommendation results based on the stock volume",
              "columnProperties": [
                {
                  "header": "Stock",
                  "horizontalAlignment": "LEADING"
                },
                {
                  "header": "Volume",
                  "horizontalAlignment": "LEADING"
                }
              ],
              "rows": [
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[0].Stock
                    },
                    {
                      "text": stock_volume.iloc[0].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[1].Stock
                    },
                    {
                      "text": stock_volume.iloc[1].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[2].Stock
                    },
                    {
                      "text": stock_volume.iloc[2].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[3].Stock
                    },
                    {
                      "text": stock_volume.iloc[3].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[4].Stock
                    },
                    {
                      "text": stock_volume.iloc[4].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[5].Stock
                    },
                    {
                      "text": stock_volume.iloc[5].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[6].Stock
                    },
                    {
                      "text": stock_volume.iloc[6].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[7].Stock
                    },
                    {
                      "text": stock_volume.iloc[7].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[8].Stock
                    },
                    {
                      "text": stock_volume.iloc[8].average_volume
                    }
                  ]
                },
                {
                  "cells": [
                    {
                      "text": stock_volume.iloc[9].Stock
                    },
                    {
                      "text": stock_volume.iloc[9].average_volume
                    }
                  ]
                }
              ]
            }
          },
          {
            "platform": "ACTIONS_ON_GOOGLE",
            "suggestions": {
              "suggestions": [
                {
                  "title": "Get more recommendation"
                },
                {
                  "title": "Back To Main Menu"
                }
              ]
            }
          }
        ]
    }

def processRequest(req):

    if req.get("queryResult").get("action") != "query":
        print("Please check your action name in DialogFlow...")
        return {}

    result = req.get("queryResult")
    parameters = result.get("parameters")
    #dateduration = parameters.get("date-period")
    price = parameters['Price']
    stockname = parameters['Stock_name']
    #date = parameters['date'].strftime('%Y-%m-%d')
    input_date=""
    if parameters['date'] != "":
        input_date=dt.fromisoformat(parameters['date'][0:10])
    #print(dateduration)
    print (price)
    print (stockname)

    date_today = datetime.date.today()
    startdate = ""
    enddate = ""
    if stockname == "":
         return {
                "fulfillmentMessages": [
                  {
                    "platform": "ACTIONS_ON_GOOGLE",
                    "simpleResponses": {
                      "simpleResponses": [
                        {
                          "textToSpeech": "Can't find this stock, please try another one."
                        }
                      ]
                    }
                  }
                ]
            }
   # if dateduration != "":
    #    startdate = dateduration['startDate']
    #    enddate = dateduration['endDate']

    if startdate == "":
        if input_date == "":
            date =  date_today
        else:
            date = input_date.date()
        res = makeWebhookResult(price , stockname , date)
    #else :
    #    res = makeWebhookResult(price , stockname , startdate , enddate)

    # print (startdate)
    # print (enddate)

    return res

def makeWebhookResult(price , stockname , datee):
    stock_data = yf.download(stockname,start=datee,end = (datee + datetime.timedelta(days=1)), interval='1d')
    if stock_data.empty == False:
        if price == 'open':
            stock_val = stock_data["Open"].item()
        elif price == 'low':
            stock_val = stock_data["Low"].item()
        elif price == 'high':
            stock_val = stock_data["High"].item()
        else :
            stock_val = stock_data["Close"].item()
        stock_val = "{:.2f}".format(stock_val)
        # url_l = "https://finance.yahoo.com/quote/" + str(stockname)
        #speech = ["Hey, here you go, the "+str(price)+" price for "+str(stockname)+" is $"+ stock_val + " on date " + str(datee)[0:10] + "\n" + "\n\nClick on the link to check the graph of " + str(stockname) + ": " + "https://finance.yahoo.com/quote/" + str(stockname) + "/"]
        speech = ["Hey, here you go, the "+str(price)+" price for "+str(stockname)+" is $"+ stock_val + " on date " + str(datee)[0:10]]
        url = "https://finance.yahoo.com/quote/" + str(stockname) + "/"

        return {
        "fulfillmentMessages": [
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                  "simpleResponses": [
                    {
                      "textToSpeech": str(random.choice(speech))
                    }
                  ]
                }
              },
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "basicCard": {
                  "title": str(stockname)+ "- $"+ stock_val,
                  "image": {
                    "imageUri": "https://s3.mobile-assets.com/production/246EcXxeSROZGjjSvBWrhSGY4KNkv5rni/newsfeed/cryptocurrency-screener-yahoo-finance-1512117067.png",
                    "accessibilityText": "Yahoo Finance"
                  },
                  "buttons": [
                    {
                      "title": "View on Yahoo Finance",
                      "openUriAction": {
                        "uri": url
                      }
                    }
                  ]
                }
              },
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "linkOutSuggestion": {
                  "destinationName": "Stock Graph",
                  "uri": url
                }
              },
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "suggestions": {
                  "suggestions": [
                    {
                      "title": "Check another price"
                    },
                    {
                      "title": "Back To Main Menu"
                    }
                  ]
                }
              }
            ]
        }

    else:
        speech = ["Sorry, can't find the "+str(price)+" price for "+str(stockname)+ " on date " + str(datee)[0:10] + ", please try another stock or date."]

        return {
        "fulfillmentMessages": [
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "simpleResponses": {
                  "simpleResponses": [
                    {
                      "textToSpeech": str(random.choice(speech))
                    }
                  ]
                }
              },
              {
                "platform": "ACTIONS_ON_GOOGLE",
                "suggestions": {
                  "suggestions": [
                    {
                      "title": "Check another price"
                    },
                    {
                      "title": "Back To Main Menu"
                    }
                  ]
                }
              }
            ]
        }

# def makeWebhookResult(price , stockname , startdate , enddate):
#     stock_data = yf.download(stockname,start=startdate,end = enddate, interval='1d')
#     if price == 'Open':
#         stock_val = stock_data["Open"].mean()
#     elif price == 'Low':
#         stock_val = stock_data["Low"].mean()
#     elif price == 'High':
#         stock_val = stock_data["High"].mean()
#     else :
#         stock_val = stock_data["Close"].mean()
#     speech = ["Hey here you go "+str(price)+" for "+str(stockname)+" is "+str(stock_val),
#                       str(stockname)+" is  "+str(stock_val)+" as a "+str(price),
#                       str(price)+" is "+str(stock_val)]
#     return {
#                         "fulfillmentText":  str(random.choice(speech)),
#                         "source": "alphavantage API"
#                     }


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = {"message":  fulfillment_text}
    return jsonify(response_text)


# run Flask app
if __name__ == "__main__":
    app.run()
