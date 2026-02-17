'use client'
import { AppShell, Button, Card, Input, toast } from '@forgeai/ui'
import { useForm } from 'react-hook-form'
import { apiFetch } from '../../lib/api'

export default function OfferBuilder() {
  const { register, handleSubmit } = useForm<any>()
  return <AppShell><Card><h1 className="mb-4 text-xl font-bold">Offer Builder</h1><form className="grid gap-2" onSubmit={handleSubmit(async (v)=>{await apiFetch('/offers',{method:'POST',body:JSON.stringify(v)});toast('Offer saved')})}>
    <Input placeholder="Dream outcome" {...register('dream_outcome')} /><Input placeholder="Timeframe" {...register('timeframe')} /><Input placeholder="Main objection" {...register('main_objection')} /><Input placeholder="Proof elements" {...register('proof_elements')} /><Input placeholder="Bonuses comma separated" {...register('bonuses')} />
    <Button>Create Offer</Button></form></Card></AppShell>
}
