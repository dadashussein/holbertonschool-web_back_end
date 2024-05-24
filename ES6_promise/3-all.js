/* eslint-disable import/prefer-default-export */
import { createUser, uploadPhoto } from './utils';

export function handleProfileSignup() {
  const promises = Promise.all([createUser(), uploadPhoto()]);
  promises
    .then((resolve) => {
      console.log(`${resolve[1].body} ${resolve[0].firstName} ${resolve[0].lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
