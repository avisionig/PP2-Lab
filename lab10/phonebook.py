import psycopg2 

def add_user():
    add = input().split()
    postgre_query = """INSERT INTO phonebook( user_name, phonenumber) VALUES (%s, %s) """
    data_toinsert = (add[0], add[1])
    cursor.execute(postgre_query, data_toinsert)

    conn.commit()
    print("Data added!")

def update():
    print("Type who's number you want to change")
    name = input()
    print("New number")
    number = input()
    postgre_query = """UPDATE phonebook SET phonenumber = %s WHERE user_name = %s """
    cursor.execute(postgre_query, (number, name))
    
    conn.commit()
    print("Data updated!")

def delete_user():
    print("Insert name you want to delete")
    name = input()
    postgre_query = """DELETE FROM phonebook WHERE user_name = %s """
    cursor.execute(postgre_query, (name,))
    
    conn.commit()
    print("Data deleted!")
try:
    cond = False
    conn = psycopg2.connect("dbname=postgres user=postgres password=1994almaZ_")
    cursor = conn.cursor()

    while not cond:
        print("\nChoose action:\n1.Add user and number\n2.Change number of existing user\n3.Delete user\n4.Exit")
        action=input()
        if action == '1':
            print("Insert data")
            add_user()
        elif action == '2':
            update()
        elif action == '3':
            delete_user()
        elif action == '4':
            cond = True 

except psycopg2.Error as e:
        print("Failed!")

finally:
    cursor.close()
    conn.close()
    print("Connection closed!")
