import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(req: NextRequest) {
  const protectedPaths = ['/dashboard', '/generate', '/offer-builder', '/history']
  if (protectedPaths.some((p) => req.nextUrl.pathname.startsWith(p))) {
    const token = req.cookies.get('access_token')
    if (!token) return NextResponse.redirect(new URL('/login', req.url))
  }
  return NextResponse.next()
}
