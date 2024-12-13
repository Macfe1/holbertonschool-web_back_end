const updateUniqueItems = (argmap) => {
  if (!argmap || !(argmap instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of argmap) {
    if (value === 1) {
      argmap.set(key, 100);
    }
  }
};

export default updateUniqueItems;
