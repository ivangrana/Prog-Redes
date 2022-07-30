import argparse, socket, ssl
def client(host, port, cafile=None):
  purpose = ssl.Purpose.SERVER_AUTH
  context = ssl.create_default_context(purpose, cafile=cafile)
  raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  raw_sock.connect((host, port))
  print(‘Connected to host {!r} and port {}’.format(host,
  port))
  ssl_sock = context.wrap_socket(raw_sock,
  server_hostname=host)
  while True:
    data = ssl_sock.recv(1024)
    if not data:
    break
  print(repr(data))
