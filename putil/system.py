# ------------------------------------------------------------------------------
#
# Execute external commands
#
# Author: Stefan Heule <stefanheule@gmail.com>
#
# ------------------------------------------------------------------------------

import subprocess
import threading
import sys

def execute(cmd, timeout = None):
  """
  Execute a command and return it's output.
  """
  return Command(cmd).run(timeout)


def execute_ok(cmd, timeout = None):
  """
  Execute a command and return it's output, and ensure it finishes without an error
  """
  (ret, out) = Command(cmd).run(timeout)
  if ret != 0:
    print(out)
    print("")
    error("Command '%s' finished with an error code of %d." % (cmd, ret))
  return out


def error(message = "Unspecified error occured"):
  """
  Output an error message and quit
  """
  sys.stderr.write("ERROR: %s\n" % (message))
  sys.exit(1)


# taken from http://stackoverflow.com/questions/1191374/subprocess-with-timeout
class Command(object):
  def __init__(self, cmd):
    self.cmd = cmd
    self.process = None
    self.output = ""
    self.error = ""

  def run(self, timeout):
    def target():
      self.process = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      self.output = self.process.stdout.read()
      self.error = self.process.stderr.read()
      self.child = self.process.communicate()[0]

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)
    if thread.is_alive():
      self.process.terminate()
      thread.join()
    retval = self.process.returncode
    return (retval, self.output + "\n" + self.error)