# Import smtplib for the actual sending function
# https://realpython.com/python-send-email/
import smtplib, ssl
from email.message import EmailMessage

def send_email(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    msg = EmailMessage()
    msg.set_content("body1")
    msg['Subject'] = "Subject1"
    msg['From'] = "svenViking"
    msg['To'] = "stuffofsven@gmail.com"
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_email('Hello test1')

# # Import smtplib for the actual sending function
# import smtplib  https://docs.python.org/3/library/email.examples.html
#
# # And imghdr to find the types of our images
# import imghdr
#
# # Here are the email package modules we'll need
# from email.message import EmailMessage
#
# # Create the container email message.
# msg = EmailMessage()
# msg['Subject'] = 'Our family reunion'
# # me == the sender's email address
# # family = the list of all recipients' email addresses
# msg['From'] = me
# msg['To'] = ', '.join(family)
# msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
#
# # Open the files in binary mode.  Use imghdr to figure out the
# # MIME subtype for each specific image.
# for file in pngfiles:
#     with open(file, 'rb') as fp:
#         img_data = fp.read()
#     msg.add_attachment(img_data, maintype='image',
#                                  subtype=imghdr.what(None, img_data))
#
# # Send the email via our own SMTP server.
# with smtplib.SMTP('localhost') as s:
#     s.send_message(msg)