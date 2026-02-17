'use client'
import { AppShell, Card, Select } from '@forgeai/ui'
import { useEffect, useState } from 'react'
import { apiFetch } from '../../lib/api'

export default function History() {
  const [items,setItems]=useState<any[]>([])
  const [platform,setPlatform]=useState('')
  useEffect(()=>{apiFetch(`/content?platform=${platform}`).then(d=>setItems(d.items||[]))},[platform])
  return <AppShell><Card><div className="mb-3 flex gap-2"><Select value={platform} onChange={(e)=>setPlatform(e.target.value)}><option value="">All</option><option>X</option><option>LinkedIn</option><option>Instagram</option><option>Email</option><option>YouTube</option></Select></div>
  <div className="space-y-2">{items.length===0?<p className="text-zinc-400">Empty state: no content yet.</p>:items.map(i=><a key={i.id} className="block rounded-lg border border-zinc-800 p-3" href={`/history/${i.id}`}>{i.topic} · {i.platform}</a>)}</div></Card></AppShell>
}
