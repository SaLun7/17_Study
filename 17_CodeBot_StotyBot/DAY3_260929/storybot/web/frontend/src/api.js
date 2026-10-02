export async function api(path, options = {}) {
  const response = await fetch(`/api${path}`, {
    credentials: 'same-origin',
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
  })
  const result = await response.json().catch(() => ({}))
  if (!response.ok) {
    const detail = result.detail
    throw new Error(typeof detail === 'string' ? detail : '요청을 처리하지 못했습니다. 다시 시도해 주세요.')
  }
  return result
}

export function jsonOptions(method, body) {
  return { method, body: JSON.stringify(body) }
}
