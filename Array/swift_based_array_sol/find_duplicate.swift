func findDuplicates(withArray array: [Int]) -> [Int] {
    var uniqueElements = Set<Int>()
    var duplicates = Set<Int>()

    for element in array {
        if uniqueElements.contains(element) {
            duplicates.insert(element)
        } else {
            uniqueElements.insert(element)
        }
    }

    return Array(duplicates)
}

let array = [1, 2, 2, 3, 4, 4, 5]
let duplicateElements = findDuplicates(withArray: array)
print("Duplicate elements in the array: \(duplicateElements)")