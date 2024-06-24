import mysql.connector
from datetime import datetime

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'anish',
    'password': 'abc123',
    'database': 'oddb'
}

# Function to connect to MySQL and insert data
def insert_od_request(name, rollno, department, fromdate, todate, event):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare INSERT query
        insert_query = """
            INSERT INTO odtable (name, rollno, department, fromdate, todate, event)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Execute the INSERT query with user input
        cursor.execute(insert_query, (name, rollno, department, fromdate, todate, event))
        conn.commit()

        # Close cursor and connection
        cursor.close()
        conn.close()

        print("OD request inserted successfully!")
        
    except mysql.connector.Error as e:
        print(f"Error inserting OD request: {e}")

# Function to check if OD was provided
def check_od_provided(name, rollno, fromdate, todate):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to check if OD was provided
        select_query = """
            SELECT * FROM odtable
            WHERE name = %s AND rollno = %s AND fromdate = %s AND todate = %s
        """
        cursor.execute(select_query, (name, rollno, fromdate, todate))
        result = cursor.fetchone()

        # Close cursor and connection
        cursor.close()
        conn.close()

        if result:
            print("OD provided.")
        else:
            print("OD not provided.")

    except mysql.connector.Error as e:
        print(f"Error checking OD status: {e}")

# Main program flow
if _name_ == "_main_":
    # Take user input
    name = input("Enter name: ")
    rollno = input("Enter roll number: ")
    department = input("Enter department: ")
    fromdate = input("Enter from date (YYYY-MM-DD): ")
    todate = input("Enter to date (YYYY-MM-DD): ")
    event = input("Enter event description: ")

    # Insert OD request
    insert_od_request(name, rollno, department, fromdate, todate, event)

    # Check if OD was provided
    check_od_provided(name, rollno, fromdate, todate)
