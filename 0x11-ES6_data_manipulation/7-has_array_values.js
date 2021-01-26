export default function hasValuesFromArray(set, Arrays) {
  for (let i = 0; i < Arrays.length; i += 1) {
    if (!set.has(Arrays[i])) {
      return false;
    }
  }
  return true;
}
