# OWL Annotations

Knotation has special support for the Web Ontology Language (OWL). OWL allows statements to be made about particular triples using "OWL Annotations".

### File: example1.kn

```kn
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
@prefix owl: <http://www.w3.org/2002/07/owl#>
@prefix ex: <http://example.com/>

: ex:s
ex:a: A
> ex:b: B is an annotation on A
```

### File: example2.ttl

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.com/> .

ex:s
  ex:a "A" .

_:b0
  rdf:type owl:Annotation ;
  owl:annotatedSource ex:s ;
  owl:annotatedProperty ex:a ;
  owl:annotatedTarget "A" ;
  ex:b "B is an annotation on A" .
```

### Example 1

```sh
kn example1.kn --sequential-blank-nodes -o example2.ttl
```

### Example 2

```sh
kn example2.ttl --sequential-blank-nodes -o example1.kn
```

## Nested Annotations

### File: example3.kn

```kn
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
@prefix owl: <http://www.w3.org/2002/07/owl#>
@prefix ex: <http://example.com/>

: ex:s
ex:a: A
> ex:b: B is an annotation on A
>> ex:c: C is an annotation on B
> ex:d: D is an annotation on A
```

### File: example4.ttl

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://example.com/> .

ex:s
  ex:a "A" .

_:b0
  rdf:type owl:Annotation ;
  owl:annotatedSource ex:s ;
  owl:annotatedProperty ex:a ;
  owl:annotatedTarget "A" ;
  ex:b "B is an annotation on A" .

_:b1
  rdf:type owl:Annotation ;
  owl:annotatedSource _:b0 ;
  owl:annotatedProperty ex:b ;
  owl:annotatedTarget "B is an annotation on A" ;
  ex:c "C is an annotation on B" .

_:b2
  rdf:type owl:Annotation ;
  owl:annotatedSource ex:s ;
  owl:annotatedProperty ex:a ;
  owl:annotatedTarget "A" ;
  ex:d "D is an annotation on A" .
```

### Example 3

```sh
kn example3.kn --sequential-blank-nodes -o example4.ttl
```

### Example 4

```sh
kn example4.ttl --sequential-blank-nodes -o example3.kn
```
