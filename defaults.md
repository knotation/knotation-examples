# Defaults

The [basic RDF](basic-rdf.md) examples show how to specify datatypes and languages for particular literals in Knotation. You can also specify a default datatype or default language for a predicate. The default will be associated with every object of that predicate, unless overridden.


### File: example1.kn

```kn
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: rdfs:label
rdfs:label: label

: kn:link
label: link

: kn:default-datatype
label: default datatype
default datatype; link: link

: kn:default-language
label: default language

: ex:child-of
label: child of
default datatype: link

: ex:translation-fr
label: French translation
default language: fr

: ex:integer
label: integer

: ex:has-count
label: has count
default datatype: integer

: ex:foo
label: Foo
French translation: Fou

: ex:bar
label: Bar
child of: Foo
has count: 42
```

### File: example2.ttl

```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix kn: <https://knotation.org/kn/> .
@prefix ex: <http://example.com/> .

rdfs:label
  rdfs:label "label" .

kn:link
  rdfs:label "link" .

kn:default-datatype
  rdfs:label "default datatype" ;
  kn:default-datatype kn:link .

kn:default-language
  rdfs:label "default language" .

ex:child-of
  rdfs:label "child of" ;
  kn:default-datatype kn:link .

ex:translation-fr
  rdfs:label "French translation" ;
  kn:default-language "fr" .

ex:integer
  rdfs:label "integer" .

ex:has-count
  rdfs:label "has count" ;
  kn:default-datatype ex:integer .

ex:foo
  rdfs:label "Foo" ;
  ex:translation-fr "Fou"@fr .

ex:bar
  rdfs:label "Bar" ;
  ex:child-of ex:foo ;
  ex:has-count "42"^^ex:integer .
```

### Example 1

```sh
kn example1.kn -o example2.ttl
```

### TODO Example 2

```sh
kn example2.ttl -o example1.kn
```

