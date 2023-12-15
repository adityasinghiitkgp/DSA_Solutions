#import <Foundation/Foundation.h>

NSArray *findDuplicates(NSArray *array) {
    NSMutableArray *uniqueElements = [NSMutableArray array];
    NSMutableArray *duplicates = [NSMutableArray array];

    for (NSNumber *element in array) {
        if ([uniqueElements containsObject:element]) {
            [duplicates addObject:element];
        } else {
            [uniqueElements addObject:element];
        }
    }

    return [duplicates copy];
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSArray *array = @[@1, @2, @2, @3, @4, @4, @5];
        NSArray *duplicateElements = findDuplicates(array);
        
        NSLog(@"Duplicate elements in the array: %@", duplicateElements);
    }
    return 0;
}
