# Naming Variables

!!!tldr "Rule"
        Variables add a layer of abstraction to a Brilliant lesson. We can make this abstraction feel seamless by selecting instructive, descriptive symbols for variables.

To the learner, variables should represent tangible, manipulatable objects — they shouldn't be a cypher that only a mathematical super-sleuths can decode.

Because variables are things that a user manipulates in a Brilliant lesson, variables are **always** formatted in the math environment. When you introduce a variable in your lesson, you need to select a symbol for the variable and consider whether you should attach a descriptive subscript.

- **Selecting a symbol**

    To start, survey resources on the subject of the lesson. Is there a consensus on representing certain quantities by certain symbols? If so, then you should follow these conventions wherever possible.

    !!! failure "Example"
        The cruising speed of the jet, $a,$ is faster than the speed of sound, $D.$

    !!! failure "Example"
        The Pythagorean Theorem, $\zeta^2 = \eta^2 + \theta^2,$ is the relationship between the lengths of the sides of a right triangle.

    If there is no consensus among teaching resources, then select a symbol that doesn't collide with the variable namespace adjacent to the topic you're teaching, and that jibes with the guidance on naming constants, vectors and matrices.

- **Attaching a subscript**

    Next, try to give the symbol you picked a descriptive subscript — an actual English word. If the lesson has a skin, the appropriate subscript should be self-evident. Descriptive subscripts should be formatted with the `\text{}` markup tag. Only capitalize the subscript if it is a proper name.

    Sometimes, the most obvious subscript is too long. If equations involving your variables with long subscripts start looking messy, try abbreviating the subscript to the first syllable or two. Don't use a period after the abbreviation.

    !!! success "Example"
        The temperature in the house is $T_\text{in}$ and the temperature outside is $T_\text{out}.$

    Some situations call for a variable with an index. To distinguish indices from exponents, we prefer subscript indices. Because indices are variables, they should **not** be formatted with the `\text{}` markup tag. Variables that need an index do **not** need a descriptive subscript. We avoid compound subscripts wherever possible.

    !!! failure "Example"
        The component of the helium molecule's velocity toward the opening is $v_{\text{He},x}.$ The component of the nitrogen molecule's velocity in the same direction is $v_{\text{N},x}.$

    !!! success "Example"
        The component of the helium molecule's velocity toward the opening is $v_x.$ The component of the nitrogen molecule's velocity in the same direction is $w_x.$

    Other situations call for variables without descriptive subscripts. If you are stating a general relationship, or if a descriptive subscript would be a burden on the learner, you can omit the subscript.

    !!! success "Example"
        A container of non-interacting gas molecules obeys the ideal gas law, $PV = NkT.$
