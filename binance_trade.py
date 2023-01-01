import binance
import api
import time

client = binance.Client(api.api_key, api.api_secret, testnet=True)

def get_asset_balance(symbol):
    try:
        asset = client.get_asset_balance(asset=symbol)
        asset_balance = asset["free"]
        print(f"{symbol} balance: {asset_balance}")
    except:
        print("asset not found")

def buy(symbol="ETHUSDT", quantity=10):
    try:
        client.order_market_buy(
            symbol=symbol,
            quantity=quantity)
        buy_price = get_price(symbol)
        print(f"purchase price: {buy_price}")
        time.sleep(1.5)
        print("purchase successful")
        return float(buy_price)
    except:
        print("failed purchase")


def sell(symbol="ETHUSDT", quantity=10):
    try:
        client.order_market_sell(
            symbol=symbol,
            quantity=quantity)
        sale_price = get_price(symbol)
        print(f"sale price: {sale_price}")
        time.sleep(1.5)
        print("sale successful")
        return float(sale_price)
    except:
        print("failed sell")

def get_price(symbol):
    price = client.get_ticker(symbol=symbol)["lastPrice"]
    return price

def Calculate(sell, buy):
    profit_loss = (sell - buy) * 10
    time.sleep(1.5)
    print(f"profit/loss: ${profit_loss}")
    return

def buy_sell():
    buy_result = buy()
    time.sleep(30)
    sell_result = sell()
    time.sleep(1)
    Calculate(sell_result, buy_result)
    get_asset_balance("usdt")

    
