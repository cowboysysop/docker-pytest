import subprocess

import pytest
import testinfra


def pytest_addoption(parser):
    parser.addoption("--image")


@pytest.fixture(scope="session")
def image(request):
    return request.config.getoption("--image")


@pytest.fixture(scope="session")
def host(image):
    run_command = ["docker", "run", "-d", image, "sleep", "infinity"]

    output = subprocess.check_output(run_command)
    docker_id = output.decode().rstrip()

    yield testinfra.get_host(f"docker://{docker_id}")

    rm_command = ["docker", "rm", "-f", docker_id]
    subprocess.check_call(rm_command)


@pytest.fixture(scope="session")
def packages(host):
    return host.pip.get_packages()
