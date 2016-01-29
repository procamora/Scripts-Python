import pexpect
import time, sys

telconn = pexpect.spawn('telnet 192.168.1.15')
time.sleep(5)
telconn.logfile = sys.stdout
telconn.expect(":")
telconn.send('PASSWORD' + "\r")
telconn.send("\r\n")
time.sleep(5)
telconn.expect(">")
telconn.send("reboot" + "\r")
telconn.send("\r\n")
