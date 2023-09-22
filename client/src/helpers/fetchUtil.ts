const BACKEND_URL = 'http://localhost:8000'

async function getBackend(queryString: string) {
	const url = `${BACKEND_URL}/${queryString}`
	const res = await fetch(url, {
		method: 'GET',
		mode: 'cors',
	})
	return await res.json()
}

async function postBackend(body: object) {
	const res = await fetch(BACKEND_URL, {
		method: 'POST',
		body: JSON.stringify(body),
		mode: 'cors',
	})
	return await res.json()
}

export { getBackend, postBackend }
