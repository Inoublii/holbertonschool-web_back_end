export default function createInt8TypedArray(length, position, value) {
  try {
    const x = new ArrayBuffer(length);
    const a = new DataView(x);
    a.setInt8(position, value);
    return a;
  } catch (e) {
    throw Error('Position outside range');
  }
}
