# Program Python untuk menghitung daily reward dan 14 days reward dalam TON, USD, dan IDR

def calculate_reward(deposited_amount, apy, days):
    # Menghitung imbal hasil dalam USDT
    reward_usdt = deposited_amount * (apy / 100) * (days / 365)
    return reward_usdt

def convert_usdt_to_ton(reward_usdt, usdt_to_ton_rate):
    # Mengonversi reward dari USDT ke TON
    return reward_usdt * usdt_to_ton_rate

def convert_ton_to_usd(reward_ton, ton_to_usd_rate):
    # Mengonversi TON ke USD
    return reward_ton * ton_to_usd_rate

def convert_usd_to_idr(reward_usd, usd_to_idr_rate):
    # Mengonversi USD ke IDR
    return reward_usd * usd_to_idr_rate

# Input dari user
deposited_amount = float(input("Masukkan jumlah USDT yang didepositkan: "))
apy = float(input("Masukkan nilai APY (dalam %): "))
usdt_to_ton_rate = float(input("Masukkan kurs USDT ke TON: "))
usd_to_idr_rate = float(input("Masukkan kurs USD ke IDR: "))
ton_to_usd_rate = 1 / usdt_to_ton_rate  # Mengonversi TON ke USD berdasarkan kurs

# Menghitung reward untuk 1 hari dan 14 hari
daily_reward_usdt = calculate_reward(deposited_amount, apy, 1)
reward_14_days_usdt = calculate_reward(deposited_amount, apy, 14)

# Mengonversi reward ke TON
daily_reward_ton = convert_usdt_to_ton(daily_reward_usdt, usdt_to_ton_rate)
reward_14_days_ton = convert_usdt_to_ton(reward_14_days_usdt, usdt_to_ton_rate)

# Mengonversi reward ke USD dan IDR
daily_reward_usd = convert_ton_to_usd(daily_reward_ton, ton_to_usd_rate)
reward_14_days_usd = convert_ton_to_usd(reward_14_days_ton, ton_to_usd_rate)

daily_reward_idr = convert_usd_to_idr(daily_reward_usd, usd_to_idr_rate)
reward_14_days_idr = convert_usd_to_idr(reward_14_days_usd, usd_to_idr_rate)

# Menampilkan hasil
print(f"\nImbal hasil harian (1 hari) dalam TON: {daily_reward_ton:.6f} TON")
print(f"Imbal hasil untuk 14 hari dalam TON: {reward_14_days_ton:.6f} TON")
print(f"\nImbal hasil harian (1 hari) dalam USD: {daily_reward_usd:.6f} USD")
print(f"Imbal hasil untuk 14 hari dalam USD: {reward_14_days_usd:.6f} USD")
print(f"\nImbal hasil harian (1 hari) dalam IDR: {daily_reward_idr:.2f} IDR")
print(f"Imbal hasil untuk 14 hari dalam IDR: {reward_14_days_idr:.2f} IDR")
