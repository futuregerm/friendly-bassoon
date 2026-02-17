import Link from 'next/link'
import { ReactNode } from 'react'

const links = [
  ['Dashboard', '/dashboard'],
  ['Generate', '/generate'],
  ['Offer Builder', '/offer-builder'],
  ['History', '/history']
]

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-violet-950 text-white">
      <div className="mx-auto flex max-w-7xl gap-4 p-4">
        <aside className="hidden w-60 rounded-2xl border border-zinc-800 bg-zinc-900/70 p-4 backdrop-blur md:block">
          <p className="mb-4 text-lg font-bold">ForgeAI</p>
          <nav className="space-y-2">
            {links.map(([label, href]) => (
              <Link key={href} href={href} className="block rounded-lg px-3 py-2 text-sm hover:bg-zinc-800">
                {label}
              </Link>
            ))}
          </nav>
        </aside>
        <main className="flex-1 rounded-2xl border border-zinc-800 bg-zinc-900/40 p-4 backdrop-blur">{children}</main>
      </div>
    </div>
  )
}
