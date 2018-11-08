# Basic RDF

Knotation is a concrete syntax for RDF. The basic elements are IRIs, literals, and blank nodes. Literals can have a language or a datatype. Knotation also includes comments.

Knotation is very similar to Turtle, and is designed to be even less verbose than Turtle overall. One aspect that is more verbose than Turtle is that when the object is an IRI or blank node (not a literal), then Knotation requires a special <https://knotation.org/kn/link> datatype.

### File: example1.kn

```kn
: <http://example.com/subject>
<http://example.com/predicate>: literal object
<http://example.com/predicate>: literal object
 multiline string
<http://example.com/predicate>; @en-CA: language literal object
<http://example.com/predicate>; <http://example.com/datatype>: typed literal object
<http://example.com/predicate>; <https://knotation.org/kn/link>: <http://example.com/object>
<http://example.com/predicate>; <https://knotation.org/kn/link>: _:b0
```

### File: example2.ttl

This translates into the following Turtle:

```ttl
<http://example.com/subject>
  <http://example.com/predicate> "literal object" ;
  <http://example.com/predicate> """literal object
multiline string""" ;
  <http://example.com/predicate> "language literal object"@en-CA ;
  <http://example.com/predicate> "typed literal object"^^<http://example.com/datatype> ;
  <http://example.com/predicate> <http://example.com/object> ;
  <http://example.com/predicate> _:b0 .
```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

## HTTP(S) IRIs

For IRIs that are `http` or `https` URLs, Knotation does not require surrounding angle brackets: `<`, `>`.

### File: example3.kn

```kn
: http://example.com/subject
http://example.com/predicate: literal object
http://example.com/predicate: literal object
 multiline string
http://example.com/predicate; @en-CA: language literal object
http://example.com/predicate; http://example.com/datatype: typed literal object
http://example.com/predicate; https://knotation.org/kn/link: http://example.com/object
http://example.com/predicate; https://knotation.org/kn/link: _:b0
```

### Example 2

```sh
kn example3.kn -o example2.ttl
```

### Example 3

```sh
kn example2.ttl --sequential-blank-nodes -o example3.kn
```


## Named Graphs

Knotation also supports RDF datasets, which means named graphs. This example starts in the default graph, switches to a named graph, and returns to the default graph.

### File: example4.kn

```kn
: <http://example.com/subject-1>
<http://example.com/predicate>: subject 1 in default graph

@graph <http://example.com/graph-1>

: <http://example.com/subject-2>
<http://example.com/predicate>: subject 2 in named graph

@graph

: <http://example.com/subject-3>
<http://example.com/predicate>: subject 3 in default graph
```

This can be translated into the following TriG:

### File: example5.trig

```trig
<http://example.com/subject-1>
  <http://example.com/predicate> "subject 1 in default graph" .

<http://example.com/graph-1> {

  <http://example.com/subject-2>
    <http://example.com/predicate> "subject 2 in named graph" .

}

<http://example.com/subject-3>
  <http://example.com/predicate> "subject 3 in default graph" .
```

### TODO Example 4

```sh
kn example4.kn -o example5.trig
```

### TODO Example 5

```sh
kn example5.trig -o example4.kn
```
