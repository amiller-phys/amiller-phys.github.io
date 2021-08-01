---
layout: post
published: true
title: Things Have Chained
date: 2021/07/31
---

>**Question**: Suppose you have a chain with infinitely many flat (i.e., one-dimensional) links. The first link has length $1,$ and the length of each successive link is a fraction $f$ of the previous link’s length. As you might expect, $f$ is less than $1.$ You place the chain flat on a table and some ink at the very end of the chain (i.e., the end with the infinitesimal links).
>
>Initially, the chain forms a straight line segment, and the longest link is fixed in place. From there, the links are constrained to move in a very specific way: The angle between each chain and the next, smaller link is always the same throughout the chain. For example, if the $N^\text{th}$ link and the $N+1^\text{st}$ link form a $40$ degree clockwise angle, then so do the $N+1^\text{st}$ link and the $N+2^\text{nd}$ link.
>
>After you move the chain around as much as you can, what shape is drawn by the ink that was at the tail end of the chain? 

<!--more-->

([FiveThirtyEight](URL))

## Solution

The chain is made of a bunch of links of lengths $1, f, f^2, \ldots $

We can write down the position of each endpoint in terms of the last. take a chain with two links, with endpoints $\mathbf{p}_0,$ $\mathbf{p}_1,$ and $\mathbf{p}_2.$ 

To find $\mathbf{p}_1,$ we start at $\mathbf{p}_0,$ lay down a link of length $1$ and rotate it $\phi$ degrees: 

$$
\mathbf{p}_1 = \mathbf{p}_0 + \mathbf{R}(\phi)\cdot \mathbf{1}.
$$

Finding $\mathbf{p}_2$ is almost the same, we start at $\mathbf{p}_1,$ lay down a link of length $f$ and rotate it by $2\phi$ degrees:  

$$
\mathbf{p}_2 = \mathbf{p}_1 + \mathbf{R}^2(\phi)\cdot \left(f\mathbf{1}\right).
$$

Recursing, $\mathbf{p}_2$ is just

$$
\begin{align}
\mathbf{p}_2 &= \mathbf{p}_0 + \mathbf{R}(\phi)\cdot\mathbf{1} + f\mathbf{R}^2(\phi)\cdot\mathbf{1} \\
&= \mathbf{R}(\phi)\cdot\mathbf{1} + f\mathbf{R}^2(\phi)\cdot\mathbf{1} \\
&= \frac{1}{f}\left[f\mathbf{R}(\phi) + f^2\mathbf{R}^2(\phi)\right]\cdot\mathbf{1}
\end{align}
$$

This pattern carries on, and the $n^\text{th}$ link is

$$
\mathbf{p}_n =  \frac{1}{f}\left[f\mathbf{R}(\phi) + \left(f\mathbf{R}(\phi)\right)^2 + \ldots + \left(f\mathbf{R}(\phi)\right)^n\right]\cdot \mathbf{1}.
$$

We can put this in a more compact form that makes the behavior clearer.

if we act on $\mathbf{p}_n$ with $f\mathbf{R}(\phi)$ and subtract it from $\mathbf{p}_n,$ we get:

$$
\mathbf{p}_n = \overbrace{\frac{f\mathbf{R}(\phi)}{1 - f\mathbf{R}(\phi)}}^\text{$n$-independent}\times\overbrace{\left(1-\left(f\mathbf{R}(\phi)\right)^n\right)}^\text{$n$-dependent}
$$

the first term describes the prevailing twist of the chain, and the second term is an adjustment that accounts for the relative movement of individual links. 

another way of looking at it is that the first term generates smooth global motion whereas we expect the second term to provide interesting twiddly-dees and doo-dahs for smaller values of $n.$

for large values of $n,$ the second term oscillates around a central point, which is where the end of the chain lives. since $f < 1,$ this orbit closes and for large $n,$ the motion is provided by the first term alone.

up to here we haven't picked a representation for the rotation $\mathbf{R}(\phi)$ and arrow $\mathbf{1},$ but we can use complex numbers to do it.

in this picture $\mathbf{R}(\phi) = e^{i\phi}$ and $\mathbf{1} = e^{i0} = 1 + 0i.$

with this we get

$$
\mathbf{p}_n = \frac{e^{i\phi}}{1-fe^{i\phi}}\left(1-fe^{in\phi}\right)
$$

and we can plot the chain:

<plot of chain>

focusing on one of the early endpoints, we see nice twiddly-dees and doo-dahs, as predicted:

<plot of early endpoint>

in the limit $n\rightarrow \infty,$ $\mathbf{p}_n$ becomes 

$$
\mathbf{p}_n = \frac{e^{i\phi}}{1-fe^{i\phi}}
$$

bringing everything to the surface, we have

$$
\begin{align}
\mathbf{p}_n &= \frac{e^{i\phi}}{1-fe^{i\phi}}\frac{1-fe^{-i\phi}}{1-fe^{-i\phi}} \\
&= \frac{e^{i\phi} - f}{1 + f^2 - f(e^{i\phi} + e^{-i\phi})} \\
&= \frac{(\cos\phi - f) + i\sin\phi}{1 + f^2 - 2f\cos\phi}
\end{align}
$$

if we squint, this looks like a circle, but let's put it in polar form.

we need the magnitude $r$ and the angle this makes $\theta.$ it's important to keep in mind that the $\phi$ we've been talking about so far is the angle between links, and not any sort of polar angle.

$r$ is just

$$
\begin{align}
\sqrt{x^2 + y^2} &= \frac{\sqrt{f^2 -2f\cos\phi + \cos^2\phi + \sin^2\phi}}{1 + f^2 - 2f\cos\phi} \\
&= \frac{\sqrt{f^2 -2f\cos\phi + 1}}{1 + f^2 - 2f\cos\phi} \\
&= \frac{1}{\sqrt{1 + f^2 - 2f\cos\phi}}
\end{align}
$$

while 

$$
\begin{align}
\cos\theta &= \frac{x}{r} \\
&= \frac{\cos\phi - f}{\sqrt{1 + f^2 - 2f\cos\phi}} \\
&= \left(\cos\phi - f\right)r
\end{align}
$$

or

$$ r(\theta) = \frac{\cos\theta}{\cos\phi - f} $$

which is a circle of radius $\frac12\left(\cos\phi - f\right)^{-1}$ centered at $\frac12\left(\cos\phi - f\right)^{-1},$ without squinting. 

<br>