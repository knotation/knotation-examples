# Anonymous Structures

Knotation is a concrete syntax for RDF. RDF is built up from triples. To encode other structures in RDF, such as lists, annotations (referring to another triple), or complex expressions like the ones used in OWL, you need to create a structure out of triples. These structures are usually trees (directed acyclic graphs) where all the subjects are blank nodes.

We have special syntax for some structures, such as RDF lists, OWL annotations, and OWL logical expressions. But in the general case Knotation supports nested "anonymous" nodes.


### File: example1.kn

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:subject
ex:predicate; kn:anon: 
 ex:a: A
 ex:b: B
```

### File: example2.ttl

This translates into the following Turtle:

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:subject
  ex:predicate [
    ex:a "A" ;
    ex:b "B"
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
