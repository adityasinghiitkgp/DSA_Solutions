import Foundation

func factorialOfNumber(withNumber number: Int) -> Int {
    if number == 0 || number == 1 {
        return 1
    } else {
        return number * factorialOfNumber(withNumber: number - 1)
    }
}

let result = factorialOfNumber(withNumber: 5)
print(result)
