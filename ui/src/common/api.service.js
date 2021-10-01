import { CSRF_TOKEN } from "./csrf_token.js"

async function getJSON(response) {
    return (response.status === 204) ? '' : response.json()
}

function apiService(endpoint, method, data) {
    const config = {
        method: method || GET,
        body: data !== undefined ? JSON.stringify(data) : null,
        headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    }
    return fetch(endpoint, config).then(getJSON).catch(e => console.log(e))
}

export { apiService };