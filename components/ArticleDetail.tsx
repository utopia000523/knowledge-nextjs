'use client';

import { useEffect, useMemo, useRef, useState } from 'react';
import { marked } from 'marked';
import { jsonrepair } from 'jsonrepair';

interface Article {
  id: string;
  category: string;
  title: string;
  keywords: string[];
  summary: string;
  importance: number;
  learned_at: string;
  source: string;
  file: string;
}

interface ArticleDetailProps {
  article: Article;
  isRead: boolean;
  onToggleRead: (articleId: string) => void;
  onClose: () => void;
}

interface ReviewEntry {
  content: string;
  wordCount: number;
  createdAt: string;
}

interface HighlightEntry {
  id: string;
  quote: string;
  comment: string;
  createdAt: string;
}

interface TocItem {
  key: string;
  title: string;
  level: number;
}

interface SelectionDraft {
  quote: string;
  comment: string;
  x: number;
  y: number;
}

function getReviews(): Record<string, ReviewEntry> {
  try {
    const stored = localStorage.getItem('knowledge_reviews');
    return stored ? JSON.parse(stored) : {};
  } catch {
    return {};
  }
}

function saveReviews(reviews: Record<string, ReviewEntry>) {
  try {
    localStorage.setItem('knowledge_reviews', JSON.stringify(reviews));
  } catch {}
}

function getHighlights(): Record<string, HighlightEntry[]> {
  try {
    const stored = localStorage.getItem('knowledge_highlights');
    return stored ? JSON.parse(stored) : {};
  } catch {
    return {};
  }
}

function saveHighlights(highlights: Record<string, HighlightEntry[]>) {
  try {
    localStorage.setItem('knowledge_highlights', JSON.stringify(highlights));
  } catch {}
}

function getBilingualPreference(): boolean {
  try {
    const stored = localStorage.getItem('knowledge_bilingual_enabled');
    return stored === 'true';
  } catch {
    return false;
  }
}

function countWords(text: string): number {
  if (!text) return 0;
  const chinese = (text.match(/[\u4e00-\u9fa5]/g) || []).length;
  const english = text
    .replace(/[\u4e00-\u9fa5]/g, '')
    .split(/\s+/)
    .filter((word) => word.length > 0).length;
  return chinese + english;
}

function formatKey(key: string, language = 'zh-CN'): string {
  const isEnglish = language.toLowerCase().startsWith('en');
  const keyMap: Record<string, { zh: string; en: string }> = {
    core_formula: { zh: '核心公式', en: 'Core Framework' },
    layers: { zh: '方法论分层', en: 'Framework Layers' },
    updates: { zh: '更新日志', en: 'Update Log' },
    summary: { zh: '内容摘要', en: 'Summary' },
    methodology: { zh: '方法论正文', en: 'Methodology' },
    content: { zh: '正文内容', en: 'Content' },
  };

  if (keyMap[key]) {
    return isEnglish ? keyMap[key].en : keyMap[key].zh;
  }

  const fallback = key.replace(/_/g, ' ').replace(/\b\w/g, (letter) => letter.toUpperCase());
  return isEnglish ? fallback : fallback;
}

function normalizeText(text: string): string {
  return text.replace(/\s+/g, ' ').trim();
}

function collectContentStrings(value: unknown, bucket = new Set<string>()) {
  if (!value) return bucket;

  if (typeof value === 'string') {
    const normalized = value.trim();
    if (normalized.length >= 2) bucket.add(value);
    return bucket;
  }

  if (Array.isArray(value)) {
    value.forEach((item) => collectContentStrings(item, bucket));
    return bucket;
  }

  if (typeof value === 'object') {
    Object.values(value).forEach((item) => collectContentStrings(item, bucket));
  }

  return bucket;
}

function replaceContentStrings(value: unknown, translations: Record<string, string>): unknown {
  if (typeof value === 'string') {
    return translations[value] || value;
  }

  if (Array.isArray(value)) {
    return value.map((item) => replaceContentStrings(item, translations));
  }

  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value).map(([key, item]) => [key, replaceContentStrings(item, translations)])
    );
  }

  return value;
}

function isMostlyChinese(text: string): boolean {
  const chinese = (text.match(/[\u4e00-\u9fa5]/g) || []).length;
  const letters = (text.match(/[A-Za-z]/g) || []).length;
  return chinese >= letters;
}

