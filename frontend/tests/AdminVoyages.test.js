import { render, screen } from '@testing-library/svelte'
import AdminVoyages from '../src/routes/admin/voyages/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock the fetch function
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      { voyage_id: '1', name: 'Voyage 1', region: 'Antarctica', start_date: '2025-01-01', end_date: '2025-03-01' },
      { voyage_id: '2', name: 'Voyage 2', region: 'Southern Ocean', start_date: '2025-06-01', end_date: '2025-07-01' },
    ]),
  })
)

test('renders voyage list', async () => {
  render(AdminVoyages)

  // Wait for the component to render with the fetched data
  await screen.findByText('Voyage 1')

  expect(screen.getByText('Voyage 1')).toBeInTheDocument()
  expect(screen.getByText('Voyage 2')).toBeInTheDocument()
})
