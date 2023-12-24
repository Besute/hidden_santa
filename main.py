# -*- encoding: utf-8 -*-
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sqlite3 as sq

one, two, three, four = None, None, None, None
if len(sys.argv) >= 2:
    one = sys.argv[1]
if len(sys.argv) >= 3:
    two = sys.argv[2]
if len(sys.argv) >= 4:
    three = sys.argv[3]
if len(sys.argv) >= 5:
    four = sys.argv[4]
print(str(one), str(two), str(three), str(four))

with sq.connect("hidden_santa.db", timeout=30) as con:  # подключаем базу данных
    cur = con.cursor()

    if four != "None" and four is not None:
        cur.execute("""CREATE TABLE IF NOT EXISTS forma_enter (
                name TEXT,
                creator_email TEXT,     
                email_rel TEXT,
                creator_password TEXT
        )""")
        cur.execute(
            f"""INSERT INTO forma_enter (name, creator_email, email_rel, creator_password) VALUES ("{one}", "{two}", "{three}", "{four}")""")
    elif three != "None" and three is not None:
        cur.execute("""CREATE TABLE IF NOT EXISTS forma_reg (
            name TEXT, 
            creator_password TEXT,
            creator_email TEXT
        )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS forma_enter (
                name TEXT,
                creator_email TEXT,     
                email_rel TEXT,
                creator_password TEXT
        )""")
        cur.execute(
            f"""INSERT INTO forma_reg (name, creator_password, creator_email) VALUES ("{one}", "{two}", "{three}")""")
        cur.execute(
            f"""INSERT INTO forma_enter (name, creator_email, email_rel, creator_password) VALUES ("{one}", "{three}", "{three}", "{two}")""")
    elif two != "None" and two is not None:
        cur.execute("""SELECT email_rel FROM forma_enter""")
        receivers_email = cur.fetchall()
        cur.execute("""SELECT name FROM forma_enter""")
        receivers_name = cur.fetchall()

        email = "mikolaenko.arina@gmail.com"
        cur.execute("SELECT creator_password from forma_enter")
        passwords = cur.fetchall()  # все creator_password из таблицы forma_reg
        cur.execute("SELECT creator_email from forma_enter")
        creator_emails = cur.fetchall()  # все creator_email из таблицы forma_reg
        cur.execute("""SELECT name FROM forma_enter""")
        names = cur.fetchall()  # все name из таблицы forma_enter
        for i in range(len(receivers_email)):  # цикл по всем участникам которые есть в таблице forma_enter
            if one == creator_emails[i][0] and two == passwords[i][0]:  # проверяем, что логин и пароль совпадают
                # с логином и паролем создателя
                if i != len(receivers_email) - 1:  # проверяем, что мы на на последнем элементе (то есть у нас нет
                    # следующего человека которому нужно отправить,
                    # поэтому отправим первому)
                    name_send = names[i + 1][0]
                else:
                    name_send = names[0][0]  # имя получателя будет самым первым именем
                receiver_email = receivers_email[i][0]
                name = receivers_name[i][0]
                msg = MIMEMultipart("alternative")
                msg["Subject"] = "Тайный Санта"
                part1 = MIMEText(
                    f"Здравстуйте {name}, Вы принимаете участие в Тайном Санте! Вы дарите подарок человеку с "
                    f"именем {name_send}", "plain", "utf-8")
                msg.attach(part1)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, "dief gsgx giww zwvs")
                print('All is done')
                server.sendmail(email, receiver_email, msg.as_string().encode('ascii'))
                cur.execute(
                    f"""DELETE FROM forma_enter WHERE name = '{name}'AND email_rel = '{receiver_email}'""")
        cur.execute(
            f"""DELETE FROM forma_reg WHERE creator_email = '{one}'"""
        )
    # удаляем всю строку бд по айди
    else:
        pass
