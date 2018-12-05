# Tables

Knotation is normally written in stanzas, each consisting of a subject line followed by one or more statement lines. Knotation also supports tables, where each subject is a row. Tables are more convenient when you have many subjects with the same pattern of predicates.

We translate a table to Knotation cell-by-cell, then process the Knotation as normal. Each cell value is appended to the header value for its column to form one line of Knotation. If a cell is empty, then no Knotation line is generated for that cell. If a header cell is empty, then that no Knotation lines are generated for any of the cells in that column.

A TSV file consists of rows separated by newline characters, and cells separated by tab characters. We introduce one more optional level: *values* separated by pipe `|` characters. This allows each cell to contain zero (i.e. empty cell) or more values. Think of this this as an optional "third dimension" added to a two-dimensional table.

We translate tables into Knotation using the following steps:

- For each non-emtpy header value, we split on pipe characters to generate one or more *header values*
    - If a header value does not end with a colon `:` or semi-colon `;` then a colon is appended
    - The special header value `@subject` is replaced by a colon `:`
- For each non-empty cell we split on pipe characters to generate one or more *cell values*
- For each combination of header value and cell value we generate a Knotation line: header value + space + cell value + newline
    - We unescape any escaped newline, tab, and pipe characters (`\n`, `\t`, `\|`)

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

# File: example2A.tsv

The colons can be omitted in this header, and `@subject` can be used as the header for the first column to make it more readable. The result is the same.

```tsv
@subject	label	type
ex:a	A	
ex:b	B	A
```

### Example 2

```sh
kn -c example1.kn example2A.tsv -o example3.kn
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

: ex:integer
label: int
```

### File: example5.tsv

This more complex example shows several table features. Consider each column in turn:

1. the first subject
2. the value for the first subject; the header value ends with `;` and the cell value starts with a datatype
3. a split header generates two lines: `next: ex:b` and `: ex:b` (the second subject)
4. a split cell generates two lines: `value: 2` and `value: 3`
5. an OWL annotation with a multiline string using an escaped newline character `\n`
6. a Knotation template
7. an indented line specifying a template value

```tsv
:	value;	next|	value	> annotation	kn:apply-template	 slot 1
ex:a	int: 1	ex:b	2|3	multi\n line	ex:some-template	value 1
```

In column 2, ending the header with `;` means that the cell values should all start with a dataype then a colon and the object. This is useful when the cell values can have different datatypes. When the datatypes are all the same, you can either provide a default datatype for the header predicate, or include the datatype in the header explicitly, e.g. `value; int`.

Split headers (as in column 3) can always be replaced by multiple columns, but then the cell value would be the same in those columns, creating some redundancy.

### File: example6.kn

In this example one row generates two stanzas, linked together via `ex:b`, as well as an OWL annotation and a Knotation template.

```kn
: ex:a
value; int: 1
next: ex:b

: ex:b
value: 2
value: 3
> annotation: multi
 line
kn:apply-template: ex:some-template
 slot 1: value 1
```

### Example 3

```sh
kn -c example4.kn example5.tsv -o example6.kn
```
