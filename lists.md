# Lists

RDF implements lists as "linked lists". Each item in the list has two triples with the same blank node as the subject. The first triple has `rdf:first` as predicate and the list item as the object. The second triple has `rdf:rest` as the predicate, and the object is the blank node for next item in the list, or `rdf:nil` to indicate the end of the list.

### File: example1.ttl

The list `"A" "B" "C"` is represented by six triples:

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p _:b1 .

_:b1
  rdf:first "A" ;
  rdf:rest _:b2 .

_:b2
  rdf:first "B" ;
  rdf:rest _:b3 .

_:b3
  rdf:first "C" ;
  rdf:rest rdf:nil .
```

### File: example2.ttl

In Turtle we could represent this with nested anonymous subjects:

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p [
    rdf:first "A" ;
    rdf:rest [
      rdf:first "B" ;
      rdf:rest [
        rdf:first "C" ;
        rdf:rest rdf:nil
      ]
    ]
  ] .
```

### File: example3.ttl

But Turtle has build-in support for RDF lists which avoids the nesting:

```ttl
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p (
    "A"
    "B"
    "C"
  ) .
```

### Example 1

The verbose version is equivalent to the terse version:

```sh
kn example1.ttl -o example3.ttl
```

### Example 2

The nested version is also equivalent to the terse version:

```sh
kn example2.ttl -o example3.ttl
```

### File: example4.kn

In Knotation a simple list looks similar to a Markdown list:

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:s
ex:p; kn:list:
 - A
 - B
 - C
```

### File: example5.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p (
    "A"
    "B"
    "C"
  ) .
```

### Example 3

```sh
kn example4.kn -o example5.ttl
```

### Example 4

```sh
kn example5.ttl -o example4.kn
```

## Typed Lists

### File: example6.kn

To add explicit types to your list, use `~` as the bullet:

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:s
ex:p; kn:list:
 ~ @en: A
 ~ ex:integer: 1
```

### File: example7.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p (
    "A"@en
    "1"^^ex:integer
  ) .
```

### Example 5

```sh
kn example6.kn -o example7.ttl
```

### Example 6

```sh
kn example7.ttl -o example6.kn
```

## Nested Lists

### File: example8.kn

You can create a nested list using `~ kn:list:` and indenting

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:s
ex:p; kn:list:
 - A
 ~ kn:list:
  - B
  ~ kn:list:
   - C
   - D
 - E
```

### File: example9.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:s
  ex:p (
    "A"
    (
      "B"
      (
        "C"
        "D"
      )
    )
    "E"
  ) .
```

### Example 7

```sh
kn example8.kn -o example9.ttl
```

### Example 8

```sh
kn example9.ttl -o example8.kn
```
