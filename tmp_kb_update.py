import json
from pathlib import Path
from datetime import datetime, timezone

base = Path('/Users/utopia/.hermes/knowledge-nextjs')
data_dir = base / 'data'
articles_dir = data_dir / 'articles'
index_path = data_dir / 'index.json'
log_path = base / 'collection_log.txt'

now_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
now_stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')

new_article = {
  'id': 'Gerald-Zaltman-Zaltman-Metaphor-Elicitation-Technique-深层隐喻消费者洞察方法论',
  'category': '营销',
  'title': 'Gerald Zaltman《Zaltman Metaphor Elicitation Technique》深层隐喻消费者洞察方法论',
  'keywords': [
    'Gerald Zaltman', 'ZMET', 'Zaltman Metaphor Elicitation Technique', 'Deep Metaphors',
    'Consumer Psychology', 'Qualitative Research', 'Marketing Research', '隐喻研究', '消费者洞察', '品牌策略'
  ],
  'summary': '核心主题：用图片、隐喻、深度访谈与心智地图，挖出消费者无法直接说清却持续支配选择的无意识结构，把“用户说了什么”升级为“用户到底如何感知世界、组织意义与做出决定”。',
  'importance': 5,
  'learned_at': now_date,
  'source': 'Vibrant Publishers 公开产品页将本书描述为 uncovering deep consumer insights 的消费者洞察工具；Olson Zaltman 官方 ZMET 页面说明其为揭示消费者无意识 thoughts / feelings / needs / desires 的定性研究方法，并强调 Deep Metaphors、trained interviewer、Mind of the Market Lab at Harvard Business School 等关键表述；本次据此整理为可执行方法论文。',
  'file': 'articles/Gerald-Zaltman-Zaltman-Metaphor-Elicitation-Technique-深层隐喻消费者洞察方法论.json',
  'content': {
    'core_formula': '\n'.join([
      'ZMET 总公式',
      '深层消费者洞察 = 图像唤起 x 隐喻提取 x 无意识联想挖掘 x 深度访谈质量 x 模式综合能力 x 战略转译能力',
      '',
      '方法主线',
      '图片准备 -> 隐喻访谈 -> 对立构念 -> 感官与情绪探索 -> 心智地图 -> 深层隐喻归纳 -> 品牌/产品/传播动作',
      '',
      '一句话理解',
      '消费者常常不会直接说出真正驱动选择的底层意义结构；ZMET 通过隐喻和图像，把“说不出来的感受”转译成可分析、可行动的认知地图。',
      '',
      '失败公式',
      '浅层洞察 = 只问态度 x 只收集显性意见 x 忽视情绪/记忆/象征意义 x 缺少综合分析',
      '',
      '战略判断',
      '如果团队只能得到“用户想要更便宜、更方便、更好用”这类表层答案，通常说明研究还没进入 ZMET 所说的深层隐喻区。'
    ]),
    'layers': [
      {'level': 1, 'title': '第一层：来源校准与方法定位', 'content': [
        'Vibrant Publishers 公共产品页把本书定位为一种 powerful tool，用来 uncover deep consumer insights 并增强 marketing research strategies。',
        'Olson Zaltman 官方页面则把 ZMET 定义为一种 qualitative research methodology，能够揭示更深层的 consumer psychology，并帮助形成更有效的 brand strategies。',
        '两组公开表述合在一起，可以给出一个非常清晰的方法定位：ZMET 不是普通深访技巧，而是一套围绕无意识意义结构展开的消费者洞察系统。',
        '它关心的不是“顾客口头说喜欢什么”，而是“顾客如何通过隐喻、意象、情绪和记忆来组织自己对世界的理解”。',
        '因此，ZMET 最适合解决那类表面数据很多、但团队仍然不明白消费者真正为什么选择、迟疑、迁移或忠诚的问题。',
        '对于营销、品牌、创新、包装、品类教育、体验设计而言，这种方法的价值在于把抽象心理机制转成更有解释力的洞察。'
      ]},
      {'level': 2, 'title': '第二层：为什么传统用户访谈经常不够深', 'content': [
        '传统访谈常常停留在显性层：你喜欢什么功能、你为什么购买、你觉得哪里不方便。',
        '这类问题当然有价值，但往往只能得到可被社会化表达的答案。',
        '而 ZMET 的假设是：大量关键决策发生在消费者难以完整自觉、也难以直接语言化的层面。',
        '用户会说“我想要更简单”，但他真正追求的也许是掌控感、体面感、风险可控感、身份确认或心理安全。',
        '用户会说“价格太高”，但背后也许是“这个品牌不像是为我这样的人设计的”。',
        '用户会说“我没时间换工具”，背后也许是“我害怕犯错并被团队评价”。',
        '因此，普通访谈的盲点不一定是问题数量不够，而是没有合适方法进入隐喻、情绪、象征和记忆层。'
      ]},
      {'level': 3, 'title': '第三层：ZMET 的核心假设：人通过隐喻理解世界', 'content': [
        'ZMET 背后的根本观点是：隐喻不是修辞装饰，而是认知结构。',
        '人们理解“成长”“控制”“自由”“压迫”“安全”“归属”时，往往借助空间、运动、容器、平衡、旅程等深层意象。',
        '所以，当消费者描述品牌体验时，他说出口的句子只是表层，真正稳定的结构常常藏在比喻、图像联想和情绪投射里。',
        '例如，理财产品可能被感知为“安全港”“迷宫”“监狱”或“方向盘”；同样的功能描述，背后的行动倾向完全不同。',
        '只要团队能识别这些深层隐喻，就能更好地理解：用户究竟害怕什么、向往什么、如何解释自己的处境、为什么会被某种品牌语言打动。',
        '这也是为什么 ZMET 特别强调图片、故事、对立构念和感官联想，而不是只靠理性问答。'
      ]},
      {'level': 4, 'title': '第四层：研究流程总览：从图片到心智地图', 'content': [
        '可把 ZMET 压缩为八步。',
        '1. 明确研究主题与决策场景。',
        '2. 让受访者提前收集与主题相关的图片。',
        '3. 以图片为起点做深度访谈。',
        '4. 追问图片背后的隐喻、情绪、记忆与意义。',
        '5. 通过对立构念、感官探索、缺失图像等技术继续向深层推进。',
        '6. 抽取反复出现的核心构念与关系。',
        '7. 形成共识图或心智地图。',
        '8. 把深层隐喻转成品牌、产品、传播、体验动作。',
        '这个流程的关键不是仪式感，而是让受访者跳出“我应该怎么回答”进入“我实际如何感受与联想”。',
        '换句话说，ZMET 不是采集观点，而是采集意义结构。'
      ]},
      {'level': 5, 'title': '第五层：图片唤起为什么这么重要', 'content': [
        'ZMET 最具辨识度的动作之一，就是让受访者提前准备能代表该主题的图片。',
        '原因在于图片更容易激活情绪、记忆、身体感受与联想，而非只激活理性描述。',
        '当受访者选择图片时，他已经在进行一次预语言化思考：什么意象最接近我对这个主题的真实感受。',
        '访谈者随后不急着解释图片，而是围绕图片问：这张图为什么重要？它代表了什么？哪里像你的经历？哪里不像？',
        '图片还提供了一个低防御的切入口。直接问“你为什么不信任这个品牌”容易得到礼貌答案；但从图片出发，更容易看到被压抑或模糊的情绪。',
        '对创新团队来说，这意味着研究对象不只是一份 verbal feedback，而是一套更丰富的意义系统。'
      ]},
      {'level': 6, 'title': '第六层：关键访谈技术：怎样把表层回答往下挖', 'content': [
        'ZMET 的价值不在“看图说话”，而在一连串向深层推进的追问技术。',
        '常见动作包括：',
        '隐喻追问：这像什么？为什么像？',
        '缺失图像：有没有一张你没找到、但非常想要的图？',
        '三分组：哪些图更接近彼此？它们为什么属于一组？',
        '对立构念：如果这是“开放”，它的反面是什么？',
        '感官唤起：这个体验如果是一种声音、颜色或气味，会是什么？',
        '重要性排序：哪张图最核心？如果只能保留一张会是哪张？',
        '这些技术共同服务一个目的：让隐性心理结构变得可见。',
        '好的 ZMET 访谈者像心理地图绘制者，而不是问卷朗读者。'
      ]},
      {'level': 7, 'title': '第七层：Deep Metaphors：从个体材料走向群体模式', 'content': [
        'Olson Zaltman 官方页面特别强调 Deep Metaphors。',
        '可以把它理解为那些跨情境、跨品牌、跨语言仍然稳定出现的深层意义母题。',
        '例如：平衡、转化、连接、控制、旅程、容器、资源、身份边界。',
        '当多个受访者反复用相似图像表达某类体验时，团队就不该把它只当作个人偏好，而应视作更底层的 category meaning。',
        '这类深层隐喻特别适合指导品牌主叙事、广告创意方向、包装与视觉语言、新品概念开发以及体验流程中的情绪节点设计。',
        '它们让团队不再只围绕功能词打转，而能围绕人类更稳定的意义逻辑组织策略。'
      ]},
      {'level': 8, 'title': '第八层：分析产出：心智地图比摘要报告更有用', 'content': [
        'ZMET 的高价值产出不是“受访者喜欢 A、不喜欢 B”的摘要句，而是一张关系图。',
        '这张图通常展示：哪些核心构念处于中心、哪些情绪和象征彼此相连、哪些冲突共同出现、哪些品牌动作能够改变整体感知。',
        '比如，某健康品牌的中心构念可能不是“营养”，而是“掌控身体的主动权”；某办公产品的中心构念可能不是“效率”，而是“减少混乱感”。',
        '一旦团队看见这张地图，就能更自然地回答几个大问题：我们到底在帮助用户获得什么深层结果？用户最强的心理阻力究竟是什么？我们现有传播语气是否和用户的深层隐喻冲突？',
        '从管理实践上看，心智地图比冗长报告更容易被跨部门共享和采用。'
      ]},
      {'level': 9, 'title': '第九层：从洞察到动作：营销、品牌、产品各自怎么用', 'content': [
        '营销团队可以用 ZMET 重写信息架构：先围绕核心隐喻命名问题，再围绕深层结果设计价值主张。',
        '品牌团队可以用它校准视觉与语言系统：如果用户把“安全”感知成“被稳稳托住”，那品牌就应避免制造尖锐、漂浮、失控的意象。',
        '产品团队可以用它理解采用阻力：用户拒绝新功能，可能不是因为功能弱，而是因为它破坏了原有掌控感。',
        '创新团队可以用它做概念筛选：哪个方向更贴近用户心中真正的成长、连接、身份或自由意象。',
        '销售与客服团队也能受益，因为他们会更清楚客户真正担心的是实施风险、身份受损，还是决策不可逆。',
        '简言之，ZMET 把“消费者研究”从一个报告环节，变成一个战略翻译引擎。'
      ]},
      {'level': 10, 'title': '第十层：与常见研究框架的关系', 'content': [
        '| 框架 | 强项 | 局限 | ZMET 的补位价值 |',
        '|---|---|---|---|',
        '| 常规深访 | 了解显性动机与流程 | 容易停在理性解释 | 进入隐喻与无意识层 |',
        '| JTBD 访谈 | 解释行为转变与选择逻辑 | 对象征和情绪层展开有限 | 丰富 job 背后的意义结构 |',
        '| 可用性测试 | 找交互阻力 | 难解释深层价值与身份感 | 揭示“为什么它让人抗拒或安心” |',
        '| 问卷调研 | 规模化验证 | 很依赖预设选项 | 为量化研究提供更深命题 |',
        '| 品牌追踪 | 看认知变化 | 多为结果监测 | 帮助解释结果背后的心理机制 |',
        '因此，ZMET 不该被误解为替代一切研究方法。',
        '更好的理解是：它特别擅长在高不确定、强情绪、强象征、强身份含义的问题上，提供普通研究难以获得的深层解释力。'
      ]},
      {'level': 11, 'title': '第十一层：常见误用、风险与实施边界', 'content': [
        '第一种误用：把 ZMET 当成“让用户发散创意”的头脑风暴工具。纠偏：它的目标不是收集灵感，而是抽取稳定的意义模式。',
        '第二种误用：只做几次访谈就草率宣布找到了一个 Deep Metaphor。纠偏：需要在多个样本里识别重复关系，并谨慎综合。',
        '第三种误用：把所有隐喻都当成创意文案素材。纠偏：真正重要的是结构，不是金句；要看隐喻如何影响行为。',
        '第四种误用：研究做得很深，但最后没有转译到产品、传播和体验动作。纠偏：研究设计时就要明确将服务哪类决策。',
        '第五种误用：忽视访谈者训练。纠偏：ZMET 对追问能力、综合能力和非引导式倾听要求很高；如果执行粗糙，结果很容易流于表演化。',
        '方法边界同样明确：它成本高于普通访谈，不适合每个运营微问题；但对于品牌重塑、品类教育、创新概念开发等重大问题，回报往往更高。'
      ]},
      {'level': 12, 'title': '第十二层：工具模板、原书金句与 30 天行动计划', 'content': [
        '研究主题：________________',
        '关键决策：品牌 / 产品 / 概念 / 传播 / 包装 / 体验',
        '目标人群：________________',
        '当前困惑：________________',
        '想挖出的深层问题：________________',
        '访谈提示：为什么选这张图？它最像你的哪段经历？如果这张图有反面，会是什么？如果这个体验是一种颜色、声音或空间，会是什么？',
        '公开表述 1：Discover the Zaltman Metaphor Elicitation Technique - a powerful tool for uncovering deep consumer insights and enhancing marketing research strategies.',
        '公开表述 2：ZMET is a qualitative research methodology that reveals deeper insights into consumer psychology.',
        '公开表述 3：It unlocks the Deep Metaphors rooted in universal human experiences.',
        '公开表述 4：A ZMET interview gives consumers a safe place to explore the deeply personal feelings and beliefs that unconsciously shape their behavior.',
        '公开表述 5：Metaphors get deep; and when you get deep, you can influence perceptions and behavior.',
        '30 天计划：第 1 周定义问题与样本；第 2 周做 5 到 8 次图片式深访；第 3 周整理构念与心智地图；第 4 周把深层隐喻翻译成首页信息、品牌意象或产品改动。',
        f'更新日志：{now_date} 首次收录，基于 Vibrant Publishers 与 Olson Zaltman 公开页面，整理 ZMET 的图片唤起、深层隐喻、心智地图与战略转译方法。'
      ]}
    ],
    'updates': [
      {'date': now_date, 'note': '创建：收录《Zaltman Metaphor Elicitation Technique》，整理 ZMET 研究流程、Deep Metaphors、图片式访谈与品牌战略转译框架。'}
    ]
  }
}

