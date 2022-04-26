def test_user(host):
    user = host.user("ansible")
    assert user.exists


def test_sudo_permission_ansible(host):
    host.run_test("sudo -u ansible sudo ls /root")


def test_ansible_key(host):
    ssh_key = host.file("/home/ansible/.ssh/authorized_keys")
    assert ssh_key.exists
    assert ssh_key.contains("ssh-")
