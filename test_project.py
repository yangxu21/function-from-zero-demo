from mylib.calc import add
from calCLI import cli
from click.testing import CliRunner

def test_add():
    assert add(1,2) == 3


def test_add_cmd():
    runner = CliRunner()
    result = runner.invoke(cli, ("add", "1", "2"))
    assert result.exit_code == 0
    assert "3" in result.output
