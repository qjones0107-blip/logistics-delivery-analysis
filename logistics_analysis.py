import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("logistics_data.csv")

# Delivery Status
plt.figure()
df["delivery_status"].value_counts().plot(kind="bar")
plt.title("Delivery Status")
plt.savefig("delivery_status.png")
plt.close()

# Delays by Region
plt.figure()
df[df["delivery_status"]=="Delayed"]["region"].value_counts().plot(kind="bar")
plt.title("Delays by Region")
plt.savefig("delays_by_region.png")
plt.close()

# Cost by Carrier
plt.figure()
df.groupby("carrier")["shipping_cost"].mean().plot(kind="bar")
plt.title("Average Shipping Cost by Carrier")
plt.savefig("cost_by_carrier.png")
plt.close()

# Delivery Time
df["ship_date"] = pd.to_datetime(df["ship_date"])
df["delivery_date"] = pd.to_datetime(df["delivery_date"])
df["delivery_days"] = (df["delivery_date"] - df["ship_date"]).dt.days

plt.figure()
df.groupby("carrier")["delivery_days"].mean().plot(kind="bar")
plt.title("Average Delivery Time by Carrier")
plt.savefig("delivery_time_by_carrier.png")
plt.close()
