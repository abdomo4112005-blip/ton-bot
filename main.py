import requests
import asyncio
from telegram import Bot

TOKEN = "8446317533:AAGjXl1oTojDWnk8IPreIwvjCFq7tM28pM8"
CHAT_ID = "@rn_h_i"
INTERVAL = 60 

bot = Bot(token=TOKEN)

def get_ton_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=TONUSDT"
        response = requests.get(url)
        data = response.json()
        return float(data["price"])
    except:
        return None

async def start_bot():
    print("Bot started...")
    while True:
        price = get_ton_price()
        if price:
            try:
                text = f"TON Price: ${price:.2f}"
                await bot.send_message(chat_id=CHAT_ID, text=text)
                print(f"Price sent: {price}")
            except Exception as e:
                print(f"Send error: {e}")
        else:
            print("Fetch error")
            
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(start_bot())
