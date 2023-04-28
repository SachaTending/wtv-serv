from socket import socket, AF_INET, SOCK_STREAM
from packets import *

def log(*argv, **kwarg): print(f"[*]", *argv, **kwarg)

class HTTPPacket():
    def parse(packet: bytes):
        p = packet.decode("utf-8").split("\r\n")
        return p

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 1615))
s.listen(1)

s2 = socket(AF_INET, SOCK_STREAM)

p_html = "<p>uhh</p>"

while True:
    a, b = s.accept()
    ab = a.recv(1024)
    p =HTTPPacket.parse(ab)
    log(f"{p[0]}")
    if not p[0].startswith(("GET wtv-1800:/preregister", "GET wtv-1800:/fuck")):
        s2.connect(("51.222.164.146", 1615))
        s2.send(ab)
        r = s2.recv(32768)
        r = r.decode().replace('51.222.164.146', '127.0.0.1').encode()
        log(f"Received: {r}")
        s2.close()
    else:
        if p[0].startswith("GET wtv-1800:/preregister"):
            r = wtv_1800_preregister.format(go_to='http://192.168.0.55').encode()
        if p[0].startswith("GET wtv-1800:/fuck"):
            r = f"200 OK\nContent-Type: text/html\nContent-length: {len(p_html)}\n\n{p_html}".encode()
    a.send(r)
    a.close()