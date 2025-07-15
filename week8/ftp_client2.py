#!/usr/bin/env python3
import os
import socket
from ftplib import FTP, error_perm

# FTP server details
FTP_SERVER   = 'ftp.ietf.org'
REMOTE_DIR   = '/ietf-ftp/charter'
REMOTE_FILE  = '1wg-charters.txt'
LOCAL_FILE   = REMOTE_FILE

def main():
    print(f"Connecting to {FTP_SERVER}:…")
    try:
        # Create client and set a 10-second timeout on all socket ops
        ftp = FTP()
        ftp.set_debuglevel(2)            # verbose FTP protocol logging
        ftp.connect(FTP_SERVER, 21, timeout=10)
        print("→ TCP connection established")
        
        ftp.login()                      # anonymous login
        print(f"→ Logged in. Welcome message: {(ftp.getwelcome)}")
        
        ftp.set_pasv(True)               # use passive mode
        print("→ Switched to passive mode")
        
        try:
            ftp.cwd(REMOTE_DIR)
            print(f"→ Changed into directory: {ftp.pwd()}")
        except error_perm:
            print(f"ERROR: Remote directory '{REMOTE_DIR}' not found.")
            return
        
        with open(LOCAL_FILE, 'w', encoding='utf-8') as fd:
            def write_line(line):
                fd.write(line + os.linesep)
            
            print(f"→ Retrieving '{REMOTE_FILE}'…")
            try:
                ftp.retrlines(f"RETR {REMOTE_FILE}", write_line)
                print("✔ Download complete!")
            except error_perm:
                print(f"ERROR: Remote file '{REMOTE_FILE}' not found.")
        
        ftp.quit()
        print("→ FTP session closed, exiting.")

    except socket.timeout:
        print("ERROR: Connection timed out. Is the server reachable?")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
