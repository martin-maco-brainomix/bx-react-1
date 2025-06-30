import { useEffect, useState } from 'react'
import { getData } from './common/utilities.js'
import { ErrorPage, HomePage, LoadingPage } from './pages'

export const App = () => {
  const [data, setData] = useState([])
  const [fetching, setFetching] = useState(true)
  const [error, setError] = useState(false)

  useEffect(() => {
    getData().then((res) => {
      setFetching(false)

      if (res.data) {
        setData(res.data)
      } else {
        setError(res.err)
      }
    })
  }, [])

  const renderLoadingPage = () => <LoadingPage />

  const renderErrorPage = () => <ErrorPage error={error} />

  const renderHomePage = () => <HomePage data={data} />

  const renderPage = () => {
    if (fetching) {
      return renderLoadingPage()
    } else if (error) {
      return renderErrorPage()
    } else {
      return renderHomePage()
    }
  }

  return <div>{renderPage()}</div>
}
