
import requests
import time
import telegram

# === НАСТРОЙКИ ===
BOT_TOKEN = '7277868783:AAHW7OGWYss2WSJsstUmD5A0MmZKzE7Y3Lg'
CHANNEL_ID = -1001234567890  # замени на ID своего канала, не забудь минус

# Инициализация бота
bot = telegram.Bot(token=BOT_TOKEN)

# Получение курсов с CoinGecko
def get_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,the-open-network&vs_currencies=usd'
    data = requests.get(url).json()
    btc = data['bitcoin']['usd']
    eth = data['ethereum']['usd']
    ton = data['the-open-network']['usd']
    return f"""💰 *Актуальные курсы криптовалют:*

• BTC: ${btc}
• ETH: ${eth}
• TON: ${ton}

_Обновляется каждые 10 минут_"""

# Основной цикл
def main():
    message = bot.send_message(
        chat_id=CHANNEL_ID,
        text=get_prices(),
        parse_mode=telegram.ParseMode.MARKDOWN
    )
    message_id = message.message_id

    while True:
        try:
            time.sleep(600)  # 10 минут
            bot.edit_message_text(
                chat_id=CHANNEL_ID,
                message_id=message_id,
                text=get_prices(),
                parse_mode=telegram.ParseMode.MARKDOWN
            )
        except Exception as e:
            print("Ошибка:", e)

# Запуск
if __name__ == '__main__':
    main()
