def test_socket(host):
    assert host.socket("tcp://0.0.0.0:9000").is_listening


def test_package_checks(host):
    nginx = host.package("php7.2-fpm")
    assert nginx.is_installed


def test_service(host):
    s = host.service("php7.2-fpm")
    assert s.is_enabled
    assert s.is_running
