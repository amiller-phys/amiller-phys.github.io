# Numbers

!!!tldr "Rule"
    Without exception, numerical digits are displayed using the inline math environment.

When displaying a number with more than three digits, place the `\numcomma{}` markup tag around your number for readability. Similarly, the `\SI{}{}` markup tag can be used to display readable numbers with units. If a number has units, the number must be displayed with `\SI{}{}`.

Decimals less between $-1$ and $1$ should always have a leading $0.$

In some cases, it might be necessary to express some words as digits, and others as words to disambiguate quantities from objects:

!!! success "Example"
    A list with two $3$s, four $7$s, and five $1$s.

Other cases where numbers should be written as words include:

- Numbers that begin a sentence, although this can usually be avoided by rewriting the sentence.
- Integers $n$ in the range $0 \leq n < 11$ (if they aren't used in a problem or solution).

!!! success "Example"
    The theorems of plane geometry can be derived from five axioms postulated by Euclid in *Elements*.

The numbers in addresses or years should always be formatted with the inline math environment.
