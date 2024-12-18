export default function handleResponseFromAPI(promise) {
  promise
    /* eslint-disable no-unused-vars */
    .then((response) => ({
      status: 200,
      body: 'success',
    }))
    .catch((error) => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
