const BACKEND_URL = 'http://localhost:8000'

async function getBackend(path: string) {
	try {
		const url = `${BACKEND_URL}/${path}`
		const res = await fetch(url, {
			method: 'GET',
			mode: 'cors',
			headers: {
				'Content-Type': 'application/json',
			},
		})

		if (res.ok) {
			return await res.json()
		} else {
			throw new Error(`HTTP error! status: ${res.status}`)
		}
	} catch (error) {
		console.error(error)
	}
}

async function postBackend(path: string, body: object) {
	try {
		const url = `${BACKEND_URL}/${path}`
		const res = await fetch(url, {
			method: 'POST',
			body: JSON.stringify(body),
			mode: 'cors',
			headers: {
				'Content-Type': 'application/json',
			},
		})

		if (res.ok) {
			return await res.json()
		} else {
			throw new Error(`HTTP error! status: ${res.status}`)
		}
	} catch (error) {
		console.error(error)
	}
}

export { getBackend, postBackend }
