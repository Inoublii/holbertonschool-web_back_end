export default function cleanSet(set, startString) {
  const str = [];
  if (typeof startString !== 'string' || startString === '') {
    return '';
  }

  set.forEach((x) => {
    if (x && x.startsWith(startString)) {
      str.push(x.substr(startString.length));
    }
  });

  return str.join('-');
}
