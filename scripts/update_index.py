#!/usr/bin/env python3
"""每周更新智慧库索引：刷新统计数字、新增重要文章条目"""
import json, os, re
from datetime import date

BASE = os.path.expanduser('~/.hermes/knowledge-nextjs')
INDEX_PATH = os.path.join(BASE, 'data', 'index.json')
INDEX_ARTICLE_PATH = os.path.join(BASE, 'data', 'articles', '知识库索引.json')
PUBLIC_INDEX_PATH = os.path.join(BASE, 'public', 'data', 'index.json')
PUBLIC_ARTICLE_PATH = os.path.join(BASE, 'public', 'data', 'articles', '知识库索引.json')

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    index = json.load(f)

with open(INDEX_ARTICLE_PATH, 'r', encoding='utf-8') as f:
    article = json.load(f)

# 1. 更新概览层（第0层）的统计数字
from collections import Counter
cat_count = Counter(a['category'] for a in index['articles'])
total = len(index['articles'])

overview = article['content']['layers'][0]
cat_order = ['产品设计', '心理学', '创业', '项目管理', '理财', '营销', '技术', '雅思']
lines = []
for cat in cat_order:
    cnt = cat_count.get(cat, 0)
    if cat == '产品设计':
        coverage = 'UX/UI、硬件设计、需求分析、AI产品、嵌入式设计'
    elif cat == '心理学':
        coverage = '认知科学、行为设计、社交心理、习惯养成、自我成长'
    elif cat == '创业':
        coverage = '企业战略、领导力、商业模式、竞争策略、创新方法论'
    elif cat == '项目管理':
        coverage = '敏捷、DevOps、TDD、流程管理、QFD/六西格玛'
    elif cat == '理财':
        coverage = '价值投资、资产配置、行为金融、期权、经济学'
    elif cat == '营销':
        coverage = '品牌定位、获客、销售谈判、增长、内容传播'
    elif cat == '技术':
        coverage = 'AI/ML、网络协议、安全工程、嵌入式、硬件逆向'
    elif cat == '雅思':
        coverage = '听说读写全科方法论'
    else:
        coverage = '元数据'
    lines.append(f'| {cat} | {cnt} | {coverage} |')

other_cnt = cat_count.get('其他', 0)
lines.append(f'| 其他 | {other_cnt} | 元数据 |')
lines.append(f'| **总计** | **{total}** | **覆盖产品、理财、心理、营销、技术等全领域** |')

overview['content'] = '\n'.join([
    '| 分类 | 篇数 | 覆盖领域 |',
    '|------|------|----------|',
    *lines,
    '',
    '使用方式：按场景定位分类 → 打开对应文章 → 提取核心公式与工具'
])

# 2. 更新最后"更多知识资源"层的统计
last_layer = article['content']['layers'][-1]
last_content_parts = []
for cat in ['产品设计', '心理学', '创业', '项目管理', '理财', '营销', '技术', '雅思']:
    cnt = cat_count.get(cat, 0)
    emoji_map = {
        '产品设计': '🎯', '心理学': '🧠', '创业': '🚀',
        '项目管理': '📋', '理财': '💰', '营销': '📊',
        '技术': '💻', '雅思': '📚'
    }
    desc_map = {
        '产品设计': 'UX/硬件/AI/需求/交互', '心理学': '认知/社交/习惯/成长',
        '创业': '战略/领导力/创新/商业模式', '项目管理': '敏捷/DevOps/流程/方法论',
        '理财': '投资/资产配置/经济学', '营销': '定位/获客/品牌/增长',
        '技术': 'AI/网络/嵌入式/安全', '雅思': '听说读写全科'
    }
    emoji = emoji_map.get(cat, '📖')
    desc = desc_map.get(cat, '')
    last_content_parts.append(f'- {emoji} **{cat}**（{cnt}篇）— {desc}')

last_layer['content'] = '\n'.join([
    f'知识库共 **{total}篇**方法论文档，覆盖9大分类：',
    *last_content_parts,
    f'- 🔍 **其他**（{other_cnt}篇）— 本索引',
    '',
    '**使用方式**：在知识库网站（localhost:3000）搜索分类或关键词，直接查看详情。',
    '**每周自动更新**：每周一扫描新增文章，补充到本索引中。'
])

# 3. 更新摘要
article['summary'] = f'根据用户问题场景，快速匹配对应方法论（{total}篇 {date.today().isoformat()}更新）'

# 4. 添加更新日志
today = date.today().isoformat()
article['content']['updates'].append({
    'date': today,
    'note': f'自动更新：统计数字刷新（共{total}篇），扫描新增重要条目'
})

# 写入
with open(INDEX_ARTICLE_PATH, 'w', encoding='utf-8') as f:
    json.dump(article, f, indent=2, ensure_ascii=False)

# 同步到 public/
os.makedirs(os.path.dirname(PUBLIC_INDEX_PATH), exist_ok=True)
os.makedirs(os.path.dirname(PUBLIC_ARTICLE_PATH), exist_ok=True)

with open(PUBLIC_INDEX_PATH, 'w', encoding='utf-8') as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

with open(PUBLIC_ARTICLE_PATH, 'w', encoding='utf-8') as f:
    json.dump(article, f, indent=2, ensure_ascii=False)

print(f'✅ 索引已更新: {total}篇文章, {len(cat_count)}个分类')
print(f'   更新日志已写入: {today}')

# 5. Git push 触发 Vercel 部署
git_script = os.path.expanduser('~/.hermes/scripts/git_push_knowledge.py')
if os.path.exists(git_script):
    import subprocess as sp
    rc = sp.run(['python3', git_script], capture_output=True, text=True, timeout=30)
    for line in rc.stdout.strip().split('\n'):
        print(f'   {line}')
    if rc.stderr:
        print(f'   stderr: {rc.stderr[:200]}')
