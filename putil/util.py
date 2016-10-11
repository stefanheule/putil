# ------------------------------------------------------------------------------
#
# Various helpers.
#
# Author: Stefan Heule <stefanheule@gmail.com>
#
# ------------------------------------------------------------------------------

import time

def get_time_str():
  """
  Returns a string of the current time.
  """
  return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())