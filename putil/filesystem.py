# ------------------------------------------------------------------------------
#
# Helper functionality to interact with the file system
#
# Author: Stefan Heule <stefanheule@gmail.com>
#
# ------------------------------------------------------------------------------

def write(f, s):
  """
  print a string to a file
  """
  f = open(f, 'w')
  f.write(s)
  f.close()


def append(f, s):
  """
  appends a string to a file
  """
  f = open(f, 'a')
  f.write(s)
  f.close()


def appendln(f, s):
  """
  appends a line to a file
  """
  append(f, s + "\n")


def read_file(f):
  """
  Read an entire file and return the contents
  """
  with open(f) as f:
    return f.read()

def read_file_lines_stripped(f):
  """
  Read all lines of a file, and remove trailing and leading whitespace
  """
  with open(f) as f:
    return map(lambda x: x.strip(), f.readlines())