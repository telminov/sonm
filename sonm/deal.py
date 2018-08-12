# https://docs.sonm.com/guides/sonm-cli-guide#deal
from . import CliMixin


class Deal(CliMixin):

    def list(self):
        command_args = ['deal', 'list', '--out', 'json']
        return self._call_command(command_args)
