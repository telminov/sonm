import subprocess
import json
from typing import Optional


class SonmException(Exception):
    pass


class CliMixin:
    cli_path = '/usr/bin/sonmcli'

    def _call_command(self, command_args: list, output_format: Optional[str] ='json', parse_json=True):
        command = [self.cli_path, *command_args]
        if output_format is not None:
            command.extend(['--out', output_format])

        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_code = proc.wait()
        (out, err) = proc.communicate()

        if return_code > 0:
            raise SonmException(
                'Error. Command: %s. Return code: %s. Stdout: "%s". Stderr: "%s"' % (
                    command, return_code, out, err
                )
            )

        result = out.decode()
        if output_format == 'json' and parse_json:
            result = json.loads(result)

        return result
