# -*- encoding: utf-8 -*-
import sqlite3
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
print(one, two, three, four)

if one == "None" or one == None:
    pass
else:
    def send_email():
        email = "mikolaenko.arina@gmail.com"
        for i in range(len(receivers_email)):
            cur.execute("""SELECT name FROM forma_enter
                """)
            names = cur.fetchall()
            if i != len(receivers_email) - 1:
                print(names[i + 1][0])
                name_send = names[i + 1][0]
            else:
                name_send = names[0][0]
            receiver_email = receivers_email[i]
            name = receivers_name[i][0]
            msg = MIMEMultipart("alternative")
            msg["Subject"] = "Тайный Санта"
            part1 = MIMEText(f"Здравстуйте {name}, Вы принимаете участие в Тайном Санте! Вы дарите подарок человеку с "
                            f"именем {name_send}", "plain", "utf-8")
            msg.attach(part1)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, "dief gsgx giww zwvs")
            server.sendmail(email, receiver_email, msg.as_string().encode('ascii'))



    with sq.connect("hidden_santa.db", timeout=30) as con:
        cur = con.cursor()

        if four != "None" and four != None:
            cur.execute("""CREATE TABLE IF NOT EXISTS forma_enter(
                    name TEXT,
                    creator_email TEXT,     
                    email_rel TEXT,
                    creator_password TEXT
            )""")

        elif three != "None" and three != None:
            cur.execute("""CREATE TABLE IF NOT EXISTS forma_reg (
                name TEXT, 
                creator_password TEXT,
                creator_email TEXT
            )""")
        elif two != "None" and two != None:
            cur.execute("""SELECT email_rel FROM forma_enter
                """)
            receivers_email = cur.fetchall()
            cur.execute("""SELECT name FROM forma_enter""")
            receivers_name = cur.fetchall()

            for k in range(len(receivers_email)):
                cur.execute("SELECT creator_email FROM forma_enter")
                current_email = cur.fetchall()[k]
                cur.execute("SELECT creator_password FROM forma_enter")
                current_password = cur.fetchall()[k]
                if one == current_email and two == current_password:
                    send_email()

        #     for j in range(len(receivers_email)):
        #         for i in range(len(receivers_email) - 1):
        #             creators_email = cur.execute("SELECT creator_email from forma_enter")
        #             creator_email_by_user = cur.fetchall()[i]
        #
        #             email_cr_reg = cur.execute("SELECT creator_email from forma_reg")
        #             email_cr_reg_adm = cur.fetchall()[i]
        #
        #             creators_passwords = cur.execute("SELECT creator_password from forma_enter")
        #             creator_pass_user = cur.fetchall()[i]
        #
        #             passwords_cr_reg = cur.execute("SELECT creator_password from forma_reg")
        #             pass_cr_reg = cur.fetchall()[i]
        #
        #             if (creator_email_by_user == email_cr_reg_adm) and (creator_pass_user == pass_cr_reg):
        #                 send_email()
        #             else:
        #                 continue
            else:
                pass



