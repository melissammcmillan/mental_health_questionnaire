# Import libraries
import streamlit as st
import pandas as pd
#import plotly.express as px
import numpy as np
from datetime import datetime

# Read in the historical data for the user so we can append the new track
pump_data = pd.read_csv('../Data/User1_Pumping_Dataset.csv', index_col = 0)
nurse_data = pd.read_csv('../Data/User1_Direct_Nursing_Dataset.csv', index_col = 0)
supp_data = pd.read_csv('../Data/User1_Supplement_Dataset.csv', index_col = 0)

# First step is for users to build their profile.
# Welcome and Introduction
st.header('Welcome to LactationBuddy!')
st.subheader("Let's get tracking!")

#st.subheader("We'll get to tracking in a moment, first, we'd like to learn more about you.")

# Collect a series of entries from the users, add them to a dictionary, then
# add the dictionary to a database for long term storage.

# Start with an empty dictionary
#user_dict = dict()

# We'll want our new user to add things like First name, Last name, pick a username,
# check if the username is already taken, email, password, and DOB.

# I've decided that the names for the dictionary keys will be firstname, lastname,
# username, email, password, dob
#st.write('What is your first name?')
#user_dict['firstname'] = st.text_input('First Name')

#st.write('What is your last name?')
#user_dict['lastname'] = st.text_input("Last Name")

#st.write('What is your Date of Birth? Please use format mm/dd/yyyy')
#user_dict['dob'] = st.text_input("mm/dd/yyyy")

#st.write('Please select a username.')
#new_username = st.text_input("username")

# Check master dataframe/database to see if that username already exists.
# if new_username in dataframe, st.write('That username is already taken,
    #please choose another name.'); else user_dict['username'] = new_username

#st.write('What is your email address?')
#new_email = st.text_input("email")

# Check master dataframe/database to see if that username already exists.
# if new_email in dataframe, st.write('That email is already in our database,
    #please go to our login page to sign in.'); else user_dict['email'] = new_email

# st.write('Please select a password of 8 characters including letters and numbers.')
# user_dict['password'] = st.text_input("password")

# st.subheader('Now we would like to learn about your lactation process.')
#
# st.write('Do you nurse directly, pump exclusively, or do a combination of both direct nursing and pumping?')
# st.selectbox('Select a Category', ['Nurse Directly', 'Pump Exclusively', 'Combo of Both'])
#
# st.subheader('Next, we would like to learn about the sweet baby you are making milk for.')
# st.write("If you aren't making milk for any one baby in particular, you'll be able to make that selection next.")
#
# # Collect information about baby
# st.write('Would you like to add information about baby? We will use this information for tracking purposes only.')
# user_select = st.selectionbox('Select yes or no.', ['Yes', 'No'])
#
# if user_select == 'Yes':
#     # Create empty dictionary for baby
#     user_baby_dict = dict()
#     # Obtain baby's name
#     st.write("What is your baby's name?")
#     user_baby_dict['babyname'] = st.text_input("Baby Name")
#     # Obtain baby's age
#     st.write("What is your baby's age?")
#     baby_years = int(st.selectionbox('Select years', [0, 1]))
#     baby_months = int(st.selectionbox('Select months', [0,1,2,3,4,5,6,7,8,9,10,11]))
#     baby_weeks = int(st.selectionbox('Select weeks', [0,1,2,3,4]))
#     if baby_weeks == 0:
#         baby_days = int(st.selectionbox('Select days', [1,2,3,4,5,6]))
#     user_baby_dict['babyage'] = [baby_years, baby_months, baby_weeks, baby_days]
#     # Obtain baby's most recent weight
#     st.write('How much does your baby weigh?')
#     st.write('You can either take a guess for how much they weigh now or put in their weight at the last weigh-in.')
#     weight_selection = st.selectionbox('Select your option.', ["Today's weight", "Last weigh-in"])
#     if weight_selection == "Today's weight":
#         weight_pounds = int(st.selectionbox('Select pounds', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
#         weight_ounces = int(st.selectionbox('Select ounces', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#
#
# st.write("Great, thank you for all of this information. Let's get to tracking!")

# I need to make functions for each of those activities.

