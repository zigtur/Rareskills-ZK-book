pragma circom 2.0.8;

template Multiply4() {
    signal input x;
    signal input y;
    signal input z;
    signal input u;
    
    signal v1;
    signal v2;
    
    signal out;
    
    v1 <== x * y;
    v2 <== z * u;
    
    out <== v1 * v2;
}

template main = Multiply4();