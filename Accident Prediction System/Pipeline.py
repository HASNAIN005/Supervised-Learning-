import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle
from PIL import Image
from streamlit import title, button

model = pickle.load(open('.venv/pipe.pkl', 'rb'))
img=Image.open('.venv/accident.png')
st.image(image=img)
st.title("Scikit Learn By Teacher Noor")

def prediction(Time, Day_of_week, Age_band_of_driver, Sex_of_driver, Educational_level, Vehicle_driver_relation,
               Driving_experience, Type_of_vehicle, Owner_of_vehicle, Service_year_of_vehicle, Defect_of_vehicle,
               Area_accident_occured, Lanes_or_Medians, Road_allignment, Types_of_Junction, Road_surface_type,
               Road_surface_conditions, Light_conditions, Weather_conditions, Type_of_collision, Number_of_vehicles_involved,
               Number_of_casualties, Vehicle_movement, Casualty_class, Sex_of_casualty, Age_band_of_casualty, Casualty_severity,
               Work_of_casuality, Fitness_of_casuality, Pedestrian_movement, Cause_of_accident):
    feature=np.array([[Time, Day_of_week, Age_band_of_driver, Sex_of_driver, Educational_level, Vehicle_driver_relation,
                       Driving_experience, Type_of_vehicle, Owner_of_vehicle, Service_year_of_vehicle, Defect_of_vehicle,
                       Area_accident_occured, Lanes_or_Medians, Road_allignment, Types_of_Junction, Road_surface_type,
                       Road_surface_conditions, Light_conditions, Weather_conditions, Type_of_collision, Number_of_vehicles_involved,
                       Number_of_casualties, Vehicle_movement, Casualty_class, Sex_of_casualty, Age_band_of_casualty, Casualty_severity,
                       Work_of_casuality, Fitness_of_casuality, Pedestrian_movement, Cause_of_accident]])
    result= model.predict(feature)
    return result


import streamlit as st

# For each column, create a selectbox with the unique values as options

