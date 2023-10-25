#include <iostream>
#include <cmath>

using namespace std;

bool primeNumber(int n) {
    for (int i = 2; i < n/2; i++) {
        if ((i % 2 != 0) && (n % i == 0) ) {
            return false;
        } 
    }
    return true;
}

void swapNumber(int a, int b){
    int temp = a;
    a = b;
    b = temp;
    
    cout << a , b;
}

void armstrongNumber(int n) {
    int digit = (int)log10(n) + 1;
    int sum = 0;
    int originalN = n;
    while(n>0) {
        int lastdigit = n%10;
        sum += pow(lastdigit, digit);
        n = n/10;
    }

    if(originalN == sum) {
        cout << "It's a armstrong number" << endl;
    } else {
        cout << "It's not a armstrong number" << endl;
    }
}

int reverse_number(int n) {
    int reverse = 0;
    while (n > 0) {
        int lastdigit = n%10;
        reverse = reverse*10 + lastdigit;
        n = n/10;
    }
    return reverse;
}

void fibo(int n) {
    int t1 = 0;
    int t2 = 1;
    int nextTerm;

    for (int i = 0; i < n; i++) {
        cout << t1 << " ";
        nextTerm = t1+t2;
        t1 = t2;
        t2 = nextTerm;
    }
    cout << endl;
}

int fact(int n) {
    int factorial = 1;
    for (int i = 2; i <= n; i++) {
        factorial *= i; 
    }
    cout << factorial << endl;
    return 0;
}

int main(int argc, char const *argv[]) {
    int n;
    int k;
    cin >> n;
    k = n;
    
    cout << reverse_number(n) << endl;
    primeNumber(k) ? cout << k << " Is a Prime Number" << endl: cout << k <<  " Isn't a Prime Number" << endl;
    armstrongNumber(k);
    fibo(k);
    fact(k);

    return 0;
}
