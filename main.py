from datetime import datetime
import pandas
import random
import smtplib

my_email = "pythonwinnersingh@gmail.com"
password = "knsxkdtddwzhezab"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row.day, data_row.month): data_row for (index, data_row) in data.iterrows()}
try:
    if today_tuple in birthday_dict:
        birthday_person = birthday_dict[today_tuple]
        file_path = f"Letter_templates/letter_{random.randint(1,3)}.txt"

        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject: Happy Birthday\n\n{contents}"
                                )

except:
    print("connection error.")

else:
    print("Email sent successfully.")




