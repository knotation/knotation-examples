# Labels

A major difference between Knotation and Turtle format is that Knotation allows labels to be used in pretty much every place that an IRI or CURIE can be used. The label must be declared as an `rdfs:label` before it is used.

### File: example1.kn

```kn
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: rdfs:label
rdfs:label: label

: ex:foo
label: Foo
```

### File: example2.ttl

```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

rdfs:label
  rdfs:label "label" .

ex:foo
  rdfs:label "Foo" .
```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

### Example 2

```sh
kn example2.ttl -o example1.kn
```

### File: example3.kn

```kn
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: rdfs:label
rdfs:label: label

: kn:link
label: link

: ex:foo
label: Foo

: ex:child-of
label: child of

: ex:bar
label: Bar
child of; link: Foo
```

### File: example4.ttl

```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

rdfs:label
  rdfs:label "label" .

kn:link
  rdfs:label "link" .

ex:foo
  rdfs:label "Foo" .

ex:child-of
  rdfs:label "child of" .

ex:bar
  rdfs:label "Bar" ;
  ex:child-of ex:foo .
```

### Example 3

```sh
kn example3.kn -o example4.ttl
```

### Example 4

```sh
kn example4.ttl -o example3.kn
```
