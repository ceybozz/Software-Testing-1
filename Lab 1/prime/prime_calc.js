// NO assertion tests/refactoring
// Set upper bounds
const max = 1000;
// Lower bounds
const min = 0;
// Global obj
let primeChecking;

class PrimeChecking {
    // Calculates prime num, use boolean in array
    constructor() {
        this.primeBucket = new Array(max + 1);
    }

    primeCheck(num) {
        //Init array, holding prime int
        let primeBucket = new Array(max + 1);

        // Init all elements to boolean
        for (let i = 2; i <= max; i++) {
            primeBucket[i] = true;
        }

        // Multiples all with 2
        let j = 2;
        // 2 j as 2 is prime
        for (let i = j + j; i <= max; i = i + j) {
            // Multiples of 2 to false
            primeBucket[i] = false;
        }
        // From 3 up to max
        for (j = 3; j <= max; j = j + 2) {
            // If primeBucket[j] still a prime (not a multiple of 3, 5, 7 and so on)
            if (primeBucket[j] == true) {
                for (let i = j + j; i <= max; i = i + j) {
                    primeBucket[i] = false;
                }
            }
        }
        // Input check against prime
        if (primeBucket[num] == true) {
            return true;
        } else {
            return false;
        }
    }

    primePreCalc() {
        let sqr = Math.sqrt(max);
        for (let i = 2; i <= max; i++) {
            this.primeBucket[i] = true;
        }

        let j = 2;
        for (let i = j + j; i <= max; i = i + j) {
            this.primeBucket[i] = false;
        }
        for (j = 3; j <= sqr; j = j + 2) {
            if (this.primeBucket[j] == true) {
                for (let i = j + j; i <= max; i = i + j) {
                    this.primeBucket[i] = false;
                }
            }
        }
    }

    // Method to check input
    checkArgs() {
        if (arguments.length != 1) {
            throw new Error("Out of range!")
        } else {
            // If undefined, expect error
            if (arguments[0] === undefined) {
                throw new Error("Can not be undifiend!");
            }
            // If empty, expect error
            else if (arguments[0] === "") {
                throw new Error("No input!")
            }
            // Not int, expect error
            else if (!Number.isInteger(arguments[0])) {
                throw new Error("No str!")
            }

            // Get int
            let number = parseInt(arguments[0], 10);
            // If not int, expect error
            if (isNaN(number)) {
                throw new Error("Not int!")
            }
            // If int to low, expect error
            if (number < 0) {
                throw new Error("Int to low!")
            }
            // If int to high, expect error
            else if (number > max) {
                throw new Error("Int to high!")
            }
        }
    }
}


// Automatically tests cases when user performs test
function checkTest(num) {
    primeChecking = new PrimeChecking();
    // Run all
    test_PrimeChecking_known_true();
    test_PrimeChecking_known_false();
    test_PrimeChecking_checkArgs_neg_input();
    test_PrimeChecking_checkArgs_above_upper_bound();
    test_PrimeChecking_checkArgs_char_input();
    test_PrimeChecking_checkArgs_2_inputs();
    test_PrimeChecking_checkArgs_zero_input();
    test_PrimeChecking_checkArgs_undefined_input();
    test_PrimeChecking_checkArgs_non_integer_input();
}

function preCalc() {
    primeChecking = new PrimeChecking();
    primeChecking.primePreCalc();
}

// Check for prime when ordinary user running solution, merge function with checkTest if wanted
function check(num) {
    primeChecking = new PrimeChecking();
    checkTest(num)
    try {
        // Checking for prime
        primeChecking.checkArgs(parseInt(num));
        // Either use assertion or alert box
        let info = `Input is prime: ${num}.`
        assert(primeChecking.primeCheck(num), info)
    } catch (err) {
        console.log(err);
        let info = `Input: ${num}, not prime. error checkArgs-Method`;
        assert(primeChecking.primeCheck(num), info);
    }
}

// Append test result in list to page 
function assert(outcome, info) {
    let output = document.querySelector('#output');
    let li = document.createElement('li');
    li.className = outcome ? 'pass' : 'fail';
    li.appendChild(document.createTextNode(info));
    output.appendChild(li);
}

// Test method we use is "AAA" (Arrange, Act and Assert)
// Test 1, check true primes
function test_PrimeChecking_known_true() {
    let info = `Test for known true primes with: 2`;
    try {
        primeChecking.checkArgs(2);
        assert(primeChecking.primeCheck(2), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(2), info);
    }
}

// Test 2, check false primes
function test_PrimeChecking_known_false() {
    let info = `Test for known false primes with: 6`;
    try {
        primeChecking.checkArgs(6);
        assert(!primeChecking.primeCheck(6), info);
    } catch (error) {
        assert(primeChecking.primeCheck(6), info);
    }
}

// Test 3, check negative input
function test_PrimeChecking_checkArgs_neg_input() {

    let info = `Test for negative input: -1`;
    try {
        primeChecking.checkArgs(-1);
        assert(primeChecking.primeCheck(-1), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(-1), info);
    }
}

// Test 4, check upper bound limit
function test_PrimeChecking_checkArgs_above_upper_bound() {
    let info = `Test for upper bound limit: 10001`;
    try {
        primeChecking.checkArgs(10001);
        assert(primeChecking.primeCheck(10001), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(10001), info);
    }
}

// Test 5, check for char input
function test_PrimeChecking_checkArgs_char_input(char) {
    let info = `Test for char input: ${'r'}`;
    try {
        primeChecking.checkArgs('r');
        assert(primeChecking.primeCheck('r'), info);
    } catch (error) {
        assert(!primeChecking.primeCheck('r'), info);
    }
}

// Test 6, check for more than one input
function test_PrimeChecking_checkArgs_2_inputs() {
    let arr = new Array(5, 99);
    let info = `Test for more then one input: ${arr[0]}, ${arr[1]}`;
    try {
        primeChecking.checkArgs(arr[0], arr[1]);
        assert(primeChecking.primeCheck(arr), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(arr), info);
    }
}

// Test 7, check zero/empty input
function test_PrimeChecking_checkArgs_zero_input() {

    let info = `Test for zero/empty input: ${''}`;
    try {
        primeChecking.checkArgs('');
        assert(primeChecking.primeCheck(''), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(''), info);
    }
}

// Test 8, check for undefined input
function test_PrimeChecking_checkArgs_undefined_input() {
    let arr = new Array();
    let info = `Test for undefined input: ${arr[0]}`;
    try {
        primeChecking.checkArgs(arr[0]);
        assert(primeChecking.primeCheck(arr), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(arr), info);
    }
}

// Test 9, check for non-integer input
function test_PrimeChecking_checkArgs_non_integer_input() {
    let info = `Test for non-integer input: ${1.5}`;
    try {
        primeChecking.checkArgs('1.5');
        assert(primeChecking.primeCheck(1.5), info);
    } catch (error) {
        assert(!primeChecking.primeCheck(1.5), info);
    }
}