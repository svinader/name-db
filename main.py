
import sqlite3

# Create or connect to the database
conn = sqlite3.connect('names.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS names (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    amount INTEGER NOT NULL
)''')

# Function to execute SQL file
#     with open(file_path, 'r') as sql_file:
#         sql_script = sql_file.read()
#         cursor.executescript(sql_script)
#     conn.commit()

while True:
    print("\n")
    print("1. Parādīt visus vārdus")
    print("2. Meklēt pēc vārda")
    print("3. Atlasīt top 5 vārdus pēc populāritātes")
    print("4. Parādīt kopējo vārdu skaitu pēc dzimuma")
    print("5. Parādīt vidējo vārdu skaitu pēc dzimuma")
    print("6. Parādīt vārdus pēc daudzuma")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        offset = 0
        limit = 10
        while True:
            cursor.execute("SELECT * FROM names LIMIT ?, ?", (offset, limit))
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
            if input("Proceed? y/n") == 'n':
                break;
            offset += limit
    if choice == '2':
        name = input("Ievadi vārdu: ")
        cursor.execute("SELECT * FROM names WHERE name=?", (name,))
        result = cursor.fetchall()
        if result:
            print("Name found:")
            for row in result:
                print(row)
    elif choice == '3':
        # atlasīt top 5 vārdus pēc populāritātes
        # https://www.w3schools.com/sql/sql_orderby.asp (ORDER BY)
        # https://www.w3schools.com/sql/sql_top.asp (LIMIT)
        pass
    elif choice == '4':
        gender = input("Ievadi VĪRIETIS/SIEVIETE: ")
        # Parādīt kopējo vārdu skaitu pēc dzimuma
        # https://www.w3schools.com/sql/sql_count.asp (COUNT)
        # https://www.w3schools.com/sql/sql_where.asp (WHERE)
    elif choice == '5':
        gender = input("Ievadi VĪRIETIS/SIEVIETE: ")
        # Parādīt vidējo vārdu skaitu pēc dzimuma
        # https://www.w3schools.com/sql/sql_avg.asp (AVG)
        # https://www.w3schools.com/sql/sql_where.asp (WHERE)
    elif choice == '6':
        amount = input("Ievadi daudzumu: ")
        # Parādīt vārdus pēc daudzuma
        # https://www.w3schools.com/sql/sql_where.asp (WHERE)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please enter a valid option.")


# Close connection
conn.close()