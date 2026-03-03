import pandas as pd

data = {
    "Color": ["Red", "Blue", "Green", "Yellow", "Pink", "Purple", "Orange", "White"],
    "Type": ["Organic", "Chemical", "Organic", "Chemical", "Organic", "Chemical", "Organic", "Chemical"],
    "Price": [50, 30, 45, 25, 55, 35, 48, 20],
    "Quantity_Sold": [200, 350, 180, 400, 150, 300, 170, 420]
}

df = pd.DataFrame(data)

# Calculate Total Revenue
df["Total_Revenue"] = df["Price"] * df["Quantity_Sold"]

print(df)

import matplotlib.pyplot as plt

plt.figure()
plt.bar(df["Color"], df["Total_Revenue"])

plt.title("Holi Color Revenue Analysis")
plt.xlabel("Colors")
plt.ylabel("Total Revenue (₹)")

plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.pie(df["Quantity_Sold"], labels=df["Color"], autopct='%1.1f%%')

plt.title("Sales Distribution of Holi Colors")
plt.show()

import seaborn as sns

plt.figure()
sns.barplot(x="Type", y="Total_Revenue", data=df)

plt.title("Organic vs Chemical Revenue Comparison")
plt.xlabel("Color Type")
plt.ylabel("Total Revenue (₹)")

plt.show()