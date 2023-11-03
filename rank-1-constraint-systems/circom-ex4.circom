pragma circom 2.0.0;

template LargerExample() {
    signal input x;
    signal input y;
    signal output out;

    signal v1;
    signal v2;

    v1 <== 3*x * x;
    v2 <== v1 * y;
    out <== 5*x*y - v2 + x + 2 * y - 3;
 }

component main = LargerExample();