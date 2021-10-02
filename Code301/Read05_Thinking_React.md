# Putting it all Together

## Thinking in React

[Thinking in React](https://reactjs.org/docs/thinking-in-react.html)

1. What is the single responsibility principle and how does it apply to components?\
   Components should do only one thing.

2. What does it mean to build a ‘static’ version of your application?\
   A static build will not handle user interaction, but will layout the component framework.

3. Once you have a static application, what do you need to add?\
   The use of state to manage user interactions.

4. What are the three questions you can ask to determine if something is state?\
   If yes then it's not state.

   - Is it passed in via props?
   - Does it remain unchanged overtime?
   - Can you compute it base on other state or props?

5. How can you identify where state needs to live?\
   If state is shared between child components or is passed in via props, then state must live in a higher/parent component.

## Higher Order Functions

[Higher-Order Functions](https://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK)

1. What is a “higher-order function”?\
   Functions that take in other functions as arguments.

2. Explore the greaterThan function as defined in the reading. In your own words, what is line 2 of this function doing?

[MPJ - Currying](https://www.youtube.com/watch?v=iZLP4qOwY8I&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=6)\
[Currying: returning nested functions](https://blog.bitsrc.io/understanding-currying-in-javascript-ceb2188c339)

The function greaterThan is returning a function that takes in an argument.

```javascript
// Returning nested functions "Currying"
function greaterThan(n) {
  return (m) => m > n;
}
// greater than returns an anonymous function
greaterThan(11); // (m) => m > n

// greaterThan10 is now a function that passes arguments into a function
let greaterThan10 = greaterThan(10);
greaterThan10(11); // true
```

3. Explain how either map or reduce operates, with regards to higher-order functions.\
   Array methods map() and reduce take in a function as parameter. They then apply the supplied function to each element of the array.  
   [Array map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)\
   [Array Iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/@@iterator)

## Things I want to know more about

- Higher order functions that return functions.
- Currying