function extractTOC(content: unknown, language = 'zh-CN'): TocItem[] {
  const toc: TocItem[] = [];
  if (!content || typeof content !== 'object') return toc;

  if ('layers' in content && Array.isArray((content as { layers?: unknown[] }).layers)) {
    (content as { layers: Array<{ title?: string; level?: number }> }).layers.forEach((item, idx) => {
      if (item.title) {
        toc.push({ key: `layer-${idx}`, title: item.title, level: item.level || 1 });
      }
    });
  }

  Object.entries(content).forEach(([key, value]) => {
    if (key !== 'layers' && key !== 'updates') {
      const title = typeof value === 'string' && value.length < 50 ? value : formatKey(key, language);
      toc.push({ key: `section-${key}`, title, level: 1 });
    }
  });

  return toc;
}

function renderMarkdown(markdown: string) {
  const html = marked.parse(markdown, {
    gfm: true,
    breaks: true,
  }) as string;

  return (
    <div
      className="prose prose-invert kb-markdown max-w-none text-gray-300 prose-sm leading-relaxed"
      dangerouslySetInnerHTML={{ __html: html }}
    />
  );
}

function parseArticlePayload(rawText: string) {
  try {
    return JSON.parse(rawText) as Record<string, unknown>;
  } catch {
    try {
      return JSON.parse(jsonrepair(rawText)) as Record<string, unknown>;
    } catch {
      const decode = (value: string) =>
        value
          .replace(/\\n/g, '\n')
          .replace(/\\r/g, '\r')
          .replace(/\\t/g, '\t')
          .replace(/\\"/g, '"')
          .replace(/\\\\/g, '\\');

      const layerRegex = /\\?"level\\?":\s*(\d+)\s*,\s*\\?"title\\?":\s*"([\s\S]*?)"\s*,\s*\\?"content\\?":\s*"([\s\S]*?)"/g;
      const layers = Array.from(rawText.matchAll(layerRegex)).map((match) => ({
        level: Number(match[1] || 1),
        title: decode(match[2] || ''),
        content: decode(match[3] || ''),
      }));

      const coreFormulaMatch = rawText.match(/\\?"core_formula\\?":\s*\\?"([\s\S]*?)"/);

      return {
        content: {
          ...(coreFormulaMatch ? { core_formula: decode(coreFormulaMatch[1]) } : {}),
          layers,
        },
      } as Record<string, unknown>;
    }
  }
}

function renderContent(obj: unknown, depth = 0, language = 'zh-CN'): React.ReactNode {
  if (!obj) return null;

  if (typeof obj === 'string') {
    return renderMarkdown(obj);
  }

  if (Array.isArray(obj)) {
    if (obj[0] && typeof obj[0] === 'object' && 'title' in obj[0] && 'level' in obj[0]) {
      return (
        <div className="space-y-5">
          {obj.map((item, idx) => {
            const section = item as { title: string; level: number; content: unknown };
            return (
              <section key={idx} id={`layer-${idx}`} className="rounded-2xl border border-white/6 bg-white/[0.02] p-4">
                <h4
                  className={`mb-3 font-semibold ${
                    section.level === 1
                      ? 'text-xl text-white'
                      : section.level === 2
                        ? 'text-base text-indigo-200'
                        : 'text-sm text-purple-200'
                  }`}
                >
                  {section.title}
                </h4>
                {renderContent(section.content, depth + 1, language)}
              </section>
            );
          })}
        </div>
      );
    }

    return (
      <ul className="list-disc pl-5 text-gray-300">
        {obj.map((item, idx) => (
          <li key={idx} className="mb-1.5">{renderContent(item, depth + 1, language)}</li>
        ))}
      </ul>
    );
  }

  if (typeof obj === 'object') {
    return (
      <div className="space-y-4">
        {Object.entries(obj).map(([key, value], idx) => (
          <section key={idx} id={`section-${key}`} className="rounded-2xl border border-white/6 bg-white/[0.02] p-4">
            <h4 className="mb-2 text-base font-semibold text-indigo-200">{formatKey(key, language)}</h4>
            {renderContent(value, depth + 1, language)}
          </section>
        ))}
      </div>
    );
  }

  return null;
}

function unwrapGeneratedHighlights(root: HTMLElement) {
  root.querySelectorAll('.kb-inline-highlight').forEach((node) => {
    const parent = node.parentNode;
    if (!parent) return;
    parent.replaceChild(document.createTextNode(node.textContent || ''), node);
    parent.normalize();
  });
}

function clearGeneratedTranslations(root: HTMLElement) {
  root.querySelectorAll('.kb-translation-block').forEach((node) => node.remove());
  root.querySelectorAll('[data-bilingual-source="true"]').forEach((node) => {
    node.classList.remove('hidden');
    node.removeAttribute('data-bilingual-source');
    node.removeAttribute('data-bilingual-id');
  });
}

function collectTranslationBlocks(root: HTMLElement): HTMLElement[] {
  const candidates = Array.from(root.querySelectorAll('h1, h2, h3, h4, h5, h6, p, li, blockquote, td, th')) as HTMLElement[];

  return candidates.filter((node) => {
    if (
      node.closest('.kb-translation-block') ||
      node.closest('pre') ||
      node.closest('code') ||
      node.closest('.kb-mermaid') ||
      node.closest('button') ||
      node.closest('aside')
    ) {
      return false;
    }

    const text = normalizeText(node.innerText || node.textContent || '');
    if (text.length < 8) return false;

    const childrenWithText = Array.from(node.children).filter((child) => normalizeText(child.textContent || '').length >= 8);
    return childrenWithText.length === 0;
  });
}

function applyHighlightsToRoot(root: HTMLElement, highlights: HighlightEntry[]) {
  unwrapGeneratedHighlights(root);

  highlights.forEach((highlight) => {
    const quote = normalizeText(highlight.quote);
    if (!quote) return;

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const parent = node.parentElement;
        if (!parent) return NodeFilter.FILTER_REJECT;
        if (
          parent.closest('script') ||
          parent.closest('style') ||
          parent.closest('code') ||
          parent.closest('pre') ||
          parent.closest('.kb-translation-block')
        ) {
          return NodeFilter.FILTER_REJECT;
        }

        return normalizeText(node.textContent || '').length > 0 ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      },
    });

    let current = walker.nextNode() as Text | null;
    while (current) {
      const source = current.textContent || '';
      const compactSource = normalizeText(source);
      const compactIndex = compactSource.indexOf(quote);
      if (compactIndex !== -1) {
        const exactIndex = source.indexOf(highlight.quote);
        const start = exactIndex !== -1 ? exactIndex : source.indexOf(quote);
        if (start !== -1) {
          const end = start + (exactIndex !== -1 ? highlight.quote.length : quote.length);
          const before = current.splitText(start);
          const after = before.splitText(end - start);
          const mark = document.createElement('mark');
          mark.className = 'kb-inline-highlight rounded px-1.5 py-0.5 text-amber-100';
          mark.dataset.highlightId = highlight.id;
          mark.title = highlight.comment;
          mark.textContent = before.textContent;
          before.parentNode?.replaceChild(mark, before);
          current = after;
          break;
        }
      }
      current = walker.nextNode() as Text | null;
    }
  });
}

