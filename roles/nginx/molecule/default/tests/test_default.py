def test_socket(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_service(host):
    s = host.service("nginx")
    assert s.is_enabled
    assert s.is_running


def test_nginx_config(host):
    host.run_test("nginx -t")
