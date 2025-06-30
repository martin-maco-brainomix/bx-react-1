export const HomePage = ({ data }) => {
  const renderData = () => {
    return JSON.stringify(data)
  }

  return (
    <div>
      <h1>This is home page</h1>
      {renderData()}
    </div>
  )
}
