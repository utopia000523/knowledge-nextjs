import fs from 'fs';
import path from 'path';

// 服务端读取数据
async function getData() {
  const dataPath = path.join(process.cwd(), 'data', 'index.json');
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
  return data;
}

export default async function HomePage() {
  const data = await getData();
  
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-2xl font-bold mb-4">知识库</h1>
        <p className="text-gray-500">共 {data.articles.length} 篇文章</p>
        <p className="text-gray-500">{data.categories.length} 个分类</p>
      </div>
    </div>
  );
}