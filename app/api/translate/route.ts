import { NextRequest, NextResponse } from 'next/server';

const translationCache = new Map<string, string>();

async function translateText(text: string, target: string, source = 'auto') {
  const normalized = text.trim();
  if (!normalized) return '';

  const cacheKey = `${source}:${target}:${normalized}`;
  const cached = translationCache.get(cacheKey);
  if (cached) return cached;

  const url = new URL('https://translate.googleapis.com/translate_a/single');
  url.searchParams.set('client', 'gtx');
  url.searchParams.set('sl', source);
  url.searchParams.set('tl', target);
  url.searchParams.set('dt', 't');
  url.searchParams.set('q', normalized);

  const response = await fetch(url.toString(), {
    headers: {
      'User-Agent': 'Mozilla/5.0',
    },
    cache: 'no-store',
  });

  if (!response.ok) {
    throw new Error(`translate_http_${response.status}`);
  }

  const data = (await response.json()) as unknown[];
  const translated = Array.isArray(data?.[0])
    ? (data[0] as unknown[])
        .map((segment) => (Array.isArray(segment) ? String(segment[0] ?? '') : ''))
        .join('')
        .trim()
    : normalized;

  const finalText = translated || normalized;
  translationCache.set(cacheKey, finalText);
  return finalText;
}

export async function POST(request: NextRequest) {
  try {
    const body = (await request.json()) as { texts?: string[]; target?: string; source?: string };
    const texts = Array.isArray(body.texts)
      ? body.texts.map((text) => String(text || '').trim()).filter(Boolean).slice(0, 240)
      : [];
    const target = body.target || 'en';
    const source = body.source || 'auto';

    const translations: string[] = [];
    const batchSize = 6;

    for (let i = 0; i < texts.length; i += batchSize) {
      const batch = texts.slice(i, i + batchSize);
      const batchTranslations = await Promise.all(
        batch.map(async (text) => {
          try {
            return await translateText(text, target, source);
          } catch {
            return text;
          }
        })
      );
      translations.push(...batchTranslations);
    }

    return NextResponse.json({ translations });
  } catch {
    return NextResponse.json({ error: 'translate_failed' }, { status: 500 });
  }
}
