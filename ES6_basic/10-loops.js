export default function appendToEachArrayValue(array, appendString) {
  const result = [];
  array.forEach((value) => {
    result.push(appendString + value);
  });

  return result;
}
