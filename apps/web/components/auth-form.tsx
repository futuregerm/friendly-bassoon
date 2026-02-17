'use client'
import { useForm } from 'react-hook-form'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { Button, Card, Input, toast } from '@forgeai/ui'
import { apiFetch } from '../lib/api'
import { useRouter } from 'next/navigation'

const schema = z.object({ email: z.string().email(), password: z.string().min(6) })

export function AuthForm({ mode }: { mode: 'login' | 'register' }) {
  const router = useRouter()
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<z.infer<typeof schema>>({ resolver: zodResolver(schema) })

  return <Card className="mx-auto mt-20 max-w-md space-y-4">
    <h1 className="text-2xl font-bold">{mode === 'login' ? 'Welcome back' : 'Create account'}</h1>
    <form className="space-y-3" onSubmit={handleSubmit(async (values) => {
      const data = await apiFetch(`/auth/${mode}`, { method: 'POST', body: JSON.stringify(values) })
      localStorage.setItem('access_token', data.access_token)
      document.cookie = `access_token=${data.access_token}; path=/`
      toast('Authenticated')
      router.push('/dashboard')
    })}>
      <Input placeholder="Email" {...register('email')} />
      {errors.email && <p className="text-xs text-red-400">{errors.email.message}</p>}
      <Input placeholder="Password" type="password" {...register('password')} />
      <Button disabled={isSubmitting} className="w-full">{isSubmitting ? 'Loading...' : mode}</Button>
    </form>
  </Card>
}
