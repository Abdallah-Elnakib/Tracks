import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Bdallh1722",
  database="python_track"
)

mycursor = mydb.cursor()



# sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
# val = ("abdallah", "123456789", 'admin')
# mycursor.execute(sql, val)

# mydb.commit()


# usernameFromUser = input('Please Enter Username : ')
# passwordFromUser = input('Please Enter Password : ')
# roleFromUser = input('Please Enter Role : ')


# sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
# val = (usernameFromUser, passwordFromUser, roleFromUser)
# mycursor.execute(sql, val)

# mydb.commit()


