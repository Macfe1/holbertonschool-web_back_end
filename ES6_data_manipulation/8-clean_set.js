const cleanSet = (set, startString) => {
  if (!startString || typeof startString !== 'string') return '';

  const result = [];
  for (const items of set) {
    if (items.startsWith(startString)) {
      result.push(items.slice(startString.length));
    }
  }

  return result.join('-');
};

export default cleanSet;
