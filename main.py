import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    try:
        response = requests.get(
            "https://min-api.cryptocompare.com/data/price",
            params={
                "fsym": "BTC",
                "tsyms": "USD,JPY,EUR",
                "tryConversion": "true", 
                "api_key": "b2ca1b2533aa03231c037324516c9d800f3b6c591536334baf2b26d5e0c221ac"
            },
            headers={"Content-type": "application/json; charset=UTF-8"}
        )
        
        data = response.json()
        print("API Response:", data)

        
        if all(k in data for k in ["USD", "JPY", "EUR"]):
            labelUSD.config(text=f"USD: {data['USD']} $")
            labelJPY.config(text=f"JPY: {data['JPY']} ¥")
            labelEUR.config(text=f"EUR: {data['EUR']} €")

            current_time = datetime.now().strftime("%H:%M:%S")
            labelTime.config(text="Updated at: " + current_time)
        else:
            labelUSD.config(text="Error fetching prices")
            labelJPY.config(text="")
            labelEUR.config(text="")
            labelTime.config(text="Try again later")

    except Exception as e:
        labelUSD.config(text="Request failed")
        labelJPY.config(text="")
        labelEUR.config(text="")
        labelTime.config(text=str(e))

    canvas.after(1000, trackBitcoin)  


canvas = tk.Tk()
canvas.geometry("500x600")
canvas.title("Bitcoin Tracker")

f1 = ("Sans-Serif", 26, "bold")
f2 = ("Sans-Serif", 22, "bold")
f3 = ("Sans-Serif", 18, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1)
label.pack(pady=20)

labelUSD = tk.Label(canvas, font=f2)
labelUSD.pack(pady=10)

labelJPY = tk.Label(canvas, font=f2)
labelJPY.pack(pady=10)

labelEUR = tk.Label(canvas, font=f2)
labelEUR.pack(pady=10)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

trackBitcoin()
canvas.mainloop()



