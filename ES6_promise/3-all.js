/* eslint-disable import/prefer-default-export */
import { createUser, uploadPhoto } from './utils';

export async function handleProfileSignup() {
  try {
    const data = await createUser();
    const data2 = await uploadPhoto();
    console.log(`${data2.body} ${data.firstName} ${data.lastName}`);
  } catch (err) {
    console.log('Signup system offline');
  }
}
