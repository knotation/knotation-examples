# Tables

Knotation is normally written in stanzas, each consisting of a subject line followed by one or more statement lines. Knotation also supports tables, where each subject is a row. Tables are more convenient when you have many subjects with the same pattern of predicates.

Each cell value is appended to the header for its column to form a line of Knotation. If a cell is emtpy, then no Knotation output line is generated. If a header cell is empty, then that no output is generated for the cells in the column.

A table is just a two-dimensional grid, but Knotation tables support an optional "third dimension" by allowing cells to contain multiple values separated by pipe characters `|`. This also applies to header cells.

We translate tables into Knotation using the following steps:

- For each non-emtpy header value, we split on pipe characters to generate one or more *header values*
- For each non-empty cell we split on pipe characters to generate one or more *cell values*
- For each combination of header value and cell value we generate a Knotation line: header value + space + cell value + newline
- Escaped newline, tab, and pipe characters (`\n`, `\t`, `\|`) are unescaped

We'll consider a basic example first, then a more complex example using pipes.


### File: example1.kn

This context file defines the columns we will use.

```kn
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: rdfs:label
rdfs:label: label

: rdf:type
label: type
kn:default-datatype; kn:link: kn:link
```

### File: example2.tsv

The first column of this table is for the subjects. Empty cells are not translated to Knotation lines.

```tsv
:	label:	type:
ex:a	A	
ex:b	B	A
```

### File: example3.kn

This is the result of translating the table to stanzas. The stanzas are then processed as usual.

```kn
: ex:a
label: A

: ex:b
label: B
type: A
```

### Example 1

```sh
kn -c example1.kn example2.tsv -o example3.kn
```

### File: example4.kn

This context defines predicates for a more complex example.

```kn
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
@prefix kn: <https://knotation.org/kn/>
@prefix ex: <http://example.com/>

: ex:value
label: value

: ex:next
label: next
kn:default-datatype; kn:link: kn:link
```

### File: example5.tsv

This more complex example shows several table features. Consider each column in turn:

1. the first subject
2. the value for the first subject
3. a split header generates two lines: `next: ex:b` and `: ex:b` (the second subject)
4. a split cell generates two lines: `value: 2` and `value: 3`
5. an OWL annotation with a multiline string using an escaped newline character `\n`
6. a Knotation template
7. an indented line specifying a template value

```tsv
:	value:	next:|:	value:	> annotation:	kn:apply-template:	 slot 1:
ex:a	1	ex:b	2|3	multi\n line	ex:some-template	value 1
```

### File: example6.kn

In this example one row generates two stanzas, linked together via `ex:b`, as well as an OWL annotation and a Knotation template.

```kn
: ex:a
value: 1
next: ex:b

: ex:b
value: 2
value: 3
> annotation: multi
 line
kn:apply-template: ex:some-template
 slot 1: value 1
```

### Example 2

```sh
kn -c example4.kn example5.tsv -o example6.kn
```
