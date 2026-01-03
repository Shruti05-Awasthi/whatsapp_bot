from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! API chal rahi hai 👍"

@app.route("/webhook", methods=["POST"])
def webhook():
    msg = request.values.get("Body", "").strip().lower()

    resp = MessagingResponse()

    if msg in ["hi", "hello", "start"]:
        resp.message(
            "Hi 👋\n"
            "Choose category:\n"
            "Friends\n"
            "Family\n"
            "Mentor\n"
            "Job\n"
            "Unknown"
        )

    elif msg == "friends":
        resp.message("Friends selected ✅\nAvailable slot: 9PM–10PM")

    elif msg == "family":
        resp.message("Family selected ✅\nAvailable slot: 8PM–9PM")

    elif msg == "mentor":
        resp.message("Mentor selected ✅\nI will contact you soon")

    elif msg == "job":
        resp.message("Job related ✅\nI will contact you soon")

    elif msg == "unknown":
        resp.message("Please specify reason:\nFather\nOther")

    elif msg == "father":
        resp.message("Unknown (Father reference) ✅\nSlot: 9PM–10PM")

    elif msg == "other":
        resp.message("Unknown (Other reason) ✅\nPlease specify purpose")

    else:
        resp.message("Invalid input ❌\nType hi to start")

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
