#!/usr/bin/env python
#
# Python Script to send email 
# Usage: sendmail.py <config.ini> <file_body.txt>
# ability to send to multiple recipients

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
import datetime
import ConfigParser
import code

#smtp_svr = "smtp.office365.com:587"
smtp_svr = "smtp.gmail.com:587"

def date_str():
    pstr = str(datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
    return str(pstr)

def parse_credentials(ini_file):
    settings = ConfigParser.ConfigParser()
    settings.read(ini_file)
    username = settings.get('sender', 'username')
    password = settings.get('sender', 'password')
    return (username, password)
    
def parse_options(ini_file):
    settings = ConfigParser.ConfigParser()
    settings.read(ini_file)
    arg_recipients = settings.get('options', 'mailto')
    arg_subject = settings.get('options', 'subject')
    return (arg_recipients, arg_subject)


# recipients must be a list
def send_email (smtp_server, fromaddr, passwd, recipients, subject, message):
    server = smtplib.SMTP(smtp_server)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, passwd)
    server.sendmail(fromaddr, recipients, 'Subject: %s\r\n%s' % (subject, message))
    server.quit()

#####################   CONFIGURATION PARMARETERS ##############################
# Will be read from ini file
'''
[sender]
username: sender@gmail.com
password: secret

[options]
mailto: alpha@gmail.com, bravo@gmail.com, charlie@gmail.com
subject: Test mail
'''
################################################################################

if __name__ == '__main__':
    argc = len(sys.argv)
    #print('argc:' + str(argc))
    if argc < 3:
        print("Usage:" + sys.argv[0] + ' <.ini_config_file> <file_body.txt>')
        sys.exit(1)

    # process command line arguments
    arg_recipients, arg_subject = parse_options(str(sys.argv[1]))
    print ("from ini file: " + arg_recipients)
    print ("subject: " + arg_subject)
    arg_body = str(sys.argv[2])

    # read variables from ini file
    arg_from, arg_from_password = parse_credentials(str(sys.argv[1]))

    # read file as string for the body
    with open(arg_body, 'r') as somefile:
        body_str = somefile.read()

        
    # send_email needs multiple recipients as a list
    to_list = arg_recipients.split(',')

    # ready for launch
    send_email(smtp_svr,
               arg_from,
               arg_from_password,
               to_list,
               arg_subject + date_str(),
               body_str)

    print 'Mail sent at ' + date_str()
