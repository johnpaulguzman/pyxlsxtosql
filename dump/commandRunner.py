import sys
import subprocess


class CommandRunner:
    @staticmethod
    def get_run_results(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err, rc) = *process.communicate(), process.returncode
        return (command, out, err, rc)
