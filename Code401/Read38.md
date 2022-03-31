# React 2

[Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)

```javascript
{isActive && (
  <Display />
)}

{isActive
  ? <DisplayActive />
  : <HideDisplay />
}

// Keys
const Component = list.map((i,idx) => (
  <li key={idx}>
    <p>{i.value}</p>
  </li>
))

// Forms
const Form = () => {(
  const handleChange = () => {
    doStuff;
  };

  return (
    <form onSubmit={handleChange}>
    <label>
      name:
      <input type='text' value={value} onChange={handleSomething} />
    </label>
    </form>
  )
)}

// textarea
<textarea>
  blah blah blah
</textarea>

// Select for dropdown
<select>
  <option value='a'>A</option>
  <option value='b'>B</option>
</select>

```

## Forms

- ev.preventDefault()
- ev.target.name: name of form item
- ev.target.value

```javascript
// update state with onChange event
setFunState = {...funState, [ev.target.name]: ev.target.value}

```

### Child Props

IOC

```javascript

const wrapperComp = (props) => (
  <div>
    {props.children}
  </div>
)

```

[Heroicons](https://heroicons.com/)
