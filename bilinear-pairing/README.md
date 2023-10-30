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

## Python code
In the next sections, we are going to use 3 groups: $\mathbb{G}_1$, $\mathbb{G}_2$ and $\mathbb{G}_{12}$.

The code can be found in [pairing.py file](./pairing.py). In this code, *py_ecc* library is used. It implements the **bn128** pairing that is used by the precompile at address 0x08 on Ethereum.


## Ethereum implementation

The **bn197** pairing is standardized on Ethereum in [EIP-197](https://eips.ethereum.org/EIPS/eip-197). The specification of the 0x08 precompile takes in a list of $\mathbb{G1}$ and $\mathbb{G2}$ points. Those are represented as $A_1, B_1, A_2, B_2, ..., A_n, B_n: A_i \in \mathbb{G1}, B_i \in \mathbb{G2}$.
```
A₁ = a₁G1
B₁ = b₁G2
A₂ = a₂G1
B₂ = b₂G2
...
Aₙ = aₙG1
Bₙ = bₙG2
```


A call to the 0x08 precompile returns `1` if the following is true: $A_1  B_1 + A_2 + B_2 + ... + A_n B_n = 0$. Otherwise, it returns `0`.

### Justification for EIP-197 design

$\mathbb{G}_{12} points are huge, so they are not returned as it would take a lot of gas to store them in memory.

Moreover, the value of the output is generally not checked. Only the fact that it is equal to another pairing is generally done.

In Groth16, the final step looks like $e(A₁, B₂) = e(α₁, β₂) + e(L₁, γ₂) + e(C₁, δ₂)$. But this can be written as $ 0 = e(-A₁, B₂) + e(α₁, β₂) + e(L₁, γ₂) + e(C₁, δ₂)$. Now it can be used with the Ethereum 0x08 precompile.

*Note: We talked about Groth16, but most ZK algorithm have verification formula that are pretty similar.**


## Solidity Example
Let's prove that:
```
a = 4
b = 3
c = 6
d = 2

-ab + cd = 0
```

By using pairing, we need to prove: $e(−aG1, bG2) + e(cG1, dG2) = 0$
### Python computation
The [pythonComputation.py](./pythonComputation.py) file contains the code t

### Solidity verification

