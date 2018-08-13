# https://docs.sonm.com/guides/sonm-cli-guide#deal
from . import CliMixin


class Deal(CliMixin):

    def list(self) -> dict:
        command_args = ['deal', 'list']
        return self._call_command(command_args)

    def open(self, ask_id: str, bid_id: str) -> dict:
        command_args = ['deal', 'open', ask_id, bid_id]
        return self._call_command(command_args)

    def status(self, deal_id: str) -> dict:
        command_args = ['deal', 'status', deal_id]
        return self._call_command(command_args)

    def close(self, deal_id: str) -> dict:
        command_args = ['deal', 'close', deal_id]
        return self._call_command(command_args)

    def quick_buy(self, ask_id: str, duration: str = None) -> dict:
        """
        :param ask_id:
        :param duration: 1h23m13s
        """
        command_args = ['deal', 'quick-buy', ask_id]
        if duration is not None:
            command_args.append(duration)

        return self._call_command(command_args)
