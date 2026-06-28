import requests
import pandas as pd
# Kripto verilerini çekmek için ücretsiz ccxt kütüphanesi
import ccxt 

# Senin Telegram Bilgilerin
TELEGRAM_TOKEN = "7836097436:AAEwJq_lQ5dH7Aet_cLQTAtW9dTQXcYCS8c"
CHAT_ID = "6303765742"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)

def check_market():
    exchange = ccxt.mexc()
    coins = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT']
    
    for coin in coins:
        # 1 Saatlik mum verilerini çek
        bars = exchange.fetch_ohlcv(coin, timeframe='1h', limit=50)
        df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # NOT: SmartMCDX'in formülü (Hacim ve RSI kombinasyonu) buraya entegre edilecek.
        # Şimdilik örnek bir "mcdx_degeri" değişkeni oluşturuyoruz.
        mcdx_degeri = 2.5 # Bu değer hesaplama fonksiyonundan gelecek
        
        # Koşul: 0 ile 4 arasında mı? (0 ve 4 dahil)
        if 0 <= mcdx_degeri <= 4:
            anlik_fiyat = df['close'].iloc[-1]
            mesaj = f"🚨 DİKKAT!\nCoin: {coin}\nFiyat: {anlik_fiyat} $\nSmartMCDX Seviyesi: {mcdx_degeri}\nDurum: [0,4] aralığına girdi, işlem fırsatı!"
            send_telegram_message(mesaj)

if __name__ == "__main__":
    check_market()
