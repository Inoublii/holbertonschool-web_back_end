export default function uploadPhoto(File) {
  return new Promise((resolve, reject) => {
    reject(Error(`${File} cannot be processed`));
  });
}
