# React

(I use react/next.js at work)

[es6](https://www.taniarascia.com/es6-syntax-and-feature-overview/)

```javascript
// Object shorthand:
const obj  {
  x,
  y
}

// Methods
const obj = {
  a(x,y){},
  b(x,y){},
}

// Destructuring
let { a, b, c } = obj;

// Array iteration

for ( let i of arr) {
  return i;
}

// Spread
let arr = [1,2,3];
let doThis = (a,b,c) => a + b + c;

doThis(...arr) => //6


// Promises exist
new Promise((resolve, reject) => {
  //
})

// async / await
```


[React Docs](https://reactjs.org/docs/hello-world.html)

```javascript
// React
const reactFunction({ spam, eggs }) => (
  <> 
    <p>The spam size: {spam.size}</p>
    <p>There are {eggs.count} eggs</p>
  </>
)

// Events
<button onClick={doFunction}>Push Me</button>

<button onClick={(e) =>doWithSomething(e)}>Push Me</button>
```

[Tailwind](https://tailwindcss.com/docs/utility-first)

Inline style classes that you pay for.
[Tailwind-Components](https://tailwindui.com/#components)

[Nextjs](https://nextjs.org/learn/basics/create-nextjs-app)

- Server Side Rendered
- page base routing
- static site generation
- initial props

[Nextjs-video](https://www.youtube.com/watch?v=rtgbaKBhdkk)
