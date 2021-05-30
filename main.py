# Import smtplib for the actual sending function
# https://realpython.com/python-send-email/
import pathlib
import smtplib, ssl, imghdr, configparser, os
from email.message import EmailMessage

def send_email(name):
    print(f'Hi, {name}')
    msg = EmailMessage()

    config = configparser.ConfigParser()
    config.read('config.ini')
    msg['From'] = config['input settings']['email']
    picture_directory = config['input settings']['directory']
    msg['To'] = config['output settings']['email']

    # get list of files in picture_directory
    print("picture_directory")
    print(picture_directory)
    true_path = picture_directory.strip('\"')
    print("path")
    print(true_path)

    print("all values")
    all_files = os.listdir(true_path)
    print(all_files)

    print("first value")
    first_file = all_files[0]
    print(first_file)

    print("abs")
    first_file_absolute = true_path+os.path.sep+first_file
    print(first_file_absolute)
    file = first_file_absolute

    msg['Subject'] = f'A picture for you'
    msg.set_content("I thought you might want to see this picture :) -STM")

    port = 465  # For SSL
    password = input(f"Type the password to send from {msg['From']} and press enter (special characters may need to be escaped): ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Get MIME subtype for image and attach to email
    with open(file, 'rb') as fp:
        img_data = fp.read()
    msg.add_attachment(img_data, maintype='image',
                       subtype=imghdr.what(None, img_data))

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(msg['From'], password)
        server.send_message(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_email('Hello test1')