import os
import shutil
from ftplib import FTP

HOST = "127.0.0.1"
USER = "diman"
PASSWORD = "user"
ftp = FTP(host=HOST, user=USER, passwd=PASSWORD)
if os.path.exists("/home/diman/test"):
    shutil.rmtree("/home/diman/test")
ftp.mkd("test")
if os.path.exists("/home/diman/test"):
    ftp.cwd('test')
    with open('data/logo.png', 'rb') as fp:
        ftp.storbinary('STOR logo.png', fp)
ftp.quit()
