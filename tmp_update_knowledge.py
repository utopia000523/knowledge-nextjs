import json
import os
from collections import Counter
from datetime import datetime

base = os.path.expanduser('~/.hermes/knowledge-nextjs')
data_dir = os.path.join(base, 'data')
articles_dir = os.path.join(data_dir, 'articles')
index_path = os.path.join(data_dir, 'index.json')
log_path = os.path.join(base, 'collection_log.txt')

new_article = json.loads(r'''{
  "id": "John-E-Kennedy-Reason-Why-Advertising-理由型广告与纸上销售方法论",
  "category": "营销",
  "title": "John E. Kennedy《Reason Why Advertising》理由型广告与纸上销售方法论",
  "keywords": [
    "John E. Kennedy",
    "Reason Why Advertising",
    "Salesmanship in Print",
    "Reason Why Copy",
    "Direct Response",
    "Claude Hopkins",
    "Scientific Advertising",
    "广告文案",
    "营销方法论",
    "纸上销售"
  ],
  "summary": "核心主题：广告不是抽象曝光，而是可验证的纸上销售。Kennedy 用“理由型广告”把广告从印象派表达推进到可测试、可证明、可归因的说服系统：先锁定可成交人群，再给出足够具体的购买理由，再用结果而非审美评判广告。",
  "importance": 5,
  "learned_at": "2026-06-01",
  "source": "本次先按要求使用 web_search 检索；公开结果提供 Google Books/Amazon/Goodreads 书目与摘要，以及 Breakthrough Marketing Secrets 对 Kennedy 核心定义“Advertising is salesmanship in print.” 的公开引述。交叉整理为可执行方法框架。",
  "file": "articles/John-E-Kennedy-Reason-Why-Advertising-理由型广告与纸上销售方法论.json",
  "content": {
    "core_formula": {
      "name": "理由型广告公式",
      "equation": "广告产出 = 可成交受众匹配度 x 购买理由清晰度 x 证据可信度 x 诉求具体性 x 测试反馈速度",
      "compressed_statement": "广告不是把名字挂在人前，而是像一个高水平销售员一样，在有限篇幅内说明：为什么是你，为什么是现在，为什么值得相信。",
      "first_principles": [
        "广告的价值不在于被内部喜欢，而在于以可接受成本带来可归因销售。",
        "抽象赞美会制造感觉，具体理由才会推动行动。",
        "不是所有人都值得说服；真正的效率来自先选对可成交受众。",
        "一则广告如果无法被测试和迭代，就无法持续累积优势。"
      ]
    },
    "layers": [
      {
        "level": 1,
        "title": "第一层：问题意识——Kennedy 到底改变了什么",
        "overview": [
          "在公开流传的历史材料中，Kennedy 最著名的定义是：Advertising is salesmanship in print。",
          "这一定义把广告从“艺术化的名片展示”拉回“可验证的销售行为”。",
          "《Reason Why Advertising》的关键，不只是告诉你要写更会卖的文案，而是重设广告评价标准：用销售结果、线索质量、成本与回收来评估，而不是用内部审美来评估。"
        ],
        "context": [
          "当广告被视为模糊曝光时，团队会偏向追求好看、宏大、讨喜、体面。",
          "当广告被视为纸上销售时，团队会追问：目标对象是谁、理由是什么、证据是什么、怎么测试。",
          "Kennedy 的贡献，是把广告决策语言变成经营语言。"
        ],
        "one_sentence_answer": "广告若不能像销售员一样解释价值、消除疑虑并推动行动，就只是昂贵的噪音。"
      },
      {
        "level": 2,
        "title": "第二层：核心定义——什么叫 Reason Why Advertising",
        "definitions": [
          {
            "term": "Reason Why Advertising",
            "definition": "围绕“客户为什么应该购买”来组织广告，而不是围绕企业想说什么来组织广告。",
            "managerial_meaning": "每一段文案都要服务于购买理由，而非修饰品牌自我表达。"
          },
          {
            "term": "Salesmanship in Print",
            "definition": "让广告像优秀销售员一样完成解释、筛选、说服、回应疑虑与促成行动。",
            "managerial_meaning": "文案必须承担销售对话功能，而不仅是装点门面。"
          },
          {
            "term": "Proof-Oriented Copy",
            "definition": "把事实、机制、对比、演示、案例、保证等要素转化为可信证据链。",
            "managerial_meaning": "如果没有证据，就会把说服任务丢给客户想象力。"
          },
          {
            "term": "Testable Advertising",
            "definition": "允许不同标题、报价、受众、版位、优惠和 CTA 在真实市场中比较效果。",
            "managerial_meaning": "最强观点不是拍脑袋决定，而是在市场里胜出。"
          }
        ],
        "non_examples": [
          "只有口号，没有购买理由。",
          "只有氛围，没有产品机制。",
          "只有曝光目标，没有行动设计。",
          "只有创意夸张，没有受众选择。"
        ]
      },
      {
        "level": 3,
        "title": "第三层：方法总图——五步理由型广告工作流",
        "workflow": [
          {
            "step": 1,
            "name": "选择最值得说服的人",
            "goal": "缩小受众，优先面向最可能成交、最能理解价值、最有支付能力的人群。",
            "deliverables": [
              "目标受众描述",
              "购买触发情境",
              "拒绝服务人群边界"
            ]
          },
          {
            "step": 2,
            "name": "提炼可成交理由",
            "goal": "把功能、结果、风险逆转、时间收益、身份收益整理为客户真正关心的购买理由。",
            "deliverables": [
              "理由清单",
              "优先级排序",
              "一句话价值主张"
            ]
          },
          {
            "step": 3,
            "name": "补强证据与机制",
            "goal": "为每条理由匹配具体证明、可理解机制、演示、对比或担保。",
            "deliverables": [
              "证据表",
              "机制说明",
              "反对意见回应"
            ]
          },
          {
            "step": 4,
            "name": "设计行动路径",
            "goal": "明确客户下一步该做什么，并降低行动门槛。",
            "deliverables": [
              "CTA 方案",
              "优惠或试用",
              "表单/咨询路径"
            ]
          },
          {
            "step": 5,
            "name": "测试与迭代",
            "goal": "让标题、角度、报价、版位、受众与承诺在市场里竞争。",
            "deliverables": [
              "测试计划",
              "指标看板",
              "迭代记录"
            ]
          }
        ]
      },
      {
        "level": 4,
        "title": "第四层：先做人群选择——不是所有流量都平等",
        "key_points": [
          "Kennedy 思路强调：先问“向谁说”，再问“说什么”。",
          "如果对象无支付能力、无紧迫性、无问题意识，再美的文案都只是浪费。",
          "高转化广告常来自更窄、更懂、更有痛感的人群，而不是更广的人群。"
        ],
        "audience_matrix": [
          {
            "segment": "痛点强、预算足、意识高",
            "priority": "最高",
            "message_style": "直接给承诺与证据",
            "risk": "竞争激烈，需要更强差异化"
          },
          {
            "segment": "痛点强、预算足、意识低",
            "priority": "高",
            "message_style": "先教育问题，再给方案",
            "risk": "教育成本更高"
          },
          {
            "segment": "痛点弱、预算足、意识高",
            "priority": "中",
            "message_style": "强调长期损失与效率收益",
            "risk": "容易拖延不行动"
          },
          {
            "segment": "痛点弱、预算低、意识低",
            "priority": "低",
            "message_style": "不宜作为首批获客主战场",
            "risk": "成本高且回收差"
          }
        ],
        "diagnostic_questions": [
          "这则广告是在说服最有可能购买的人，还是在讨好所有人？",
          "受众是否已经知道自己有问题？",
          "他们最担心损失什么：钱、时间、风险、身份还是麻烦？"
        ]
      },
      {
        "level": 5,
        "title": "第五层：购买理由设计——让客户知道为什么值得买",
        "reason_types": [
          {
            "type": "结果理由",
            "description": "买了之后能得到什么更好结果。",
            "examples": [
              "更快完成工作",
              "更稳定产生线索",
              "更低错误率"
            ]
          },
          {
            "type": "机制理由",
            "description": "为什么这个结果能够发生。",
            "examples": [
              "采用特定流程",
              "独特配方/系统",
              "服务保障机制"
            ]
          },
          {
            "type": "比较理由",
            "description": "相对替代方案为何更优。",
            "examples": [
              "比人工更省时",
              "比低价方案更稳",
              "比通用产品更贴合场景"
            ]
          },
          {
            "type": "风险逆转理由",
            "description": "降低试错恐惧。",
            "examples": [
              "退款保证",
              "免费试用",
              "按结果付费"
            ]
          },
          {
            "type": "时机理由",
            "description": "为什么现在就该行动。",
            "examples": [
              "错过窗口成本上升",
              "旺季前准备",
              "现有问题正在扩大"
            ]
          }
        ],
        "warning": "多数文案失败不是因为写得不够花，而是购买理由不够具体、可感、可信。"
      },
      {
        "level": 6,
        "title": "第六层：证据系统——说服不是喊得更大声，而是证明得更清楚",
        "proof_stack": [
          {
            "proof": "事实数据",
            "usage": "量化节省、增长、准确率、时间或成本",
            "best_for": "理性评估型客户"
          },
          {
            "proof": "机制解释",
            "usage": "解释为什么能做到，而非只说结果",
            "best_for": "复杂产品或高客单价场景"
          },
          {
            "proof": "案例/见证",
            "usage": "把抽象承诺变成真实故事",
            "best_for": "降低陌生感与怀疑"
          },
          {
            "proof": "演示/样本",
            "usage": "让客户提前感受结果",
            "best_for": "产品可见性高的场景"
          },
          {
            "proof": "担保/承诺",
            "usage": "缓解行动风险",
            "best_for": "首次购买或信任弱场景"
          }
        ],
        "evidence_sequence": [
          "先给主要利益点。",
          "再解释机制。",
          "随后补案例和证明。",
          "最后处理疑虑并引导行动。"
        ]
      },
      {
        "level": 7,
        "title": "第七层：标题、正文、CTA——纸上销售的三段推进",
        "headline_rules": [
          "标题优先承担筛选与抓住兴趣的任务，而不是追求文学性。",
          "好标题通常包含对象、问题、结果、机会或新机制。",
          "标题要帮正确的人意识到“这条信息与我有关”。"
        ],
        "body_rules": [
          "正文负责展开理由、解释机制、补证据、应对疑虑。",
          "结构应从最关心的利益点切入，再逐步提供证明。",
          "不要用企业自夸取代客户判断。"
        ],
        "cta_rules": [
          "CTA 必须清楚、单一、低摩擦。",
          "越高客单价、越陌生的交易，越需要把 CTA 设计为低承诺下一步。",
          "CTA 不是结束语，而是销售路径的一部分。"
        ],
        "cta_examples": [
          "立即申请试用",
          "获取诊断报告",
          "领取案例与报价",
          "预约 15 分钟评估"
        ]
      },
      {
        "level": 8,
        "title": "第八层：测试逻辑——让市场而不是会议室决定答案",
        "test_dimensions": [
          {
            "dimension": "标题",
            "question": "哪一种问题切入或结果切入更有效？"
          },
          {
            "dimension": "受众",
            "question": "哪一类人群的响应率与回收更高？"
          },
          {
            "dimension": "理由优先级",
            "question": "客户最先被哪个价值点打动？"
          },
          {
            "dimension": "报价/优惠",
            "question": "免费试用、样品、报告、折扣哪种更推动行动？"
          },
          {
            "dimension": "版位/渠道",
            "question": "搜索、邮件、着陆页、直邮、社群哪种更适合这一说服任务？"
          }
        ],
        "measurement": [
          "响应率 / 点击率：是否抓住正确对象。",
          "转化率：是否有效推进行动。",
          "获客成本：是否具备商业可持续性。",
          "线索质量 / 成交率：是否吸引到真正合适的人。",
          "回收周期：是否值得扩大投放。"
        ],
        "discipline": "测试不是为了证明自己对，而是为了更快找到更赚钱的表达。"
      },
      {
        "level": 9,
        "title": "第九层：与品牌广告、科学广告、现代增长的关系",
        "comparisons": [
          {
            "framework": "品牌曝光导向",
            "similarity": "都希望影响认知。",
            "difference": "Kennedy 更强调可归因结果与销售动作，而非模糊好感。",
            "best_use": "需要短中期转化验证的场景。"
          },
          {
            "framework": "Claude Hopkins《Scientific Advertising》",
            "similarity": "都强调测试、结果与销售导向。",
            "difference": "Kennedy 的标志性切口更集中在“购买理由”与“纸上销售”表达。",
            "best_use": "作为直接反应与证据型文案的源头方法。"
          },
          {
            "framework": "现代增长营销",
            "similarity": "都强调实验、指标与漏斗。",
            "difference": "现代增长工具更多，Kennedy 的原点更聚焦文案说服本身。",
            "best_use": "把增长实验建立在更强的说服单元之上。"
          }
        ],
        "takeaway": "现代工具变了，但“选对人—给理由—给证据—促行动—看结果”的骨架并没有过时。"
      },
      {
        "level": 10,
        "title": "第十层：常见误区——为什么团队会把广告做成自我感动",
        "mistakes": [
          {
            "mistake": "把品牌口号当购买理由",
            "correction": "把口号翻译成客户可验证的收益、机制和证据。"
          },
          {
            "mistake": "对所有人说同一套话",
            "correction": "优先针对最强痛点、最高价值人群。"
          },
          {
            "mistake": "堆卖点，不排序",
            "correction": "只突出最能成交的主理由，其余作为辅助证据。"
          },
          {
            "mistake": "只讲结果，不讲为什么可信",
            "correction": "增加机制、案例、演示与担保。"
          },
          {
            "mistake": "没有行动设计",
            "correction": "让 CTA 成为一条低摩擦的下一步。"
          },
          {
            "mistake": "不测试，只争论",
            "correction": "让市场反馈替代内部偏好。"
          }
        ]
      },
      {
        "level": 11,
        "title": "第十一层：落地模板——把 Reason Why 变成可执行清单",
        "templates": [
          {
            "name": "模板1：受众聚焦卡",
            "fields": [
              "谁最可能购买",
              "他们何时最痛",
              "他们已知道什么",
              "他们最怕什么",
              "我们不服务谁"
            ]
          },
          {
            "name": "模板2：购买理由排序表",
            "fields": [
              "理由名称",
              "客户重视度",
              "差异化强度",
              "证据现成度",
              "适合放在标题/正文/CTA"
            ]
          },
          {
            "name": "模板3：证据矩阵",
            "fields": [
              "主张",
              "证据类型",
              "素材来源",
              "可信风险",
              "补强动作"
            ]
          },
          {
            "name": "模板4：文案骨架",
            "fields": [
              "标题",
              "问题",
              "结果",
              "机制",
              "证明",
              "风险逆转",
              "CTA"
            ]
          },
          {
            "name": "模板5：测试记录表",
            "fields": [
              "测试假设",
              "变量",
              "样本量",
              "结果",
              "下一轮迭代"
            ]
          }
        ]
      },
      {
        "level": 12,
        "title": "第十二层：应用场景——这套方法在哪些地方最有价值",
        "scenarios": [
          {
            "scenario": "高客单价 B2B 服务",
            "why_it_fits": "客户谨慎、需要证据、需要明确下一步。"
          },
          {
            "scenario": "新产品冷启动着陆页",
            "why_it_fits": "需要快速验证哪种价值主张更能驱动注册或咨询。"
          },
          {
            "scenario": "直邮/邮件营销",
            "why_it_fits": "天然适合测试标题、优惠和 CTA。"
          },
          {
            "scenario": "搜索广告与高意图渠道",
            "why_it_fits": "用户已接近购买，理由与证据的影响很直接。"
          },
          {
            "scenario": "电商详情页",
            "why_it_fits": "需要把理由、证明和风险逆转放在临门一脚。"
          }
        ],
        "boundary": [
          "对纯情绪氛围型传播并非唯一答案，但仍可用于着陆页和转化末端。",
          "若产品本身没有真实价值，理由型广告只能加速暴露问题。"
        ]
      },
      {
        "level": 13,
        "title": "第十三层：原书金句与公开可验证表述",
        "quotes": [
          "Advertising is salesmanship in print.",
          "广告应按它已知卖出多少货、以多高成本卖出而被评判。",
          "当广告不再承担销售任务时，它就容易退化成笼统 publicity。",
          "受众选择与理由说明，是广告效率的起点。",
          "最强文案不是最华丽的文案，而是最能证明购买合理性的文案。"
        ],
        "note": "以上金句中第一句为公开网页可核验引述；其余为基于公开摘要与方法脉络的中文归纳表述。"
      },
      {
        "level": 14,
        "title": "第十四层：30 天实践计划",
        "plan": [
          {
            "week": "第1周",
            "focus": "重做受众聚焦",
            "actions": [
              "识别最有价值的 1-2 个细分人群",
              "梳理他们的购买触发事件",
              "列出当前广告最模糊的地方"
            ]
          },
          {
            "week": "第2周",
            "focus": "提炼主购买理由与证据",
            "actions": [
              "完成购买理由排序表",
              "为每条理由寻找至少一种证据",
              "补齐 FAQ 与反对意见回应"
            ]
          },
          {
            "week": "第3周",
            "focus": "重写文案与 CTA",
            "actions": [
              "产出 3 版标题",
              "产出 2 版正文框架",
              "设计低摩擦下一步 CTA"
            ]
          },
          {
            "week": "第4周",
            "focus": "上线测试与复盘",
            "actions": [
              "至少运行 2 组 A/B 测试",
              "比较受众、标题和 CTA 数据",
              "写下下一轮迭代假设"
            ]
          }
        ]
      },
      {
        "level": 15,
        "title": "第十五层：更新日志",
        "changelog": [
          {
            "date": "2026-06-01",
            "change": "初次收录：基于 web_search 得到的公开书目信息与可验证公开引述，整理《Reason Why Advertising》的理由型广告、纸上销售、证据链与测试方法。"
          }
        ]
      }
    ],
    "updates": [
      {
        "date": "2026-06-01",
        "note": "创建：新增 John E. Kennedy《Reason Why Advertising》方法论文，完成理由型广告公式、15 层展开、金句与 30 天计划。"
      }
    ]
  }
}''')

