import pandas as pd
import matplotlib.pyplot as plt

# Зареждане на данни
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Филтрираме за България и Германия
bg = df[df['location'] == 'Bulgaria']
de = df[df['location'] == 'Germany']

# Нови случаи в България
plt.figure(figsize=(10,5))
plt.plot(bg['date'], bg['new_cases'], label="Нови случаи")
plt.title("COVID-19 нови случаи в България")
plt.xlabel("Дата")
plt.ylabel("Брой случаи")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/bg_cases.png")
plt.close()

# Сравнение BG vs DE (7-дн. средно)
plt.figure(figsize=(10,5))
plt.plot(bg['date'], bg['new_cases'].rolling(7).mean(), label="България (7-дн. средно)")
plt.plot(de['date'], de['new_cases'].rolling(7).mean(), label="Германия (7-дн. средно)")
plt.title("Сравнение: Нови случаи COVID-19 (BG vs DE)")
plt.xlabel("Дата")
plt.ylabel("Брой случаи")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/bg_vs_de.png")
plt.close()
