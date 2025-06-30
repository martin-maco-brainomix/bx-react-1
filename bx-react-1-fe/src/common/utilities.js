import { ApiPaths } from './constants.js'

const sendRequest = async ({ url, config = {} }) =>
  await fetch(url, config)
    .then((res) => res.json())
    .then((data) => ({ data }))
    .catch((err) => ({
      err
    }))

export const getData = async () => await sendRequest({ url: ApiPaths.getAll })

export const addNewScan = async (data) =>
  await sendRequest({ url: ApiPaths.add, config: { method: 'POST', body: JSON.stringify(data) } })

export const editScan = async (data, id) =>
  await sendRequest({
    url: `${ApiPaths.edit}/${id}/`,
    config: { method: 'POST', body: JSON.stringify(data) }
  })

export const deleteScan = async (id) =>
  await sendRequest({
    url: `${ApiPaths.delete}/${id}/`,
    config: { method: 'POST' }
  })
