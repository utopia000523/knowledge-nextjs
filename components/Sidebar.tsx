'use client';

interface SidebarProps {
  categories: string[];
  categoryCounts: Record<string, number>;
  activeCategory: string | null;
  onCategoryChange: (category: string | null) => void;
  articleCount: number;
  isOpen: boolean;
  onToggle: () => void;
}

export default function Sidebar({
  categories,
  categoryCounts,
  activeCategory,
  onCategoryChange,
  articleCount,
  isOpen,
  onToggle,
}: SidebarProps) {
  return (
    <>
      {/* 移动端遮罩 */}
      {isOpen && (
        <div
          className="fixed inset-0 z-30 bg-black/60 backdrop-blur-sm lg:hidden"
          onClick={onToggle}
        />
      )}

      {/* 侧边栏 */}
      <aside
        className={`fixed left-0 top-0 z-40 flex h-screen w-[280px] flex-col overflow-y-auto border-r border-white/10 bg-[rgba(7,12,24,0.96)] px-5 pb-20 pt-4 backdrop-blur-2xl transition-transform duration-300 lg:w-[320px] lg:px-6 lg:translate-x-0 ${
          isOpen ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        <div className="flex h-full flex-1 flex-col rounded-[28px] border border-white/10 bg-white/[0.03] p-4 shadow-[0_18px_48px_rgba(2,6,23,0.28)]">
          {/* 移动端关闭按钮 */}
          <div className="mb-3 flex items-center justify-between">
            <p className="text-xs uppercase tracking-[0.24em] text-slate-500">分类导航</p>
            <div className="flex items-center gap-2">
              <button type="button" onClick={onToggle} className="inline-flex h-7 w-7 items-center justify-center rounded-full border border-white/10 bg-white/5 text-sm text-slate-400 hover:text-white lg:hidden">
                ✕
              </button>
              <span className="rounded-full border border-white/10 bg-white/5 px-2.5 py-1 text-[11px] text-slate-400">
                {categories.length} 类
              </span>
            </div>
          </div>

          <button
            type="button"
            className={`mb-2 flex w-full items-center justify-between rounded-2xl px-4 py-3 text-left text-sm transition-all ${
              activeCategory === null
                ? 'border border-indigo-400/25 bg-indigo-500/15 text-indigo-100 shadow-[0_12px_30px_rgba(79,70,229,0.2)]'
                : 'border border-transparent bg-white/[0.03] text-slate-300 hover:border-white/10 hover:bg-white/[0.06]'
            }`}
            onClick={() => { onCategoryChange(null); onToggle(); }}
          >
            <span className="font-medium">全部内容</span>
            <span className="rounded-full bg-black/20 px-2.5 py-1 text-[11px] text-slate-300">{articleCount}</span>
          </button>

          <div className="flex-1 space-y-2">
            {categories.map((category) => {
              const isActive = activeCategory === category;
              return (
                <button
                  type="button"
                  key={category}
                  className={`flex w-full items-center justify-between rounded-2xl px-4 py-3 text-left text-sm transition-all ${
                    isActive
                      ? 'border border-cyan-400/20 bg-cyan-400/10 text-cyan-100 shadow-[0_12px_28px_rgba(56,189,248,0.15)]'
                      : 'border border-transparent bg-white/[0.03] text-slate-300 hover:border-white/10 hover:bg-white/[0.06]'
                  }`}
                  onClick={() => { onCategoryChange(category); onToggle(); }}
                >
                  <span className="line-clamp-1 font-medium">{category}</span>
                  <span className={`rounded-full px-2.5 py-1 text-[11px] ${
                    isActive ? 'bg-cyan-400/10 text-cyan-100' : 'bg-black/20 text-slate-400'
                  }`}>
                    {categoryCounts[category] || 0}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </aside>
    </>
  );
}
