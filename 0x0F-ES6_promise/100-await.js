import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let ph;
  let user;
  try {
    ph = await uploadPhoto();
    user = await createUser();
  } catch (e) {
    ph = null;
    user = null;
  }
  return { photo: ph, user };
}
