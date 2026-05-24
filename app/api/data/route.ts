import { NextResponse } from 'next/server';
import data from '@/data/index.json';

export async function GET() {
  return NextResponse.json(data);
}