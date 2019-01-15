# Prefixes

IRIs have many advantages, but their main disadvantage is that they're long. By specifying a set of prefixes we can shorten IRIs to CURIEs. Knotation is similar to Turtle and SPARQL.

### File: example1.kn

```kn
@prefix ex: <http://example.com/>

: ex:subject
ex:predicate: literal object
ex:predicate; ex:datatype: typed literal object
```

### File: example2.ttl

```ttl
@prefix ex: <http://example.com/> .

ex:subject
  ex:predicate "literal object" ;
  ex:predicate "typed literal object"^^ex:datatype .
```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

### Example 2

```sh
kn example2.ttl -o example1.kn
```

## Links

To indicate a link, we use a special Knotation datatype.

### File: example3.kn

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:subject
ex:predicate; kn:link: ex:object
```

### File: example4.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:subject
  ex:predicate ex:object .
```

### Example 3

```sh
kn example3.kn -o example4.ttl
```

### Example 4

```sh
kn example4.ttl -o example3.kn
```


## Empty Prefix

The "empty prefix" is valid.

### File: example5.kn

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix : <http://example.com/>

: :subject
:predicate; kn:link: :object
```

### File: example6.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix : <http://example.com/> .

:subject
  :predicate :object .
```

### Example 5

```sh
kn example5.kn -o example6.ttl
```

### Example 6

```sh
kn example6.ttl -o example5.kn
```
