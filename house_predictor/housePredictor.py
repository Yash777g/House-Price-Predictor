import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression

# Training data
data = {
    'Size': [1200, 1500, 1800, 2000, 2400, 3000],
    'Locality': ['Urban', 'Suburban', 'Rural', 'Urban', 'Suburban', 'Urban'],
    'Region': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Hyderabad', 'Delhi'],
    'Seaview': [1, 0, 0, 1, 0, 0],
    'LandRate': [50000, 30000, 25000, 50000, 28000, 30000],
    'Price': [7500000, 4500000, 4500000, 10000000, 6720000, 9000000]
}

df = pd.DataFrame(data)
df = pd.get_dummies(df, columns=["Locality", "Region"])

X = df.drop("Price", axis=1)
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

# Mock land rate function
def get_land_rate(region):
    rates = {
        "Mumbai": 50000,
        "Delhi": 30000,
        "Bangalore": 25000,
        "Hyderabad": 28000,
        "Chennai": 22000
    }
    return rates.get(region, 25000)

# Interface
class HousePricePredictor:

    def __init__(self, root):
        self.root = root
        self.root.title("House Price Predictor")
        self.root.geometry("420x450")
        self.root.resizable(False, False)

        self.size = tk.DoubleVar()
        self.locality = tk.StringVar()
        self.region = tk.StringVar()
        self.seaview = tk.BooleanVar()
        self.land_rate = tk.DoubleVar()

        ttk.Label(root, text="🏠 House Price Predictor", font=("Arial", 16, "bold")).pack(pady=10)

        self.create_form()

    def create_form(self):
        ttk.Label(self.root, text="House Size (sq ft)").pack()
        ttk.Entry(self.root, textvariable=self.size).pack()

        ttk.Label(self.root, text="Locality").pack()
        ttk.Combobox(
            self.root,
            textvariable=self.locality,
            values=["Urban", "Suburban", "Rural"],
            state="readonly"
        ).pack()

        ttk.Label(self.root, text="Region").pack()
        region_cb = ttk.Combobox(
            self.root,
            textvariable=self.region,
            values=["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"],
            state="readonly"
        )
        region_cb.pack()
        region_cb.bind("<<ComboboxSelected>>", self.update_land_rate)

        ttk.Label(self.root, text="Land Rate (₹/sq ft)").pack()
        ttk.Label(self.root, textvariable=self.land_rate, font=("Arial", 10, "bold")).pack()

        ttk.Checkbutton(self.root, text="Seaview Property", variable=self.seaview).pack(pady=5)

        ttk.Button(self.root, text="Predict Price", command=self.predict).pack(pady=20)

        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack()

    def update_land_rate(self, event=None):
        self.land_rate.set(get_land_rate(self.region.get()))

    def predict(self):
        try:
            if self.size.get() <= 0:
                raise ValueError("House size must be greater than zero.")

            input_data = {
                "Size": [self.size.get()],
                "Seaview": [1 if self.seaview.get() else 0],
                "LandRate": [self.land_rate.get()]
            }

            for loc in ["Urban", "Suburban", "Rural"]:
                input_data[f"Locality_{loc}"] = [1 if self.locality.get() == loc else 0]

            for reg in ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai"]:
                input_data[f"Region_{reg}"] = [1 if self.region.get() == reg else 0]

            input_df = pd.DataFrame(input_data)

            for col in X.columns:
                if col not in input_df:
                    input_df[col] = 0

            input_df = input_df[X.columns]

            prediction = model.predict(input_df)[0]
            self.result_label.config(text=f"Predicted Price: ₹{prediction:,.2f}")

        except Exception as e:
            messagebox.showerror("Error", str(e))


# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = HousePricePredictor(root)
    root.mainloop()
