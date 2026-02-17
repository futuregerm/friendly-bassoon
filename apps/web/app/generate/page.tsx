'use client'
import { AppShell, Button, Card, Input, Select, toast } from '@forgeai/ui'
import { useForm } from 'react-hook-form'
import { apiFetch } from '../../lib/api'
import { useState, useEffect } from 'react'

export default function GeneratePage() {
  const { register, handleSubmit } = useForm<any>()
  const [result, setResult] = useState<any>()
  const [offers, setOffers] = useState<any[]>([])
  useEffect(()=>{apiFetch('/offers').then((d)=>setOffers(d.items||[])).catch(()=>{})},[])
  return <AppShell><div className="grid gap-4 lg:grid-cols-2"><Card><form className="space-y-2" onSubmit={handleSubmit(async (v)=>{setResult(await apiFetch('/content/generate',{method:'POST',body:JSON.stringify(v)}))})}>
    <Input placeholder="Topic" {...register('topic')} />
    <Input placeholder="Audience" {...register('target_audience')} />
    <Select {...register('awareness_level')}><option>Unaware</option><option>Problem-aware</option><option>Solution-aware</option><option>Product-aware</option><option>Most-aware</option></Select>
    <Select {...register('platform')}><option>X</option><option>LinkedIn</option><option>Instagram</option><option>Email</option><option>YouTube</option></Select>
    <Select {...register('objective')}><option>Growth</option><option>Sales</option><option>Authority</option><option>Lead Gen</option></Select>
    <Select {...register('offer_id')}><option value="">No Offer</option>{offers.map(o=><option key={o.id} value={o.id}>{o.generated_offer.slice(0,40)}</option>)}</Select>
    <Button className="w-full">Generate</Button></form></Card>
    <Card>{!result?<p className="animate-pulse">Run generation to see output</p>:<div className="space-y-2"><pre className="whitespace-pre-wrap text-sm">{result.generated_content}</pre><p>{result.framework_used}</p><ul>{result.triggers_used?.map((t:string)=><li key={t}>• {t}</li>)}</ul><Button onClick={()=>navigator.clipboard.writeText(result.generated_content).then(()=>toast('Copied'))}>Copy</Button><Button onClick={async ()=>{await apiFetch('/content',{method:'POST',body:JSON.stringify(result)});toast('Saved')}}>Save</Button></div>}</Card></div></AppShell>
}
