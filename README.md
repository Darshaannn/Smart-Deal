# 🚗 SmartDeal
## https://samrt-deal.streamlit.app/
SmartDeal is a machine learning app that estimates the fair price of a used car and compares it with the seller's asking price.

It then gives a simple verdict:

- Excellent Deal
- Good Deal
- Fair Deal
- Overpriced
- Very Overpriced

---

## How It Works

The user enters:

- Make
- Model
- Variant
- Fuel Type
- City
- Body Type
- Transmission
- Vehicle Age
- Kilometres Driven
- Number of Owners
- Seller Asking Price

SmartDeal then:


Car Details
   ↓
ML Model
   ↓
Estimated Fair Price
   ↓
Compare with Seller Price
   ↓
Deal Verdict

---

## Model Used

I tested:

Linear Regression
Random Forest Regressor

Random Forest performed better, so it was selected as the final model.

Performance
Metric	                           Random Forest
MAE	                               ₹49,156
RMSE	                           ₹90,493
R² Score	                       0.8992
MAPE	                           12.58%

---

## Tech Stack

- Python
-Pandas
-NumPy
-Scikit-learn
-Random Forest
-Streamlit
-Joblib
-Matplotlib

---

## Project Structure

SmartDeal/
│
├── app.py
├── deal_logic.py
├── smartdeal_bunddle.joblib
├── SmartDeal.ipynb
└── README.md
Run Locally


## Install dependencies:

pip install -r requirements.txt


## Run the app:

python -m streamlit run app.py

Example
Estimated Fair Price: ₹10,74,000
Seller Asking Price: ₹10,00,000
Price Difference: -₹74,000
Verdict: Fair Deal
Note

SmartDeal is an educational ML project trained on historical used-car data.

It should be treated as an estimated reference price, not a guaranteed live market valuation.

**Author**

**Darshan Gadhave**

**GitHub: https://github.com/Darshaannn**
