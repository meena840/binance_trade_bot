from utils import show_menu
from services.binance_service import BasicBot

if __name__=="__main__":
    
    trade_bot=BasicBot()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\nFetching account info")
            data = trade_bot.get_account_info()
            print(data)

        elif choice == "2":
            symbol = input(
                "Enter symbol (default BTCUSDT): ").strip() or "BTCUSDT"
            print(f"\nFetching price for {symbol}")
            data = trade_bot.get_price(symbol=symbol)
            print(data)

        elif choice == "3":
            print("\nFetching account balance")
            data = trade_bot.get_account_balance()
            print(data)

        elif choice == "4":
            symbol = input(
                "Enter symbol (default BTCUSDT): ").strip() or "BTCUSDT"
            side = input(
                "Enter order side (BUY/SELL): ").strip().upper() or "BUY"
            quantity = input(
                "Enter quantity (default 0.001): ").strip() or "0.001"
            print(
                f"\nPlacing {side} market order for {symbol} ({quantity})")
            data = trade_bot.place_order(
                event=side, symbol=symbol, quantity=float(quantity))
            print(data)

        elif choice == "5":
            symbol = input(
                "Enter symbol (default BTCUSDT): ").strip() or "BTCUSDT"
            side = input(
                "Enter order side (BUY/SELL): ").strip().upper() or "BUY"
            quantity = input(
                "Enter quantity (default 0.002): ").strip() or "0.002"
            price = input(
                "Enter limit price (default 65000): ").strip() or "65000"
            print(
                f"\n Placing {side} limit order for {symbol} ({quantity}) at {price}")
            data = trade_bot.place_limit_order(
                event=side, symbol=symbol, quantity=float(quantity), price=price)
            print(data)

        elif choice == "6":
            print("\n Exiting Binance trade bot. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
