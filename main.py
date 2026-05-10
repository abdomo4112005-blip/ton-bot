import requests
import asyncio
from telegram import Bot
from telegram.request import HTTPXRequest

# ========== إعداداتك ==========
TOKEN = "8446317533:AAGjXl1oTojDWnk8IPreIwvjCFq7tM28pM8"
CHAT_ID = "@rn_h_i"
INTERVAL = 60 

# نظام اتصال أقوى عشان يتخطى مشاكل السيرفرات
async def start_bot():
    t_request = HTTPXRequest(connection_pool_size=8)
    bot = Bot(token=TOKEN, request=t_request)
    
    print("بدء محاولة الاتصال بالAPI...")
    
    while True:
        try:
            # جلب السعر من بينانس
            url = "https://api.binance.com/api/v3/ticker/price?symbol=TONUSDT"
            response = requests.get(url)
            data = response.json()
            price = float(data["price"])
            
            # إرسال الرسالة
            text = f"💎 سعر عملة TON الآن:\n\n💰 ${price:.2f}"
            await bot.send_message(chat_id=CHAT_ID, text=text)
            print(f"✅ تم الإرسال للقناة: {price}")
            
        except Exception as e:
            print(f"❌ حدث خطأ: {e}")
            
        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    asyncio.run(start_bot())
