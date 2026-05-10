import requests
import asyncio
from telegram import Bot

# ========== إعداداتك ==========
TOKEN = "8446317533:AAGjXlloTojDWnk8IPreIwvjCuNl8j4o2MY"
CHAT_ID = "@rn_h_i"
INTERVAL = 1 

bot = Bot(token=TOKEN)

def get_ton_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=TONUSDT"
        data = requests.get(url).json()
        return float(data["price"])
    except:
        return None

async def send_price():
    print("بدأ البوت في إرسال التحديثات...")
    while True:
        price_usd = get_ton_price()
        if price_usd is not None:
            message = f"{price_usd:.2f}$"
            try:
                await bot.send_message(chat_id=CHAT_ID, text=message)
            except Exception as e:
                print(f"خطأ: {e}")
        await asyncio.sleep(INTERVAL)

async def main():
    await send_price()

if __name__ == "__main__":
    asyncio.run(main())
