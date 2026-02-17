'use client'
import { useEffect, useState } from 'react'
import { AppShell, Card } from '@forgeai/ui'
import { motion } from 'framer-motion'
import { apiFetch } from '../../lib/api'

export default function Dashboard() {
  const [items, setItems] = useState<any[]>([])
  useEffect(() => { apiFetch('/content?limit=5').then((d) => setItems(d.items || [])) }, [])
  return <AppShell>
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="grid gap-4 md:grid-cols-3">
      <Card><p>Total content generated</p><p className="text-3xl font-bold">{items.length}</p></Card>
      <Card className="md:col-span-2"><p className="mb-2 font-semibold">Quick actions</p><div className="flex gap-2"><a href="/generate">Generate Content</a><a href="/offer-builder">Offer Builder</a></div></Card>
      <Card className="md:col-span-3"><p className="mb-2 font-semibold">Recent Items</p>{items.length===0?<p className="animate-pulse text-sm text-zinc-400">No entries yet</p>:items.map((i)=><p key={i.id}>{i.topic} · {i.platform}</p>)}</Card>
    </motion.div>
  </AppShell>
}
