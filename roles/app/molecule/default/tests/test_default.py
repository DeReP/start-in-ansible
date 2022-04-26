import pytest


def test_app_directory_file(host):
    dir = host.file("/opt/linfo-4.0.6")
    assert dir.exists
    assert dir.is_directory


def test_app_config_file(host):
    conf = host.file("/opt/linfo-4.0.6/config.inc.php")
    assert conf.exists
