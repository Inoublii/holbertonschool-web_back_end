export default function createIteratorObject(report) {
  const x = [];
  for (const a of Object.keys(report.allEmployees)) {
    x.push(...report.allEmployees[a]);
  }
  return x;
}
