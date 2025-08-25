#include <stdio.h>

int add(int a, int b) {
    int sum = a + b;
    return sum;
}

void greet() {
    printf("Hello, world!\n");
}

int main() {
    int result = add(5, 3);
    printf("Result: %d\n", result);
    greet();
    return 0;
}
