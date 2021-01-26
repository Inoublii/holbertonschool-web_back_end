export default function updateStudentGradeByCity(students, city, newGrades) {
  if (Array.isArray(students) === false) {
    return [];
  }
  /* eslint-disable no-param-reassign */
  return students.filter((x) => x.location === city).map((x) => {
    x.grade = 'N/A';
    for (const a of newGrades) {
      if (a.studentId === x.id) {
        x.grade = a.grade;
      }
    }
    return x;
  });
}
