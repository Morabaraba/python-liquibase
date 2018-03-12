import sys
import subprocess
from pkg_resources import resource_filename


def get_jar_filename():
    """Return the full path to the Liquibase Java archive."""
    return resource_filename(__name__, "/jar/liquibase.jar")

def get_jar_cmd():
    return ["java", "-jar", get_jar_filename()]
    
def run(*args, **kwargs):
    cmd_args = get_jar_cmd() + list(args)
    return subprocess.call(cmd_args, **kwargs)

def run_output(*args, **kwargs):
    cmd_args = get_jar_cmd() + list(args)
    return subprocess.check_output(cmd_args, **kwargs)

def main():
    exit_code = run(*sys.argv[1:])
    sys.exit(exit_code)
