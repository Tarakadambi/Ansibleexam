import pytest
import socket

@pytest.mark.parametrize("port", [80, 3306])
def test_ports_open(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(("localhost", port))
    sock.close()
    assert result == 0, f"Port {port} is not open"

def test_magento_homepage(host):
    cmd = host.run("curl -s -o /dev/null -w '%{http_code}' http://localhost")
    assert cmd.stdout == "200"
