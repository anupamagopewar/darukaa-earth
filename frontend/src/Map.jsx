import { useEffect, useRef, useState } from 'react'
import mapboxgl from 'mapbox-gl'
import 'mapbox-gl/dist/mapbox-gl.css'
import '@mapbox/mapbox-gl-draw/dist/mapbox-gl-draw.css'
import axios from 'axios'
import MapboxDraw from '@mapbox/mapbox-gl-draw'
import AnalyticsChart from './AnalyticsChart'

mapboxgl.accessToken = import.meta.env.VITE_MAPBOX_TOKEN
console.log('MAPBOX SUPPORTED:', mapboxgl.supported())
console.log('MAPBOX TOKEN FOUND:', !!mapboxgl.accessToken)
function Map() {
  const mapContainer = useRef(null)
  const map = useRef(null)
  const [analytics, setAnalytics] = useState([])

  useEffect(() => {
    if (map.current) return
      console.log('MAP COMPONENT STARTED')
    map.current = new mapboxgl.Map({
      container: mapContainer.current,
      style: 'mapbox://styles/mapbox/streets-v12',
      center: [77.5946, 12.9716],
      zoom: 10,
    })
    
    map.current.on('load', async () => {
  console.log('MAPBOX MAP LOADED SUCCESSFULLY')

  const response = await axios.get('http://127.0.0.1:8000/sites/')
  const sites = response.data

  console.log('SITES FROM BACKEND:', sites)

  sites.forEach((site) => {
    map.current.addSource(`site-${site.id}`, {
      type: 'geojson',
      data: site.geometry,
    })

    map.current.addLayer({
      id: `site-${site.id}`,
      type: 'fill',
      source: `site-${site.id}`,
      paint: {
        'fill-opacity': 0.4,
      },
    })

    const coordinates = site.geometry.coordinates[0]

const bounds = coordinates.reduce(
  (bounds, coordinate) => bounds.extend(coordinate),
  new mapboxgl.LngLatBounds(coordinates[0], coordinates[0])
)

map.current.fitBounds(bounds, {
  padding: 50,
  maxZoom: 15,
})

map.current.on('click', `site-${site.id}`, async () => {
  const response = await axios.get(
    `http://127.0.0.1:8000/analytics/${site.id}`
  )

  setAnalytics(response.data)

  new mapboxgl.Popup()
    .setLngLat(map.current.getCenter())
    .setHTML(`
      <h3>${site.name}</h3>
      <p><strong>Area:</strong> ${site.area}</p>
      <p>${site.description}</p>
    `)
    .addTo(map.current)
})

    map.current.addLayer({
      id: `site-${site.id}-outline`,
      type: 'line',
      source: `site-${site.id}`,
      paint: {
        'line-width': 3,
      },
    })
  })
})

  map.current.on('error', (event) => {
    console.error('MAPBOX ERROR:', event.error)
  })


   

map.current = new mapboxgl.Map({
  container: mapContainer.current,
  style: 'mapbox://styles/mapbox/streets-v12',
  center: [77.5946, 12.9716],
  zoom: 10,
})

map.current.addControl(new mapboxgl.NavigationControl(), 'top-right')

const draw = new MapboxDraw({
  displayControlsDefault: false,
  controls: {
    polygon: true,
    trash: true,
  },
})

map.current.addControl(draw, 'top-left')

map.current.on('draw.create', async (event) => {
  const feature = event.features[0]

  console.log('DRAWN POLYGON:', feature.geometry)

  try {
    const response = await axios.post('http://127.0.0.1:8000/sites/', {
      project_id: 1,
      name: `New Site ${Date.now()}`,
      description: 'Site created from map',
      area: null,
      geometry: feature.geometry,
    })

    console.log('SITE SAVED:', response.data)

    alert('Site saved successfully!')
  } catch (error) {
    console.error('SAVE SITE ERROR:', error)
    alert('Failed to save site')
  }
})
    return () => {
  if (map.current) {
    map.current.remove()
    map.current = null
  }
}
  }, [])

  return (
  <div>
    <div ref={mapContainer} className="map-container" />

    {analytics.length > 0 && (
      <div className="analytics-chart">
        <h3>Site Performance Over Time</h3>
        <AnalyticsChart analytics={analytics} />
      </div>
    )}
  </div>
)
}

export default Map