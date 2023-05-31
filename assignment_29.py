# CRUD Operations : 1] C : Create/Insert
#                   2] R : Read/Fetch
#                   3] U : Update
#                   4] D : Delete

import mysql.connector

connection = mysql.connector.connect(
    user="root", password="Sudeep_123", host="localhost", database="csp_login"
)

cursor = connection.cursor()
# query = "CREATE DATABASE csp_login"
# query = "CREATE TABLE user_login_details (email_id varchar(100), password varchar(100))"
# cursor.execute(query)
print("**********************************")
print("---------- LOGIN SYSTEM ----------")
print("**********************************")
while True:
    print("___________________________________")
    print(
        "\t1] New User\n\t2] Login\n\t3] Update User Name\n\t4] Update Password\n\t5] DELETE ACCOUNT\n\t6] Exit"
    )
    print("___________________________________")
    choice = input("Enter Your Choice = ")

    if choice == "1":
        print("\n ---------- SIGN-UP ---------- ")
        email = input("Enter Your E-Mail ID = ")
        password = input("Enter Password = ")
        query = f"INSERT INTO user_login_details (email_id, password) VALUES ('{email}','{password}')"
        cursor.execute(query)
        connection.commit()

    elif choice == "2":
        print("\n ---------- SIGN-IN ----------")
        email = input("Enter Your E-Mail ID = ")
        password = input("Enter Password = ")
        query = f"SELECT 'one' from user_login_details WHERE email_id = '{email}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            for i in result:
                print("Logged-In Successfully")
                break
        else:
            print("INVALID CREDENTIALS")

    elif choice == "3":
        print("\n ---------- UPDATE USER-NAME ----------")
        email = input("Enter Your E-Mail ID = ")
        password = input("Enter Password = ")
        new_email = input("Enter New E-mail ID = ")
        query = f"SELECT * FROM user_login_details"
        cursor.execute(query)
        connection.commit()

    elif choice == "4":
        print("\n ---------- UPDATE PASSWORD ----------")
        email = input("Enter Your E-Mail ID = ")
        password = input("Enter Password = ")
        new_pass = input("Enter New Password ID = ")
        query = f"UPDATE user_login_details SET password = '{new_pass}' WHERE email_id = '{email}'"
        cursor.execute(query)
        connection.commit()

    elif choice == "5":
        print("\n ---------- DELETE ACCOUNT ----------")
        email = input("Enter Your E-Mail ID = ")
        password = input("Enter Password = ")
        query = f"TRUNCATE FROM user_login_details WHERE email_id = '{email}' and password = '{password}'"
        cursor.execute(query)
        connection.commit()

    elif choice == "6":
        print("\n ---------- EXIT ----------")
        break

    else:
        print("Enter A Valid Choice !")
