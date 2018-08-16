# https://docs.sonm.com/guides/sonm-cli-guide#order
import os

from . import CliMixin
from .bid import BidParams


class Order(CliMixin):

    def create(self, bid: BidParams) -> dict:
        yaml_path = bid.save_yaml()
        try:
            command_args = ['order', 'create', yaml_path]
            return self._call_command(command_args)
        finally:
            os.unlink(yaml_path)

    def list(self) -> dict:
        command_args = ['order', 'list']
        return self._call_command(command_args)

    def status(self, order_id: str) -> dict:
        command_args = ['order', 'status', order_id]
        return self._call_command(command_args)

    def cancel(self, order_id: str) -> dict:
        command_args = ['order', 'cancel', order_id]
        return self._call_command(command_args)

    def purge(self) -> dict:
        command_args = ['order', 'purge']
        return self._call_command(command_args)

