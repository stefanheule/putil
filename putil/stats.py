# ------------------------------------------------------------------------------
#
# Helper functionality for statistics
#
# Author: Stefan Heule <stefanheule@gmail.com>
#
# ------------------------------------------------------------------------------

import numpy as np

def sample(n, cmd, maxtries = 10):
  res = []
  tries = 0
  for i in range(n):
    c = 0
    while True:
      c = cmd()
      if c is not None: break
      tries += 1
      if tries > maxtries: return (-1.0, -1.0)
    res.append(c)
  return (np.mean(res), np.std(res))