# Function for tracking a pumping Session
def record_pumping():
    """ This function will prompt the user for necessary information and create a
    database entry for that session.

    Arguments: none.

    Returns: Summary of pumping entry
    """

    # Define the empty dictionary that will become the database entry
    pump_session = {}

    # Get the date for the pump session
    st.write("What is the date of the session you would like to track? If you would like to enter today's date, leave the date field blank.")
    track_date = st.date_input("Enter the date as format yyyy/mm/dd.",)
    pump_session['Date'] = track_date

    # Get the time for the pump Session
    st.write("What is the time of the session you would like to track?")
    track_time = st.time_input("Enter the time as format HH, MM in military time.",)
    pump_session['Time'] = track_time

    # Get the duration of the pump session.
    st.write('How long was the pump session in minutes?')
    pump_session['Duration'] = st.text_input("Minutes")

    # Find out if this was a pump session or not.
    is_power_pump = st.selectbox('Was this a Power Pump?', ['No', 'Yes'])
    pump_session['Power Pump'] = is_power_pump

    # Obtain total volume pumped from user
    st.write("How much volume did you pump during that session? Please report in milliliters (mL)")

    volume_ml = st.number_input('Enter milliliters (mL)')
    num_ounces = 0
    num_ml = 0

    if volume_ml > 29:
        num_ounces = volume_ml // 30
        num_ml = volume_ml % 30
    else:
        num_ml = volume_ml

#    volume = st.selectbox('Would you like to report that volume in ounces, milliliters, or a combination of both?', ['ounces', 'mL', 'Combo of Both'])

    # volume_ounces = 0
    # volume_ml = 0
    # num_ounces = 0
    # num_ml = 0
    #
    # if volume == 'Combo of Both':
    #     volume_ounces = int(st.selectbox('Select ounces', [0,1,2,3,4,5,6,7,8,9,10,11]))
    #     volume_ml = int(st.text_input('Enter milliliters (mL)'))
    # elif volume == 'ounces':
    #     volume_ounces = int(st.selectbox('Select ounces', [0,1,2,3,4,5,6,7,8,9,10,11]))
    # else:
    #     volume_ml = int(st.text_input('Enter milliliters (mL)'))
    #
    # if volume_ml > 29:
    #     num_ounces = volume_ml / 30
    #     num_ml = volume_ml % 30
    #
    # total_ounces = volume_ounces + num_ounces
    # total_ml     = volume_ml + num_ml

    pump_session['Volume'] = volume_ml

    # Eventually get the day of week from the user's input of date
    #import calendar
    #curr_date = date.today()
    #print(calendar.day_name[curr_date.weekday()])
    #st.write(f"You have entered the following pump session details: Date = {pump_session['Date']}, Time = {pump_session['Time']}, Duration = {pump_session['Duration']}, Power Pump = {pump_session['Power Pump']}")
    #st.write(f"You have entered the following pump session details: Date = {pump_session['Date']}, Time = {pump_session['Time']}, Duration = {pump_session['Duration']}, Power Pump = {pump_session['Power Pump']}, Volume = {volume_ml} mL")
    st.write(f"You have entered the following pump session details: Date = {pump_session['Date']}, Time = {pump_session['Time']}, Duration = {pump_session['Duration']}, Power Pump = {pump_session['Power Pump']}, Volume = {num_ounces} oz, {num_ml} mL")
    return(pump_session)

# Function for tracking a nursing Session
def record_nurse_session():
    """ This function will prompt the user for necessary information and create a
    database entry for that session.

    Arguments: none.

    Returns: Summary of nursing entry
    """

    # Define the empty dictionary that will become the database entry
    nurse_session = {}

    # Get the date for the nurse session
    st.write("What is the date of the session you would like to track? If you would like to enter today's date, leave the date field blank.")
    track_date = st.date_input("Enter the date as format yyyy/mm/dd.")
    nurse_session['Date'] = track_date

    # Get the time for the nurse session
    st.write("What is the time of the session you would like to track?")
    track_time = st.time_input("Enter the time as format HH, MM in military time.")
    nurse_session['Time'] = track_time

    # Get the duration of the nurse session.
    st.write('How long was the nurse session in (total) minutes?')
    nurse_session['Duration'] = st.text_input("Minutes")

    # Obtain qualitative information on baby
    st.write("Now let's get some information on the baby and their behavior during this session.")

    # Was baby fussy?
    fussy = st.selectbox('Was baby fussy during this session as a result of milk flow, hunger, etc?', ['No', 'Yes'])
    nurse_session['was_fussy'] = fussy

    # Did baby seem satisfied from the nursing session?
    satisfied = st.selectbox('Did baby seem satisfied from this nursing session?', ['No', 'Yes'])
    nurse_session['was_satisfied'] = satisfied

    # Prefer one side vs another?
    side_preference = st.selectbox('Did baby nurse on one breast/side over another during this session?', ['Left', 'Right', 'Both', 'NA'])
    nurse_session['side_preference'] = side_preference

    # Did baby fall asleep as a result of this nursing session?
    fell_asleep = st.selectbox('Did baby fall asleep as a result of this nursing session?', ['No', 'Yes'])
    nurse_session['fell_asleep'] = fell_asleep

    # Return summary of nurse_session
    st.write(f"You have entered the following nurse session details. Date = {nurse_session['Date']}, Time = {nurse_session['Time']}, Duration = {nurse_session['Duration']} minutes, Was fussy? = {nurse_session['was_fussy']}, Was satisfied? = {nurse_session['was_satisfied']}, Side preference = {nurse_session['side_preference']}, Fell asleep = {nurse_session['fell_asleep']}")
    return(nurse_session)

