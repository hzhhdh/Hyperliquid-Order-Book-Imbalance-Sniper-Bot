export function sanitizeInput(input: string): string {
  return input.replace(/[<>&'"]/g, char => ({
    '<': '&lt;', '>': '&gt;', '&': '&amp;', "'": '&#39;', '"': '&quot;'
  }[char] || char));
}
