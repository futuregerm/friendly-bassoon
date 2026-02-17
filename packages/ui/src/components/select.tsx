import { SelectHTMLAttributes } from 'react'
import clsx from 'clsx'

export function Select({ className, ...props }: SelectHTMLAttributes<HTMLSelectElement>) {
  return <select className={clsx('w-full rounded-xl border border-zinc-700 bg-zinc-950 px-3 py-2 text-sm text-white', className)} {...props} />
}
