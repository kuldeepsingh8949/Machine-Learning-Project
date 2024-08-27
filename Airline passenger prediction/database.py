import sqlite3
conn = sqlite3.connect('passengerdata.db')
query_to_create_the_table = """
CREATE TABLE PassengerDetails(
     age INT,
     flight_distance INT,
     inflight_entertainment INT,
     baggage_handling INT,
     cleanliness INT,
     departure_delay INT,
     arrival_delay INT,
     gender VARCHAR(250),
     customer_type INT,
     travel_type INT,
     class_type INT,
     predicted VARCHAR(500)

)
"""



cur = conn.cursor() 
cur.execute(query_to_create_the_table) 
print("Your database and tables is created!")
cur.close() 
conn.close()
