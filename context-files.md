# Context Files

It's often convenient to keep your prefixes and declarations of defaults in a separate file that you can reuse.


### File: example1.kn

This is the context file, declaring the prefixes, some common subjects and predicates, and defaults for datatypes and languages.

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
```

### File: example2.kn

Here is the content that we really care about:

```kn
: ex:foo
label: Foo
French translation: Fou

: ex:bar
label: Bar
child of: Foo
has count: 42
```

### File: example3.ttl

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
kn example1.kn example2.kn -o example3.ttl
```

