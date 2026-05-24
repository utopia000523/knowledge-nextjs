'use client';

import { useState, useMemo } from 'react';
import Sidebar from '@/components/Sidebar';
import SearchBar from '@/components/SearchBar';
import CardList from '@/components/CardList';

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

interface Data {
  categories: string[];
  articles: Article[];
}

export default function KnowledgeBase({ initialData }: { initialData: Data }) {
  const [activeCategory, setActiveCategory] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');

  const categories = initialData.categories;
  const allArticles = initialData.articles;

  const filteredArticles = useMemo(() => {
    let articles = allArticles;
    if (activeCategory) {
      articles = articles.filter(a => a.category === activeCategory);
    }
    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      articles = articles.filter(a => 
        a.title.toLowerCase().includes(query) ||
        a.summary.toLowerCase().includes(query) ||
        a.keywords.some(k => k.toLowerCase().includes(query))
      );
    }
    return articles;
  }, [activeCategory, searchQuery, allArticles]);

  const categoryCounts = useMemo(() => {
    const counts: Record<string, number> = {};
    allArticles.forEach((article) => {
      counts[article.category] = (counts[article.category] || 0) + 1;
    });
    return counts;
  }, [allArticles]);

  return (
    <>
      {/* <SplashCursor RAINBOW_MODE={true} TRANSPARENT={true} SPLAT_RADIUS={0.15} /> */}
      <Sidebar 
        categories={categories}
        categoryCounts={categoryCounts}
        activeCategory={activeCategory}
        onCategoryChange={setActiveCategory}
        articleCount={allArticles.length}
      />
      <main className="ml-[280px] min-h-screen p-8">
        <div className="max-w-4xl mx-auto">
          <SearchBar onSearch={setSearchQuery} />
          <p className="text-sm text-gray-500 mb-4">显示 {filteredArticles.length} 篇文章</p>
          <CardList
            articles={filteredArticles}
            readStatus={{}}
            onArticleClick={(a) => console.log(a.id)}
            onToggleRead={() => {}}
          />
        </div>
      </main>
    </>
  );
}