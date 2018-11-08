# Knotation Examples

This repository contains a number of examples of Knotation with explanations. The examples can be run as an integration test suite.

WARNING: This is work in progress.


## Examples

- [basic RDF](basic-rdf.md): IRIs and literals
- [prefixes](prefixes.md) and CURIEs
- [labels](labels.md)
- [defaults](defaults.md) for datatypes and languages
- [context files](context-files.md)


## Work In Progress

- [templates](templates.md)
- RDF lists
- [OWL annotations](owl-annotations.md)
- Manchester
- tables


## Test Harness

The `run-tests.py` script reads the Examples list above, then reads each Markdown file, extracts the example files, and runs each `Example X` command in its own directory with those files. The generated output files are compared to the expected output files.

The script expects a single argument: the specific command that will replace `kn` in each of the example commands. This could be `java -jar /path/to/knotation-cljc.jar`, for example.
