export const getData = async () =>
  await fetch('https://jsonplaceholder.typicode.com/photos?_limit=50')
    .then((res) => res.json())
    .then((data) => ({ data }))
    .catch((err) => ({
      err
    }))
