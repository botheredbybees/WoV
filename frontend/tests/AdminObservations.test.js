import { render, screen } from '@testing-library/svelte'
import AdminObservations from '../src/routes/admin/observations/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock the fetch function
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      { observation_id: '1', species_guess: 'Penguin', observed_on: '2025-01-01', latitude: -77, longitude: 166 },
      { observation_id: '2', species_guess: 'Whale', observed_on: '2025-01-02', latitude: -64, longitude: 120 },
    ]),
  })
)

test('renders observation list', async () => {
  render(AdminObservations)

  // Wait for the component to render with the fetched data
  await screen.findByText('Penguin')

  expect(screen.getByText('Penguin')).toBeInTheDocument()
  expect(screen.getByText('Whale')).toBeInTheDocument()
})
