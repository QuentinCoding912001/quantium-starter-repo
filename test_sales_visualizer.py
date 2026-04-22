import chromedriver_autoinstaller
from sales_visualizer_interactive import app


def setup_module():
    chromedriver_autoinstaller.install()


def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("#app-header")
    assert header.text == "Soul Foods Pink Morsel Sales Visualiser"


def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-picker")
    assert picker is not None