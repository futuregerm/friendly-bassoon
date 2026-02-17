import type { Config } from 'tailwindcss'

const preset: Partial<Config> = {
  darkMode: ['class'],
  theme: {
    extend: {
      colors: {
        background: '#09090b',
        foreground: '#fafafa',
        card: '#111114',
        border: '#27272a',
        primary: '#7c3aed'
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(124,58,237,.4), 0 10px 30px rgba(124,58,237,.25)'
      }
    }
  }
}

export default preset
