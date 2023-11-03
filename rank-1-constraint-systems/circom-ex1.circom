pragma circom 2.0.0;

template Multiply2() {
    signal input x;
    signal input y;
    signal output out;

    out <== x * y;
 }

component main = Multiply2();