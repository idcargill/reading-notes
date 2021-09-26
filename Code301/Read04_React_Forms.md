
# React and Forms

[React Forms](https://reactjs.org/docs/forms.html
)

1. What is a ‘Controlled Component’?<br>
A form element that is controlled by React.

2. Should we wait to store the users responses from the form into state when they submit the form OR should we update the state with their responses as soon as they enter them? Why?<br>
By listening to on change events we can interact with user data on every key stroke.

3. How do we target what the user is entering if we have an event handler on an input field?
<br>By using the even target passed to a handler function we can access the event target properties.
> event.target.value

[Ternary Operator Explained](https://codeburst.io/javascript-the-conditional-ternary-operator-explained-cac7218beeff)

1. Why would we use a ternary operator?<br>
Ternary operators result in cleaner and more condensed code than traditional if statements.

2. Rewrite the following statement using a 
ternary statement:

```javascript
// Traditional If statement
  if(x===y){
 console.log(true);
  } else {
 console.log(false);
  }

// Ternary Operator
x ? console.log(true) : console.log(false);
```

### Further Reading

[React Bootstrap - Forms](https://react-bootstrap.github.io/components/forms/)

[React - conditional rendering](https://reactjs.org/docs/conditional-rendering.html)

## Things I want to know more aboout

- Events
