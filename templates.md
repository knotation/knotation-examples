# Templates

Knotation includes basic templating. You define a template with the `kn:template-content` predicate, including "slots" for substitutions, then apply the template using the `kn:apply-template` predicate and specifying values for the slots.

### File: example1.kn

```kn
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:template
kn:template-content: 
 ex:label: Foo {label}

: ex:foo-bar
kn:apply-template: ex:template
 label: Bar
```

### File: example2.ttl

```ttl
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

ex:template
  kn:template-content """
ex:label: Foo {label}""" .

ex:foo-bar
  kn:applied-template """ex:template
label: Bar""" ;
  ex:label "Foo Bar" .

```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

### TODO Example 2

```sh
kn example2.ttl -o example1.kn
```
