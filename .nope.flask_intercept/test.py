# Sadly this does not work. You simply can't force the firestick to
# Use a seperate dns server to block ads, it hard-codes 
# 8.8.8.8 for ads, so you specifically can't do it without
# Proxiying trafic. 
import socket
import ssl
import mitmproxy.certs as certs
from cryptography.hazmat.primitives import serialization
from flask import Flask
from pathlib import Path
from mitmproxy.net import tls
import os
# HOST, PORT = 'aviary.amazon.com', 443
# cert = ssl.get_server_certificate((HOST, PORT))

# c = (certs.Cert.from_pem(cert.encode("utf-8")))



ca = certs.CertStore.from_files(Path(os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")), Path(os.path.expanduser("~/.mitmproxy/mitmproxy-dhparam.pem")))

#server_cert = ca.get_cert(commonname=c.cn, sans=c.altnames)
server_cert = ca.get_cert(commonname="amazon.com", sans=["*.amazon.com", "127.0.0.1", "amazon.com", "192.168.1.211", "yourdomain.local"])
print(server_cert)
pcert = server_cert.cert.to_pem()
pkey =server_cert.privatekey.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption(),
                )


f = open("cert.pem", "wb")
f.write(pcert)
f.close()
f = open("key.pem", "wb")
f.write(pkey)
f.close()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

if __name__ == '__main__':

    app.run(debug=True, ssl_context=("cert.pem", "key.pem"), host="0.0.0.0", port = 443)