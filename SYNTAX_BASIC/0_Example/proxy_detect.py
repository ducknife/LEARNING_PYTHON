import socket

def detect_proxy_type(host, port, timeout=5):
    try:
        sock = socket.create_connection((host, port), timeout)
        # Thử handshake SOCKS5
        sock.sendall(b"\x05\x01\x00")  # version 5, 1 method, no auth
        resp = sock.recv(2)
        if resp.startswith(b"\x05"):
            return "SOCKS5"
        sock.close()
    except:
        pass

    try:
        sock = socket.create_connection((host, port), timeout)
        # Thử handshake SOCKS4 (gửi request không hợp lệ)
        sock.sendall(b"\x04\x01\x00\x50\x7F\x00\x00\x01\x00")
        resp = sock.recv(8)
        if resp and resp[0] == 0x00:
            return "SOCKS4"
        sock.close()
    except:
        pass

    try:
        sock = socket.create_connection((host, port), timeout)
        sock.sendall(b"GET / HTTP/1.0\r\n\r\n")
        resp = sock.recv(12)
        if resp.startswith(b"HTTP/"):
            return "HTTP"
        sock.close()
    except:
        pass

    return "Unknown"

print(detect_proxy_type("31.41.39.96", 63162))