expanded_article = json.loads(r'''{
  "id": "Indi-Young-Mental-Models-心智模型研究与设计策略方法论",
  "category": "产品设计",
  "title": "Indi Young《Mental Models》心智模型研究与设计策略方法论",
  "keywords": [
    "Indi Young",
    "Mental Models",
    "Mental Model Skyline",
    "Design Strategy",
    "Human Behavior",
    "Task Analysis",
    "Behavioral Segmentation",
    "Audience Thinking",
    "UX Research",
    "Opportunity Map",
    "Persona Alternative",
    "Problem Space"
  ],
  "summary": "核心主题：不是先想界面怎么组织，而是先重建人们在真实情境中的思考顺序、顾虑、判断规则与任务塔，再用心智模型天际线对照现有支撑结构，找出缺口、重叠与战略机会。",
  "importance": 5,
  "learned_at": "2026-06-01",
  "source": "来源综合：Rosenfeld Media 公开书目信息与书介摘要（task analysis / aligning design strategy with human behavior）；Indi Young 官网 Method 页面关于 problem space research、mental model skyline、support people’s cognition 的公开描述；Opportunity Maps 课程页关于 skylines / thinking styles / gaps and weaknesses 的公开说明。",
  "file": "articles/Indi-Young-Mental-Models-心智模型研究与设计策略方法论.json",
  "content": {
    "core_formula": {
      "name": "心智模型战略公式",
      "equation": "设计战略洞察 = 深度行为访谈 x 思维与动机抽取 x 任务塔归纳 x Mental Model Skyline x 支撑结构映射 x 机会重排",
      "compressed_statement": "先理解人脑里发生了什么，再决定屏幕上应该出现什么。",
      "first_principles": [
        "用户不是按组织架构、功能模块或菜单树来思考世界。",
        "行为背后总有判断逻辑、顾虑、目标与个人规则；如果只看点击与任务流，就会漏掉真正的决策结构。",
        "设计的上游任务不是画界面，而是重建人们怎样定义问题、怎样判断下一步、怎样解释进展。",
        "当组织的支撑结构与用户的思考结构错位时，体验摩擦、教育成本和路线图浪费都会上升。"
      ]
    },
    "layers": [
      {
        "level": 1,
        "title": "第一层：Mental Models 的出发点——为什么“功能视角”总会让产品偏掉",
        "overview": [
          "Indi Young 的核心提醒是：组织会按部门、能力、数据库字段和流程图切世界，但用户通常按自己的目标、情境、担忧与判断路径来切世界。",
          "所以团队常觉得“信息架构已经很清楚”，用户却仍然迷路，因为两者用的不是同一张地图。",
          "Mental Models 的真正作用，不是多做一张研究图，而是逼迫组织从内部结构切换到人的认知结构。"
        ],
        "public_clues": [
          "Rosenfeld Media 公开书介强调：本书帮助团队 grasp, and design for, those reasons，并把方法定位为 practical set of techniques for task analysis。",
          "Indi 官网 Method 页面强调从 problem space 开始，询问人们如何 mentally approach a goal, intent, or purpose。",
          "这说明它关注的不只是任务步骤，而是人们为什么这么想、这样想意味着什么。"
        ],
        "one_sentence_answer": "如果你按系统结构设计，而不是按人的思考结构设计，产品就会越来越像组织内部，而不是越来越像用户的解决路径。"
      },
      {
        "level": 2,
        "title": "第二层：关键定义——Mental Model、Tower、Skyline、Support Structure 分别是什么",
        "definitions": [
          {
            "term": "Mental Model",
            "definition": "人们围绕某个目标、情境或问题，如何组织理解、判断和行动的内部结构。",
            "design_meaning": "不是研究“他们点哪里”，而是研究“他们如何解释世界与决定下一步”。"
          },
          {
            "term": "Mental Model Tower",
            "definition": "把相近的思考、判断、顾虑、动作片段沿着目标层级堆叠起来形成的任务塔。",
            "design_meaning": "塔让团队看到认知活动的层级，而不只是零散摘录。"
          },
          {
            "term": "Mental Model Skyline",
            "definition": "多座任务塔形成的整体天际线，用来观察一个目标域中人们的认知全景。",
            "design_meaning": "天际线让组织能俯瞰全局，识别哪些区域被支持、哪些区域被忽视。"
          },
          {
            "term": "Support Structure",
            "definition": "组织现有的产品、内容、服务、流程、团队与工具，对这些认知活动的支撑布局。",
            "design_meaning": "把现有能力映射到塔下方，才能看见缺口与重叠。"
          },
          {
            "term": "Thinking Styles / Skyline Variants",
            "definition": "不同人群面对相同目标时，采用的不同思考方式与路径。",
            "design_meaning": "分群的重点从 demographic labels 转向 cognitive patterns。"
          }
        ]
      },
      {
        "level": 3,
        "title": "第三层：为什么它比 Persona 更上游——从“是谁”走向“怎么想”",
        "comparison": [
          {
            "method": "Persona",
            "best_at": "回答“我们在服务谁”。",
            "blind_spot": "容易停留在角色标签、职责和人口属性。",
            "mental_model_upgrade": "继续向下追问：同一个角色的人会不会用完全不同方式思考同一件事？"
          },
          {
            "method": "Journey Map",
            "best_at": "回答“经历了哪些触点”。",
            "blind_spot": "容易过度线性，忽略内在判断结构。",
            "mental_model_upgrade": "把触点背后的认知活动挖出来。"
          },
          {
            "method": "JTBD",
            "best_at": "回答“试图完成什么工作”。",
            "blind_spot": "常在 hurried context 中退回功能规格，且较少展开 thinking style 差异。",
            "mental_model_upgrade": "不仅问要完成什么，还问怎样理解、怎样权衡、怎样感受。"
          }
        ],
        "takeaway": "Mental Models 不是替代所有方法，而是作为更上游的认知结构底图，为 persona、journey、JTBD、内容策略和信息架构提供更深依据。"
      },
      {
        "level": 4,
        "title": "第四层：研究输入——要收集的不是需求，而是判断与解释",
        "input_principles": [
          "访谈重点不是功能许愿单，而是人们如何开始、如何判断、如何改变主意、如何定义成功。",
          "好的原始材料同时包含行为、解释、顾虑、情绪、个人规则和环境约束。",
          "如果只问“你想要什么功能”，你拿到的是解决方案碎片，不是认知结构。"
        ],
        "interview_targets": [
          "触发事件：什么情况下会开始这件事？",
          "目标与成功标准：做成了意味着什么？",
          "判断顺序：为什么先做 A 再做 B？",
          "疑虑与担忧：哪一步最不确定？",
          "替代路径：你还考虑过什么方式？",
          "情绪与身份：你想避免被怎样看待？"
        ],
        "sample_questions": [
          "最近一次遇到这个问题是什么时候？",
          "当时你最先想到的是什么？",
          "你怎么知道该先做哪一步？",
          "哪些信息会让你更安心？",
          "在哪个时刻你会停止、犹豫或改道？"
        ]
      },
      {
        "level": 5,
        "title": "第五层：数据处理——从原句到思考单元，不要把访谈直接变成功能清单",
        "processing_steps": [
          {
            "step": 1,
            "name": "拆原句",
            "description": "把受访者表达切成最小思考单元，而不是按主题直接贴墙。"
          },
          {
            "step": 2,
            "name": "辨识意图",
            "description": "区分这句话是在表达目标、判断、动作、担忧、原则还是情绪。"
          },
          {
            "step": 3,
            "name": "抽象上卷",
            "description": "把若干细节归到更高层目的与思考节点。"
          },
          {
            "step": 4,
            "name": "形成塔结构",
            "description": "把相关思维活动按层级堆叠，构成任务塔。"
          },
          {
            "step": 5,
            "name": "交叉比对",
            "description": "对比不同受访者间的共性塔与差异塔。"
          }
        ],
        "quality_bar": [
          "记录动作不够，还要记录为什么这么做。",
          "记录抱怨不够，还要知道抱怨指向哪个认知障碍。",
          "记录任务不够，还要知道任务之间的上位关系。"
        ]
      },
      {
        "level": 6,
        "title": "第六层：塔结构——从零散素材到认知层级",
        "tower_levels": [
          {
            "layer": "高层目的",
            "question": "我究竟想达成什么更大的结果？",
            "design_use": "决定产品主导航、信息架构与价值主张的主轴。"
          },
          {
            "layer": "中层判断",
            "question": "我接下来该判断什么、比较什么、确认什么？",
            "design_use": "决定解释内容、辅助决策与引导节点。"
          },
          {
            "layer": "底层动作",
            "question": "我具体要执行什么步骤？",
            "design_use": "决定界面流程、字段、按钮与操作顺序。"
          }
        ],
        "insight": "很多团队一上来就设计底层动作，但真正决定用户是否顺畅的，往往是中层判断没有被支持。"
      },
      {
        "level": 7,
        "title": "第七层：Mental Model Skyline——为什么天际线视角能暴露战略问题",
        "skyline_value": [
          "把大量任务塔放到同一视图中，可以看到一个目标领域的认知全景，而不是单个流程截面。",
          "天际线之上是人的思考结构，之下可以叠加组织现有支撑结构，于是缺口会被看得很清楚。",
          "Opportunity Maps 课程页公开描述强调：可以在 towers 上方/周围叠加其他研究，并看到 gaps and weaknesses。"
        ],
        "what_to_look_for": [
          "哪些高频认知区域几乎没有支撑？",
          "哪些区域组织投入过度，但用户并不重视？",
          "哪些支撑只服务一种 thinking style，却误以为覆盖了所有人？",
          "哪些塔是未来战略最值得扩张的机会窗口？"
        ],
        "managerial_meaning": "Skyline 让路线图讨论从“再加什么功能”变成“先支持哪段关键认知”。"
      },
      {
        "level": 8,
        "title": "第八层：Support Structure Mapping——把产品、内容、服务压到塔下面",
        "mapping_layers": [
          {
            "layer": "产品界面",
            "examples": [
              "导航结构",
              "关键流程",
              "搜索与筛选",
              "设置与反馈"
            ]
          },
          {
            "layer": "内容系统",
            "examples": [
              "帮助中心",
              "解释型文案",
              "案例",
              "教育内容"
            ]
          },
          {
            "layer": "人工服务",
            "examples": [
              "客服",
              "顾问",
              "培训",
              "社区支持"
            ]
          },
          {
            "layer": "组织流程",
            "examples": [
              "审批与交付",
              "通知与跟进",
              "异常处理",
              "售后机制"
            ]
          }
        ],
        "three_outcomes": [
          "支撑过强：内部投入很重，但用户价值感低。",
          "支撑不足：用户高度在意，但方案很薄。",
          "完全缺口：用户脑中有重要塔，组织根本没接住。"
        ]
      },
      {
        "level": 9,
        "title": "第九层：Thinking Styles——真正有用的分群不是人群标签，而是认知模式",
        "style_examples": [
          {
            "style": "求稳验证型",
            "signals": [
              "先收集证据再行动",
              "偏好对比与证明",
              "害怕高风险决策"
            ],
            "design_implication": "需要更多解释、对比、证明与可逆选项。"
          },
          {
            "style": "快速试错型",
            "signals": [
              "先尝试后修正",
              "偏好低门槛探索",
              "容忍不完整信息"
            ],
            "design_implication": "需要快速开始、低摩擦反馈与可撤销机制。"
          },
          {
            "style": "协作征询型",
            "signals": [
              "习惯寻求他人意见",
              "重视共识",
              "容易受角色关系影响"
            ],
            "design_implication": "需要分享、协作、讨论与审批支持。"
          }
        ],
        "why_it_matters": "同一个 persona 可能内部存在多种 thinking style；如果不识别这些差异，统一流程只会照顾到最像团队自己的那一类人。"
      },
      {
        "level": 10,
        "title": "第十层：从洞察到设计——Mental Models 如何影响 IA、内容、流程与路线图",
        "design_targets": [
          {
            "target": "信息架构",
            "translation": "让导航按用户目标与判断顺序组织，而不是按内部部门组织。"
          },
          {
            "target": "内容策略",
            "translation": "把解释、 reassurance、比较材料放到高不确定节点。"
          },
          {
            "target": "功能优先级",
            "translation": "先建设支撑不足但高重要的塔。"
          },
          {
            "target": "服务流程",
            "translation": "在关键判断点插入人工支持或自动辅助。"
          },
          {
            "target": "产品路线图",
            "translation": "从 feature backlog 转向 cognition support backlog。"
          }
        ],
        "bridge_sentence": "Mental Models 最强的地方，在于它不是停在研究报告，而是直接改变战略排序逻辑。"
      },
      {
        "level": 11,
        "title": "第十一层：与 JTBD、服务蓝图、持续发现的关系",
        "relations": [
          {
            "framework": "JTBD",
            "how_it_connects": "都从问题空间切入，都反对直接问功能。",
            "difference": "Mental Models 更强调 thinking style、内在判断与广义认知活动；JTBD 更常聚焦进展、情境和替代品。"
          },
          {
            "framework": "Service Blueprint",
            "how_it_connects": "都关心前台与后台如何支撑价值交付。",
            "difference": "Service Blueprint 更偏服务运作映射；Mental Models 更偏认知结构映射。"
          },
          {
            "framework": "Continuous Discovery",
            "how_it_connects": "都重视持续接触客户、持续学习。",
            "difference": "Continuous Discovery 偏节奏与决策习惯；Mental Models 偏深度认知框架构建。"
          }
        ],
        "practical_rule": "如果你已经有持续研究机制，Mental Models 可以作为“高价值深挖专题”的上游框架，而不必每个问题都画完整天际线。"
      },
      {
        "level": 12,
        "title": "第十二层：质量标准——什么样的心智模型图谱才算真的有用",
        "quality_criteria": [
          "能解释为什么用户会觉得系统难用，而不是只罗列难用点。",
          "能指出哪些路线图项应该推迟，哪些应该提前。",
          "能被产品、设计、研究、内容、服务多角色共同使用。",
          "能清楚区分共性塔与 thinking style 差异。",
          "能映射到现实支撑结构，而不只是停在研究洞察层。"
        ],
        "failure_signals": [
          "图很漂亮，但无法指导优先级。",
          "全是主题聚类，没有层级结构。",
          "只有动作，没有判断与顾虑。",
          "没有把现有产品/服务压到塔下验证。"
        ]
      },
      {
        "level": 13,
        "title": "第十三层：常见误区——为什么很多团队做不出真正的 Mental Models",
        "mistakes": [
          {
            "mistake": "把观点按主题贴墙就叫心智模型",
            "why_wrong": "那更像 affinity map，还没有形成认知层级。",
            "fix": "继续上卷为塔，明确目标—判断—动作关系。"
          },
          {
            "mistake": "只记录动作，不记录判断",
            "why_wrong": "会退化成流程图，失去认知深度。",
            "fix": "在每个关键动作前追问“为什么做这一步”。"
          },
          {
            "mistake": "过早把用户塞进既有角色标签",
            "why_wrong": "会错过新的 thinking style。",
            "fix": "先从认知模式分群，再看角色特征。"
          },
          {
            "mistake": "只看共性，不看 skyline 差异",
            "why_wrong": "会做出只适合平均用户的解决方案。",
            "fix": "识别少数但高价值/高风险的思维路径。"
          },
          {
            "mistake": "研究结果不映射现有支撑结构",
            "why_wrong": "看得到人，看不到战略机会。",
            "fix": "把内容、功能、服务、流程逐层压到塔下。"
          }
        ]
      },
      {
        "level": 14,
        "title": "第十四层：适用边界——什么场景值得做重型 Mental Model 研究",
        "best_for": [
          "复杂决策链路：金融、医疗、B2B、教育、企业软件、跨渠道服务。",
          "高认知负荷：用户需要理解、比较、评估、协调多方。",
          "组织要做战略重排：信息架构重构、产品线整合、服务转型。"
        ],
        "less_necessary_for": [
          "极低参与、极简单的一步式任务。",
          "只需快速验证某个局部 UI 假设的情境。",
          "资源不足且问题极窄的小迭代。"
        ],
        "lightweight_option": "小团队可先做轻量版：聚焦单一目标域，画 3-5 座核心塔，并只映射最关键支撑结构。"
      },
      {
        "level": 15,
        "title": "第十五层：实战模板——从访谈到机会地图的最小工作包",
        "templates": [
          {
            "name": "模板1：访谈提纲",
            "items": [
              "触发情境",
              "目标与成功定义",
              "首次判断",
              "替代方案",
              "顾虑与阻力",
              "收尾与复盘"
            ]
          },
          {
            "name": "模板2：思考单元抽取卡",
            "items": [
              "原句",
              "目标",
              "判断",
              "动作",
              "情绪/担忧",
              "外部约束"
            ]
          },
          {
            "name": "模板3：任务塔归纳表",
            "items": [
              "上层目标",
              "中层判断",
              "下层动作",
              "证据片段",
              "频率"
            ]
          },
          {
            "name": "模板4：支撑结构映射表",
            "items": [
              "当前页面/功能/服务",
              "支撑到哪段塔",
              "强/弱/缺口",
              "风险与机会"
            ]
          },
          {
            "name": "模板5：机会优先级表",
            "items": [
              "用户重要性",
              "支撑弱度",
              "战略相关性",
              "实施难度",
              "优先级结论"
            ]
          }
        ]
      },
      {
        "level": 16,
        "title": "第十六层：组织落地——如何让心智模型不止停在研究团队",
        "stakeholder_moves": [
          "先用一张高层 skyline 给高管展示“我们服务的其实不是内部流程，而是人的认知进展”。",
          "把若干关键塔映射到当前功能/内容/服务，直接展示支撑不足和过度投入。",
          "用 thinking styles 说明为什么一个统一流程无法照顾关键差异。",
          "把心智模型输出嵌入产品规划、内容规划、服务培训与设计评审。"
        ],
        "operating_rhythm": [
          "季度：选一个高价值目标域做深度 mental model 研究。",
          "月度：把塔上的缺口转成机会 backlog。",
          "周度：在功能评审时检查“这项变更到底支撑了哪段认知”。"
        ]
      },
      {
        "level": 17,
        "title": "第十七层：原书金句与公开页面表述",
        "quotes": [
          "Mental Models gives you the tools to help you grasp, and design for, those reasons.",
          "Mental Models offers a practical set of techniques for task analysis in the early stage of design thinking and strategic design planning.",
          "Start in the problem space – Ask a variety of people how they mentally approach a goal, intent, or purpose.",
          "The mental model skyline shows where an org’s capabilities support people’s cognition, and where it does not.",
          "You’ll see how to find gaps and weaknesses, measure progress, and even create scenarios for different thinking styles."
        ],
        "interpretation": "这些公开表述共同指向同一个主题：Mental Models 的重点不是界面小修小补，而是以人的认知为中心重构设计战略。"
      },
      {
        "level": 18,
        "title": "第十八层：30 天实践计划",
        "plan": [
          {
            "week": "第1周",
            "focus": "界定目标域与问题空间",
            "actions": [
              "选择一个高认知负荷任务域",
              "列出假设最多的关键问题",
              "招募 6-8 位代表性受访者"
            ]
          },
          {
            "week": "第2周",
            "focus": "深访与思考单元抽取",
            "actions": [
              "完成深度访谈",
              "逐句拆解判断、动作与顾虑",
              "建立原始思考单元库"
            ]
          },
          {
            "week": "第3周",
            "focus": "搭建任务塔与 skyline",
            "actions": [
              "归纳高层目标与中层判断",
              "标出共性塔与差异塔",
              "初步识别 thinking styles"
            ]
          },
          {
            "week": "第4周",
            "focus": "映射支撑结构与重排优先级",
            "actions": [
              "把现有功能/内容/服务压到塔下",
              "标出支撑不足与过度投入区域",
              "输出 3-5 个高优先级机会项"
            ]
          }
        ]
      },
      {
        "level": 19,
        "title": "第十九层：更新日志",
        "changelog": [
          {
            "date": "2026-06-01",
            "change": "初次收录：整理 Mental Models、任务塔、支撑结构映射、skyline 分群、与 persona / journey / JTBD 的关系。"
          },
          {
            "date": "2026-06-01",
            "change": "扩写：重构为 19 层系统结构，新增 public 页面可验证表述、thinking styles、组织落地、质量标准、适用边界与 30 天实践计划。"
          }
        ]
      }
    ],
    "updates": [
      {
        "date": "2026-06-01",
        "note": "创建：收录《Mental Models》，补充任务塔、支撑结构映射、skyline 分群与设计战略迁移。"
      },
      {
        "date": "2026-06-01",
        "note": "扩写：从 12 层基础版重构为 19 层系统版，增加定义系统、thinking styles、组织落地、金句与 30 天计划。"
      }
    ]
  }
}''')

