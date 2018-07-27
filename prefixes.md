# Prefixes

IRIs have many advantages, but their main disadvantage is that they're long. By specifying a set of prefixes we can shorten IRIs to CURIEs. Knotation is similar to Turtle and SPARQL.

### example1.kn

```kn
@prefix ex: <http://example.com/>

: ex:subject
ex:predicate: literal object
ex:predicate; ex:datatype: typed literal object
```

### example2.ttl

```ttl
@prefix ex: <http://example.com/> .

ex:subject
  ex:predicate "literal object" ;
  ex:predicate "typed literal object"^^ex:datatype .
```

### Test 1

```sh
kn example1.kn -o example2.ttl
```

### Test 2

```sh
kn example2.ttl -o example1.kn
```

## Links

To indicate a link, we use a special Knotation datatype.

### example3.kn

```kn
@prefix kn: <https://knotation.org/>
@prefix ex: <http://example.com/>

: ex:subject
ex:predicate; kn:link: ex:object
```

### example4.ttl

```ttl
@prefix kn: <https://knotation.org/> .
@prefix ex: <http://example.com/> .

ex:subject
  ex:predicate ex:object .
```

### Test 3

```sh
kn example3.kn -o example4.ttl
```

### Test 4

```sh
kn example4.ttl -o example3.kn
```
