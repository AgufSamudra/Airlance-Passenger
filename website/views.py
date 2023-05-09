from flask import Blueprint, render_template, request
import pandas as pd
import pickle

views = Blueprint('views', __name__)

dir = '../model/final_model_airlance.pkl'
with open(dir, "rb") as file:
    model = pickle.load(file)

@views.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        # Get form data from the request
        gender = request.form['gender']
        customer_type = request.form['customer_type']
        age = int(request.form['age'])
        travel_type = request.form['travel_type']
        clas = request.form['class']
        flight_distance = int(request.form['flight_distance'])
        inflight_wifi = int(request.form['inflight_wifi'])
        time_convenience = int(request.form['time_convenience'])
        online_booking = int(request.form['online_booking'])
        food_and_drink = int(request.form['food_and_drink'])
        online_boarding = int(request.form['online_boarding'])
        seat_comfort = int(request.form['seat_comfort'])
        inflight_entertainment = int(request.form['inflight_entertainment'])
        on_board_service = int(request.form['on_board_service'])
        checkin_service = int(request.form['checkin_service'])
        inflight_service = int(request.form['inflight_service'])
        cleanliness = int(request.form['cleanliness'])
        depature_delay = int(request.form['departure_delay'])
        arrival_delay = int(request.form['arrival_delay'])

        columns = ['Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',
                   'Flight Distance', 'Inflight wifi service',
                   'Departure/Arrival time convenient', 'Ease of Online booking',
                   'Food and drink', 'Online boarding', 'Seat comfort',
                   'Inflight entertainment', 'On-board service', 'Checkin service',
                   'Inflight service', 'Cleanliness', 'Departure Delay in Minutes',
                   'Arrival Delay in Minutes']

        # Transform the form data into a feature vector for prediction
        X = pd.DataFrame([[gender, customer_type, age, travel_type, clas, flight_distance, inflight_wifi, time_convenience, online_booking, food_and_drink,
              online_boarding, seat_comfort, inflight_entertainment, on_board_service, checkin_service, inflight_service, cleanliness,
              depature_delay, arrival_delay]], columns=columns)

        if model.predict(X) != 0:
            print("Customer Puas")
            result = "Customer Puas"
        else:
            print("Customer Tidak Puas")
            result = "Customer Tidak Puas"

        return result
