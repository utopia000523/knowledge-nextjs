'use client';

import dynamic from 'next/dynamic';
import { useEffect, useMemo, useState } from 'react';
import Sidebar from '@/components/Sidebar';
import SearchBar from '@/components/SearchBar';
import CardList from '@/components/CardList';
import ArticleDetail from '@/components/ArticleDetail';

const SplashCursor = dynamic(() => import('@/components/animations/SplashCursor'), {
  ssr: false,
});

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

function getReadStatus(): Record<string, boolean> {
  try {
    const stored = localStorage.getItem('knowledge_read_status');
    return stored ? JSON.parse(stored) : {};
  } catch {
    return {};
  }
}

function saveReadStatus(status: Record<string, boolean>) {
  try {
    localStorage.setItem('knowledge_read_status', JSON.stringify(status));
  } catch {}
}

function getUiSettings() {
  try {
    const stored = localStorage.getItem('knowledge_ui_settings');
    return stored ? JSON.parse(stored) : { enableCursorEffect: true };
  } catch {
    return { enableCursorEffect: true };
  }
}

function saveUiSettings(settings: { enableCursorEffect: boolean }) {
  try {
    localStorage.setItem('knowledge_ui_settings', JSON.stringify(settings));
  } catch {}
}

export default function Home() {
  const [data, setData] = useState<{ categories: string[]; articles: Article[] } | null>(null);
  const [activeCategory, setActiveCategory] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [settingsOpen, setSettingsOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [readStatus, setReadStatus] = useState<Record<string, boolean>>(() => {
    if (typeof window === 'undefined') return {};
    return getReadStatus();
  });
  const [enableCursorEffect, setEnableCursorEffect] = useState(() => {
    if (typeof window === 'undefined') return false;
    return window.matchMedia('(min-width: 1024px)').matches && getUiSettings().enableCursorEffect;
  });

  useEffect(() => {
    const desktopQuery = window.matchMedia('(min-width: 1024px)');
    const applyCursorPreference = () => {
      setEnableCursorEffect(desktopQuery.matches && getUiSettings().enableCursorEffect);
    };

    if (desktopQuery.addEventListener) {
      desktopQuery.addEventListener('change', applyCursorPreference);
    } else {
      desktopQuery.addListener(applyCursorPreference);
    }

    fetch('/data/index.json')
      .then((r) => r.json())
      .then((d) => setData(d))
      .catch(() => {});

    return () => {
      if (desktopQuery.removeEventListener) {
        desktopQuery.removeEventListener('change', applyCursorPreference);
      } else {
        desktopQuery.removeListener(applyCursorPreference);
      }
    };
  }, []);

  const categoryCounts = useMemo(() => {
    const counts: Record<string, number> = {};
    (data?.articles ?? []).forEach((article) => {
      counts[article.category] = (counts[article.category] || 0) + 1;
    });
    return counts;
  }, [data]);

  const readCount = useMemo(() => {
    return Object.keys(readStatus).filter((id) => readStatus[id]).length;
  }, [readStatus]);

  const filteredArticles = useMemo(() => {
    let articles = data?.articles ?? [];
    if (activeCategory) {
      articles = articles.filter((article) => article.category === activeCategory);
    }
    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      articles = articles.filter((article) =>
        article.title.toLowerCase().includes(query) ||
        article.summary.toLowerCase().includes(query) ||
        article.keywords.some((keyword) => keyword.toLowerCase().includes(query))
      );
    }

    return [...articles].sort((a, b) => {
      const aRead = readStatus[a.id] || false;
      const bRead = readStatus[b.id] || false;
      if (aRead === bRead) return b.importance - a.importance;
      return aRead ? 1 : -1;
    });
  }, [activeCategory, data, searchQuery, readStatus]);

  const toggleRead = (articleId: string) => {
    const newStatus = { ...readStatus, [articleId]: !readStatus[articleId] };
    setReadStatus(newStatus);
    saveReadStatus(newStatus);
  };

  const filteredReadCount = filteredArticles.filter((article) => readStatus[article.id]).length;
  const filteredUnreadCount = filteredArticles.length - filteredReadCount;

  const toggleCursorEffect = () => {
    const nextValue = !enableCursorEffect;
    setEnableCursorEffect(nextValue);
    saveUiSettings({ enableCursorEffect: nextValue });
  };

  const completionRate = (data?.articles?.length ?? 0) === 0 ? 0 : Math.round((readCount / (data?.articles?.length ?? 1)) * 100);

  if (!data) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#07111f] text-slate-400">
        <div className="text-center">
          <div className="mb-4 text-4xl">📚</div>
          <p>加载知识库中...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="kb-shell relative min-h-screen overflow-hidden text-white">
      {enableCursorEffect && (
        <div className="pointer-events-none absolute inset-0 z-0 opacity-70">
          <SplashCursor TRANSPARENT={true} SPLAT_RADIUS={0.12} />
        </div>
      )}

      <div className="kb-orb kb-orb-primary" />
      <div className="kb-orb kb-orb-secondary" />
      <div className="kb-grid" />

      <Sidebar
        categories={data.categories}
        categoryCounts={categoryCounts}
        activeCategory={activeCategory}
        onCategoryChange={setActiveCategory}
        articleCount={data.articles.length}
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(!sidebarOpen)}
      />

      {/* 移动端顶栏 */}
      <header className="fixed left-0 top-0 z-20 flex h-14 w-full items-center justify-between border-b border-white/10 bg-[rgba(7,12,24,0.9)] px-4 backdrop-blur-2xl lg:hidden">
        <button
          type="button"
          onClick={() => setSidebarOpen(true)}
          className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-white/10 bg-white/5 text-base text-slate-300 hover:text-white"
        >
          ☰
        </button>
        <span className="text-sm font-medium text-slate-200">个人知识库</span>
        <button
          type="button"
          onClick={() => setSettingsOpen((prev) => !prev)}
          className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-white/10 bg-white/5 text-base text-slate-300 hover:text-white"
        >
          ⚙
        </button>
      </header>

      <main className="relative z-10 min-h-screen px-4 pt-20 pb-24 lg:ml-[320px] lg:px-8 lg:pt-8 xl:px-10">
        <div className="mx-auto max-w-7xl space-y-6">
          <section className="kb-panel overflow-hidden p-3 lg:p-3.5">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(129,140,248,0.18),transparent_28%),radial-gradient(circle_at_bottom_left,rgba(56,189,248,0.12),transparent_24%)]" />
            <div className="relative space-y-2">
              <div className="flex flex-wrap items-center gap-1.5 text-[11px]">
                <div className="inline-flex items-center gap-2 rounded-full border border-emerald-400/20 bg-emerald-500/10 px-3 py-1 font-medium text-emerald-200">
                  <span className="h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_12px_rgba(74,222,128,0.8)]" />
                  {filteredArticles.length} 篇内容
                </div>
                <span className="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-slate-300">
                  {activeCategory || '全部分类'}
                </span>
                {searchQuery && (
                  <span className="rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-cyan-200">
                    搜索：{searchQuery}
                  </span>
                )}
              </div>

              <div className="grid gap-2 grid-cols-2 sm:grid-cols-3 xl:grid-cols-5">
                <div className="kb-stat-card">
                  <span className="kb-stat-label">总量</span>
                  <strong className="kb-stat-value">{data.articles.length}</strong>
                  <span className="kb-stat-foot">全部文章</span>
                </div>
                <div className="kb-stat-card">
                  <span className="kb-stat-label">结果</span>
                  <strong className="kb-stat-value">{filteredArticles.length}</strong>
                  <span className="kb-stat-foot">当前范围</span>
                </div>
                <div className="kb-stat-card">
                  <span className="kb-stat-label">已读</span>
                  <strong className="kb-stat-value">{filteredReadCount}</strong>
                  <span className="kb-stat-foot">当前范围</span>
                </div>
                <div className="kb-stat-card">
                  <span className="kb-stat-label">未读</span>
                  <strong className="kb-stat-value">{filteredUnreadCount}</strong>
                  <span className="kb-stat-foot">当前范围</span>
                </div>
                <div className="kb-stat-card">
                  <span className="kb-stat-label">完成进度</span>
                  <strong className="kb-stat-value">{completionRate}%</strong>
                  <span className="kb-stat-foot">全库进度</span>
                </div>
              </div>
            </div>
          </section>

          <section className="space-y-6">
            <SearchBar onSearch={setSearchQuery} />
            <CardList
              articles={filteredArticles}
              readStatus={readStatus}
              onArticleClick={(article) => setSelectedArticle(article)}
              onToggleRead={toggleRead}
            />
          </section>
        </div>
      </main>

      {/* 桌面端设置按钮 */}
      <div className="fixed bottom-6 left-6 z-30 hidden flex-col items-start gap-3 lg:flex">
        {settingsOpen && (
          <div className="w-[280px] rounded-[28px] border border-white/10 bg-slate-950/90 p-5 text-sm text-slate-200 shadow-[0_24px_60px_rgba(2,6,23,0.55)] backdrop-blur-2xl">
            <div className="flex items-start justify-between gap-3">
              <div>
                <p className="text-xs uppercase tracking-[0.24em] text-slate-500">个性化设置</p>
                <h3 className="mt-2 text-base font-semibold text-white">显示与交互</h3>
              </div>
              <button
                type="button"
                onClick={() => setSettingsOpen(false)}
                className="inline-flex h-8 w-8 items-center justify-center rounded-full border border-white/10 bg-white/5 text-slate-300 transition hover:border-white/20 hover:bg-white/10 hover:text-white"
                aria-label="关闭个性化设置"
              >
                ×
              </button>
            </div>

            <div className="mt-5 space-y-3 rounded-2xl border border-white/8 bg-black/20 p-4">
              <div className="flex items-center justify-between gap-4">
                <div>
                  <p className="font-medium text-white">水波光标</p>
                  <p className="mt-1 text-xs leading-5 text-slate-400">控制首页背景光标动效</p>
                </div>
                <button
                  type="button"
                  onClick={toggleCursorEffect}
                  className={`inline-flex min-w-[72px] items-center justify-center rounded-full border px-3 py-1.5 text-xs transition ${
                    enableCursorEffect
                      ? 'border-emerald-400/20 bg-emerald-500/10 text-emerald-200 hover:bg-emerald-500/20'
                      : 'border-white/10 bg-white/5 text-slate-300 hover:border-indigo-400/30 hover:bg-indigo-500/10 hover:text-white'
                  }`}
                >
                  {enableCursorEffect ? '已开启' : '已关闭'}
                </button>
              </div>
            </div>

            <div className="mt-4 rounded-2xl border border-dashed border-white/10 bg-white/[0.03] p-4 text-xs leading-6 text-slate-400">
              后续可在这里继续加入主题、卡片密度、字体大小等个性化选项。
            </div>
          </div>
        )}

        <button
          type="button"
          onClick={() => setSettingsOpen((prev) => !prev)}
          className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-slate-950/80 px-4 py-3 text-sm text-slate-200 shadow-[0_18px_40px_rgba(2,6,23,0.45)] backdrop-blur-xl transition hover:border-indigo-400/30 hover:bg-slate-900/90 hover:text-white"
        >
          <span className="inline-flex h-8 w-8 items-center justify-center rounded-full border border-white/10 bg-white/5 text-base">⚙</span>
          个性化设置
        </button>
      </div>

      {selectedArticle && (
        <ArticleDetail
          article={selectedArticle}
          isRead={Boolean(readStatus[selectedArticle.id])}
          onToggleRead={toggleRead}
          onClose={() => setSelectedArticle(null)}
        />
      )}
    </div>
  );
}
