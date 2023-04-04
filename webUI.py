#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 17:19:38 2022

@author: srinivaspallapu
"""

import numpy as np
import pickle
import streamlit as st

loaded_model =pickle.load(open('/Users/srinivaspallapu/Documents/5502/Project/trained_model.sav','rb'))


def predictionofsatisfaction(input_data):
    
    input_data_as_np=np.asarray(input_data)
    input_data_reshaped = input_data_as_np.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
        return 'Not Satisfied'
    elif prediction[0]==1:
        return 'Sastified'


def main():
    st.title('Air Passenger Satisfaction Prediction')
    On_board_Service =st.text_input('On-board Service rating ')
    Seat_Comfort =st.text_input('Seat Comfort rating')
    Leg_Room_Service=st.text_input('Leg Room Service rating')
    Cleanliness=st.text_input('Cleanliness rating')
    Food_and_Drink=st.text_input('Food and drink rating')
    In_flight_Service =st.text_input("In-flight Service rating")
    In_flight_Wifi_Service=st.text_input('In-flight Wifi Service rating')
    In_flight_Entertainment=st.text_input('In-flight Entertainment rating')
    Baggage_Handling=st.text_input('Baggage Handling rating')
       
    results= ''
    if st.button('Predict'):
        results = predictionofsatisfaction([On_board_Service,Seat_Comfort,Leg_Room_Service,Cleanliness,Food_and_Drink,In_flight_Service,In_flight_Wifi_Service ,In_flight_Entertainment,Baggage_Handling])
        st.success(results)
           
if __name__=='__main__':
    main()
       
       