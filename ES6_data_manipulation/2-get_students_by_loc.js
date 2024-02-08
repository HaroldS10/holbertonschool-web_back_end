export default function getStudentsByLocation(students, city) {
  const idFilter = students.filter((students) => city === students.location);
  return idFilter;
}
