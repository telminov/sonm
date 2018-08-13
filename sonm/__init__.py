import subprocess
import json


class SonmException(Exception):
    pass


class CliMixin:
    cli_path = '/usr/bin/sonmcli'

    def _call_command(self, command_args: list, parse_json=True):
        command = [self.cli_path, *command_args]
        if parse_json:
            command.extend(['--out', 'json'])

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
        if parse_json:
            result = json.loads(result)

        return result
