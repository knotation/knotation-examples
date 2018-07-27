#!/usr/bin/env python3 
#
# Use README files to run a series of integration tests.

import argparse, os, re, shutil, subprocess, sys
from collections import OrderedDict

def run_test(command, dirname, example, content, files):
  """Run a single example command in its own directory."""
  output = None
  inputs = []

  match = re.search('-o example(\d+)\.(\w+)', content)
  if match:
    output = 'example' + match[1] + '.' + match[2]

  matches = re.finditer('example(\d+)\.(\w+)', content)
  for match in matches:
    inputs.append('example' + match[1] + '.' + match[2])
  inputs.remove(output)

  path = os.path.join('results', dirname, example)
  os.makedirs(path, exist_ok=True)
  for filename in inputs:
    with open(os.path.join(path, filename), 'w') as f:
      f.write(files[filename])
  expected = re.sub('example', 'expected', output)
  with open(os.path.join(path, expected), 'w') as f:
    f.write(files[output])

  try:
    p = subprocess.run(command + content[2:], cwd=path, shell=True)
    if p.returncode != 0:
      print('ERROR', example)
      return 'ERROR'

    p = subprocess.run(['diff', output, expected], cwd=path)
    if p.returncode == 0:
      print('PASS', example)
      return 'SUCCESS'
    else:
      print('FAIL', example)
      return 'FAILURE'
  except:
    print('ERROR', example)
    return 'ERROR'



def run_tests(command, example_file):
  """Read a README file and use it to test examples."""
  dirname = example_file[:-3]
  files = OrderedDict()
  examples = OrderedDict()
  errors = 0
  failures = 0
  successes = 0

  with open(example_file) as f:
    filename = None
    example = None
    fenced = False
    for line in f:
      if line.startswith('### File: '):
        filename = line.strip()[10:]
        files[filename] = ''
        example = None
        fenced = False
      elif line.startswith('### Example '):
        filename = None
        example = line.strip()[4:]
        fenced = False
      elif line.startswith('#'):
        filename = None
        example = None
        fenced = False
      elif filename:
        if line.startswith('```'):
          fenced = not fenced
        elif fenced:
          files[filename] += line
      elif example:
        if line.startswith('```'):
          fenced = not fenced
        elif fenced:
          examples[example] = line.strip()

    for example, content in examples.items():
      result = run_test(command, dirname, example, content, files)
      if result == 'ERROR':
        errors += 1
      elif result == 'FAILURE':
        failures += 1
      elif result == 'success':
        successes += 1

  return (errors, successes, failures)


def main():
  parser = argparse.ArgumentParser(
      description='Run examples as tests using a given command')
  parser.add_argument('command',
      type=str,
      default='./kn',
      nargs='?',
      help='The command to substitute for "kn"')
  args = parser.parse_args()

  # Get a list of example files from the main README.md file
  example_files = []
  reading = False
  with open('README.md') as readme:
    for line in readme:
      line = line.strip()
      if reading and line.startswith('- ['):
        links = re.findall('\(\S+.md\)', line)
        if len(links) > 0:
          example_file = links[0].strip('()')
          example_files.append(example_file)
      elif line == '## Examples':
        reading = True
      elif line.startswith('#'):
        reading = False

  # For each example directory, run the tests.
  shutil.rmtree('results', ignore_errors=True)
  tests = 0
  errors = 0
  failures = 0
  successes = 0
  for example_file in example_files:
    e, f, s = run_tests(args.command, example_file)
    errors += e
    failures += f
    successes += s

  # Report
  print('Errors:', errors)
  print('Failures:', failures)
  print('Successes:', successes)
  print('Tests:', errors + failures + successes)

  if errors > 0:
    sys.exit('FAIL There were errors')
  elif failures > 0:
    sys.exit('FAIL There were failures')
  else:
    print('PASS All tests passed')


if __name__ == "__main__":
  main()
