# Functional Programming

[Functional Programming Concepts](https://medium.com/the-renaissance-developer/concepts-of-functional-programming-in-javascript-6bc84220d2aa)

1. What is functional programming?\
   A programming paradigm that treats computations as the evaluation of functions.

2. What is a pure function and how do we know if something is a pure function?\
   A pure function hos no side effects and always returns the same result given a set of arguments.

3. What are the benefits of a pure function?\
   Pure functions are easy to test, and predictable.

4. What is immutability?\
   An immutable object can not change state.

5. What is Referential transparency?\
   Consistent results given the same input. A guaranteed reliable result.

[Node](https://www.youtube.com/watch?v=xHLd36QoS4k)

1. What is a module?\
   A javascript file that can be imported or accessed from another file. A modular chunk of code.

2. What does the word ‘require’ do?\
   Require imports a javascript module.

3. How do we bring another module into the file the we are working in?

```javascript
const myModule = require("./myModule");
```

4. What do we have to do to make a module available?\
   A module must be labeled as an export module.

```javascript
module.exports = myModule;

// or
module.exports = { myFunction, myOtherFunction };
```

## Things I want to know more about

- Functional programming
- Regression
