import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler


def main() -> None:
    webdir = '.'
    addr = ''
    port = 80

    os.chdir(webdir)
    srvraddr = (addr, port)
    srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
    srvrobj.serve_forever()


if __name__ == '__main__':
    main()