expanded_article = {
  'id': 'Donald-Miller-Building-a-StoryBrand',
  'title': 'Donald Miller《Building a StoryBrand》SB7品牌叙事方法论',
  'category': '营销',
  'keywords': [
    'Building a StoryBrand', 'Donald Miller', 'SB7', 'StoryBrand 7-Part Framework', '品牌叙事', '客户英雄',
    '品牌指南', '营销信息清晰度', '品牌文案', '叙事营销', '过渡CTA', 'homepage messaging', 'sales narrative',
    'message clarity', 'brand script', 'marketing funnel'
  ],
  'summary': '核心主题：StoryBrand 不是“给品牌讲故事”，而是用客户英雄视角，把定位、信息架构、页面文案、销售开场、邮件序列与产品内引导统一成一个低认知负担的行动系统。',
  'importance': 5,
  'learned_at': '2026-05-31',
  'source': 'Donald Miller《Building a StoryBrand: Clarify Your Message So Customers Will Listen》(2017)；StoryBrand 公开 SB7 框架表述；既有知识库版本；本次扩写继续将其升级为“定位 x 叙事 x 触点 x 实验 x 组织协同”的完整应用方法。',
  'file': 'articles/Donald-Miller-Building-a-StoryBrand.json',
  'expanded_at': now_date,
  'content': {
    'core_formula': '\n'.join([
      'SB7 总公式',
      '高转化品牌叙事 = 英雄（客户） x 三层问题（外在/内在/哲学） x 指南（共情+权威） x 简明计划 x 明确 CTA x 失败代价 x 成功愿景',
      '',
      '经营化公式',
      '品牌清晰度 = 价值主张清晰度 x 触点一致性 x 行动指令明确度 x 证据可信度 x 受众匹配度',
      '',
      '一句话理解',
      'StoryBrand 的本质不是让品牌更会讲故事，而是让客户更快听懂：这是不是在帮我、为什么可信、我现在该做什么。',
      '',
      '失败公式',
      '信息失效 = 品牌自恋 x 问题模糊 x 方案复杂 x CTA 含糊 x 证据后置 x 成功画面缺席'
    ]),
    'layers': [
      {'level': 1, 'title': '第一层：StoryBrand 真正解决的问题是“信息混乱”而不是“创意不够”', 'content': [
        'Donald Miller 的关键洞见不是“品牌应该浪漫化自己”，而是“客户的注意力极其有限”。',
        '当品牌首页、广告、提案、销售开场都在讲自己时，客户的大脑会自动跳过。',
        '所以 StoryBrand 的首要任务不是增加表达，而是删减杂讯。',
        '如果顾客在 5 秒内还看不懂你是做什么的，后面的优势、案例、功能、奖项几乎都失去作用。',
        'SB7 用一个极简叙事骨架，把复杂业务压缩成更容易被理解和复述的形式。',
        '这使它成为定位与文案之间的翻译层，也成为市场、销售、创始人和产品团队之间的统一语言。'
      ]},
      {'level': 2, 'title': '第二层：客户是英雄，品牌是指南，这是整个框架的支点', 'content': [
        'StoryBrand 最经典的一句话是：The customer is the hero, not your brand.',
        '这句话之所以重要，是因为它强迫品牌从“自我介绍模式”切换到“客户问题模式”。',
        '自我介绍模式会产出这样的表达：我们成立于哪一年、获得过什么奖、采用什么技术、愿景有多宏大。',
        '客户问题模式则会产出这样的表达：你现在被什么问题困住、为什么这很烦、我们如何帮助你更快获得结果。',
        '品牌不是主角，并不意味着品牌不重要，而是品牌的角色更像可信的向导。',
        '向导要做两件事：理解客户的处境，并让客户相信自己有能力带路。',
        '如果缺少共情，品牌像一个居高临下的专家；如果缺少权威，品牌像一个善良但没用的朋友。'
      ]},
      {'level': 3, 'title': '第三层：SB7 七要素的真正作用不是背诵，而是压缩决策路径', 'content': [
        'Hero 负责让客户看到自己。',
        'Problem 负责让客户承认“这件事值得现在处理”。',
        'Guide 负责建立信任。',
        'Plan 负责降低开始难度。',
        'CTA 负责推动动作。',
        'Failure 负责增加行动张力。',
        'Success 负责放大愿景吸引。',
        '这七步如果拆开看像文案模块；合起来看，其实是在缩短客户从理解到行动的路径。',
        '所以 SB7 的高明之处不是结构本身，而是它把认知阻力、情绪阻力和执行阻力同时往下降。'
      ]},
      {'level': 4, 'title': '第四层：三层问题模型，外在问题只是入口', 'content': [
        '很多品牌只会写外在问题，例如“数据分散”“项目延期”“线索转化低”。',
        '这还不够，因为外在问题只是表面麻烦。',
        '客户真正愿意采取行动，通常是因为内在问题和哲学问题被点中。',
        '| 层次 | 含义 | 典型表达 |',
        '|---|---|---|',
        '| 外在问题 | 具体发生了什么 | 团队信息散落在不同工具里 |',
        '| 内在问题 | 这让我感觉如何 | 我总在救火，像自己失控了一样 |',
        '| 哲学问题 | 这在价值上为什么不该继续 | 好团队不该被低效流程困住 |',
        '真正强的首页、广告或销售开场，往往至少会碰到其中两层，最好三层都有。',
        '外在问题让客户知道你理解处境，内在问题让客户感到被看见，哲学问题让行动获得道义正当性。'
      ]},
      {'level': 5, 'title': '第五层：Guide 模块，共情与权威如何共同构成信任', 'content': [
        'Guide 是 SB7 中最容易被做偏的部分。',
        '很多品牌只会用“我们服务过很多客户”“我们技术领先”来表达权威，却没有共情。',
        '也有团队只会说“我们理解你的痛苦”，却拿不出任何可信证据。',
        '更好的 Guide 应同时具备：共情、权威与风险缓释。',
        '例如：我们知道第一次迁移系统很焦虑；我们已帮助 300+ 团队在 30 天内完成迁移；并提供专人上手和阶段检查。',
        'Guide 写得好，客户会从“你在推销我”转向“你在带我走”；写不好，后面的计划和 CTA 只会显得更像催促。'
      ]},
      {'level': 6, 'title': '第六层：Plan 与 CTA，把“听懂”变成“愿意开始”', 'content': [
        'Plan 的主要任务是降低复杂感。客户即使认同问题，也可能因为开始门槛太高而停下。',
        '因此，一个好计划往往是短、清楚、低风险的。',
        '| 类型 | 作用 | 例子 |',
        '|---|---|---|',
        '| Process Plan | 告诉客户如何开始 | 预约演示 -> 获得诊断 -> 启动试点 |',
        '| Agreement Plan | 告诉客户这件事很安全 | 专人实施 / 随时取消 / 无隐藏成本 |',
        'CTA 则负责把模糊意向变成明确动作。直接 CTA 适合高意图场景，过渡 CTA 适合低意图场景。',
        '很多页面失败，不是没有价值，而是没有明确教客户怎么往前走。'
      ]},
      {'level': 7, 'title': '第七层：Failure 与 Success，为什么行动张力不能只靠“好处”支撑', 'content': [
        '客户大脑天然偏好维持现状，因此只描绘成功好处还不够。',
        'Failure 模块不是制造恐吓，而是提醒客户：不行动也有代价，例如继续浪费时间、继续让团队混乱、继续错失窗口。',
        'Success 模块则要把未来描绘得具体、可感知。',
        '最有效的成功画面通常包含三层：功能结果、情绪结果、身份结果。',
        'Failure 让拖延失去吸引力，Success 让前进拥有意义，这两者一起才形成足够的行动张力。'
      ]},
      {'level': 8, 'title': '第八层：StoryBrand 不是一句口号，而是一套消息架构系统', 'content': [
        '成熟的 StoryBrand 不等于“想出一句好 slogan”。',
        '它更像一套消息架构：我们服务谁，对方正在经历什么问题，我们凭什么值得信任，我们建议他先走哪一步，他继续拖延会损失什么，成功后的世界是什么样。',
        '这套架构可以被翻译到首页首屏、产品页、广告、邮件、销售提案、客服脚本、产品内提示。',
        '因此 StoryBrand 的真正价值不是单点转化率优化，而是降低全链路解释成本。',
        '当客户在不同触点听到的是同一套结构，他会更快形成稳定认知。'
      ]},
      {'level': 9, 'title': '第九层：分受众、分阶段写 StoryBrand，不能只写一个通用版本', 'content': [
        '最常见的误区之一，是把一套 SB7 文案复制到所有场景。',
        '但冷流量、热线索、试用用户、续费客户，面对的问题和行动阻力完全不同。',
        '| 阶段 | 叙事重点 | 适合的 CTA |',
        '|---|---|---|',
        '| 冷流量 | 问题命名 + 结果吸引 | 下载资料 / 获取清单 |',
        '| 温流量 | 指南证据 + 简明计划 | 预约演示 / 申请咨询 |',
        '| 热流量 | 差异化证据 + 风险缓释 | 购买 / 试用 |',
        '| 已购买 | 激活路径 + 首次成功 | 完成设置 / 导入数据 |',
        '| 老客户 | 新成果愿景 + 扩展价值 | 升级 / 续费 / 推荐 |',
        '复杂 B2B 业务还要按角色拆分版本：使用者、管理者、采购者看到的 Hero、Problem、Proof 都不同。'
      ]},
      {'level': 10, 'title': '第十层：多触点落地，官网、销售、邮件、视频、onboarding 要说同一套话', 'content': [
        '首页首屏要做四件事：点明对象、点明问题或结果、点明你是解决方案、给 CTA。',
        '销售开场不要从公司介绍开始，而要从客户正在承受的张力开始。',
        '邮件序列不要一次性说完所有信息，而要按“问题 -> 代价 -> 指南 -> 计划 -> CTA”推进。',
        '视频脚本也能使用 SB7：前三秒点问题，中段给转机，结尾给动作。',
        '产品 onboarding 同样属于 StoryBrand 的范围，因为用户进入产品后必须继续感到“这条路我走得下去”。',
        '因此，StoryBrand 不只是营销部门的写作框架，也是一种跨触点体验一致性框架。'
      ]},
      {'level': 11, 'title': '第十一层：与 Positioning、JTBD、AIDA、PAS 的关系', 'content': [
        '| 框架 | 回答的问题 | 与 StoryBrand 的关系 |',
        '|---|---|---|',
        '| Positioning | 我们在市场中占什么位置 | StoryBrand 负责把定位翻译成客户更快听懂的话 |',
        '| JTBD | 用户为什么在某情境下“雇佣”产品 | StoryBrand 可用 JTBD 结果强化 Hero 与 Problem |',
        '| AIDA | 如何从注意推进到行动 | StoryBrand 提供更完整的叙事角色与信任结构 |',
        '| PAS | 如何先放大问题再给方案 | StoryBrand 在品牌角色、计划、成功愿景上更完整 |',
        '所以 StoryBrand 不是一切的上位替代。定位错了，StoryBrand 只会把错误说得更清楚；用户研究做浅了，StoryBrand 只会把模糊理解包成好听文案。'
      ]},
      {'level': 12, 'title': '第十二层：诊断、实验与评分卡，有效故事必须被行为数据验证', 'content': [
        '一个故事好不好，不能只靠团队主观判断。',
        '最直接的验证来自行为：点击率、表单完成率、销售转化、用户复述准确度、激活率。',
        '首页评分卡：清晰度、共鸣度、信任度、可行性、动机性。',
        '优先测试变量：标题、问题表达、CTA、证据位置、计划形式。',
        '如果用户看完页面仍复述不出“你帮谁解决什么问题”，说明故事还没成功。'
      ]},
      {'level': 13, 'title': '第十三层：常见误区与纠偏', 'content': [
        '误区 1：把创始人故事放在最前面。纠偏：创始人故事更适合做 Guide 证据，而不是首屏主叙事。',
        '误区 2：把成功写成功能列表。纠偏：补上情绪结果与身份结果。',
        '误区 3：CTA 太礼貌。纠偏：用清晰动词和明确收益。',
        '误区 4：每个页面试图讲三个故事。纠偏：每个页面保留一条主线，一个主要动作。',
        '误区 5：只讲好处，不讲不作为的代价。纠偏：加入 Failure，让客户知道拖延不是中性。',
        '误区 6：营销说一套，销售说一套，产品又是另一套。纠偏：维护统一品牌脚本并按场景做派生版本。'
      ]},
      {'level': 14, 'title': '第十四层：团队实施模板、金句与更新日志', 'content': [
        '一句话品牌脚本：我们帮助【谁】解决【什么问题】，让他们能够【获得什么结果】。',
        '完整 SB7 模板：一个【客户】想要【目标】；但他正经历【外在问题】、【内在问题】与【哲学问题】；我们理解【他的感受】，并具备【权威证据】；所以我们提供【三步计划】；现在就【直接 CTA】；否则你可能继续遭遇【失败后果】；这样你就能获得【成功愿景】。',
        '原书高频金句：The customer is the hero, not your brand. If you confuse, you lose. A confused mind always says no. People do not buy the best products; they buy the products they can understand the fastest. Customers are not looking for another hero; they are looking for a guide. Empathy and authority are the two things a guide must have to earn trust.',
        '30 天执行计划：第 1 周盘点现有触点中的“我们式表达”；第 2 周重写 Hero、Problem、Guide、Plan、CTA；第 3 周拆成首页版、销售版、邮件版、onboarding 版；第 4 周运行标题和 CTA 实验，并做目标客户复述测试。',
        f'更新日志：2026-05-10 初稿创建；2026-05-18 补充 SB7 七要素与案例；2026-05-31 第一次系统扩写；{now_date} 二次深扩写，升级为定位、叙事、触点、实验、组织协同一体化操作系统。'
      ]}
    ],
    'updates': [
      {'date': '2026-05-10', 'note': '初稿创建（占位文档）。'},
      {'date': '2026-05-18', 'note': '补充 SB7 七要素、案例与实施清单。'},
      {'date': '2026-05-31', 'note': '第一次系统扩写：统一为五层结构，补充首页/邮件/销售应用、工具箱与方法边界。'},
      {'date': now_date, 'note': '二次深扩写：重构为 14 层系统结构，补充三层问题、消息架构、多触点落地、分受众版本、实验评分卡与执行模板。'}
    ]
  }
}

