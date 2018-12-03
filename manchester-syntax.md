# Manchester Syntax

Knotation has special support for [Manchester syntax](https://www.w3.org/TR/owl2-manchester-syntax/) for writing OWL logical expressions.


### File: example1.kn

OWL Manchester syntax is abbreviated as `omn`. Use the `kn:omn` datatype to indicate that Manchester syntax is being used. Labels are important for Manchester syntax.

```kn
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix owl: <http://www.w3.org/2002/07/owl#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:frog
rdfs:label: frog

: ex:heart
rdfs:label: heart

: ex:in-taxon
rdfs:label: in taxon

: ex:frog-heart
rdfs:subClassOf; kn:omn: heart and 'in taxon' some frog
```

### File: example2.ttl

Turtle does not support Manchester syntax, so the Turtle version of is much longer and more difficult to read.

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:frog
  rdfs:label "frog" .

ex:heart
  rdfs:label "heart" .

ex:in-taxon
  rdfs:label "in taxon" .

ex:frog-heart
  rdfs:subClassOf [
    rdf:type owl:Class ;
    rdf:intersectionOf (
      ex:heart
      [
        rdf:type owl:Restriction ;
        owl:onProperty ex:in-taxon ;
        owl:someValuesFrom ex:frog
      ]
    )
  ] .
```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

### Example 2

```sh
kn example2.ttl -o example1.kn
```
