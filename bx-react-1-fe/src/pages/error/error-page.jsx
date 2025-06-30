export const ErrorPage = ({ error }) => {
  const renderError = () => {
    return error.message
  }

  return (
    <div>
      <h1>This is fallback page</h1>
      {renderError()}
    </div>
  )
}
