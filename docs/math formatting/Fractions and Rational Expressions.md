# Fractions and Rational Expressions

<aside>
📏 Inline fractions are always formatted using `/` , except for simple fraction like $\frac34$or $\frac{\pi}{2}$.

</aside>

Guidelines for formatting fractions are similar to formatting numbers, with one complication.

The built-in markup tag, `\frac`, formats fractions and rational expressions with a horizontal bar, which, used inline, makes expressions painful to read and wreaks havoc on line spacing within a step (go ahead and try it, then kindly delete it). Using `\frac` in the inline math environment is a poor reading experience for the learner.

The formatting recommendation for inline fractions and rational expressions is to use the `/` symbol for the bar. Most fractions and simple rational expressions — like $n/(1+n)$  — are readable formatted like this.

If the content demands fractions formatted with a horizontal bar, or you need nested parentheses to write a complicated rational expression inline, then you should use `\frac` in the centered math environment `$$$`.
