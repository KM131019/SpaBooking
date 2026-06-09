import imaplib
import email
import re
import time
from email.header import decode_header

def get_reset_link(gmail, app_password, timeout=120):

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(gmail, app_password)

    start = time.time()
    newest_seen = None

    while time.time()-start < timeout:
        mail.select("inbox")

        # ép Gmail refresh
        mail.noop()
        status, data = mail.search(None, '(UNSEEN SUBJECT "Password Reset Request")')

        ids = data[0].split()

        if ids:
            newest = ids[-1]

            if newest != newest_seen:

                newest_seen = newest

                status,msg = mail.fetch(newest, "(RFC822)")

                raw = msg[0][1]

                email_msg = email.message_from_bytes(raw)

                body=""

                for part in email_msg.walk():

                    if part.get_content_type()=="text/html":

                        body = part.get_payload(
                            decode=True
                        ).decode(errors="ignore")

                link = re.search(r'https://chimmymeowspa\.com[^"\'> ]+', body)

                if link:
                    return link.group()
        time.sleep(5)

    return None