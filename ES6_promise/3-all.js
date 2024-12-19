import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promise = Promise.all([uploadPhoto(), createUser()]);
  promise
    .then((response) => {
      const { body, firstName, lastName } = response.reduce((acc, item) => ({
        ...acc, ...item,
      }), {});
      console.log(body, firstName, lastName);
    });
}

handleProfileSignup();
