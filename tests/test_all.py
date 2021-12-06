import re


def test_grpcio_package(packages):
    assert "grpcio" in packages


def test_grpcio_health_checking_package(packages):
    assert "grpcio-health-checking" in packages


def test_mariadb_package(packages):
    assert "mariadb" in packages


def test_psycopg2_package(packages):
    assert "psycopg2" in packages


def test_pytest_package(packages):
    assert "pytest" in packages


def test_pytest_version(host):
    command = "pytest -V 2>&1"

    output = host.check_output(command)
    assert re.match(r"^pytest \d+\.\d+\.\d+$", output)


def test_requests_package(packages):
    assert "requests" in packages
