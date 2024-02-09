/**
 *
 * @param {Map} mapGroceries
 * @returns
 */
export default function updateUniqueItems(mapGroceries) {
  if (!(mapGroceries instanceof Map)) {
    throw new Error('Cannot process');
  }
  mapGroceries.forEach((value, key) => {
    if (value === 1) {
      mapGroceries.set(key, 100);
    }
  });
}