new_path = articles_dir / new_article['file'].split('/', 1)[1]
new_path.write_text(json.dumps(new_article, ensure_ascii=False, indent=2) + '\n')

storybrand_path = articles_dir / 'Donald-Miller-Building-a-StoryBrand.json'
storybrand_path.write_text(json.dumps(expanded_article, ensure_ascii=False, indent=2) + '\n')

index = json.loads(index_path.read_text())
articles = [a for a in index['articles'] if a.get('id') != new_article['id']]
for i, a in enumerate(articles):
    if a.get('id') == expanded_article['id']:
        articles[i] = {k: expanded_article[k] for k in ['id', 'category', 'title', 'keywords', 'summary', 'importance', 'learned_at', 'source', 'file']}
        break
else:
    articles.append({k: expanded_article[k] for k in ['id', 'category', 'title', 'keywords', 'summary', 'importance', 'learned_at', 'source', 'file']})
articles.append({k: new_article[k] for k in ['id', 'category', 'title', 'keywords', 'summary', 'importance', 'learned_at', 'source', 'file']})
index['articles'] = articles
index_path.write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')

with log_path.open('a') as f:
    f.write(f"\n{now_stamp} — Cron Job Collection Run\n")
    f.write("=============================================\n\n")
    f.write("=== TASK 1: 收录新书 (1本) — 营销 ===\n")
    f.write("1. Gerald Zaltman《Zaltman Metaphor Elicitation Technique》深层隐喻消费者洞察方法论\n")
    f.write("   - 核心公式: 深层消费者洞察 = 图像唤起 x 隐喻提取 x 无意识联想挖掘 x 深度访谈质量 x 模式综合能力 x 战略转译能力\n")
    f.write("   - 关键框架: 图片式深访八步法 x Deep Metaphors x 心智地图 x 品牌/产品/传播转译\n")
    f.write("   - 文件: Gerald-Zaltman-Zaltman-Metaphor-Elicitation-Technique-深层隐喻消费者洞察方法论.json\n\n")
    f.write("=== TASK 2: 扩写已有文章 (1篇) — 营销 ===\n")
    f.write("- Donald Miller《Building a StoryBrand》SB7品牌叙事方法论\n")
    f.write("  - 扩写前: 91 行, 20.6KB\n")
    f.write("  - 扩写后: 待统计\n")
    f.write("  - 扩写内容: 新增三层问题模型、消息架构、多触点落地、分受众版本、实验评分卡与执行模板\n\n")

print('ok')
print('index_count', len(index['articles']))
print('new_file', new_path)
