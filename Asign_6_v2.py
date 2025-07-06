import yfinance 
apple=yfinance.Ticker("SONY")
df = apple.history(period="20y")
import matplotlib.pyplot as plt
import altair as alt
import altair_viewer

Short = 20
Long = 50
InitBalance = 1000
Balance = InitBalance
ShareAmount = 0

df["RolAvS"] = df['Close'].rolling(window=20).mean()
df["RolAvL"] = df['Close'].rolling(window=50).mean()

df["Status"] = "Hold"

FirstBuy = False



for i in range(Long, len(df)):
    if i != Long:
        if df.iloc[i-1]["RolAvS"] < df.iloc[i-1]["RolAvL"] and df.iloc[i]["RolAvS"] > df.iloc[i]["RolAvL"]:
            df.iloc[i, df.columns.get_loc("Status")] = "Buy"
            ShareAmount = Balance / df.iloc[i]["Close"]
            print(f"Bought {ShareAmount} shares for {Balance}")
            Balance = 0
            FirstBuy = True
        elif df.iloc[i-1]["RolAvS"] > df.iloc[i-1]["RolAvL"] and df.iloc[i]["RolAvS"] < df.iloc[i]["RolAvL"] and FirstBuy:
            df.iloc[i, df.columns.get_loc("Status")] = "Sell"
            Balance = ShareAmount * df.iloc[i]["Close"]
            print(f"Sold {ShareAmount} shares for {Balance}")
            percent = round(((Balance-InitBalance)/InitBalance)*100, 2)
            print(f"Change of percentage - {percent}")
            ShareAmount = 0

if ShareAmount !=0:
    Balance = ShareAmount*df.iloc[-1]["Close"]


print(f"Final balance - {Balance}")
print(f"Change of percentage - {round(((Balance-InitBalance)/InitBalance)*100, 2)}%")