Time = st.selectbox("Select Time", options=[17, 1, 14, 22, 8, 15, 12, 18, 13, 20, 16, 21, 9, 10, 19, 11, 23, 7, 0, 5, 6, 4, 3, 2])
Day_of_week = st.selectbox("Select Day of Week", options=['Monday', 'Sunday', 'Friday', 'Wednesday', 'Saturday', 'Thursday', 'Tuesday'])
Age_band_of_driver = st.selectbox("Select Age Band of Driver", options=['18-30', '31-50', 'Under 18', 'Over 51', 'Unknown'])
Sex_of_driver = st.selectbox("Select Sex of Driver", options=['Male', 'Female', 'Unknown'])
Educational_level = st.selectbox("Select Educational Level", options=['Above high school', 'Junior high school', 'nan', 'Elementary school', 'High school', 'Unknown', 'Illiterate', 'Writing & reading'])
Vehicle_driver_relation = st.selectbox("Select Vehicle-Driver Relation", options=['Employee', 'Unknown', 'Owner', 'nan', 'Other'])
Driving_experience = st.selectbox("Select Driving Experience", options=['1-2yr', 'Above 10yr', '5-10yr', '2-5yr', 'nan', 'No Licence', 'Below 1yr', 'unknown'])
Type_of_vehicle = st.selectbox("Select Type of Vehicle", options=['Automobile', 'Public (> 45 seats)', 'Lorry (41?100Q)', 'nan', 'Public (13?45 seats)', 'Lorry (11?40Q)', 'Long lorry', 'Public (12 seats)', 'Taxi', 'Pick up upto 10Q', 'Stationwagen', 'Ridden horse', 'Other', 'Bajaj', 'Turbo', 'Motorcycle', 'Special vehicle', 'Bicycle'])
Owner_of_vehicle = st.selectbox("Select Owner of Vehicle", options=['Owner', 'Governmental', 'nan', 'Organization', 'Other'])
Service_year_of_vehicle = st.selectbox("Select Service Year of Vehicle", options=['Above 10yr', '5-10yrs', 'nan', '1-2yr', '2-5yrs', 'Unknown', 'Below 1yr'])
Defect_of_vehicle = st.selectbox("Select Defect of Vehicle", options=['No defect', 'nan', '7', '5'])
Area_accident_occured = st.selectbox("Select Area Accident Occurred", options=['Residential areas', 'Office areas', '  Recreational areas', ' Industrial areas', 'nan', 'Other', ' Church areas', '  Market areas', 'Unknown', 'Rural village areas', ' Outside rural areas', ' Hospital areas', 'School areas', 'Rural village areasOffice areas', 'Recreational areas'])
Lanes_or_Medians = st.selectbox("Select Lanes or Medians", options=['nan', 'Undivided Two way', 'other', 'Double carriageway (median)', 'One way', 'Two-way (divided with solid lines road marking)', 'Two-way (divided with broken lines road marking)', 'Unknown'])
Road_allignment = st.selectbox("Select Road Alignment", options=['Tangent road with flat terrain', 'nan', 'Tangent road with mild grade and flat terrain', 'Escarpments', 'Tangent road with rolling terrain', 'Gentle horizontal curve', 'Tangent road with mountainous terrain and', 'Steep grade downward with mountainous terrain', 'Sharp reverse curve', 'Steep grade upward with mountainous terrain'])
Types_of_Junction = st.selectbox("Select Types of Junction", options=['No junction', 'Y Shape', 'Crossing', 'O Shape', 'Other', 'Unknown', 'T Shape', 'X Shape', 'nan'])
Road_surface_type = st.selectbox("Select Road Surface Type", options=['Asphalt roads', 'Earth roads', 'nan', 'Asphalt roads with some distress', 'Gravel roads', 'Other'])
Road_surface_conditions = st.selectbox("Select Road Surface Conditions", options=['Dry', 'Wet or damp', 'Snow', 'Flood over 3cm. deep'])
Light_conditions = st.selectbox("Select Light Conditions", options=['Daylight', 'Darkness - lights lit', 'Darkness - no lighting', 'Darkness - lights unlit'])
Weather_conditions = st.selectbox("Select Weather Conditions", options=['Normal', 'Raining', 'Raining and Windy', 'Cloudy', 'Other', 'Windy', 'Snow', 'Unknown', 'Fog or mist'])
Type_of_collision = st.selectbox("Select Type of Collision", options=['Collision with roadside-parked vehicles', 'Vehicle with vehicle collision', 'Collision with roadside objects', 'Collision with animals', 'Other', 'Rollover', 'Fall from vehicles', 'Collision with pedestrians', 'With Train', 'Unknown', 'nan'])
Number_of_vehicles_involved = st.selectbox("Select Number of Vehicles Involved", options=[2, 1, 3, 6, 4, 7])
Number_of_casualties = st.selectbox("Select Number of Casualties", options=[2, 1, 3, 4, 6, 5, 8, 7])
Vehicle_movement = st.selectbox("Select Vehicle Movement", options=['Going straight', 'U-Turn', 'Moving Backward', 'Turnover', 'Waiting to go', 'Getting off', 'Reversing', 'Unknown', 'Parked', 'Stopping', 'Overtaking', 'Other', 'Entering a junction', 'nan'])
Casualty_class = st.selectbox("Select Casualty Class", options=[None , 'Driver or rider', 'Pedestrian', 'Passenger'])
Sex_of_casualty = st.selectbox("Select Sex of Casualty", options=[None, 'Male', 'Female'])
Age_band_of_casualty = st.selectbox("Select Age Band of Casualty", options=[None, '31-50', '18-30', 'Under 18', 'Over 51', '5'])
Casualty_severity = st.selectbox("Select Casualty Severity", options=[None, '3', '2', '1'])
Work_of_casuality = st.selectbox("Select Work of Casuality", options=['nan', 'Driver', 'Other', 'Unemployed', 'Employee', 'Self-employed', 'Student', 'Unknown'])
Fitness_of_casuality = st.selectbox("Select Fitness of Casuality", options=['nan', 'Normal', 'Deaf', 'Other', 'Blind', 'NormalNormal'])
Pedestrian_movement = st.selectbox("Select Pedestrian Movement", options=['Not a Pedestrian', "Crossing from driver's nearside", 'Crossing from nearside - masked by parked or statioNot a Pedestrianry vehicle', 'Unknown or other', 'Crossing from offside - masked by  parked or statioNot a Pedestrianry vehicle', 'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing)', 'Walking along in carriageway, back to traffic', 'Walking along in carriageway, facing traffic', 'In carriageway, statioNot a Pedestrianry - not crossing  (standing or playing) - masked by parked or statioNot a Pedestrianry vehicle'])
Cause_of_accident = st.selectbox("Select Cause of Accident", options=['Moving Backward', 'Overtaking', 'Changing lane to the left', 'Changing lane to the right', 'Overloading', 'Other', 'No priority to vehicle', 'No priority to pedestrian', 'No distancing', 'Getting off the vehicle improperly', 'Improper parking', 'Overspeed', 'Driving carelessly', 'Driving at high speed', 'Driving to the left', 'Unknown', 'Overturning', 'Turnover', 'Driving under the influence of drugs', 'Drunk driving'])



if button('Predict'):


    predicted_class=prediction(Time, Day_of_week, Age_band_of_driver, Sex_of_driver, Educational_level, Vehicle_driver_relation,
               Driving_experience, Type_of_vehicle, Owner_of_vehicle, Service_year_of_vehicle, Defect_of_vehicle,
               Area_accident_occured, Lanes_or_Medians, Road_allignment, Types_of_Junction, Road_surface_type,
               Road_surface_conditions, Light_conditions, Weather_conditions, Type_of_collision, Number_of_vehicles_involved,
               Number_of_casualties, Vehicle_movement, Casualty_class, Sex_of_casualty, Age_band_of_casualty, Casualty_severity,
               Work_of_casuality, Fitness_of_casuality, Pedestrian_movement, Cause_of_accident)


    if predicted_class[0]==0:
        st.write("Ziada zakhmi nahi hua .......")
    elif predicted_class[0]==1:
        st.write("kafi zakham aye hein par bach gya..")
    else:
        st.write("Halat bhot nazuk hai bas ALLAH se dua kerin....")