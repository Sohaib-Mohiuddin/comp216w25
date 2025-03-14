from ftplib import FTP

# ftp://ftp.cs.brown.edu/
URL = 'ftp.ietf.org'
FILE = 'sohaib.txt' # file to write to

print(f'Connecting to {URL}')
client = FTP(URL) # instantiates the client with a connection
print(f'Connected to {URL}')

client.login() # login to the
print(client.pwd()) # print the current directory

client.cwd('charter') # change directory to charter

fd = open(FILE, 'w')

def writeData(data): # the callback in writing data
    fd.write(data)
    fd.write('\n') # use os.linesep

# a new port is created for you when retrieving data
client.retrlines('RETR 1wg-charters.txt', writeData)
client.quit() # closes the connection