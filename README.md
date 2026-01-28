# 🏠 House Price Predictor

A simple **Python GUI application** that predicts house prices based on key property features like size, locality, region, seaview, and land rate.  
Powered by a **Linear Regression** model trained on a small sample dataset.

---

## 🚀 Features

- Predicts house price based on:
  - **Size (sq ft)**
  - **Locality** (Urban, Suburban, Rural)
  - **Region** (Mumbai, Delhi, Bangalore, Hyderabad, Chennai)
  - **Seaview** property
  - **Land rate** per sq ft (auto-updated based on region)
- Interactive GUI built with **Tkinter** and **ttk**
- Automatic land rate update when region is selected
- Formatted predicted price display
- Input validation to prevent errors (e.g., size > 0)

---

## 💻 Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-directory>

2. Install required packages:

pip install pandas scikit-learn


Tkinter is included with Python by default.

📝 Usage

Run the application:

python house_price_predictor.py


Fill in the form:

Enter house size in sq ft

Select locality and region

Check Seaview if applicable

Land rate updates automatically

Click Predict Price to see the estimated house price.

📊 Sample Dataset
Size	Locality	Region	Seaview	LandRate	Price
1200	Urban	Mumbai	1	50000	7,500,000
1500	Suburban	Delhi	0	30000	4,500,000
1800	Rural	Bangalore	0	25000	4,500,000
2000	Urban	Mumbai	1	50000	10,000,000
2400	Suburban	Hyderabad	0	28000	6,720,000
3000	Urban	Delhi	0	30000	9,000,000
⚙️ How It Works

A Linear Regression model is trained on a small sample dataset.

One-hot encoding is used for categorical variables (Locality and Region).

User inputs are converted into the same format as training data.

The model predicts the house price, which is displayed in the GUI.

📌 Notes

The model is trained on a small sample dataset, so predictions are for demonstration purposes only.

More real-world data will improve accuracy.

Currently supports limited regions and localities. To extend, update the data dictionary and get_land_rate function.

🌟 Future Enhancements

Dynamic addition of new regions with land rates

Include more features (bedrooms, bathrooms, amenities)

Provide price range or confidence interval

Connect with real estate databases for live predictions

