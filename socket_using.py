import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

received_data = ""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    received_data += data.decode()
    print(data.decode(), end='')

mysock.close()

headers_and_body = received_data.split('\r\n\r\n', 1)
headers = headers_and_body[0]

header_lines = headers.split('\r\n')
for line in header_lines[1:]:
    if line.startswith('Last-Modified:'):
        last_modified = line.split(':', 1)[1].strip()
    elif line.startswith('ETag:'):
        etag = line.split(':', 1)[1].strip()
    elif line.startswith('Content-Length:'):
        content_length = line.split(':', 1)[1].strip()
    elif line.startswith('Cache-Control:'):
        cache_control = line.split(':', 1)[1].strip()
    elif line.startswith('Content-Type:'):
        content_type = line.split(':', 1)[1].strip()

print(f"Last-Modified: {last_modified if 'last_modified' in locals() else 'Not found'}")
print(f"ETag: {etag if 'etag' in locals() else 'Not found'}")
print(f"Content-Length: {content_length if 'content_length' in locals() else 'Not found'}")
print(f"Cache-Control: {cache_control if 'cache_control' in locals() else 'Not found'}")
print(f"Content-Type: {content_type if 'content_type' in locals() else 'Not found'}")