with open(index_path, 'r', encoding='utf-8') as f:
    index = json.load(f)

before_total = len(index['articles'])
before_counter = Counter(a['category'] for a in index['articles'])

os.makedirs(articles_dir, exist_ok=True)
for article in [new_article, expanded_article]:
    path = os.path.join(base, 'data', article['file'])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
        f.write('\n')

meta_keys = ['id','category','title','keywords','summary','importance','learned_at','source','file']
meta_map = {a['id']: a for a in index['articles']}
meta_map[new_article['id']] = {k: new_article[k] for k in meta_keys}
meta_map[expanded_article['id']] = {k: expanded_article[k] for k in meta_keys}
index['articles'] = sorted(meta_map.values(), key=lambda x: x['id'])

with open(index_path, 'w', encoding='utf-8') as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
    f.write('\n')

after_total = len(index['articles'])
after_counter = Counter(a['category'] for a in index['articles'])
new_path = os.path.join(base, 'data', new_article['file'])
exp_path = os.path.join(base, 'data', expanded_article['file'])
new_lines = sum(1 for _ in open(new_path, encoding='utf-8'))
exp_lines = sum(1 for _ in open(exp_path, encoding='utf-8'))
new_size = os.path.getsize(new_path)
exp_size = os.path.getsize(exp_path)
now = datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

