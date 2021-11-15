# Inline vs. Centered Math

The math environment in Camperdown has two settings: inline (`$...$`) and centered (`$$$`).

You should think of inline mode as the default for Brilliant lessons. It treats math as an extension of the text by keeping it close to the writing.

The centered environment introduces a lot of white space, so it should be used judiciously. Centered environment is the correct choice in the following use cases:

- Multi-line calculations or derivations (should be formatted with `\begin{align} ... \end{align}`)
- Equations or expressions that would need nested parentheses to be correct inline
- Equations or expressions that would be easier to read if they weren't inline
- To draw special attention to an equation or expression so it can be referenced easily.

The tradeoff is that centered math introduces a lot of white space onto the screen, and divorces the math expressions from the text describing them, which we only want to do if necessary.

If you find the need to refer to a centered mathematical expression many times, you should establish a name or symbol for it and use that for repeated inline reference.
