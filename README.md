whatismyip
==========

Why write this junk?

To be honest this is a first attempt at doing something useful in Python. Past that, this is because I'm lazy. If you use a dynamic dns service like NoIP or DynDNS, you have experienced the joy of responding to those confirmation emails every 30 days. While I could just pay the $X per year and not have to click a link in an email every once in a while, I thought why not sick Python on the job? Hence the code in this repository.

Configuration:

At the top of the whatismyip.py file you'll find the following:

# Constants
json_site = "http://ip-api.com/json"
save_ipaddress_location = '/somewhere'
myemail = 'your_email@somewhere.here'
myserver = 'remote_host or localhost'
myreceiver = 'destination@somewhere.else'
mysubject = 'IP address changed'

Change each parameter to what works for your setup. This should work with almost any json ip reporting tool out there. Should you use somehting other than what I have here, don't forget to change the field name in the JSON call within the code.

Please feel free to make this better, worse, or mock the code. I'm learning and will take any and all constructive criticism.
