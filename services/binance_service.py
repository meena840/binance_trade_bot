from binance.client import Client
from settings import BINANCE_CONFIGS


class BasicBot:
    def __init__(self):
        self.api_key=BINANCE_CONFIGS.api_key
        self.secret_key=BINANCE_CONFIGS.api_secret_key
        self.base_url=BINANCE_CONFIGS.base_url

        self.client = Client(self.api_key, self.secret_key,testnet=True)
        self.client.API_URL = self.base_url
    

    def get_account_info(self):
        try:
            return self.client.futures_account()
        except Exception as e:
            print(f"error getting account info -> {str(e)}")
    
    def get_price(self, symbol="BTCUSDT"):
        try:
            return self.client.futures_symbol_ticker(symbol=symbol)
        except Exception as e:
            print(f"error getting price info -> {str(e)}")
    
    def get_account_balance(self):
        try:
            return self.client.futures_account_balance()
        except Exception as e:
            print(f"error getting account balance -> {str(e)}")   


    
    def place_order(self,event="BUY", symbol="BTCUSDT",quantity=0.001):
        try:
            return self.client.futures_create_order(
            symbol=symbol,
            side=event,
            type='MARKET',
            quantity=quantity,
            )
        except Exception as e:
            print(f"error placing order -> {str(e)}")

    def place_limit_order(self,event="BUY",symbol="BTCUSDT",quantity=0.002,price='65000'):
        try:
            return self.client.futures_create_order(
                symbol=symbol,
                side=event,
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity,
                price=price,
            )
        except Exception as e:
            print(f"error placing limit order -> {str(e)}")
    


    
    
