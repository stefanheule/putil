#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
# Code to interact with STOKE (http://stoke.stanford.edu)
#
# Author: Stefan Heule <stefanheule@gmail.com>
#
# ------------------------------------------------------------------------------

import sys

from . import system
from . import stats


def default_config():
  return {
    'def_in': '{ ... }',
    'live_out': "{ }",
  }


def __read_config(config, key, alt):
  if alt is not None: return alt
  if key not in config:
    system.error("Could not find key '%s' in configuration." % (key))
  return config[key]


def __arg(config, key, alt):
  if alt is None and key not in config: return ""
  return ' --' + key + ' "' + __read_config(config, key, alt) + '"'


def cost(config=default_config(), cost=None, target=None, rewrite=None, testcases=None, def_in=None, live_out=None):
  a = __arg
  c = config
  cmd = 'stoke debug cost'
  cmd += a(c, "cost", cost)
  cmd += a(c, "target", target)
  cmd += a(c, "rewrite", rewrite)
  cmd += a(c, "testcases", testcases)
  cmd += a(c, "def_in", def_in)
  cmd += a(c, "live_out", live_out)
  cmd += a(c, "max_jumps", None)
  (res, out) = system.execute(cmd)
  if res is not 0: return None
  import re
  match = re.search("Cost: ([0-9]+)", out, re.MULTILINE)
  if match: return int(match.group(1))
  return None


def sample_cost(n, **kwargs):
  return stats.sample(n, lambda: cost(**kwargs), maxtries=10)
