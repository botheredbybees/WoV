import { render, screen } from '@testing-library/svelte'
import ObservationList from '../src/routes/observations/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock the fetch function
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      { species_guess: 'Penguin', common_name: 'Emperor Penguin', observed_on: '2025-01-01', latitude: -77, longitude: 166 },
      { species_guess: 'Whale', common_name: 'Orca', observed_on: '2025-01-02', latitude: -64, longitude: 120 },
    ]),
  })
)

test('renders observation list', async () => {
  render(ObservationList)

  // Wait for the component to render with the fetched data
  await screen.findByText('Penguin')

  expect(screen.getByText('Penguin')).toBeInTheDocument()
  expect(screen.getByText('Whale')).toBeInTheDocument()
})
