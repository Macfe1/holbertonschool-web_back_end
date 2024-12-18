export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const resultMath = mathFunction();
    queue.push(resultMath);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
