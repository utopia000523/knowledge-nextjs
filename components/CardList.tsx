'use client';

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

interface CardListProps {
  articles: Article[];
  readStatus: Record<string, boolean>;
  onArticleClick: (article: Article) => void;
  onToggleRead: (articleId: string) => void;
}

export default function CardList({ articles, readStatus, onArticleClick, onToggleRead }: CardListProps) {
  const importanceStars = (rating: number) => {
    const fullStars = Math.floor(rating);
    const hasHalf = rating - fullStars >= 0.5;
    let stars = '★'.repeat(fullStars);
    if (hasHalf) stars += '☆';
    stars += '☆'.repeat(5 - fullStars - (hasHalf ? 1 : 0));
    return stars;
  };

  const importanceLabel = (rating: number) => {
    if (rating >= 5) return '核心必读';
    if (rating >= 4) return '高价值';
    if (rating >= 3) return '值得读';
    return '可补充';
  };

  if (articles.length === 0) {
    return (
      <div className="kb-panel flex min-h-[320px] flex-col items-center justify-center px-6 py-12 text-center">
        <div className="flex h-16 w-16 items-center justify-center rounded-3xl border border-white/10 bg-white/5 text-2xl text-slate-300">
          ⌁
        </div>
        <h3 className="mt-5 text-xl font-semibold text-white">没找到匹配内容</h3>
        <p className="mt-2 max-w-md text-sm leading-7 text-slate-400">
          请更换关键词，或返回“全部内容”查看完整文章列表。
        </p>
      </div>
    );
  }

  return (
    <div className="grid gap-5 md:grid-cols-2 2xl:grid-cols-3">
      {articles.map((article) => {
        const isRead = readStatus[article.id];
        return (
          <article
            key={article.id}
            className={`group relative overflow-hidden rounded-[28px] border p-6 transition duration-300 ${
              isRead
                ? 'border-white/8 bg-[linear-gradient(180deg,rgba(15,23,42,0.58),rgba(15,23,42,0.42))]'
                : 'border-white/12 bg-[linear-gradient(180deg,rgba(15,23,42,0.82),rgba(10,15,27,0.68))] hover:-translate-y-1 hover:border-indigo-300/20 hover:shadow-[0_24px_60px_rgba(30,41,59,0.45)]'
            }`}
          >
            <div className="pointer-events-none absolute inset-0 opacity-0 transition duration-300 group-hover:opacity-100 bg-[radial-gradient(circle_at_top_right,rgba(129,140,248,0.15),transparent_28%),radial-gradient(circle_at_bottom_left,rgba(34,211,238,0.12),transparent_24%)]" />

            <div className="relative flex h-full flex-col">
              <div className="flex items-start justify-between gap-4">
                <div className="space-y-2" onClick={() => onArticleClick(article)}>
                  <div className="flex flex-wrap items-center gap-2 text-xs text-slate-400">
                    <span className="rounded-full border border-white/10 bg-white/5 px-2.5 py-1">
                      {article.category}
                    </span>
                    <span className="rounded-full border border-yellow-400/15 bg-yellow-500/10 px-2.5 py-1 text-yellow-200">
                      {importanceLabel(article.importance)}
                    </span>
                  </div>
                  <h3 className={`text-xl font-semibold leading-8 ${isRead ? 'text-slate-300' : 'text-white'}`}>
                    {article.title}
                  </h3>
                </div>

                <button
                  type="button"
                  onClick={(e) => {
                    e.stopPropagation();
                    onToggleRead(article.id);
                  }}
                  className={`shrink-0 rounded-full border px-3 py-1.5 text-xs transition ${
                    isRead
                      ? 'border-emerald-400/15 bg-emerald-500/10 text-emerald-300 hover:bg-emerald-500/20'
                      : 'border-white/10 bg-white/5 text-slate-300 hover:border-indigo-400/20 hover:bg-indigo-500/10 hover:text-white'
                  }`}
                >
                  {isRead ? '已读' : '标记已读'}
                </button>
              </div>

              <button type="button" className="mt-4 text-left" onClick={() => onArticleClick(article)}>
                <p className={`line-clamp-4 text-sm leading-7 ${isRead ? 'text-slate-500' : 'text-slate-300'}`}>
                  {article.summary}
                </p>
              </button>

              <div className="mt-5 flex items-center gap-2 text-sm text-yellow-200/90">
                <span>{importanceStars(article.importance)}</span>
                {isRead && <span className="text-xs text-emerald-300">✓ 已读</span>}
              </div>

              <div className="mt-5 flex flex-wrap gap-2 text-xs">
                <span className="rounded-full border border-white/10 bg-black/20 px-2.5 py-1 text-slate-400">
                  {article.learned_at}
                </span>
                {article.keywords.slice(0, 3).map((keyword, idx) => (
                  <span
                    key={`${article.id}-${idx}`}
                    className="rounded-full border border-purple-400/15 bg-purple-500/10 px-2.5 py-1 text-purple-200"
                  >
                    {keyword}
                  </span>
                ))}
              </div>

              <button
                type="button"
                onClick={() => onArticleClick(article)}
                className="mt-6 inline-flex items-center gap-2 text-sm text-slate-300 transition group-hover:text-white"
              >
                打开全文
                <span className="transition group-hover:translate-x-1">→</span>
              </button>
            </div>
          </article>
        );
      })}
    </div>
  );
}
