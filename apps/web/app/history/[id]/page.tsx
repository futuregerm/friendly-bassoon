'use client'
import { useEffect, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { AppShell, Button, Card, toast } from '@forgeai/ui'
import { apiFetch } from '../../../lib/api'

export default function HistoryDetail() {
  const { id } = useParams<{id:string}>(); const [item,setItem]=useState<any>(); const r=useRouter()
  useEffect(()=>{apiFetch(`/content/${id}`).then(setItem)},[id])
  if(!item) return <AppShell><Card className="animate-pulse">Loading skeleton...</Card></AppShell>
  return <AppShell><Card><pre className="whitespace-pre-wrap">{item.generated_content}</pre><div className="mt-3 flex gap-2"><Button onClick={async()=>{await apiFetch(`/content/${id}/regenerate`,{method:'POST'});toast('Regenerated')}}>Regenerate</Button><Button onClick={async()=>{await apiFetch(`/content/${id}`,{method:'DELETE'});r.push('/history')}}>Delete</Button></div></Card></AppShell>
}
