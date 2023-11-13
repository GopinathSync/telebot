import telebot


TOKEN = '6813273007:AAGhjGShknyUrRp5bdoTrZXc4egu2f7HHcs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['todayspecial'])
def handle_start(message):
    bot.send_message(message.chat.id, "TODAY IS DIWALI, HAPPY DIWALI TO U😍")



roll_numbers = ["/1521041001",
              "/1521041004",
              "/1521041006",
              "/1521041007",
              "/1521041010",
              "/1521041012",
              "/1521041013",
              "/1521041014",
              "/1521041016",
              "/1521041019",
              "/1521041020",
              "/1521041021",
              "/1521041022",
              "/1521041023",
              "/1521041025",
              "/1521041026",
              "/1521041028",
              "/1521041035",
              "/1521041036",
              "/1521041038",
              "/1521041042"
              ]


@bot.message_handler(commands=['showrollnumbers'])
def display_roll_numbers(message):
    # Format the roll numbers
    roll_number_info = "\n".join([f"Roll Number: {roll_number}" for roll_number in roll_numbers])

    # Send the roll numbers to the user
    bot.send_message(message.chat.id, f"Roll Numbers:\n{roll_number_info}")


@bot.message_handler(commands=['1521041001'])
def display_students(message):
    aknish = [
        {'name': 'Aknishwaran', 'age': 18, 'roll no': 1521041001}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in aknish])
    bot.send_message(message.chat.id, f" IAM 1ST IN YOUR CLASS LIST:\n{student_info}")


@bot.message_handler(commands=['1521041004'])
def display_students(message):
    giri = [
        {'name': 'Giriraj', 'age': "--", 'roll no': 1521041004}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in giri])
    bot.send_message(message.chat.id, f"IT'S ME:\n{student_info}")


@bot.message_handler(commands=['1521041006'])
def display_students(message):
    gopi = [
        {'name': 'Gopinath', 'age': 18, 'roll no': 1521041006}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in gopi])
    bot.send_message(message.chat.id, f"NOT HUMAN:\n{student_info}")


@bot.message_handler(commands=['1521041007'])
def display_students(message):
    gowtham = [
        {'name': 'Gowtham', 'age': 18, 'roll no': 1521041007}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\n Age: {student['age']}, \nRoll no: {student['roll no']}" for student in gowtham])
    bot.send_message(message.chat.id, f"ERROR 404:\n{student_info}")


@bot.message_handler(commands=['1521041010'])
def display_students(message):
    harish = [
        {'name': 'Harish', 'age': 18, 'roll no': 1521041010}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in harish])
    bot.send_message(message.chat.id, f"IAM KOLARU:\n{student_info}")


@bot.message_handler(commands=['1521041012'])
def display_students(message):
    kalai = [
        {'name': 'Kalai', 'age': 18, 'roll no': 15210410012}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in kalai])
    bot.send_message(message.chat.id, f" INVAILED USERS:\n{student_info}")


@bot.message_handler(commands=['1521041013'])
def display_students(message):
    kamalesh = [
        {'name': 'Kamalesh', 'age': 18, 'roll no': 15210410013}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']},\nRoll no:{student['roll no']}" for student in kamalesh])
    bot.send_message(message.chat.id, f" DEFINE YOU????:\n{student_info}")


@bot.message_handler(commands=['1521041014'])
def display_students(message):
    karikala = [
        {'name': 'Karikala', 'age': 18, 'roll no': 15210410014}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']},\n Roll no: {student['roll no']}" for student in karikala])
    bot.send_message(message.chat.id, f"ABOUT PARAMBARIYA VILAIYATTU FOUNDER:\n{student_info}")


@bot.message_handler(commands=['1521041016'])
def display_students(message):
    krithick = [
        {'name': 'krithick', 'age': 18, 'roll no': 1521041016}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in krithick])
    bot.send_message(message.chat.id, f" ABOUT APPLE LOVER:\n{student_info}")


@bot.message_handler(commands=['1521041019'])
def display_students(message):
    mathew = [
        {'name': 'Mathew', 'age': 18, 'roll no': 1521041019}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\n Age: {student['age']}, \nRoll no: {student['roll no']}" for student in mathew])
    bot.send_message(message.chat.id, f"ABOUT IDFC MATH U:\n{student_info}")


@bot.message_handler(commands=['1521041020'])
def display_students(message):
    ajmal = [
        {'name': 'Ajmal', 'age': 18, 'roll no': 1521041020}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in ajmal])
    bot.send_message(message.chat.id, f"ABOUT PHOTOGRAPHER:\n{student_info}")


@bot.message_handler(commands=['1521041021'])
def display_students(message):
    arshath = [
        {'name': 'Arshath', 'age': 18, 'roll no': 15210410021}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in arshath])
    bot.send_message(message.chat.id, f"ABOUT REENA BF:\n{student_info}")