# Function for tracking a supplement
def record_supplement():
    """ Thid function will prompt the user for necessary information and create a
    database entry for the supplement taken.

    Arguments: none.

    Returns: Summary of supplement entry
    """

    # Define the empty dictionary that will become the database entry
    supp_track = {}

    # Get the date for the supplement taken
    st.write("What date did you take the supplement on? If you would like to enter today's date, leave the date field blank.")
    track_date = st.date_input("Enter the date as format yyyy/mm/dd.")
    supp_track['Date'] = track_date

    # Get the time for the nurse session
    st.write("What time did you take the supplement?")
    track_time = st.time_input("Enter the time as format HH, MM in military time.")
    supp_track['Time'] = track_time

    # Which supplement was taken?
    st.write('Which supplement did you take?')
    supp_track['Supplement'] = st.text_input("Name of supplement")

    # What is the dosage or quantity of the supplement taken?
    st.write('What was the dosage or quantity of the supplement taken?')
    supp_track['Quantity'] = st.text_input('Numerical portion of dosage.')
    supp_track['Units'] = st.text_input('Units of supplement (e.g. mg, ounces, pills, etc)')

    # Return summary of supplement taken
    st.write(f"You have entered the following supplement details: Date = {supp_track['Date']}, Time = {supp_track['Time']}, Supplement = {supp_track['Supplement']}, Amount = {supp_track['Quantity']} {supp_track['Units']}")

     # Add some control flow here to ensure there is no missing data
    empty_supp_df = pd.DataFrame(columns = ['Date', 'Time', 'Supplement', 'Quantity', 'Units'])
    supp_df = empty_supp_df.append(supp_track, ignore_index = True)
    missing_entries = 0
    for idx, row in enumerate(supp_df.isna().sum()):
        if supp_df.isna().sum()[idx] > 0:
            missing_entries += 1
            st.write(f"missing entries = {missing_entries}")

    if missing_entries > 0:
        st.write(f"Your tracking session isn't ready for saving yet as you have {missing_entries} empty fields.")
    else:
        st.write("Your tracking session is ready for saving.")
    # for i in range(0, len(new_pump_session.columns()):
    #     if new_pump_session[col] != NA:
    #         continue
    #     else:
    #         print(f"You are missing an entry for new_pump_session[col]")

    return(supp_df)

# Get activity to track from the user
st.subheader('What are we tracking?')
track_activity = st.selectbox('Select an Activity', ['Pump Session', 'Nurse Session', 'Supplement Taken'])

# Append to existing dataset for that user
if track_activity == 'Nurse Session':
    new_nurse_session = record_nurse_session()
    nurse_data = nurse_data.append(new_nurse_session, ignore_index = True)
    nurse_data.to_csv('../Data/User1_Direct_Nursing_Dataset.csv')
elif track_activity == 'Pump Session':
    new_pump_session = record_pumping()
    pump_data = pump_data.append(new_pump_session, ignore_index = True)
    pump_data.to_csv('../Data/User1_Pumping_Dataset.csv')
else:
    new_supp_track = record_supplement()
    supp_data = supp_data.append(new_supp_track, ignore_index = True)
    supp_data.to_csv('../Data/User1_Supplement_Dataset.csv')
