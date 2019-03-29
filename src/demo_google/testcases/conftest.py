# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--cmd_opt_browser_name", action="store", default="chrome", help="Define a browser name: 'chrome', 'firefox'"
    )
    parser.addoption(
        "--cmd_opt_eth_title", action="store", default="TEST - Пошук Google", help="Set an eth title"
    )
    parser.addoption(
        "--cmd_opt_page_to_switch", action="store", default="2", help="Define a page to switch"
    )


@pytest.fixture
def cmd_opt_browser_name(request):
    return request.config.getoption("--cmd_opt_browser_name")


@pytest.fixture
def cmd_opt_eth_title(request):
    return request.config.getoption("--cmd_opt_eth_title")


@pytest.fixture
def cmd_opt_page_to_switch(request):
    return request.config.getoption("--cmd_opt_page_to_switch")
