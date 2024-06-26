### Difference between “ == “ and “ === “ operators in JavaScript

The `==` operator (equality operator) compares two values for equality after converting both values to a common type (type coercion). The `===` operator (strict equality operator) compares both the values and their types without performing any type conversion.

**Example Scenario:**
- Using `==`:
  - `5 == '5'` returns `true` because `5` (number) is equal to `'5'` (string) after type coercion.
- Using `===`:
  - `5 === '5'` returns `false` because `5` (number) is not equal to `'5'` (string) without type conversion.

### Explain Closures in JavaScript

A closure is a function that remembers its outer variables and can access them. This is possible because functions in JavaScript form closures, which means they have access to variables in their scope chain, even after the outer function has finished executing.

**Example Scenario:**
```javascript
function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log('Outer Variable:', outerVariable);
        console.log('Inner Variable:', innerVariable);
    };
}
const newFunction = outerFunction('outside');
newFunction('inside');
```
In this example, `innerFunction` is a closure that captures and remembers `outerVariable` from `outerFunction` even after `outerFunction` has executed.

### What are callbacks in JavaScript?

Callbacks are functions passed as arguments to other functions and are executed after the completion of the outer function. They are commonly used for asynchronous operations like reading files, making API calls, or handling events.

**Example Scenario:**
```javascript
function fetchData(callback) {
    setTimeout(() => {
        console.log('Data fetched');
        callback();
    }, 2000);
}
function displayData() {
    console.log('Displaying data');
}
fetchData(displayData);
```
In this example, `displayData` is a callback function passed to `fetchData` and executed after a simulated data fetch operation.

### What is the use of promises in JavaScript?

Promises are used to handle asynchronous operations in JavaScript, providing a way to handle the result of an operation that will complete in the future. They allow for chaining multiple asynchronous operations and provide better error handling compared to callbacks.

**Example Scenario:**
```javascript
const fetchData = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Data fetched');
    }, 2000);
});
fetchData
    .then(data => {
        console.log(data);
        return 'Next step';
    })
    .then(step => {
        console.log(step);
    })
    .catch(error => {
        console.error(error);
    });
```
In this example, `fetchData` is a promise that resolves after fetching data, allowing chained `then` calls to handle the result and any potential errors.

### Explain call(), apply() and bind() methods

These methods are used to control the `this` context of functions in JavaScript.

- **call()**: Invokes a function with a given `this` value and arguments provided individually.
- **apply()**: Invokes a function with a given `this` value and arguments provided as an array.
- **bind()**: Creates a new function that, when called, has its `this` value set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.

**Example Scenario:**
```javascript
const person = {
    name: 'John',
    greet: function(greeting, punctuation) {
        console.log(greeting + ', ' + this.name + punctuation);
    }
};

// call()
person.greet.call({ name: 'Jane' }, 'Hello', '!'); // Hello, Jane!

// apply()
person.greet.apply({ name: 'Jane' }, ['Hi', '.']); // Hi, Jane.

// bind()
const greetJane = person.greet.bind({ name: 'Jane' });
greetJane('Hey', '!!'); // Hey, Jane!!
```
In this example, `call` and `apply` immediately invoke `person.greet` with a different `this` context and arguments. `bind` creates a new function with `this` bound to `{ name: 'Jane' }` that can be called later.