@bot.message_handler(commands=['1521041022'])
def display_students(message):
    basith = [
        {'name': 'Basith', 'age': 18, 'roll no': 15210410022}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in basith])
    bot.send_message(message.chat.id, f"ABOUT AAAAHHHH:\n{student_info}")


@bot.message_handler(commands=['1521041023'])
def display_students(message):
    faizal = [
        {'name': 'Faizal', 'age': 18, 'roll no': 15210410023}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\n Age: {student['age']}, \nRoll no: {student['roll no']}" for student in faizal])
    bot.send_message(message.chat.id, f"ABOUT YOU:\n{student_info}")


@bot.message_handler(commands=['1521041025'])
def display_students(message):
    adhil = [
        {'name': 'Adil', 'age': 18, 'roll no': 1521041025}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\n Age: {student['age']}, \nRoll no: {student['roll no']}" for student in adhil])
    bot.send_message(message.chat.id, f"ABOUT LEGEND:\n{student_info}")


@bot.message_handler(commands=['1521041026'])
def display_students(message):
    murali = [
        {'name': 'Murali', 'age': 18, 'roll no': 1521041026}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in murali])
    bot.send_message(message.chat.id, f"ABOUT UTHAMAN:\n{student_info}")


@bot.message_handler(commands=['1521041028'])
def display_students(message):
    raj = [
        {'name': 'RajKumar', 'age': 18, 'roll no': 15210410028}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']},\n Roll no: {student['roll no']}" for student in raj])
    bot.send_message(message.chat.id, f"ABOUT MADURAI BOY:\n{student_info}")


@bot.message_handler(commands=['1521041035'])
def display_students(message):
    gokul = [
        {'name': 'Gokul', 'age': 18, 'roll no': 15210410035}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in gokul])
    bot.send_message(message.chat.id, f"ABOUT BABY:\n{student_info}")


@bot.message_handler(commands=['1521041036'])
def display_students(message):
    sriram = [
        {'name': 'Sriram', 'age': 18, 'roll no': 1521041036}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in sriram])
    bot.send_message(message.chat.id, f"GAMER:\n{student_info}")


@bot.message_handler(commands=['1521041038'])
def display_students(message):
    tamil = [
        {'name': 'Tamil', 'age': 18, 'roll no': 15210410038}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in tamil])
    bot.send_message(message.chat.id, f" ABOUT THAMBAKEDA:\n{student_info}")


@bot.message_handler(commands=['1521041042'])
def display_students(message):
    muruga = [
        {'name': 'Vignesh Muruga', 'age': 18, 'roll no': 15210410042}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in muruga])
    bot.send_message(message.chat.id, f"ABOUT MAMA:\n{student_info}")


@bot.message_handler(commands=['1521041033'])
def display_students(message):
    sasi = [
        {'name': 'Sasi', 'age': 18, 'roll no': 15210410033}
    ]
    student_info = "\n".join(
        [f"{student['name']} - \nAge: {student['age']}, \nRoll no: {student['roll no']}" for student in sasi])
    bot.send_message(message.chat.id, f"ABOUT SASI:\n{student_info}")


@bot.message_handler(commands=['1521041031'])
def display_students(message):
    chandu = [
        {'name': 'Chandu', 'age': 18, 'roll no': 15210410031}
    ]
    student_info = "\n".join(
        [f"{student['name']} -\n Age: {student['age']}, \nRoll no: {student['roll no']}" for student in chandu])
    bot.send_message(message.chat.id, f"ABOUT CHANDU:\n{student_info}")


# Start the bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
