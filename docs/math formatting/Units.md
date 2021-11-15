# Units

<aside>
📏 Most numbers in a Brilliant lesson should have units of measure attached.

</aside>

Calculating with unit-less numbers can yield ambiguous results. But equally important, units provide additional context to the learner. A number with units can be imagined and compared.

When a number has a unit of measure, we include the unit wherever we write the number. SI units are used in Brilliant courses, universally.

Unit symbols are written in lower case letters except for liter $(\text{L})$ and those units derived from the name of a person. You should never format unit symbols yourself. The built-in tag `\SI{}{}` will handle this for you. If you want to write just the unit symbol without a number, you can use the tag `\si{}`.

By default, the tag `\SI{}{}` formats units in the denominator of a compound unit with a negative exponent — for example, $\text{m} \ \text{s}^{-2}.$ This tag accepts an option `[per-mode=symbol]` that sets a `/` in the unit, which is more easily interpretable for most of the Brilliant audience.

<aside>
👍 Near the surface of Earth, the acceleration due to gravity is roughly `$\SI[per-mode=symbol]{9.8}{\meter\per\second\squared}$.`

</aside>

In the above example, the option sets the unit of $g$ as $\text{m}/\text{s}^2$.

This option incorrect sets a compound unit with a product of units in the denominator. We are working on this capability, and this guidance will be updated when this correct setting of compound units is available. Until then, flag compound unit issues in the Slack channel `#editorial-lounge`.

If you are writing the name of a unit in text, the names of all units start with a lower case letter except, of course, at the beginning of the sentence. There is one exception: in "degree Celsius" the unit "degree" is lower case but the modifier "Celsius" is capitalized.

When a metric value is used as a modifier before a noun, hyphenating the quantity is not necessary.

<aside>
✅ Can you fill a `$\SI{2}{\liter}$` bottle with this pair of pitchers?

</aside>