with open(log_path, 'a', encoding='utf-8') as log:
    log.write(f"\n\n{now} — Cron Job Collection Run\n")
    log.write("=============================================\n\n")
    log.write("=== TASK 1: 收录新书 (1本) — 营销 ===\n")
    log.write("1. John E. Kennedy《Reason Why Advertising》理由型广告与纸上销售方法论 (营销, importance=5)\n")
    log.write("   - 核心公式: 广告产出 = 可成交受众匹配度 x 购买理由清晰度 x 证据可信度 x 诉求具体性 x 测试反馈速度\n")
    log.write("   - 关键框架: Salesmanship in Print x 理由型广告五步工作流 x 证据矩阵 x 测试维度表\n")
    log.write(f"   - 文件: {os.path.basename(new_path)} ({new_lines} 行, {new_size} bytes)\n")
    log.write("   - 来源说明: 已按要求先使用 web_search 检索，再结合公开书目摘要与可验证公开引述整理。\n\n")
    log.write("=== TASK 2: 扩写已有文章 (1篇) — 产品设计 ===\n")
    log.write("- Indi Young《Mental Models》心智模型研究与设计策略方法论 (产品设计, importance=5)\n")
    log.write(f"  - 扩写后规模: {exp_lines} 行, {exp_size} bytes\n")
    log.write("  - 新增内容:\n")
    log.write("    * Mental Model / Tower / Skyline / Support Structure 定义系统\n")
    log.write("    * Thinking Styles 与 skyline 分群\n")
    log.write("    * 质量标准、适用边界、组织落地与 30 天实践计划\n")
    log.write("    * 引入 Indi 官网公开表述作为可验证来源\n\n")
    log.write("=== 统计更新 ===\n")
    log.write(f"- 总文章: {before_total} -> {after_total}\n")
    log.write(f"- 营销分类: {before_counter['营销']} -> {after_counter['营销']}\n")
    log.write(f"- 产品设计分类: {before_counter['产品设计']} (扩写1篇)\n")
    log.write(f"- 新增: {os.path.basename(new_path)}\n")
    log.write(f"- 扩写: {os.path.basename(exp_path)}\n")

print(json.dumps({
    'before_total': before_total,
    'after_total': after_total,
    'before_marketing': before_counter['营销'],
    'after_marketing': after_counter['营销'],
    'before_product': before_counter['产品设计'],
    'after_product': after_counter['产品设计'],
    'new_file': new_article['file'],
    'new_lines': new_lines,
    'expanded_file': expanded_article['file'],
    'expanded_lines': exp_lines
}, ensure_ascii=False, indent=2))
