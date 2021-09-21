# [State and Props](https://canvas.instructure.com/courses/3385247/discussion_topics/12410576?module_item_id=52730790)

## Questions: React Lifecyle   
[React lifecyle](https://medium.com/@joshuablankenshipnola/react-component-lifecycle-events-cb77e670a093)

1. Based off the diagram, what happens first, the ‘render’ or the ‘componentDidMount’?
&nbsp;&nbsp;&nbsp;&nbsp;A: render
2. What is the very first thing to happen in the lifecycle of React?
&nbsp;&nbsp;&nbsp;&nbsp;A: a constructor function is called.
3. Put the following things in the order that they happen: componentDidMount, render, constructor, componentWillUnmount, React Updates
&nbsp;&nbsp;&nbsp;&nbsp;Answer:
    - constructor
    - render
    - componentDidMount
    - React Updates
    - componentWillUnmount

4. What does componentDidMount do?
&nbsp;&nbsp;&nbsp;&nbsp;A: componentDidMount() is invoked immmediatly after a component has been mounted/created.

## Questions: React State VS Props
[state vs props](https://www.youtube.com/watch?v=IYvD9oBCuJI)

1. What types of things can you pass in the props?
&nbsp;&nbsp;&nbsp;&nbsp;A: Any value that you could pass to a function that is handled outside of a component.
2. What is the big difference between props and state?
&nbsp;&nbsp;&nbsp;&nbsp;A: Props are handled outside of a component and passed down. State is private and managed within a component.
3. When do we re-render our application?
&nbsp;&nbsp;&nbsp;&nbsp;A: When there is a state change and new data must be displayed.
4. What are some examples of things that we could store in state?

   - Strings: "Hungry" / "Hangry"
   - Booleans: ToggleOn: false
   - Numbers: Count: 42

## Things I want to know more about

### Class Methods

- componenetDidMount()
&nbsp;&nbsp;&nbsp;&nbsp; Invoked immediatly after a component is mounted. Network requests should go here.

- shouldComponentUpdate()
&nbsp;&nbsp;&nbsp;&nbsp; Set to false will prevent default updating. Check if previous props and state have changed.

- getSnapshotBeforeUpdate()
&nbsp;&nbsp;&nbsp;&nbsp; Privious state of the DOM before anything renders.

- componenetDidUpdate()
&nbsp;&nbsp;&nbsp; Perform network requets after a change has occured.

- componentWillUnmount()
&nbsp;&nbsp;&nbsp;&nbsp; Cleanup after a componenet is unmounted.

### UNSAFE Lifecycle Events

- UNSAFE_componentWillMount() - use - componentDidMount()
- UNSAFE_componentWillUpdate() - use - getSnapshotBeforeUpdate()
- UNSAFE_ componenetWillReceiveProps() - use - getDerivedStateFromProps()
