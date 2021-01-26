export default function hasValuesFromArray(set, arrays) {
  return arrays.filter((x) => set.has(x)).length === arrays.length;
}
