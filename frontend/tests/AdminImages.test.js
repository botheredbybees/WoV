import { render, screen, fireEvent } from '@testing-library/svelte'
import AdminImages from '../src/routes/admin/images/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock fetch and supabase
global.fetch = vi.fn(() => Promise.resolve({ ok: true }))
const mockSupabase = {
  storage: {
    from: () => ({
      remove: () => Promise.resolve({ error: null }),
      getPublicUrl: () => ({ data: { publicUrl: 'http://example.com/image.jpg' } }),
    }),
  },
}
vi.mock('$lib/supabaseClient', () => ({
  supabase: mockSupabase,
}))

test('renders image list and deletes an image', async () => {
  // Mock the initial fetch
  global.fetch.mockResolvedValueOnce({
    json: () => Promise.resolve([
        { image_id: '1', file_path: 'path/to/image.jpg', observation_id: 1 },
    ]),
  })

  render(AdminImages)

  // Wait for the component to render with the fetched data
  await screen.findByText('path/to/image.jpg')
  expect(screen.getByText('path/to/image.jpg')).toBeInTheDocument()

  // Click the delete button
  global.confirm = () => true // Mock the confirm dialog
  await fireEvent.click(screen.getByText('Delete'))

  // Check that fetch was called for deletion
  expect(global.fetch).toHaveBeenCalledWith('http://localhost:8004/images/1', { method: 'DELETE' })
})
