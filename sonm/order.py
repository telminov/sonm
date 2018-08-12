# https://docs.sonm.com/guides/sonm-cli-guide#order
from . import CliMixin


class Order(CliMixin):

    def list(self):
        command_args = ['order', 'list', '--out', 'json']
        return self._call_command(command_args)
