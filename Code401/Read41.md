# React 4 Dynamic Routing

## getStaticProps

- export an async getStaticProps with page component
- getStaticProps runs at build time and collects data before rendering HTML
- Static Generation is pre rendering HTML at build time.
- Server Side Rendering is a pre rendering method that generates the HTML on request.

## Dynamic Routes

- page path depends on external data
- getStaticPaths exported with page

Page Must contain:

- A component
- getStaticPaths: which returns possible route params
- getStaticProps: which fetches the data with route params
- pages/[variable].js


### Router

```javascript
// Dynamic Routing with useRouter
import { useRouter } from 'next/router';

const DisplayItem = ({ obj }) => {
  const router = useRouter();

  const id = router.query.id;

  return (
    <h1>Dynamic Route {id}</h1>
  )
}
export default DisplayItem
```

### Static Paths

```javascript
const data = [{id: 1,name: 'frank'},{id: 2,name: 'Jo'}];
export async function getStaticPaths() {
  const mapped = data.map((i) => ({params: {id: i.id.toString()}}));
  return {
    paths: mapped,
    fallback: false
  }
}

export async function getStaticProps(context) {
  const id = context.params.id;
  const filteredData = data.filter((i) => i.id == id)
  return {
    props: {
      propData:filteredData
    }
  }
}

const DisplayItem = ({ propData }) => {
  const person = propData[0];
  return (
    <>
      <h1>Dynamic Route {person.name}</h1>
      <p>{person.id}</p>
    </>
  )
}

export default DisplayItem

```

[nextjs 10](https://www.youtube.com/watch?v=JWCS5IdECVI)

- Optimized images


### Static Files

> public/images/

```javascript
import Image from 'next/image'

const Pic = () => (
  <Image
    src="image/me.png"
    alt="image of a fish"
    width="100"
    height="100"
  />
)

```

### Local Environment Variables

> .env.local  will override defaults

> .env.development

> .env.production



