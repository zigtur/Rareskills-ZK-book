# Bilinear pairing


## Introduction

This is an operation that allows to transform $a*b=c$ into $E(a)*E(b) = E(c)$, where $E$ is an encryption function. 

Then, the three encrypted values can be sent to a verifier. He will be able to verify that $E(a)*E(b) = E(c)$.

In the following explanations:
- Capital letters $\rightarrow$ EC points
- Lower case letters $\rightarrow$ elements of finite field


## How numbers are encrypted
### EC basics

A curve point is produced by multiplying a scalar by another point of the elliptic curve: $P = pG$. Given $P, G$, it is impossible to determine $p$.


### Use of EC points

Let's assume that $pq=r$. We use $P=pG$, $Q=qG$ and $R=rG$ to convince the verifier that $pq=r$.

If $p*q=r$, we want a function such that $f(P,Q)=R$. When $p*q \neq r$, we want this function to be $f(P,Q) \neq R$. This should be true for all possible combinations of $p,q,r$ in the group.

Typically, this $R$ function is expressed this way: $f(P,Q) = f(R,G)$. Here, $G$ is the EC generator, it can be seen as the value "1". Symbolically, it is the same as saying $P \times Q = R \times 1$.

In practice, the feature of bilinear pairing that we care about is: $f(aG, bG) = f(abG, G) = f(G, abG)$

### Maths notation
In the literature, the function we previously called $f$ is written as $e$: $e: G \times G \rightarrow G_T$. Note that $T$ is the "target group".

Respecting the literature, notation is $e(aG, bG) = e(abG, G) = e(G, abG)$.

## Pairing: Asymetric VS Symmetric
### Practice
In practice, it turns out to be easier to create bilinear pairings with different groups for the arguments. We say $e(G, G') = G''$. All groups are different. But the property still holds: $e(aG, bG') = e(abG, G') = e(G, abG')$.

*Note: $G''$ is not explicitely shown in the previous notation. It is the output of the function, the codomain of $e(G, G')$.

### Symmetric pairing
In symmetric pairing, the same group is used for both arguments of the function.
The generator $G$ and EC group used in arguments is the same.

A symmetric pairing function: $e(aG, bG) = e(abG, G) = e(G, abG)$.

## Asymmetric pairing
In asymmetric pairing, the arguments of the function use different groups.
The generator and the EC group can be different.
The pairing function can still satisfy the property we are looking for.

An asymmetric pairing function: $e(aG, bG') = e(abG, G') = e(G, abG')$.

## Field extensions
In Ethereum's bilinear pairing uses elliptic curves with **field extensions**.

With field extensions, EC points consist of several $(x,y)$ pairs.
Field extension is a very abstract concept.
The thing to remember is that EC points are defined with more than 2 dimensions.

But those points still have the properties of [cyclic groups](../group-theory/README.md#cyclic-groups). They do all the same stuffs than classic EC points.

