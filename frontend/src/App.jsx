
import './index.css'
import Map from './Map'

function App() {
  return (
    <div className="dashboard">
      <header className="header">
        <h1>Darukaa.Earth</h1>
        <p>Geospatial Carbon & Biodiversity Analytics</p>
      </header>

      <main className="content">
        <div className="welcome">
          <h2>Dashboard</h2>
          <p>Monitor your environmental projects and sites.</p>
        </div>

       <div className="cards">
  <div className="card">
    <h3>Total Projects</h3>
    <p>1</p>
  </div>

  <div className="card">
    <h3>Total Sites</h3>
    <p>1</p>
  </div>

  <div className="card">
    <h3>Performance Score</h3>
    <p>82</p>
  </div>
</div>

<div className="map-section">
  <h2>Project Sites</h2>
  <Map />
</div>
      </main>
    </div>
  )
}

export default App