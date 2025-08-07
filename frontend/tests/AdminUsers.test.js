import { render, screen } from '@testing-library/svelte'
import AdminUsers from '../src/routes/admin/users/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock the fetch function
global.fetch = vi.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      { user_id: '1', username: 'tester1', email: 'tester1@example.com', role: 'scientist' },
      { user_id: '2', username: 'tester2', email: 'tester2@example.com', role: 'crew' },
    ]),
  })
)

test('renders user list', async () => {
  render(AdminUsers)

  // Wait for the component to render with the fetched data
  await screen.findByText('tester1')

  expect(screen.getByText('tester1')).toBeInTheDocument()
  expect(screen.getByText('tester2')).toBeInTheDocument()
})
