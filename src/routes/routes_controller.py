from flask import jsonify
from flask import request
from flask import Flask
from src.controllers.get_historical_kandles import get_historical_kandles
from binance.client import Client

class routes_controller:

    app = any
    binance_client = Client('CDmG49sRfS3pXUMChi5itOH0f6elIW0frAvizDDpuE0UCYJRt1pccggO7JXhWfYv', 
                '8trKMxv8WjS3tn04QNycWY6RSVNULkwE0HfDtYm5cKk9rQHYwm4URyGGhcHCbF5i')

    def __init__(self):
        """ Init the historical enpoints """
        self.init_app()
        self.init_historical_kandles_enpoints()
        
        """ Start Server """
        self.app.run(debug=True)

    """ Init flask app """
    def init_app(self):
        self.app = Flask(__name__)
   
    def init_historical_kandles_enpoints(self):
        """ Get historical Kandles object """
        historical_kandles = get_historical_kandles(self.binance_client)
        
        @self.app.route('/api/historical/between-dates', methods=['GET'])
        def get_historical_between_dates():
            initial_date = str(request.args.get('init_date', default = "1 Apr, 2022"))
            finish_date = str(request.args.get('finish_date', default= "5 Apr, 2022"))
            pair_coin = str(request.args.get('pair_coin' , default= 'BNBBTC'))
            kandle_interval = str(request.args.get('kandle_interval', default= '1h'))
            
            response = historical_kandles.get_historical_between_dates(pair_coin, kandle_interval, initial_date, finish_date)
            return jsonify(response)
        
        @self.app.route('/api/historical/between-dates', methods=['GET'])
        def get_historical_from_time_ago():
                time_ago = str(request.args.get('time_ago', default = "1 day ago UTC"))
                pair_coin = str(request.args.get('pair_coin' , default= 'BNBBTC'))
                kandle_interval = str(request.args.get('kandle_interval', default= '1h'))
                
                response = historical_kandles.get_historical_from_time_ago(pair_coin, kandle_interval, time_ago)
                return jsonify(response)
