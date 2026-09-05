# python -m streamlit run app.py

import pandas as pd
import streamlit as st 
import joblib
from deal_logic import get_deal

st.title("Smart Deal")

st.write("AI-Assisted Used Car Price & Deal Intelligence")

bundle=joblib.load("smartdeal_bundle.joblib")

model=bundle["model"]
tolerance =bundle["tolerance"]
features=bundle["features"]

make_model_map=bundle["make_model_map"]
make_model_variant_map=bundle["make_model_variant_map"]

# Car company 
make_option = sorted(make_model_map.keys())

make = st.selectbox(
    "Select Car Make",
    make_option
)

#Car Model
model_option=sorted(make_model_map[make])

car_model = st.selectbox(
    "Select Car Model",
    model_option
)

#Car Variant
variant_option=sorted(make_model_variant_map[(make,car_model)])

variant = st.selectbox(
    "Select Car Variant",
    variant_option
)

preprocessor = model.named_steps["preprocessor"]
encoder = preprocessor.named_transformers_["categorical"]


# categorical_features = [
#     "make",          # 0
#     "model",         # 1
#     "variant",       # 2
#     "fuel_type",     # 3
#     "city",          # 4
#     "body_type",     # 5
#     "transmission"   # 6
# ]


fuel_options=sorted(encoder.categories_[3])
city_options=sorted(encoder.categories_[4])
body_type_options=sorted(encoder.categories_[5])
transmission_options=sorted(encoder.categories_[6])


fuel_type = st.selectbox(
    "Select Fuel Type",
    fuel_options
)

city = st.selectbox(
    "Select City Type",
    city_options
)

body_type = st.selectbox(
    "Select Body Type",
    body_type_options
)

transmission = st.selectbox(
    "Select Transmission Type",
    transmission_options
)

# NUMBER INPUT 
vehicle_age = st.number_input(
    "Vehicle Age (Years)",
     min_value=0,
     max_value=30
)

kms_run = st.number_input(
    "Kilometres Driven",
     min_value=0
)

total_owner = st.number_input(
    "Number of Previous Owners",
     min_value=1,
     max_value=10
)



asking_price=st.number_input(
    "At what price is the seller selling you the car in (₹)",
    min_value=0,
    max_value=50000000,
    step=10000
)


if st.button("Analyze Deal"):

    car_data = pd.DataFrame(
        [        # STORING DICT IN LIST
            {   
                "make": make,
                "model": car_model,
                "variant": variant,
                "fuel_type": fuel_type,
                "city": city,
                "body_type": body_type,
                "transmission": transmission,
                "vehicle_age": vehicle_age,
                "kms_run": kms_run,
                "total_owners": total_owner
            }
        ]
    )
    predicted_price=model.predict(car_data)[0]

    difference, diff_percent, verdict = get_deal(predicted_price, asking_price, tolerance)

    st.write("Estimated Fair Price: ₹", round(predicted_price,2))

    st.write("Seller's asking Price: ₹", round(asking_price,2))

    st.write("Price Differance", round(difference,2))

    st.write("Differeance Pecentange: ", round(diff_percent,2) , "%")

    st.write("Verdict: ", verdict)
