'use client';

import { useState } from 'react';

interface SearchBarProps {
  onSearch: (query: string) => void;
}

export default function SearchBar({ onSearch }: SearchBarProps) {
  const [query, setQuery] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
    onSearch(e.target.value);
  };

  return (
    <div className="kb-panel p-4 sm:p-5">
      <div className="flex items-center gap-3 rounded-[22px] border border-white/10 bg-black/20 px-4 py-3 shadow-[inset_0_1px_0_rgba(255,255,255,0.04)] transition focus-within:border-indigo-400/40 focus-within:bg-white/[0.06]">
        <span className="text-lg text-slate-500">⌕</span>
        <input
          type="text"
          placeholder="搜索关键词、标题、摘要..."
          value={query}
          onChange={handleChange}
          className="w-full bg-transparent text-sm text-white placeholder:text-slate-500 focus:outline-none"
        />
        {query && (
          <button
            type="button"
            onClick={() => {
              setQuery('');
              onSearch('');
            }}
            className="rounded-full border border-white/10 bg-white/5 px-2.5 py-1 text-xs text-slate-400 transition hover:border-white/20 hover:text-white"
          >
            清空
          </button>
        )}
      </div>
    </div>
  );
}
