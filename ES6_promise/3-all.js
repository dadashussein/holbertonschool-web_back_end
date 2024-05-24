/* eslint-disable import/prefer-default-export */
import { createUser, uploadPhoto } from './utils';

export function handleProfileSignup() {
  Promise.all([createUser(), uploadPhoto()])
    .then(([user, photo]) => {
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
