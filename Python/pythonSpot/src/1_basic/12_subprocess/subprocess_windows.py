import sys
import subprocess

theproc = subprocess.Popen([sys.executable, "__init__.py"])
theproc.communicate()