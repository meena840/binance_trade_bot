# in this file we will include all the settings for this project

from decouple import config

class BINANCE_CONFIGS:
    base_url = "https://testnet.binancefuture.com/fapi"
    api_key=config("BINANCE_API_KEY")
    api_secret_key=config("BINANCE_API_SECRET_KEY")