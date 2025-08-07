import { render, screen } from '@testing-library/svelte'
import Navbar from '../src/lib/components/Navbar.svelte'
import { test, expect } from 'vitest'

test('renders navbar with links', () => {
  render(Navbar)

  expect(screen.getByText('Home')).toBeInTheDocument()
  expect(screen.getByText('Observations')).toBeInTheDocument()
  expect(screen.getByText('Admin')).toBeInTheDocument()
})
