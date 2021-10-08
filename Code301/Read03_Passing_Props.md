# Passing Functions as Props

## [List and Keys - React Docs](https://reactjs.org/docs/lists-and-keys.html)

1. What does .map() return?<br>
   &nbsp;&nbsp;The map method perfomrs code on each array item and returns an array of equal lenght.

2. If I want to loop through an array and display each value in JSX, how do I do that in React?

```javascript
// code can be wrappped in brakcets of the render function
{arr.map(i) => (
    <li key={i.id}>{i.value}</li>
    )
}

// Or build a new array and render the results - This may be cleaner code
let NewJsxArray = arr.map((i) => {
    return (
        <li key={i.id}>{i.value}</li>
    )
})

render() {
    <ul>
    <NewJsxArray />
    </ul>
}
```

3. Each item needs a unique?<br>
   &nbsp;&nbsp; Key

4. What is the purpose of a key?<br>
   &nbsp;&nbsp;Keys tell react which elements have changed so react knows when and what to render.

## [Spread Operator](https://medium.com/coding-at-dawn/how-to-use-the-spread-operator-in-javascript-b9e4a8b06fab)

1. What is the spread operator? <br>
   &nbsp;&nbsp;The spread operator will expand an object into individual items that can be passed as arguments.

```javascript
    // spread operator
    ...
    // The calling each item of an array individually.
    function doStuffToEachItem(...array)
```

2. List 4 things that the spread operator can do.

- Pass items form an object one by one into a function call.
- Concatenating arrays.
- Pass arguments to Math functions.
- Add items to a list

3. Give an example of using the spread operator to combine two arrays.

```javascript
// Concatenating arrays
const arr1 = ["cat", "bat", "shark"];
const arr2 = ["tiger", "batman", "sharknado"];
const newArr = [...arr1, ...arr2];
// results newArr = ['cat', 'bat', 'shark', 'tiger', 'batman', 'sharknado']
```

4. Give an example of using the spread operator to add a new item to an array.

```javascript
// Adding and item to an array
const arr1 = ["cat", "kitten", "tiger"];
const newItem = "shark";
const newArr = [...arr1, newItem];

// newArr = [ 'cat', 'kitten', 'tiger', 'shark' ]
```

5. Give an example of using the spread operator to combine two objects into one.

```javascript
// Combine 2 objects into 1
const obj1 = { animal: "cat", weapon: "claws of death" };
const obj2 = { job: "napping hard", hobby: "Hating People" };
const newObj = { ...obj1, ...obj2 };

/* newObj = {
    animal: 'cat',
    weapon: 'claws of death',
    job: 'napping hard',
    hobby: 'Hating People'
}
*/
```

## [Passing Functions Between Components](https://www.youtube.com/watch?v=c05OL7XbwXU)

1. In the video, what is the first step that the developer does to pass functions between components?<br>
   &nbsp;&nbsp;Create a function at the state level to update state.

2. In your own words, what does the increment function do?<br>
   &nbsp;&nbsp;The increment function takes in an a name that was &passed to a child component and is able to update the state located in the parent component.

3. How can you pass a method from a parent component into a child component?<br>
   &nbsp;&nbsp;The same way as passing a prop to a child element.

4. How does the child component invoke a method that was passed to it from a parent component?<br>
   &nbsp;&nbsp;this.props.ParentMethod

## Things I want to konw more about

- Spread operator
- State management
- Markdown tricks

## Further Reading

[React Tutorial](https://reactjs.org/tutorial/tutorial.html)

[Lifting up State](https://reactjs.org/docs/lifting-state-up.html)
