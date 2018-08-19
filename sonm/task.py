# https://docs.sonm.com/guides/sonm-cli-guide#task
import os
import tempfile
from typing import Optional, List

from jinja2 import Template

from . import CliMixin


class Task(CliMixin):

    def list(self, deal_id: str) -> Optional[dict]:
        command_args = ['task', 'list', deal_id]
        return self._call_command(command_args)

    def start(self, deal_id: str, params: 'TaskParams') -> dict:
        yaml_path = self._save_yaml(params)
        command_args = ['task', 'start', deal_id, yaml_path]
        result = self._call_command(command_args)
        os.unlink(yaml_path)
        return result

    def status(self, deal_id: str, task_id: str) -> dict:
        command_args = ['task', 'status', deal_id, task_id]
        return self._call_command(command_args)

    def logs(self, deal_id: str, task_id: str) -> dict:
        command_args = ['task', 'logs', deal_id, task_id]
        result = self._call_command(command_args, output_format=None)
        return {
            'logs': result.split('\n')
        }

    def stop(self, deal_id: str, task_id: str) -> dict:
        command_args = ['task', 'stop', deal_id, task_id]
        return self._call_command(command_args)

    def _save_yaml(self, params: 'TaskParams') -> str:
        import sonm
        template_path = os.path.join(os.path.dirname(sonm.__file__), 'templates/task.jinja2')

        with open(template_path) as f:
            template_content = f.read()

        t = Template(template_content)
        yaml = t.render(task=params)

        _, yaml_path = tempfile.mkstemp(prefix='task_', suffix='.yaml')
        with open(yaml_path, 'w') as f:
            f.write(yaml)

        return yaml_path


class TaskParams:

    def __init__(self, image: str, env: dict = None, commit_on_stop: bool = False, expose: list = None,
                 networks: List['Network'] = None):
        """
        https://docs.sonm.com/guides/sonm-cli-guide#task_start
        :type expose: tuple of tuples with tow strings: source port and destination port for exposing
        """
        self.image = image
        self.env = env
        self.commit_on_stop = commit_on_stop
        self.expose = expose
        self.networks = networks


class Network:
    pass


class NetworkTinc(Network):
    def __init__(self, subnet: str, invitation: str):
        self.type = 'tinc'
        self.subnet = subnet
        self.invitation = invitation