# React 3 Nextjs

[Nextjs Documentation](https://nextjs.org/learn/basics/create-nextjs-app)

- Built on webpack.
- Static or Server side rendering
- dynamic routing and client side prefetching

```sh
npx create-next-app <name-app>

npm run dev
```

## Navigation

- pages require an default export

## Links

Code is prefetched for pages that Link.

```javascript
import Link from 'next/link';

<Link href='/'>
  <a>Home</a>
</Link>

```

### Assets

- store static assets in the public directory
- public/images
- public directories are referenced from root of project

- Images are lazy loaded by default
- Image handles CLS

```javascript

import Image from 'next/image';


<Image 
  src='/images/fish.jpg'
  height={200}
  width={200}
  alt='a huge fish'
/>
```

### Metadata

- Head component allows head html modifications.
- Script component prevents blocking

```javascript

import Head from 'next/head';
import Script from 'next/script';

<Head>
  <title>New Title</title>
  <link rel='icon' href='/favicon.ico' />
</Head>
<Script
  src="someCDN"
  strategy="lazyOnLoad"
  onLoad={() => stuff}
/>
```

### CSS

- To use CSS Modules, the CSS file name must end with .module.css. Import into component
- Load global CSS into the _app.js page



### Tailwind with Nextjs

```sh
npm i -D tailwindcss autoprefixer postcss
```

```javascript
// create a postcss.config.js

module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
}

// tailwind.config.js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}'
  ]
}
```

[Tailwind install](https://tailwindcss.com/docs/installation)

[Why nextjs](https://www.youtube.com/watch?v=rtgbaKBhdkk)

- Choice of where to render.
- Data fetching control.
- Framework abstraction for building apps with react.
- Built in code splitting and pre rendering.
- Webpack under the hood.

### React Context

- a react hook for passing state down to all child components.
- context is an object

```javascript
import React, { useContext} from 'react';

const SomeContext = React.createContext({})

const FunComponent = () => {
  const piceOfContext = useContext(SomeContext);
  ....
}
```