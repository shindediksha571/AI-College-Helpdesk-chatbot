import datetime

print("=" * 50)
print("🤖 AI College Helpdesk Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

responses = {
    "admission": "Admissions are open from June to August.",
    "fees": "Please contact the Accounts Office for fee details.",
    "exam": "Exams are conducted at the end of each semester.",
    "result": "Results are available on the college portal.",
    "library": "Library timings are 9:00 AM to 5:00 PM.",
    "hostel": "Hostel facilities are available for boys and girls.",
    "placement": "Placement Cell organizes campus interviews every year.",
    "courses": "We offer B.Tech, M.Tech, MBA and Diploma courses.",
    "contact": "Call us at +91-9876543210 or email: info@college.edu",
    "principal": "You can meet the Principal between 11:00 AM and 1:00 PM.",
    "timing": "College timings are 9:00 AM to 4:30 PM."
}

while True:

    user = input("\nYou : ").lower().strip()

    if user == "bye":
        print("Bot : Thank you! Have a nice day 😊")
        break

    elif "hello" in user or "hi" in user:
        print("Bot : Hello! How can I help you?")

    elif "admission" in user:
        print("Bot :", responses["admission"])

    elif "fees" in user or "fee" in user:
        print("Bot :", responses["fees"])

    elif "exam" in user:
        print("Bot :", responses["exam"])

    elif "result" in user:
        print("Bot :", responses["result"])

    elif "library" in user:
        print("Bot :", responses["library"])

    elif "hostel" in user:
        print("Bot :", responses["hostel"])

    elif "placement" in user:
        print("Bot :", responses["placement"])

    elif "course" in user or "courses" in user:
        print("Bot :", responses["courses"])

    elif "contact" in user:
        print("Bot :", responses["contact"])

    elif "principal" in user:
        print("Bot :", responses["principal"])

    elif "time" in user:
        print("Bot :", responses["timing"])

    elif "date" in user:
        print("Bot : Today's Date is", datetime.date.today())

    elif "thank" in user:
        print("Bot : You're Welcome 😊")

    else:
        print("Bot : Sorry, I don't understand your question.")
        print("Try asking about:")
        print("- Admission")
        print("- Fees")
        print("- Exam")
        print("- Result")
        print("- Library")
        print("- Hostel")
        print("- Placement")
        print("- Courses")
        print("- Contact")
        print("- Principal")
        print("- Timing")
        print("- Date")
