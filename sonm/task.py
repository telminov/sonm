# https://docs.sonm.com/guides/sonm-cli-guide#task
from jinja2 import Template
import os
import tempfile

from . import CliMixin


class Task(CliMixin):
    def __init__(self, image: str):
        self.image = image

    def list(self, deal_id: int) -> dict:
        command_args = ['task', 'list', str(deal_id)]
        results = self._call_command(command_args, parse_json=False)
        # TODO
        results = []
        return results

    def start(self, deal_id: int) -> dict:
        yaml_path = self._save_yaml()
        command_args = ['task', 'start', str(deal_id), yaml_path]
        return self._call_command(command_args)

    def _save_yaml(self) -> str:
        import sonm
        template_path = os.path.join(os.path.dirname(sonm.__file__), 'templates/task.jinja2')

        with open(template_path) as f:
            template_content = f.read()

        t = Template(template_content)
        yaml = t.render(task=self)

        yaml_path = tempfile.mkstemp(prefix='task_', suffix='.yaml')
        with open(yaml_path, 'w') as f:
            f.write(yaml)

        return yaml_path
