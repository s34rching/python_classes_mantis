import pytest
import json
import os.path
from fixtures.application import Application


fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as config:
            target = json.load(config)
    return target

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, baseUrl=web_config['baseUrl'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def final():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(final)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default="target.json")

