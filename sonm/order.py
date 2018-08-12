# https://docs.sonm.com/guides/sonm-cli-guide#order
import os

from . import CliMixin
from .bid import Bid


class Order(CliMixin):

    def create(self, bid: Bid) -> dict:
        yaml_path = bid.save_yaml()
        try:
            command_args = ['order', 'create', yaml_path, '--out', 'json']
            return self._call_command(command_args)
        finally:
            os.unlink(yaml_path)

    def list(self) -> dict:
        command_args = ['order', 'list', '--out', 'json']
        return self._call_command(command_args)

    def status(self, order_id: int) -> dict:
        command_args = ['order', 'status', str(order_id), '--out', 'json']
        return self._call_command(command_args)

    def cancel(self, order_id: int) -> dict:
        command_args = ['order', 'cancel', str(order_id), '--out', 'json']
        return self._call_command(command_args)

    def purge(self) -> dict:
        command_args = ['order', 'purge', '--out', 'json']
        return self._call_command(command_args)
