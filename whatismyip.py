#!/usr/bin/python

# Requests ip from JSON enabled site and emails it on change to my gmail

# Imports
import json
import urllib2
import smtplib

# Constants
json_site = "http://ip-api.com/json"
save_ipaddress_location = '/somewhere'
myemail = 'your_email@somewhere.here'
myserver = 'remote_host or localhost'
myreceiver = 'destination@somewhere.else'
mysubject = 'IP address changed'

# Functions
def get_data(site):
    site_data = urllib2.urlopen(site)
    return site_data

def get_json_data(raw_json, item_name):
    formatted_json = json.load(raw_json)
    return formatted_json[item_name]

def send_email(server_name, sender, receiver, subject, outmessage):
    outgoing_message = "From: " + sender + "\nTo: " + receiver + "\nSubject: " + subject + "\n\n" + outmessage + "\n"
    try:
        smtp_out = smtplib.SMTP(server_name, 25)
        smtp_out.sendmail(sender, receiver, outgoing_message)
        return True
    except:
        print "Unable to send email, please check send_email parameters."
        return False

def write_ipaddress(write_item, location):
    try:
        write_file = open(save_ipaddress_location + '.whatismyip.conf', 'w')
        write_file.write(write_item)
        write_file.close()
        return True
    except:
        print "Error in saving file, please check the save_ipaddress_location setting."
        return False

def read_ipaddress(location):
    try:
        read_file = open(location + '.whatismyip.conf', 'r')
        saved_ipaddress = read_file.read().strip('\n')
        read_file.close()
        return saved_ipaddress
    except:
        print "Cannot read file located at: " + location + ". Please check settings."
        return False

# We're running this and not importing it
if __name__ == "__main__":
    # Test if we have a new ipaddress
    if read_ipaddress(save_ipaddress_location) != get_json_data(get_data(json_site), "query"):
        try:
            mymessage = 'The IP address has changed to: ' + get_json_data(get_data(json_site), "query")
            send_email(myserver, myemail, myreceiver, mysubject, mymessage)
        except:
            quit()

        try:
            write_ipaddress(get_json_data(get_data(json_site), "query"), save_ipaddress_location)
        except:
            quit()