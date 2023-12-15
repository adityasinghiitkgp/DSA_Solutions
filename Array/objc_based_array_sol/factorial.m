#import <Foundation/Foundation.h>

NSInteger factorialOfNumber(NSInteger number) {
    if (number == 0 || number == 1) {
        return 1;
    } else {
        return number * factorialOfNumber(number - 1);
    }
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSInteger result = factorialOfNumber(5);
        NSLog(@"%ld", result);
    }
    return 0;
}
