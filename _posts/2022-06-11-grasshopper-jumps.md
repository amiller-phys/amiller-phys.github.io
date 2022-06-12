---
layout: post
published: true
title: Grasshopper jumps
subtitle: Where will you find this mysterious creature?
tags: equilibrium detailed-balance rates
date: 2022/06/11
---

>**Question:** You are trying to catch a grasshopper on a balance beam that is 1 meter long. Every time you try to catch it, it jumps to a random point along the interval between 20 centimeters left of its current position and 20 centimeters right of its current position.
>
>If the grasshopper is within 20 centimeters of one of the edges, it will not jump off the edge. For example, if it is 10 centimeters from the left edge of the beam, then it will randomly jump to anywhere within 30 centimeters of that edge with equal probability (meaning it will be twice as likely to jump right as it is to jump left).
>
>After many, many failed attempts to catch the grasshopper, where is it most likely to be on the beam? Where is it least likely? And what is the ratio between these respective probabilities?

<!--more-->

([FiveThirtyEight](https://fivethirtyeight.com/features/can-you-catch-the-grasshopper/))

## Solution

To make this problem more concrete, we can think about infinitely many grasshoppers jumping around. Put them on the beam and then let them hop around. The relative fraction of grasshoppers at position $x$ in this situation is equal to $P(x)$ in the single grasshopper problem. 

### Grasshopper equilibrium

After a long time has gone by, the grasshoppers will reach an equilibrium state where the probability distribution isn't changing anymore. 

Next, take a video of the grasshoppers jumping in the equilibrium state. If we play this movie backward, we wouldn't be able to tell the difference, since the equilibrium probability distribution is constant in time. This means that the probability of any transition is the same as the probability of the reverse transition: $P(a\rightarrow b) = P(b\rightarrow a).$ 

### Time-reversal equality

The probability of observing the transition $a\rightarrow b$ is the probability of being at $a$ times the probability of transitioning to $b$ given a start at $a:$

$$
  P(a\rightarrow b) = P(a)\times P(a \rightarrow b\rvert a)
$$

So, the time reverse equality becomes

$$
  P(a) P(a\rightarrow b\rvert a) = P(b) P(b\rightarrow a\rvert b).
$$

### Wherefore art thou grasshoppers?

If we compare two points $x$ and $y$ that have the full freedom of jumping to the left or right, then $P(x\rightarrow y\rvert x)$ is a uniform probability distribution $P(y) = 1/\left(\frac25\right)$ for $x-\frac15\leq y \leq x + \frac15$ and likewise for $P(y\rightarrow x\rvert y).$ 

This means that $P(x) = P(y)$ for any such points and so $P(x) = \text{const.}$ between $\frac15$ and $\frac45.$

<!-- Starting from the edges of this region, we can exploit the time-reversal equality again to get the rest of $P(x).$ -->

Now let's compare $x=\frac15$ with a point $y$ between $0$ and $\frac15.$

$P(y\rightarrow x\rvert x)$ is a uniform distribution over $\left(0,y + \frac15\right),$ so

$$
  P(y) = \text{const.} \frac{y + \frac15}{\frac25}.
$$

Immediately, we see that the greatest probability is anywhere in the central region, and the lowest probability is at either edge of the balance beam. plugging in, we get $\boxed{P(1/5)/P(0) = 2}.$

### Grasshopper distribution

We can continue on like this and peel off the probability distribution.

Working the other side, we get $P(y) = \text{const.}\times \frac{\frac15 + 1-y}{\frac25}$ for $0.8\leq y\leq 1.$

This gives us the shape of the probability distribution: it starts at $\frac12\text{const.},$ then grows linearly to $\text{const.}$ at $x=\frac15,$ then stays constant until $x=\frac45,$ at which point it shrinks linearly back down to $\frac12\text{const.}$

![](/img/2022-06-11-grasshopper-distribution-sketch.png){:width="450 px" class="image-centered"}

The total area under $P(x)$ has to be $1,$ which we can use to find $\text{const.}$ Adding up the central rectangle and the trapezoids on the wings, we get

$$
  \begin{align}
    \text{area} &= \text{const.}\times\frac35 + 2\frac{\text{const.} + \frac12\text{const.}}{2}\times\frac15 \\
    &= \left(\frac35 + \frac32\frac15\right)\text{const.} \\
    &= \left(\frac{6}{10} + \frac{3}{10}\right)\text{const.},
  \end{align}
$$

which shows that $\text{const.} = 10/9.$

### Truth in numbers

Indeed, an $N=10^8$ simulation yields the data in blue, plotted alongside the analytic prediction in gold:

![](/img/2022-06-11-grasshopper-jump.png){:width="450 px" class="image-centered"}

```mathematica
transition[x_] := RandomReal[{Max[0, x - 0.2], Min[1, x + 0.2]}]

round[] := (
  point = 0.5;
  Do[
   point = transition[point]
   , {i, 1, 1000}
   ];
  Return[point]
  )
```

<br>