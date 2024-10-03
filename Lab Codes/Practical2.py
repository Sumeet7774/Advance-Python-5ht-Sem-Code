import pandas as pd

# Load the datasets
trains_df = pd.read_csv(r'trains.csv')
passenger_df = pd.read_csv(r'Passengers.csv')

# Constants
rate_per_ticket = 1000  # Rate per ticket, assumed constant for simplicity

def check_seat_availability_and_calculate_fare(passengerName, trainId, numTickets):
    global trains_df, passenger_df

    # Find the train by Train ID
    train = trains_df[trains_df['TrainID'] == trainId]
    if train.empty:
        return 'Train ID not found'

    # Get available seats
    available_seats = train.iloc[0]['Available Seats']
    
    if numTickets > available_seats:
        return 'Not Enough Seats Available'
    
    # Calculate the total fare
    total_fare = numTickets * rate_per_ticket
    
    # Update available seats in the trains_df
    trains_df.loc[trains_df['TrainID'] == trainId, 'Available Seats'] -= numTickets
    
    # Add the new booking to passenger_df
    new_booking = pd.DataFrame({
        'PassengerName': [passengerName],
        'TrainID': [trainId],
        'Bookings': [numTickets]
    })
    passenger_df = pd.concat([passenger_df, new_booking], ignore_index=True)

    return f"Booking confirmed for {passengerName}. Total fare: ₹ {total_fare:.2f}"

def generate_train_report():
    # Generate the train report showing train details
    report = trains_df[['TrainID', 'Train Name', 'Source Station', 'Destination Station', 'Total Seats', 'Available Seats']]
    report = report.reset_index(drop=True)
    report.index += 1  # Start serial number from 1
    report = report.rename_axis('Sr No').reset_index()

    # Save the report to a CSV file
    report.to_csv('train_report.csv', index=False)
    
    return report

def generate_revenue_report():
    # Merge passenger_df with train details to calculate revenue
    revenue_df = passenger_df.merge(trains_df[['TrainID', 'Train Name']], on='TrainID', how='left')
    
    # Calculate total revenue per train
    revenue_df['Revenue'] = revenue_df['Bookings'] * rate_per_ticket
    
    # Group by TrainID and Train Name to get total revenue per train
    revenue_report = revenue_df.groupby(['TrainID', 'Train Name'])['Revenue'].sum().reset_index()
    revenue_report = revenue_report.rename(columns={'Revenue': 'Total Revenue'})
    
    # Add a serial number to the report
    revenue_report = revenue_report.reset_index(drop=True)
    revenue_report.index += 1  # Start serial number from 1
    revenue_report = revenue_report.rename_axis('Sr No').reset_index()

    # Save the report to a CSV file
    revenue_report.to_csv('revenue_report.csv', index=False)
    
    return revenue_report

# Sample function calls for output generation:

# Check availability and book tickets for a passenger
print(check_seat_availability_and_calculate_fare('Sunita Reddy', 'T006', 3))
print(check_seat_availability_and_calculate_fare('Rahul Sharma', 'T001', 2))
print(check_seat_availability_and_calculate_fare('Kavita Joshi', 'T008', 2))

# Generate and save the train report to a file
train_report = generate_train_report()
print("\nTrain Report:\n", train_report)

# Generate and save the revenue report to a file
revenue_report = generate_revenue_report()
print("\nRevenue Report:\n", revenue_report)
