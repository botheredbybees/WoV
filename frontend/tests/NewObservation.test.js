import { render, screen, fireEvent } from '@testing-library/svelte'
import NewObservation from '../src/routes/observations/new/+page.svelte'
import { test, expect, vi } from 'vitest'

// Mock fetch and supabase
global.fetch = vi.fn(() => Promise.resolve({ ok: true }))
const mockSupabase = {
  storage: {
    from: () => ({
      upload: () => Promise.resolve({ data: { path: 'path/to/image.jpg' }, error: null }),
    }),
  },
}
vi.mock('$lib/supabaseClient', () => ({
  supabase: mockSupabase,
}))

test('renders new observation form and submits', async () => {
  render(NewObservation)

  // Fill out the form
  await fireEvent.input(screen.getByLabelText('Species Guess'), { target: { value: 'Test Species' } })
  await fireEvent.click(screen.getByText('Submit'))

  // Check that fetch was called
  expect(global.fetch).toHaveBeenCalled()
})