export default function ArticleDetail({ article, isRead, onToggleRead, onClose }: ArticleDetailProps) {
  const [content, setContent] = useState<unknown>(null);
  const [loading, setLoading] = useState(true);
  const [activeSection, setActiveSection] = useState<string | null>(null);
  const [showReviewEditor, setShowReviewEditor] = useState(false);
  const [mobileTocOpen, setMobileTocOpen] = useState(false);
  const [isMobileViewport, setIsMobileViewport] = useState(() => {
    if (typeof window === 'undefined') return false;
    return window.matchMedia('(max-width: 639px)').matches;
  });
  const [reviewContent, setReviewContent] = useState('');
  const [reviews, setReviews] = useState<Record<string, ReviewEntry>>(() => {
    if (typeof window === 'undefined') return {};
    return getReviews();
  });
  const [highlights, setHighlights] = useState<Record<string, HighlightEntry[]>>(() => {
    if (typeof window === 'undefined') return {};
    return getHighlights();
  });
  const [hasReview, setHasReview] = useState(false);
  const [selectionDraft, setSelectionDraft] = useState<SelectionDraft | null>(null);
  const [bilingualEnabled, setBilingualEnabled] = useState(() => {
    if (typeof window === 'undefined') return false;
    return getBilingualPreference();
  });
  const [translatedContent, setTranslatedContent] = useState<unknown>(null);
  const [translationLoading, setTranslationLoading] = useState(false);
  const [translationError, setTranslationError] = useState('');
  const contentRef = useRef<HTMLDivElement | null>(null);
  const translationCacheRef = useRef<Record<string, string>>({});
  const articleLanguageIsChinese = useMemo(
    () => isMostlyChinese(`${article.title} ${article.summary}`),
    [article.summary, article.title]
  );

  const articleHighlights = useMemo(() => highlights[article.id] || [], [article.id, highlights]);
  const bilingualActive = bilingualEnabled && !isMobileViewport;
  const displayLanguage = bilingualActive
    ? articleLanguageIsChinese
      ? 'en'
      : 'zh-CN'
    : articleLanguageIsChinese
      ? 'zh-CN'
      : 'en';
  const renderedContent = bilingualActive && translatedContent ? translatedContent : content;

  useEffect(() => {
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = '';
    };
  }, []);

  useEffect(() => {
    const mobileQuery = window.matchMedia('(max-width: 639px)');
    const updateMobileViewport = () => setIsMobileViewport(mobileQuery.matches);

    updateMobileViewport();
    if (mobileQuery.addEventListener) {
      mobileQuery.addEventListener('change', updateMobileViewport);
    } else {
      mobileQuery.addListener(updateMobileViewport);
    }

    return () => {
      if (mobileQuery.removeEventListener) {
        mobileQuery.removeEventListener('change', updateMobileViewport);
      } else {
        mobileQuery.removeListener(updateMobileViewport);
      }
    };
  }, []);

  useEffect(() => {
    const loadedReviews = getReviews();
    const loadedHighlights = getHighlights();
    setReviews(loadedReviews);
    setHighlights(loadedHighlights);
    setHasReview(Boolean(loadedReviews[article.id]));
    setReviewContent(loadedReviews[article.id]?.content || '');
    setLoading(true);
    setActiveSection(null);
    setMobileTocOpen(false);
    setSelectionDraft(null);
    setTranslationError('');
    setTranslatedContent(null);

    const loadContent = async () => {
      try {
        const res = await fetch(`/data/${article.file}`);
        if (res.ok) {
          const rawText = await res.text();
          const data = parseArticlePayload(rawText);
          setContent(data.content || data.methodology || data);
        } else {
          setContent(article.summary);
        }
      } catch {
        setContent(article.summary);
      }
      setLoading(false);
    };

    loadContent();
  }, [article]);

  useEffect(() => {
    const handleEsc = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setSelectionDraft(null);
        onClose();
      }
    };
    window.addEventListener('keydown', handleEsc);
    return () => window.removeEventListener('keydown', handleEsc);
  }, [onClose]);

  useEffect(() => {
    const enhanceRichBlocks = async () => {
      if (!contentRef.current) return;

      contentRef.current.querySelectorAll('table').forEach((table) => {
        if (!table.parentElement?.classList.contains('kb-table-wrap')) {
          const wrapper = document.createElement('div');
          wrapper.className = 'kb-table-wrap';
          table.parentNode?.insertBefore(wrapper, table);
          wrapper.appendChild(table);
        }
      });

      const mermaidNodes = Array.from(
        contentRef.current.querySelectorAll('pre code.language-mermaid, pre code.lang-mermaid')
      );

      if (mermaidNodes.length === 0) return;

      const mermaid = (await import('mermaid')).default;
      mermaid.initialize({
        startOnLoad: false,
        theme: 'dark',
        securityLevel: 'loose',
        themeVariables: {
          primaryColor: '#172554',
          primaryTextColor: '#e2e8f0',
          primaryBorderColor: '#818cf8',
          lineColor: '#38bdf8',
          secondaryColor: '#0f172a',
          tertiaryColor: '#111827',
          background: '#0b1120',
          mainBkg: '#0f172a',
          nodeBorder: '#818cf8',
          clusterBkg: '#111827',
          clusterBorder: '#334155',
          edgeLabelBackground: '#0f172a',
          fontFamily: 'inherit',
        },
        flowchart: {
          useMaxWidth: true,
          htmlLabels: true,
          curve: 'basis',
        },
      });

      await Promise.all(
        mermaidNodes.map(async (node, idx) => {
          const source = node.textContent?.trim();
          const pre = node.closest('pre');
          if (!source || !pre || pre.dataset.enhanced === 'true') return;

          const chart = document.createElement('div');
          chart.className = 'kb-mermaid';

          try {
            const id = `mermaid-${article.id.replace(/[^a-zA-Z0-9_-]/g, '-')}-${idx}`;
            const { svg } = await mermaid.render(id, source);
            chart.innerHTML = svg;
          } catch {
            chart.innerHTML = `<pre class="kb-mermaid-fallback"><code>${source.replace(/</g, '&lt;').replace(/>/g, '&gt;')}</code></pre>`;
          }

          pre.dataset.enhanced = 'true';
          pre.replaceWith(chart);
        })
      );
    };

    enhanceRichBlocks();
  }, [article.id, content, loading]);

  useEffect(() => {
    if (!contentRef.current || loading) return;
    applyHighlightsToRoot(contentRef.current, articleHighlights);
  }, [articleHighlights, content, loading]);

  useEffect(() => {
    if (loading || !content) return;

    if (!bilingualActive) {
      setTranslatedContent(null);
      setTranslationLoading(false);
      setTranslationError('');
      return;
    }

    const targetLanguage = articleLanguageIsChinese ? 'en' : 'zh-CN';
    const sourceStrings = Array.from(collectContentStrings(content));
    if (sourceStrings.length === 0) {
      setTranslatedContent(content);
      return;
    }

    const buildTranslatedContent = () => {
      const translations = Object.fromEntries(
        sourceStrings.map((text) => [text, translationCacheRef.current[`${targetLanguage}:${text}`] || text])
      );
      setTranslatedContent(replaceContentStrings(content, translations));
    };

    const missingTexts = sourceStrings.filter((text) => !translationCacheRef.current[`${targetLanguage}:${text}`]);
    if (missingTexts.length === 0) {
      buildTranslatedContent();
      return;
    }

    let cancelled = false;
    setTranslationLoading(true);
    setTranslationError('');

    const loadTranslations = async () => {
      const chunkSize = 24;

      try {
        for (let i = 0; i < missingTexts.length; i += chunkSize) {
          const chunk = missingTexts.slice(i, i + chunkSize);
          const res = await fetch('/api/translate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ texts: chunk, target: targetLanguage }),
          });

          if (!res.ok) throw new Error('translate_failed');
          const data = (await res.json()) as { translations?: string[] };
          (data.translations || []).forEach((item, index) => {
            translationCacheRef.current[`${targetLanguage}:${chunk[index]}`] = item || chunk[index];
          });

          if (cancelled) return;
          buildTranslatedContent();
        }
      } catch {
        if (!cancelled) setTranslationError(articleLanguageIsChinese ? '英文版暂时不可用' : '中文版暂时不可用');
      } finally {
        if (!cancelled) setTranslationLoading(false);
      }
    };

    loadTranslations();

    return () => {
      cancelled = true;
    };
  }, [article.id, articleLanguageIsChinese, bilingualActive, content, loading]);

  useEffect(() => {
    const root = contentRef.current;
    if (!root || loading) return;

    const handleMouseUp = () => {
      const selection = window.getSelection();
      if (!selection || selection.rangeCount === 0 || selection.isCollapsed) return;
      if (!root.contains(selection.anchorNode) || !root.contains(selection.focusNode)) return;

      const quote = normalizeText(selection.toString());
      if (quote.length < 2 || quote.length > 240) return;

      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      setSelectionDraft({
        quote,
        comment: '',
        x: Math.min(rect.left, window.innerWidth - 340),
        y: Math.min(rect.bottom + 12, window.innerHeight - 260),
      });
    };

    root.addEventListener('mouseup', handleMouseUp);
    return () => root.removeEventListener('mouseup', handleMouseUp);
  }, [loading, content]);

  const tocItems = extractTOC(renderedContent, displayLanguage);

  const scrollToSection = (key: string) => {
    setActiveSection(key);
    setMobileTocOpen(false);
    const el = document.getElementById(key);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const importanceStars = (rating: number) => {
    const full = Math.floor(rating);
    const half = rating - full >= 0.5;
    return '★'.repeat(full) + (half ? '☆' : '') + '☆'.repeat(5 - full - (half ? 1 : 0));
  };

  const saveReview = () => {
    const wordCount = countWords(reviewContent);
    const nextReviews = { ...reviews };

    if (reviewContent.trim()) {
      nextReviews[article.id] = {
        content: reviewContent,
        wordCount,
        createdAt: new Date().toISOString(),
      };
    } else {
      delete nextReviews[article.id];
    }

    setReviews(nextReviews);
    saveReviews(nextReviews);
    setHasReview(Boolean(reviewContent.trim()));
    setShowReviewEditor(false);
  };

  const deleteReview = () => {
    const nextReviews = { ...reviews };
    delete nextReviews[article.id];
    setReviews(nextReviews);
    saveReviews(nextReviews);
    setHasReview(false);
    setReviewContent('');
    setShowReviewEditor(false);
  };

  const saveHighlight = () => {
    if (!selectionDraft?.quote || !selectionDraft.comment.trim()) return;
    const nextHighlights = {
      ...highlights,
      [article.id]: [
        {
          id: `${article.id}-${Date.now()}`,
          quote: selectionDraft.quote,
          comment: selectionDraft.comment.trim(),
          createdAt: new Date().toISOString(),
        },
        ...(highlights[article.id] || []),
      ],
    };
    setHighlights(nextHighlights);
    saveHighlights(nextHighlights);
    setSelectionDraft(null);
    window.getSelection()?.removeAllRanges();
  };

  const deleteHighlight = (highlightId: string) => {
    const nextList = (highlights[article.id] || []).filter((item) => item.id !== highlightId);
    const nextHighlights = { ...highlights, [article.id]: nextList };
    setHighlights(nextHighlights);
    saveHighlights(nextHighlights);
  };

  const toggleBilingual = () => {
    const next = !bilingualEnabled;
    setBilingualEnabled(next);
    try {
      localStorage.setItem('knowledge_bilingual_enabled', String(next));
    } catch {}
  };

  const wordCount = countWords(reviewContent);

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center overflow-hidden bg-slate-950/88 p-2 backdrop-blur-md sm:p-6"
      onClick={(e) => {
        if (e.target === e.currentTarget) {
          setSelectionDraft(null);
          onClose();
        }
      }}
    >
      <div className="relative flex max-h-[96vh] w-full min-w-0 max-w-7xl overflow-hidden rounded-[24px] border border-white/10 bg-[linear-gradient(180deg,rgba(7,12,24,0.98),rgba(8,14,28,0.94))] shadow-[0_32px_120px_rgba(2,6,23,0.72)] sm:max-h-[92vh] sm:rounded-[32px]">
        {tocItems.length > 0 && (
          <aside className="hidden w-[240px] shrink-0 border-r border-white/10 bg-white/[0.03] p-5 xl:block">
            <p className="text-xs uppercase tracking-[0.24em] text-slate-500">目录导航</p>
            <div className="mt-4 space-y-2 overflow-y-auto pr-1">
              {tocItems.map((item) => (
                <button
                  key={item.key}
                  onClick={() => scrollToSection(item.key)}
                  className={`w-full rounded-2xl px-3 py-2.5 text-left text-sm transition ${
                    activeSection === item.key
                      ? 'border border-indigo-400/20 bg-indigo-500/15 text-indigo-100'
                      : 'border border-transparent text-slate-400 hover:border-white/8 hover:bg-white/[0.04] hover:text-white'
                  }`}
                >
                  <span className={`block ${item.level > 1 ? 'pl-3 text-[13px]' : ''}`}>{item.title}</span>
                </button>
              ))}
            </div>
          </aside>
        )}

        <div className="relative min-w-0 flex-1 overflow-x-hidden overflow-y-auto">
          <div className="sticky top-0 z-10 border-b border-white/10 bg-[rgba(7,12,24,0.88)] px-4 py-4 backdrop-blur-xl sm:px-6 sm:py-5">
            <div className="mb-3 flex items-center justify-between gap-2 sm:hidden">
              <button
                onClick={() => {
                  setSelectionDraft(null);
                  onClose();
                }}
                className="rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-sm text-slate-300 transition hover:border-white/20 hover:text-white"
              >
                返回
              </button>
              {tocItems.length > 0 && (
                <button
                  type="button"
                  onClick={() => setMobileTocOpen((open) => !open)}
                  className={`rounded-full border px-3 py-1.5 text-sm transition ${
                    mobileTocOpen
                      ? 'border-indigo-400/20 bg-indigo-500/15 text-indigo-100'
                      : 'border-white/10 bg-white/5 text-slate-300'
                  }`}
                >
                  目录
                </button>
              )}
            </div>

            {mobileTocOpen && tocItems.length > 0 && (
              <div className="mb-3 max-h-[38vh] overflow-y-auto rounded-2xl border border-white/10 bg-black/20 p-2 sm:hidden">
                {tocItems.map((item) => (
                  <button
                    key={item.key}
                    type="button"
                    onClick={() => scrollToSection(item.key)}
                    className={`block w-full rounded-xl px-3 py-2 text-left text-sm transition ${
                      activeSection === item.key
                        ? 'bg-indigo-500/15 text-indigo-100'
                        : 'text-slate-300 hover:bg-white/[0.06] hover:text-white'
                    }`}
                  >
                    <span className={item.level > 1 ? 'block pl-3 text-[13px]' : 'block'}>{item.title}</span>
                  </button>
                ))}
              </div>
            )}

            <button
              onClick={() => {
                setSelectionDraft(null);
                onClose();
              }}
              className="absolute right-5 top-5 hidden rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-sm text-slate-300 transition hover:border-white/20 hover:text-white sm:block"
            >
              关闭
            </button>
            <div className="absolute right-24 top-5 hidden items-center gap-2 sm:flex">
              <button
                onClick={toggleBilingual}
                className={`rounded-full border px-3 py-1.5 text-sm transition ${
                  bilingualEnabled
                    ? 'border-cyan-400/20 bg-cyan-500/15 text-cyan-100 hover:bg-cyan-500/20'
                    : 'border-cyan-400/15 bg-cyan-500/8 text-cyan-200 hover:bg-cyan-500/15'
                }`}
              >
                {bilingualEnabled
                  ? `切回${articleLanguageIsChinese ? '中文版' : '英文版'}`
                  : `切换到${articleLanguageIsChinese ? '英文版' : '中文版'}`}
              </button>
            </div>
            <div className="hidden max-w-4xl sm:block sm:pr-44">
              <div className="flex flex-wrap items-center gap-2 text-xs">
                <span className="rounded-full border border-yellow-400/15 bg-yellow-500/10 px-2.5 py-1 text-yellow-200">
                  {importanceStars(article.importance)}
                </span>
                <span className="rounded-full border border-indigo-400/15 bg-indigo-500/10 px-2.5 py-1 text-indigo-200">
                  {article.category}
                </span>
                <span className="rounded-full border border-white/10 bg-white/5 px-2.5 py-1 text-slate-400">
                  {article.learned_at}
                </span>
                <span
                  className={`rounded-full border px-2.5 py-1 ${
                    isRead
                      ? 'border-emerald-400/15 bg-emerald-500/10 text-emerald-300'
                      : 'border-amber-400/15 bg-amber-500/10 text-amber-200'
                  }`}
                >
                  {isRead ? '已读' : '未读'}
                </span>
                {hasReview && (
                  <span className="rounded-full border border-emerald-400/15 bg-emerald-500/10 px-2.5 py-1 text-emerald-300">
                    已写读后感
                  </span>
                )}
                {articleHighlights.length > 0 && (
                  <span className="rounded-full border border-amber-400/15 bg-amber-500/10 px-2.5 py-1 text-amber-200">
                    划词评论 {articleHighlights.length}
                  </span>
                )}
                {bilingualActive && (
                  <span className="rounded-full border border-cyan-400/15 bg-cyan-500/10 px-2.5 py-1 text-cyan-200">
                    {articleLanguageIsChinese ? '英文版' : '中文版'}
                  </span>
                )}
              </div>
              <h2 className="mt-4 text-2xl font-semibold leading-tight text-white sm:text-3xl">{article.title}</h2>
              <p className="mt-3 max-w-3xl text-sm leading-7 text-slate-400">{article.summary}</p>
              <div className="mt-4 flex flex-wrap gap-2">
                {article.keywords.map((kw, idx) => (
                  <span
                    key={`${article.id}-kw-${idx}`}
                    className="rounded-full border border-purple-400/15 bg-purple-500/10 px-2.5 py-1 text-xs text-purple-200"
                  >
                    {kw}
                  </span>
                ))}
              </div>
            </div>
          </div>

          <div className="mx-auto min-w-0 max-w-4xl px-4 py-5 sm:px-6 sm:py-6">
            <div className="mb-6 flex flex-wrap items-center gap-3">
              <button
                onClick={() => onToggleRead(article.id)}
                className={`rounded-full border px-4 py-2 text-sm transition ${
                  isRead
                    ? 'border-emerald-400/15 bg-emerald-500/10 text-emerald-300 hover:bg-emerald-500/20'
                    : 'border-amber-400/15 bg-amber-500/10 text-amber-100 hover:bg-amber-500/20'
                }`}
              >
                {isRead ? '取消已读' : '标记已读'}
              </button>
              <button
                onClick={() => setShowReviewEditor(true)}
                className={`rounded-full border px-4 py-2 text-sm transition ${
                  hasReview
                    ? 'border-emerald-400/15 bg-emerald-500/10 text-emerald-300 hover:bg-emerald-500/20'
                    : 'border-indigo-400/15 bg-indigo-500/10 text-indigo-200 hover:bg-indigo-500/20'
                }`}
              >
                {hasReview ? '查看 / 编辑读后感' : '写读后感'}
              </button>
              <span className="text-xs text-slate-500">来源：{article.source}</span>
            </div>

            {((bilingualActive && (translationLoading || translationError)) || articleHighlights.length > 0) && (
              <div className="mb-6 space-y-3">
                {bilingualActive && translationLoading && (
                  <div className="rounded-2xl border border-cyan-400/10 bg-cyan-500/[0.06] px-4 py-3 text-sm text-cyan-100">
                    {articleLanguageIsChinese ? '英文版生成中...' : '中文版生成中...'}
                  </div>
                )}
                {bilingualActive && translationError && (
                  <div className="rounded-2xl border border-red-400/10 bg-red-500/[0.06] px-4 py-3 text-sm text-red-200">
                    {translationError}
                  </div>
                )}
                {articleHighlights.length > 0 && (
                  <div className="rounded-3xl border border-white/8 bg-white/[0.03] p-4">
                    <div className="mb-3 flex items-center justify-between gap-3">
                      <div>
                        <p className="text-xs uppercase tracking-[0.24em] text-slate-500">划词评论</p>
                        <h3 className="mt-1 text-base font-semibold text-white">本篇共 {articleHighlights.length} 条</h3>
                      </div>
                    </div>
                    <div className="space-y-3">
                      {articleHighlights.map((item) => (
                        <div key={item.id} className="rounded-2xl border border-amber-400/12 bg-amber-500/[0.05] p-4">
                          <p className="text-sm leading-7 text-amber-50">“{item.quote}”</p>
                          <p className="mt-2 text-sm leading-7 text-slate-300">{item.comment}</p>
                          <div className="mt-3 flex items-center justify-between gap-3 text-xs text-slate-500">
                            <span>{new Date(item.createdAt).toLocaleString()}</span>
                            <button
                              onClick={() => deleteHighlight(item.id)}
                              className="rounded-full border border-red-400/15 bg-red-500/10 px-3 py-1 text-red-200 transition hover:bg-red-500/20"
                            >
                              删除
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {loading ? (
              <div className="rounded-3xl border border-white/8 bg-white/[0.03] p-8 text-sm text-slate-400">加载中...</div>
            ) : (
              <div ref={contentRef} className="min-w-0 space-y-5 selection:bg-cyan-400/25 selection:text-white">
                {renderContent(renderedContent, 0, displayLanguage)}
              </div>
            )}
          </div>
        </div>
      </div>

      {selectionDraft && (
        <div
          className="fixed z-[70] w-[320px] rounded-[24px] border border-white/10 bg-[linear-gradient(180deg,rgba(7,12,24,0.98),rgba(9,16,31,0.96))] p-4 shadow-[0_24px_80px_rgba(2,6,23,0.7)]"
          style={{ left: selectionDraft.x, top: selectionDraft.y }}
        >
          <p className="text-xs uppercase tracking-[0.24em] text-slate-500">划词评论</p>
          <p className="mt-2 rounded-2xl border border-amber-400/12 bg-amber-500/[0.05] px-3 py-2 text-sm leading-6 text-amber-50">
            “{selectionDraft.quote}”
          </p>
          <textarea
            value={selectionDraft.comment}
            onChange={(e) => setSelectionDraft((prev) => (prev ? { ...prev, comment: e.target.value } : prev))}
            className="mt-3 h-28 w-full resize-none rounded-2xl border border-white/10 bg-black/20 p-3 text-sm leading-6 text-slate-200 outline-none transition focus:border-indigo-400/30 focus:bg-white/[0.04]"
            placeholder="写下你的评论..."
          />
          <div className="mt-3 flex justify-end gap-2">
            <button
              onClick={() => {
                setSelectionDraft(null);
                window.getSelection()?.removeAllRanges();
              }}
              className="rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-sm text-slate-300 transition hover:border-white/20 hover:text-white"
            >
              取消
            </button>
            <button
              onClick={saveHighlight}
              className="rounded-full border border-amber-400/20 bg-amber-500/15 px-3 py-1.5 text-sm text-amber-100 transition hover:bg-amber-500/25"
            >
              保存评论
            </button>
          </div>
        </div>
      )}

      {showReviewEditor && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center bg-black/80 p-6 backdrop-blur-sm">
          <div className="w-full max-w-3xl rounded-[28px] border border-white/10 bg-[linear-gradient(180deg,rgba(7,12,24,0.98),rgba(9,16,31,0.96))] p-6 shadow-[0_24px_100px_rgba(2,6,23,0.7)]">
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-xs uppercase tracking-[0.24em] text-slate-500">Review Note</p>
                <h3 className="mt-2 text-xl font-semibold text-white">读后感 - {article.title}</h3>
              </div>
              <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs text-slate-400">
                字数 {wordCount}
              </span>
            </div>

            <textarea
              value={reviewContent}
              onChange={(e) => setReviewContent(e.target.value)}
              className="mt-5 h-[320px] w-full resize-none rounded-[24px] border border-white/10 bg-black/20 p-5 text-sm leading-7 text-slate-200 outline-none transition focus:border-indigo-400/30 focus:bg-white/[0.04]"
              placeholder="写下你的读后感..."
            />

            <div className="mt-5 flex flex-wrap justify-end gap-2">
              {hasReview && (
                <button
                  onClick={deleteReview}
                  className="rounded-full border border-red-400/15 bg-red-500/10 px-4 py-2 text-sm text-red-300 transition hover:bg-red-500/20"
                >
                  删除
                </button>
              )}
              <button
                onClick={() => setShowReviewEditor(false)}
                className="rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-slate-300 transition hover:border-white/20 hover:text-white"
              >
                取消
              </button>
              <button
                onClick={saveReview}
                className="rounded-full border border-indigo-400/20 bg-indigo-500/15 px-4 py-2 text-sm text-indigo-100 transition hover:bg-indigo-500/25"
              >
                保存
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
