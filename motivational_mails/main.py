import os
import random
import smtplib
from email.message import EmailMessage
from pathlib import Path

MY_MAIL = os.environ["MY_MAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

BASE_DIR = Path(__file__).resolve().parent
QUOTES_FILE = BASE_DIR / "motivational_quotes.txt"
RECIPIENTS_FILE = BASE_DIR / "recipients.txt"


def read_lines(path):
    """Return non-empty lines, skipping comments that start with #."""
    with open(path, encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.strip().startswith("#")
        ]


def main():
    quotes = read_lines(QUOTES_FILE)
    recipients = sorted(set(read_lines(RECIPIENTS_FILE)))  # removes duplicates

    quote = random.choice(quotes)  # same quote for everyone this week
    sent, failed = 0, []

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)

        for address in recipients:
            msg = EmailMessage()
            msg["Subject"] = "Quote"
            msg["From"] = MY_MAIL
            msg["To"] = address
            msg.set_content(quote)

            try:
                connection.send_message(msg)
                sent += 1
                print(f"Sent to {address}")
            except Exception as e:
                failed.append(address)
                print(f"FAILED for {address}: {e}")

    print(f"Done. Sent: {sent}, Failed: {len(failed)}")
    if failed:
        raise SystemExit(1)  # marks the workflow run as failed so you notice


if __name__ == "__main__":
    main()
