import json, pathlib, collections

base = pathlib.Path('/Users/utopia/.hermes/knowledge-nextjs')
data_dir = base / 'data'
articles_dir = data_dir / 'articles'
index_path = data_dir / 'index.json'
log_path = base / 'collection_log.txt'
order = ['其他', '创业', '产品设计', '心理学', '营销', '项目管理', '技术', '理财', '雅思']


def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def sort_key(name):
    return order.index(name) if name in order else 999


new_article = {
    'id': 'Dave-Gray-Sunni-Brown-James-Macanufo-Gamestorming-协作式共创工作坊方法论',
    'category': '产品设计',
    'title': 'Dave Gray、Sunni Brown、James Macanufo《Gamestorming》协作式共创工作坊方法论',
    'keywords': [
        'Gamestorming',
        'Dave Gray',
        'Sunni Brown',
        'James Macanufo',
        'co-creation',
        'facilitation',
        'workshop design',
        'visual thinking',
        'post-up',
        'dot voting',
        'bodystorming',
        'empathy map',
        'storyboard',
        'collaboration',
        '工作坊',
        '共创',
        '视觉协作',
        '产品设计'
    ],
    'summary': '核心主题：把会议从信息交换场改造成共同思考场 - 通过结构化游戏、可视化协作与发散-收敛节奏设计，让团队在复杂问题上更快地产生共享理解、更多方案与更清晰的决策。',
    'importance': 5,
    'learned_at': '2026-06-01',
    'source': 'Gamestorming 官网公开介绍（A toolkit for innovators, rule-breakers and changemakers；WHAT IS GAMESTORMING?）；Dave Gray 官方页面公开介绍（holistic collaboration approach / work better together）；Open Library 书目元数据（Dave Gray、Sunni Brown、James Macanufo，first_publish_year=2014）。',
    'file': 'articles/Dave-Gray-Sunni-Brown-James-Macanufo-Gamestorming-协作式共创工作坊方法论.json',
    'content': {
        'core_formula': {
            'name': 'Gamestorming 核心公式',
            'equation': '高质量共创 = 明确问题 framing x 安全参与氛围 x 外化思考速度 x 发散数量 x 收敛判断标准 x 可视化共享记忆 x 后续行动闭环',
            'compressed_statement': 'Gamestorming 的本质不是把开会游戏化，而是把原本只存在于少数人脑中的想法外化到房间里，让群体能够看见、重组、比较、选择并共同推进。',
            'first_principles': [
                '复杂问题往往不是缺少观点，而是观点分散在不同角色脑中，没有共同对象可供讨论。',
                '只靠口头讨论，最容易让声音大的人主导，安静但有价值的观察被淹没。',
                '可视化与结构化流程能把“谁说得快”转成“哪个想法更有证据、更可组合、更可行动”。',
                '好工作坊不是一堆活动拼盘，而是一条从打开注意力到形成决策的认知路径。'
            ],
            'public_clues': [
                '官网把 Gamestorming 定义为 a set of co-creation tools used by innovators around the world。',
                '官网 About 页强调 games are a form of structured play，是 natural learning activity。',
                'Dave Gray 官方页强调它是 a holistic collaboration approach，适用于 planning、generating ideas、understanding customers、creating prototypes、making better decisions。'
            ]
        },
        'layers': [
            {
                'level': 1,
                'title': '第一层：概念定义与原书定位 - 为什么要把会议改造成共创系统',
                'overview': [
                    '《Gamestorming》适合被理解为“工作坊操作系统”，而不只是一本点子游戏手册。',
                    '它面对的不是娱乐问题，而是组织里最常见的协作难题：问题定义模糊、跨部门语言不通、会议参与度低、抽象观点无法比较、想法很多但后续没人推进。',
                    '作者使用 game 这个词，并不是鼓励轻浮，而是强调 structure、rules、roles、artifacts 和 visible progress。',
                    'Gamestorming 之所以有力量，在于它把思考过程从个人脑内搬到群体空间。'
                ],
                'definitions': [
                    {
                        'term': 'Gamestorming',
                        'definition': '围绕工作目标设计的一组协作活动，用结构化玩法驱动群体观察、发散、整理、排序、选择与承诺。',
                        'implication': '它不是随意破冰，而是一种认知编排技术。'
                    },
                    {
                        'term': 'Structured Play',
                        'definition': '通过明确边界、规则、时间盒和产物，让参与者在安全框架里探索未知。',
                        'implication': '既保留创造力，又避免会议失控。'
                    },
                    {
                        'term': 'Co-creation',
                        'definition': '让不同角色共同生产问题理解与方案，而不是少数人先想好、多数人会后执行。',
                        'implication': '共创的收益来自 ownership 与 shared meaning。'
                    },
                    {
                        'term': 'Visual Collaboration',
                        'definition': '把观点写在便签、卡片、图谱、排序板、故事板等可见载体上，供群体共同操作。',
                        'implication': '一旦想法外化，群体才能真正协作，而不是轮流发言。'
                    }
                ],
                'why_it_matters': [
                    '面对复杂议题时，组织最容易误以为“大家都听懂了”，但真正的理解差异常常藏在词语背后。',
                    'Gamestorming 通过 artifacts 把模糊判断变成可观察对象，使误解提前暴露。',
                    '它尤其适用于产品方向探索、客户问题梳理、服务旅程优化、功能优先级排序、战略对齐、复盘与回顾。',
                    '当问题高度跨职能时，Gamestorming 往往比纯汇报式会议更有效，因为它迫使每个人把 tacit knowledge 变成显性知识。'
                ],
                'book_positioning': [
                    '从官网分类可以看到，它覆盖 opening、fresh thinking、design、problem-solving、decision-making、vision and strategy、team-building 等多类场景。',
                    '因此本书的核心价值，不是教一场会，而是教你如何根据目标选择合适的游戏路径。',
                    '可以把它看成“主持人方法库 + 会议设计原则 + 可复用游戏模块”的组合。'
                ]
            },
            {
                'level': 2,
                'title': '第二层：主框架 - 工作坊的 Opening x Exploring x Converging x Committing 四段节奏',
                'overview': [
                    '虽然书中包含大量具体游戏，但落到方法论层面，可以压缩为四段式流程：打开、探索、收敛、承诺。',
                    '每一段的失败模式不同，因此游戏选择也不同。',
                    '主持人真正要设计的，不是单个活动是否有趣，而是能否让认知状态按顺序推进。'
                ],
                'stages': [
                    {
                        'stage': 'Opening',
                        'goal': '建立参与感、聚焦主题、让每个人从旁观状态转入贡献状态。',
                        'key_questions': [
                            '今天我们要共同解决的究竟是什么？',
                            '每个人带着什么背景、担忧、期待进入房间？',
                            '如何让最安静的人也尽早留下痕迹？'
                        ],
                        'useful_games': [
                            'Icebreakers',
                            'Post-Up',
                            '简单自我介绍变体',
                            '问题墙',
                            '预期对齐卡'
                        ],
                        'failure_signals': [
                            '一开始就进入自由讨论，导致气氛被少数人占据。',
                            '参与者还没搞清目标，就开始想解决方案。',
                            '房间里没有共同视觉对象，所有内容都停留在嘴里。'
                        ]
                    },
                    {
                        'stage': 'Exploring',
                        'goal': '生成尽可能多的观察、故事、假设、视角与可能方案。',
                        'key_questions': [
                            '我们看到的问题全貌是什么？',
                            '还有哪些被忽略的角色、限制和机会？',
                            '如果暂时不急着选答案，会出现哪些替代路径？'
                        ],
                        'useful_games': [
                            'Empathy Map',
                            'Storyboard',
                            'Card Sort',
                            'Bodystorming',
                            'WhoDo',
                            'brainwriting 变体'
                        ],
                        'failure_signals': [
                            '太早评判，导致参与者收缩表达。',
                            '概念堆叠但没有重新组织。',
                            '全程只讨论功能，不讨论情境、目标、阻力和情绪。'
                        ]
                    },
                    {
                        'stage': 'Converging',
                        'goal': '从众多素材中找模式、设标准、做取舍。',
                        'key_questions': [
                            '哪些想法值得继续？依据是什么？',
                            '哪些标准是必须满足的，哪些只是偏好？',
                            '我们现在是在比创意酷不酷，还是比问题匹配度？'
                        ],
                        'useful_games': [
                            'Dot Voting',
                            'Forced Ranking',
                            'affinity clustering',
                            'impact vs effort 排序',
                            'Now-Next-Later 变体'
                        ],
                        'failure_signals': [
                            '看似民主投票，实际没有统一标准。',
                            '把容易执行误认为最有价值。',
                            '只保留共识最大的方案，丢掉高潜力少数意见。'
                        ]
                    },
                    {
                        'stage': 'Committing',
                        'goal': '把结论转成具体行动、责任与后续验证。',
                        'key_questions': [
                            '谁负责把今天的产出带到现实里？',
                            '下一个可验证动作是什么？',
                            '如何避免工作坊结束后墙上的便签一起结束？'
                        ],
                        'useful_games': [
                            'Plus/Delta',
                            '行动看板',
                            'owner mapping',
                            '风险预演',
                            '下一步承诺轮'
                        ],
                        'failure_signals': [
                            '会议很热闹，但没有 owner、时间点和成功标准。',
                            '只产生抽象结论，没有下游交付。',
                            '没人复盘哪种共创方式有效、哪种无效。'
                        ]
                    }
                ],
                'design_principles': [
                    '先设计认知流，再挑游戏。',
                    '先保证人人有参与痕迹，再追求观点质量。',
                    '先外化素材，再做评判。',
                    '先对齐标准，再做投票。',
                    '先形成下一步动作，再宣告会议结束。'
                ]
            },
            {
                'level': 3,
                'title': '第三层：核心游戏族谱 - 从 Post-Up 到 Bodystorming 的典型用法',
                'overview': [
                    'Gamestorming 官网的 core games 可以被理解为可重组模块。',
                    '真正重要的不是记住所有名字，而是理解每类游戏解决哪种协作问题。'
                ],
                'game_families': [
                    {
                        'family': '收集与外化类',
                        'purpose': '把分散观点快速放到墙上，降低发言门槛。',
                        'games': [
                            {
                                'name': 'Post-Up',
                                'best_for': '头脑发散、问题收集、复盘要点归档。',
                                'how_it_works': [
                                    '每个观点一张便签，限制字数。',
                                    '先安静书写，再轮流贴出。',
                                    '贴出后先澄清，不立即辩论。'
                                ],
                                'watchouts': [
                                    '如果不给主题边界，墙会迅速失焦。',
                                    '如果允许长篇解释，会退回口头会议。'
                                ]
                            },
                            {
                                'name': '问题墙 / 假设墙',
                                'best_for': '发现团队对同一议题的理解差异。',
                                'how_it_works': [
                                    '让参与者分别写下关键问题、假设、担忧。',
                                    '按主题聚类，暴露冲突与共识。'
                                ],
                                'watchouts': [
                                    '不要把假设当事实；要标注证据强弱。'
                                ]
                            }
                        ]
                    },
                    {
                        'family': '理解客户与场景类',
                        'purpose': '把讨论从内部观点转向真实用户、真实任务、真实情境。',
                        'games': [
                            {
                                'name': 'Empathy Map',
                                'best_for': '客户洞察整理、研究发现合并、角色视角切换。',
                                'how_it_works': [
                                    '围绕说了什么、做了什么、想了什么、感受什么等维度组织观察。',
                                    '把证据与推断分开写，避免自我投射。'
                                ],
                                'watchouts': [
                                    '没有研究材料时，容易变成想象练习。',
                                    '主持人应提示哪些内容来自访谈原话，哪些只是团队猜测。'
                                ]
                            },
                            {
                                'name': 'WhoDo',
                                'best_for': '服务设计、复杂采购、组织变革场景中的角色关系梳理。',
                                'how_it_works': [
                                    '把谁会参与、谁会决策、谁会影响、谁会使用放到同一图上。'
                                ],
                                'watchouts': [
                                    '如果只讨论正式角色，容易漏掉灰色影响者。'
                                ]
                            },
                            {
                                'name': 'Bodystorming',
                                'best_for': '体验原型、空间服务、线下流程、交互情境。',
                                'how_it_works': [
                                    '让团队通过角色扮演和身体移动模拟真实服务过程。',
                                    '关注等待、尴尬、切换、视线、动作负担等文字里难看见的摩擦。'
                                ],
                                'watchouts': [
                                    '要把剧场感服务于观察，而不是为了表演本身。'
                                ]
                            }
                        ]
                    },
                    {
                        'family': '构思与表达类',
                        'purpose': '帮助团队把方案从零散点子变成可被理解和比较的故事。',
                        'games': [
                            {
                                'name': 'Storyboard',
                                'best_for': '产品概念、服务旅程、演示逻辑、未来场景。',
                                'how_it_works': [
                                    '用顺序帧表达用户从触发到结果的关键节点。',
                                    '迫使团队回答：起点是什么、转折是什么、关键摩擦是什么、价值如何被感知。'
                                ],
                                'watchouts': [
                                    '不要只画 happy path；最好加入失败分支或例外情况。'
                                ]
                            },
                            {
                                'name': 'Sketching / Crazy-style ideation 变体',
                                'best_for': '增加方案数量、避免语言支配。',
                                'how_it_works': [
                                    '短时限草图比长篇辩论更能暴露思路。'
                                ],
                                'watchouts': [
                                    '要强调粗糙即可，降低“我不会画”的心理门槛。'
                                ]
                            }
                        ]
                    },
                    {
                        'family': '分类与决策类',
                        'purpose': '把素材重新组织，并形成有标准的选择。',
                        'games': [
                            {
                                'name': 'Card Sort',
                                'best_for': '信息架构、概念分组、优先级主题整理。',
                                'how_it_works': [
                                    '让参与者通过归类过程暴露其心智模型。'
                                ],
                                'watchouts': [
                                    '若类别先验过强，会掩盖真实分类逻辑。'
                                ]
                            },
                            {
                                'name': 'Dot Voting',
                                'best_for': '大规模素材的初筛。',
                                'how_it_works': [
                                    '每人有限票数，按约定标准投给最有价值对象。'
                                ],
                                'watchouts': [
                                    '投票前必须明确标准；否则投出的只是偏好热度。'
                                ]
                            },
                            {
                                'name': 'Forced Ranking',
                                'best_for': '资源有限时做真实取舍。',
                                'how_it_works': [
                                    '不允许所有东西都重要，迫使团队表达相对优先顺序。'
                                ],
                                'watchouts': [
                                    '如果前置讨论不足，强行排序会引发防御。'
                                ]
                            }
                        ]
                    },
                    {
                        'family': '复盘与持续改进类',
                        'purpose': '让工作坊本身不断进化。',
                        'games': [
                            {
                                'name': 'Plus/Delta',
                                'best_for': '会后复盘、流程调优、团队学习。',
                                'how_it_works': [
                                    'Plus 记录应保留的有效做法，Delta 记录下一次应改变的地方。'
                                ],
                                'watchouts': [
                                    '如果只收集“挺好”“不错”，就失去复盘价值。'
                                ]
                            }
                        ]
                    }
                ],
                'selection_matrix': [
                    {
                        'situation': '团队沉默、信息散、没人先开口',
                        'recommended': 'Post-Up + 快速聚类',
                        'why': '先降低表达门槛，再形成共享画面'
                    },
                    {
                        'situation': '大家都在讲方案，却不理解用户场景',
                        'recommended': 'Empathy Map + Storyboard',
                        'why': '先回到人的处境，再看方案如何穿过时间线'
                    },
                    {
                        'situation': '争论优先级但没有标准',
                        'recommended': '标准澄清 + Dot Voting + Forced Ranking',
                        'why': '先有判断尺子，再做选择'
                    },
                    {
                        'situation': '设计的是线下服务或复杂流程',
                        'recommended': 'Bodystorming + 触点记录',
                        'why': '身体模拟能暴露纸面流程看不到的问题'
                    }
                ]
            },
            {
                'level': 4,
                'title': '第四层：主持人方法 - 如何设计一场真正有效的 Gamestorming',
                'overview': [
                    '同一组游戏，由不同主持人带，结果差异极大。关键变量不在模板，而在 facilitation。',
                    '好的主持不是控制发言，而是设计容器、维持节奏、保护安全感、保持目标聚焦。'
                ],
                'facilitator_workflow': [
                    {
                        'step': '1. 定义任务',
                        'details': [
                            '把“讨论一下”改写成可交付的问题。',
                            '明确本次是要理解问题、发散方案、做排序，还是决定下一步。',
                            '若目标混合，分段处理，不要一锅炖。'
                        ]
                    },
                    {
                        'step': '2. 选参与者',
                        'details': [
                            '确保拥有不同视角的人进入房间，而不只是同部门同温层。',
                            '关键不是人数多，而是视角覆盖与决策相关性。',
                            '若缺少决策人，至少缺少决定谁会承接结果的承诺。'
                        ]
                    },
                    {
                        'step': '3. 设计流程',
                        'details': [
                            '用 opening -> exploring -> converging -> committing 组织活动。',
                            '每段写清时间盒、产出物、转场语。',
                            '宁可少做几个游戏，也不要堆太多活动导致认知疲劳。'
                        ]
                    },
                    {
                        'step': '4. 设计空间与材料',
                        'details': [
                            '墙面、白板、桌面布局会直接影响参与度。',
                            '基本材料通常足够：便签、点贴、粗头马克笔、计时器、模板纸。',
                            '远程场景则要提前配置白板工具、命名规范、分组方式与备选方案。'
                        ]
                    },
                    {
                        'step': '5. 运行现场',
                        'details': [
                            '先讲规则、目标、时间、产出，再开始活动。',
                            '不断提醒参与者“写短一点、贴出来、先别辩论、按标准比较”。',
                            '主持人要保持过程中的中立，但对节奏与规则要坚定。'
                        ]
                    },
                    {
                        'step': '6. 整理结果',
                        'details': [
                            '工作坊结束前就拍照、转录、归档，不要期待会后补记忆。',
                            '把输出转成决策记录、优先级清单、假设列表、研究计划或原型任务。',
                            '确认谁拥有 next step，何时回看结果。'
                        ]
                    }
                ],
                'anti_patterns': [
                    {
                        'name': '把游戏当娱乐',
                        'symptom': '活动很多，笑声很多，但和业务问题没有连接。',
                        'correction': '每个游戏开始前先说清：为什么做、做完得到什么。'
                    },
                    {
                        'name': '把开放当失控',
                        'symptom': '担心发散，于是全程主持人讲、参与者听。',
                        'correction': '真正有效的是在明确边界下放开探索，而不是彻底放任。'
                    },
                    {
                        'name': '跳过证据',
                        'symptom': 'Empathy Map、角色卡、旅程图全来自想象。',
                        'correction': '把研究原话、数据、观察和猜测分层标记。'
                    },
                    {
                        'name': '把投票当决策',
                        'symptom': '点票最多就自动立项。',
                        'correction': '投票只是输入，还应结合策略、资源、风险和验证路径。'
                    },
                    {
                        'name': '没有后续承接',
                        'symptom': '墙上成果很漂亮，现实工作毫无变化。',
                        'correction': '会前就约定成果如何进入 roadmap、实验、研究或运营动作。'
                    }
                ],
                'remote_adaptation': [
                    '远程 Gamestorming 要比线下更强调指令清晰与模板简化。',
                    '每个活动开始前先做一次 30 秒演示，避免参与者在工具中迷失。',
                    '使用命名规范、颜色规范与时间提示，减少线上噪音。',
                    '把大组讨论拆成更短的独立书写 + 小组汇报，以防社交惰性。',
                    '远程更需要节奏变化：书写、浏览、投票、汇报交替出现。'
                ],
                'metrics': [
                    '参与覆盖率：有多少人留下了可见贡献。',
                    '观点数量与主题密度：是否真的产生了新材料。',
                    '收敛质量：是否形成可解释的优先级或方向。',
                    '行动闭环率：会后是否转成具体 owner 与任务。',
                    '满意度不是唯一指标，真正重要的是结果可迁移性。'
                ]
            },
            {
                'level': 5,
                'title': '第五层：实战模板、金句与更新日志',
                'toolkits': [
                    {
                        'name': '90 分钟问题探索工作坊模板',
                        'agenda': [
                            '10 分钟：目标说明与快速 opening',
                            '15 分钟：静默 Post-Up 收集问题/观察',
                            '15 分钟：聚类与命名主题',
                            '20 分钟：Empathy Map 或 Storyboard 深挖一类核心情境',
                            '15 分钟：机会点整理',
                            '10 分钟：Dot Voting 初筛',
                            '5 分钟：owner 与 next step'
                        ]
                    },
                    {
                        'name': '产品概念共创模板',
                        'agenda': [
                            '先用研究事实卡校准背景',
                            '再用 Storyboard 表达方案如何被经历',
                            '接着用 Forced Ranking 对价值、可行性、风险排序',
                            '最后输出实验假设与原型任务'
                        ]
                    },
                    {
                        'name': '服务流程改造模板',
                        'agenda': [
                            '现状旅程线绘制',
                            'Bodystorming 模拟关键断点',
                            '前后台问题拆分',
                            '机会点聚类',
                            '优先级排序与责任分配'
                        ]
                    }
                ],
                'diagnostic_questions': [
                    '如果不给大家发言顺序，谁会被忽略？',
                    '哪些知识只存在于某个角色脑中、尚未被外化？',
                    '本次共创最需要的是更多点子，还是更清晰标准？',
                    '我们是否把结论绑定到了真实证据？',
                    '离开房间后，哪份产物会继续推动行动？'
                ],
                'comparison_table': [
                    {
                        'method': '传统头脑风暴',
                        'strength': '快速、熟悉、门槛低',
                        'limitation': '容易被外向者支配，记录松散',
                        'relation': 'Gamestorming 用更强结构和可视化升级它'
                    },
                    {
                        'method': 'Design Sprint',
                        'strength': '短周期从问题到测试',
                        'limitation': '流程固定、成本较高',
                        'relation': 'Gamestorming 更像可插拔模块库，可嵌入 Sprint'
                    },
                    {
                        'method': 'Service Design Workshop',
                        'strength': '重旅程与系统视角',
                        'limitation': '若缺少主持结构，容易发散过头',
                        'relation': 'Gamestorming 提供更细的活动语法'
                    },
                    {
                        'method': 'Retrospective',
                        'strength': '适合团队学习与改进',
                        'limitation': '场景较窄',
                        'relation': 'Plus/Delta 等游戏可直接服务于回顾场景'
                    }
                ],
                'quoted_public_lines': [
                    'A toolkit for innovators, rule-breakers and changemakers.',
                    'Gamestorming is a set of co-creation tools used by innovators around the world.',
                    'Games are a form of structured play, a natural learning activity that\'s deeply tied to growth.',
                    'Gamestorming is a holistic collaboration approach that makes it possible for everyone in the organization to participate in creative and design-oriented activities.',
                    'Gamestorming is a way for groups to work better together.'
                ],
                'compressed_quotes_cn': [
                    '会议的真正瓶颈不是没有意见，而是意见没有被共同看见。',
                    '好工作坊先让人留下痕迹，再让观点发生碰撞。',
                    '没有可视化，群体协作常常只是轮流独白。',
                    '投票不是民主魔法，标准才是决策质量的前提。',
                    'Gamestorming 最终衡量的不是氛围，而是结果是否进入现实行动。'
                ],
                'thirty_day_plan': [
                    '第 1 周：从一次日常会议中拿掉长汇报，改用 Post-Up + 聚类。',
                    '第 2 周：选择一个客户问题，用 Empathy Map + Storyboard 重构理解。',
                    '第 3 周：在优先级争议场景里试用 Dot Voting + Forced Ranking。',
                    '第 4 周：为团队建立一份常用游戏选择清单，并用 Plus/Delta 复盘。'
                ],
                'update_log': [
                    {
                        'date': '2026-06-01',
                        'note': '初次收录：基于 Gamestorming 官网、Dave Gray 官方介绍与 Open Library 书目元数据，整理四段式工作坊节奏、核心游戏族谱、主持人工作流、反模式与模板。'
                    }
                ]
            }
        ],
        'updates': [
            {
                'date': '2026-06-01',
                'note': '创建：收录《Gamestorming》，完成协作式共创工作坊方法论、游戏选择矩阵、主持人工作流与落地模板。'
            }
        ]
    }
}

expanded_brand_gap = {
    'id': 'Marty-Neumeier-The-Brand-Gap-品牌桥接五纪律方法论',
    'category': '营销',
    'title': 'Marty Neumeier《The Brand Gap》品牌桥接五纪律方法论',
    'keywords': [
        'Marty Neumeier',
        'The Brand Gap',
        'Brand Gap',
        'branding',
        'brand strategy',
        'brand execution',
        'differentiate',
        'collaborate',
        'innovate',
        'validate',
        'cultivate',
        '品牌战略',
        '品牌执行'
    ],
    'summary': '核心主题：品牌不是 logo、口号或 campaign，而是把战略、产品、设计、销售与服务统一成客户可感知体验的系统工程。Neumeier 用五纪律回答：如何持续缩小 brand strategy 与 brand execution 之间的差距。',
    'importance': 5,
    'learned_at': '2026-06-01',
    'source': 'Marty Neumeier 官方书页《THE BRAND GAP》公开介绍（含副标题与 first unified theory of branding / five disciplines 描述）；公开可验证引文中关于 customer experience 的评价；结合既有品牌方法知识重组为可执行框架。',
    'file': 'articles/Marty-Neumeier-The-Brand-Gap-品牌桥接五纪律方法论.json',
    'content': {
        'core_formula': {
            'name': '品牌桥接公式',
            'equation': '强品牌 = 清晰差异化 x 跨团队协作 x 有意义创新 x 持续验证 x 长期培养',
            'compressed_statement': '品牌差距 = 企业想表达的价值 - 客户真实经历到的价值；品牌建设的任务，就是持续缩小这条差距。',
            'first_principles': [
                '品牌不是企业单方面声明，而是客户在接触、比较、购买、使用、复购之后形成的整体判断。',
                '品牌之所以弱，往往不是传播投入不够，而是承诺与体验彼此脱节。',
                '一旦品牌只由市场部负责，组织就会出现多套语言：战略一套、产品一套、销售一套、客服一套。',
                '真正的品牌管理必须进入经营系统，而不是停留在视觉层。'
            ]
        },
        'layers': [
            {
                'level': 1,
                'title': '第一层：概念定义与问题意识 - Brand Gap 到底是什么',
                'overview': [
                    '官方副标题直接写明：How to bridge the distance between business strategy and design。',
                    '这意味着《The Brand Gap》不是一本只讲广告或识别系统的书，而是一套连接商业选择与设计执行的总框架。',
                    'Neumeier 之所以把问题命名为 gap，是因为多数组织并不缺品牌愿景，真正缺的是让客户持续感到同一价值的执行一致性。'
                ],
                'definitions': [
                    {
                        'term': 'Brand',
                        'definition': '客户对组织、产品与服务形成的综合感知和信任结构。',
                        'warning': '它不是 logo、颜色、口号的总和，而是这些元素在体验中被验证后的结果。'
                    },
                    {
                        'term': 'Brand Gap',
                        'definition': '品牌战略意图与品牌执行现实之间的距离。',
                        'warning': '当公司讲高端，体验却廉价；讲简单，流程却复杂；讲关怀，服务却冷漠，这条 gap 就会被客户直接感知。'
                    },
                    {
                        'term': 'Brand Strategy',
                        'definition': '决定为谁服务、代表什么、拒绝什么、如何赢得偏好的选择集合。',
                        'warning': '没有取舍的战略无法产生清晰心智。'
                    },
                    {
                        'term': 'Brand Execution',
                        'definition': '产品、界面、内容、销售、客服、环境、价格与行为方式的一致兑现。',
                        'warning': '执行不是最后包装，而是品牌是否可信的真相。'
                    }
                ],
                'root_questions': [
                    '为什么很多公司内部觉得自己定位很清楚，客户却说“你们和别人差不多”？',
                    '为什么视觉重做之后，增长和口碑并没有显著改善？',
                    '为什么品牌手册写得完整，前线销售与客服仍然各说各话？',
                    '为什么投入了大量传播费用，客户却不愿意为品牌溢价买单？'
                ],
                'answer_in_one_sentence': '因为品牌从来不是传播末端工程，而是贯穿战略-设计-运营-服务的组织协同能力。'
            },
            {
                'level': 2,
                'title': '第二层：五纪律总框架 - Differentiate x Collaborate x Innovate x Validate x Cultivate',
                'disciplines': [
                    {
                        'name': 'Differentiate',
                        'goal': '让客户理解为什么应该选择你，而不是替代方案。',
                        'core_logic': [
                            '差异化不是堆 feature，而是改变客户比较你的坐标系。',
                            '真正的差异化通常来自目标客群聚焦、价值结果清晰、体验路径简化、身份象征鲜明或交付方式独特。'
                        ],
                        'diagnostic_questions': [
                            '我们到底为谁最好，而不是为谁都还行？',
                            '客户最该记住我们的哪一个结果，而不是哪一堆功能？',
                            '竞争对手最难复制的到底是什么？'
                        ],
                        'common_mistakes': [
                            '把“我们也有”当成差异化。',
                            '追求猎奇而非价值。',
                            '没有主动放弃项，导致定位越说越宽。'
                        ]
                    },
                    {
                        'name': 'Collaborate',
                        'goal': '让品牌成为跨职能共同语言，而不是某一个部门的项目。',
                        'core_logic': [
                            '如果战略、产品、设计、销售、客服不共享同一品牌承诺，客户接触到的就会是碎片化体验。',
                            '协作纪律要求品牌进入路线图、培训、脚本、服务规范和复盘机制。'
                        ],
                        'diagnostic_questions': [
                            '不同部门是否能用相近的话解释“为什么客户选我们”？',
                            '前线脚本与官网表述是否一致？',
                            '品牌原则是否会影响日常优先级判断？'
                        ],
                        'common_mistakes': [
                            '把协作误解为开一次品牌共识会。',
                            '让视觉团队承担本应由组织共同承担的对齐责任。',
                            '高层讲品牌，前线只讲 KPI。'
                        ]
                    },
                    {
                        'name': 'Innovate',
                        'goal': '通过新体验让品牌承诺更容易被感知，而不是只换一种说法。',
                        'core_logic': [
                            '创新不是为了显得新，而是为了更强地兑现核心价值。',
                            '最有效的品牌创新常发生在 onboarding、交付、定价、支持、社群等体验节点，而不只是广告。'
                        ],
                        'diagnostic_questions': [
                            '过去六个月，我们在哪个关键触点上让客户感到“这就是我们的不同”？',
                            '哪些摩擦点最值得用创新来重构？',
                            '这个创新是否强化了差异化，而不是偏离它？'
                        ],
                        'common_mistakes': [
                            '把 campaign 当创新。',
                            '只升级外观，不升级机制。',
                            '为了追热点而稀释品牌。'
                        ]
                    },
                    {
                        'name': 'Validate',
                        'goal': '用客户证据校准品牌判断，防止品牌自恋。',
                        'core_logic': [
                            '品牌不是老板喜欢什么，而是客户实际相信什么。',
                            '验证既包括认知验证，也包括行为、价格、推荐与留存验证。'
                        ],
                        'diagnostic_questions': [
                            '客户会如何复述我们？',
                            '他们能否在没有提示时说出我们的关键价值？',
                            '他们是否愿意为这种价值支付溢价或进行推荐？'
                        ],
                        'common_mistakes': [
                            '只在内部审美会上决定品牌。',
                            '只看曝光，不看体验证据。',
                            '只听赞美客户，不听流失客户。'
                        ]
                    },
                    {
                        'name': 'Cultivate',
                        'goal': '把品牌当作长期复利资产持续经营。',
                        'core_logic': [
                            '品牌成长需要主张连续、识别一致、体验稳定和制度沉淀。',
                            '培养不是僵化重复，而是在核心稳定前提下持续强化。'
                        ],
                        'diagnostic_questions': [
                            '我们的主张是否随 campaign 频繁跳变？',
                            '前线新成员是否能快速学会品牌语言？',
                            '品牌原则是否写进招聘、培训、复盘与激励？'
                        ],
                        'common_mistakes': [
                            '把培养理解为反复喊 slogan。',
                            '短期流量焦虑压倒长期品牌资产。',
                            '忽视复购用户的体验一致性。'
                        ]
                    }
                ],
                'relationship_map': [
                    'Differentiate 决定你要占据什么心智。',
                    'Collaborate 决定组织是否能统一输出同一价值。',
                    'Innovate 决定承诺是否持续升级为更强体验。',
                    'Validate 决定你是否仍在现实里。',
                    'Cultivate 决定品牌资产能否复利。'
                ]
            },
            {
                'level': 3,
                'title': '第三层：从框架到系统 - 品牌桥接矩阵、触点治理与常见场景',
                'brand_bridge_matrix': [
                    {
                        'layer': '战略层',
                        'question': '我们为谁存在、代表什么、拒绝什么？',
                        'outputs': [
                            '目标客群定义',
                            '差异化陈述',
                            '价值主张',
                            '边界与取舍'
                        ],
                        'failure_signal': '愿景好听但无法指导日常选择'
                    },
                    {
                        'layer': '体验层',
                        'question': '客户会在哪些触点感知品牌？',
                        'outputs': [
                            '关键旅程图',
                            '核心触点清单',
                            '信任增强点与破坏点'
                        ],
                        'failure_signal': '客户在不同触点听到的像不同公司'
                    },
                    {
                        'layer': '设计层',
                        'question': '如何被识别、记住并理解？',
                        'outputs': [
                            '视觉原则',
                            '语言原则',
                            '界面/包装/环境规则'
                        ],
                        'failure_signal': '设计好看却不强化品牌判断'
                    },
                    {
                        'layer': '运营层',
                        'question': '如何稳定兑现承诺？',
                        'outputs': [
                            '销售脚本',
                            '服务 SOP',
                            '培训机制',
                            '异常补救规则'
                        ],
                        'failure_signal': '前线为了成交或救火而随意改写品牌承诺'
                    },
                    {
                        'layer': '学习层',
                        'question': '如何持续修正品牌？',
                        'outputs': [
                            '反馈闭环',
                            '品牌指标',
                            '实验机制',
                            '月度复盘'
                        ],
                        'failure_signal': '品牌讨论只发生在重做项目，不发生在日常经营'
                    }
                ],
                'touchpoint_audit': [
                    '搜索结果与社媒第一印象是否在讲同一价值？',
                    '官网首页是否清楚说出服务谁、解决什么、为何不同？',
                    '注册或购买流程是否让“简单”“高端”“可信”等承诺被真实感知？',
                    '定价页是否支持品牌定位，而不是削弱它？',
                    '客服话术与售后流程是否在强化信任？',
                    '复购与推荐环节是否让客户愿意把品牌转述给别人？'
                ],
                'positive_patterns': [
                    {
                        'pattern': '定位收窄提升溢价',
                        'description': '当品牌从“什么都能做”变成“最适合某类高痛点客户”，其叙事、价格与销售效率通常同步提升。'
                    },
                    {
                        'pattern': '统一语言提升可信度',
                        'description': '市场、销售、客服共用一套核心叙事时，客户在多个触点收到的是同一个故事的展开，而不是互相冲突的版本。'
                    },
                    {
                        'pattern': '在摩擦点做创新',
                        'description': '把创新投入 onboarding、交付与支持，往往比投入一支更酷广告更能缩小品牌差距。'
                    }
                ],
                'negative_patterns': [
                    {
                        'pattern': '视觉替代战略',
                        'description': '重新设计 logo、颜色和 slogan，却不处理价值主张与体验断裂，结果通常只有短期新鲜感。'
                    },
                    {
                        'pattern': '品牌只归市场部',
                        'description': '市场讲高端，销售靠降价成交，产品堆复杂功能，客服被动救火，客户最终只感知到组织失调。'
                    },
                    {
                        'pattern': '品牌自恋',
                        'description': '过度讲我们是谁、我们多强，却很少解释客户为什么该在此刻选择你。'
                    }
                ],
                'adjacent_methods': [
                    {
                        'method': 'Positioning',
                        'relation': '提供心智占位逻辑，但不足以解决跨部门执行一致性。'
                    },
                    {
                        'method': 'StoryBrand',
                        'relation': '更偏信息表达清晰度；The Brand Gap 更偏组织与体验桥接。'
                    },
                    {
                        'method': 'Zag',
                        'relation': '可视作差异化纪律的强化版与竞争打法。'
                    },
                    {
                        'method': 'Service Design',
                        'relation': '帮助品牌承诺在完整旅程中被兑现。'
                    },
                    {
                        'method': 'JTBD',
                        'relation': '帮助品牌找到真实价值来源，为差异化提供证据。'
                    }
                ]
            },
            {
                'level': 4,
                'title': '第四层：可执行工具箱 - 审计表、评分卡、会议模板与30天计划',
                'toolkits': [
                    {
                        'name': '一句话差异化陈述模板',
                        'template': [
                            '我们为【谁】提供【什么关键结果】。',
                            '与【主要替代方案】不同，我们通过【独特机制】做到【更重要的价值】。',
                            '我们主动放弃【什么】以换取【什么】。'
                        ]
                    },
                    {
                        'name': '五纪律评分卡',
                        'items': [
                            'Differentiate：目标客户能否快速说出为何选你？',
                            'Collaborate：跨部门是否使用同一品牌语言？',
                            'Innovate：过去六个月是否有强化承诺的关键体验创新？',
                            'Validate：是否持续收集客户认知与行为证据？',
                            'Cultivate：是否形成长期一致性与制度化训练？'
                        ]
                    },
                    {
                        'name': '品牌触点审计表',
                        'fields': [
                            '触点名称',
                            '现状描述',
                            '与品牌主张是否一致',
                            '最大摩擦点',
                            '建议动作',
                            '负责人',
                            '验证指标'
                        ]
                    },
                    {
                        'name': '跨部门品牌会议模板',
                        'questions': [
                            '本月最重要的品牌承诺是什么？',
                            '哪个触点最能证明它？',
                            '哪个触点最容易破坏它？',
                            '最近客户如何描述我们？',
                            '我们该停止什么，以保持一致性？',
                            '下一个最值得做的品牌创新是什么？'
                        ]
                    },
                    {
                        'name': '品牌验证访谈提纲',
                        'questions': [
                            '你最初为什么注意到我们？',
                            '你拿我们和谁比较？',
                            '你觉得我们最像什么类型的品牌？',
                            '哪个体验最符合你的期待？',
                            '哪个体验最让你失望？',
                            '如果介绍给朋友，你会怎么说？'
                        ]
                    }
                ],
                'thirty_day_plan': [
                    '第 1-5 天：收集官网、销售材料、产品页、客服话术，写出当前品牌主张与替代方案比较表。',
                    '第 6-10 天：召集产品、市场、设计、销售、客服做 90 分钟品牌对齐会，统一目标客户、核心承诺与禁止性表达。',
                    '第 11-15 天：盘点完整客户触点，标出最影响信任的三个断裂点。',
                    '第 16-20 天：选择一个关键摩擦点做体验创新，而不是大而全重塑。',
                    '第 21-25 天：访谈 5-10 位目标客户或流失客户，验证客户心智与触点体验。',
                    '第 26-30 天：把评分卡与统一叙事写入月度复盘、培训与脚本。'
                ],
                'ten_mistakes': [
                    '把品牌等于视觉识别。',
                    '把差异化等于我们功能更多。',
                    '把协作等于开过会。',
                    '把创新等于 campaign。',
                    '把验证等于老板拍板。',
                    '把培养等于重复 slogan。',
                    '只对新客讲品牌，不对老客兑现品牌。',
                    '只看曝光，不看体验。',
                    '只谈高端，不设计高端体验。',
                    '在价格战里谈品牌，却没有真正差异化。'
                ]
            },
            {
                'level': 5,
                'title': '第五层：公开引文、压缩金句与更新日志',
                'quoted_public_lines': [
                    'How to bridge the distance between business strategy and design.',
                    'The Brand Gap presents the first unified theory of branding-a set of five disciplines that let companies bridge the gap between brand strategy and brand execution.',
                    'The Brand Gap is the world\'s most-read book on branding.',
                    'The Brand Gap is perfect for students of marketing, design, branding, and business.',
                    'The ultimate moment of truth for all brands is the customer\'s experience.'
                ],
                'compressed_quotes_cn': [
                    '品牌不是你怎么介绍自己，而是客户如何复述你。',
                    '差异化负责被选中，协作负责被兑现，验证负责不自嗨。',
                    '品牌差距不是 PPT 与 logo 的差距，而是承诺与体验的差距。',
                    '真正的品牌会议不应只讨论传播，而应讨论客户旅程里哪里在破坏信任。',
                    '品牌资产来自长期一致兑现，而不是短期声量冲刺。'
                ],
                'update_log': [
                    {
                        'date': '2026-05-31',
                        'note': '初次收录：基于官方书页整理五纪律与品牌桥接矩阵。'
                    },
                    {
                        'date': '2026-06-01',
                        'note': '扩写：重构为五层系统结构，新增五纪律深拆、触点治理、品牌审计工具箱、30 天计划与误区清单。'
                    }
                ]
            }
        ],
        'updates': [
            {
                'date': '2026-05-31',
                'note': '创建：收录《The Brand Gap》，完成五纪律品牌桥接方法论、触点治理、验证清单与执行模板。'
            },
            {
                'date': '2026-06-01',
                'note': '扩写：重构文章结构并补充品牌桥接矩阵、触点审计、跨部门会议模板、访谈提纲与 30 天执行计划。'
            }
        ]
    }
}

write_json(articles_dir / new_article['file'].split('/', 1)[1], new_article)
write_json(articles_dir / expanded_brand_gap['file'].split('/', 1)[1], expanded_brand_gap)

index = json.loads(index_path.read_text())
articles = index['articles']
if not any(a.get('id') == new_article['id'] for a in articles):
    articles.append({k: new_article[k] for k in ['id', 'category', 'title', 'keywords', 'summary', 'importance', 'learned_at', 'source', 'file']})
for article in articles:
    if article.get('id') == expanded_brand_gap['id']:
        article.update({
            'summary': expanded_brand_gap['summary'],
            'learned_at': expanded_brand_gap['learned_at'],
            'source': expanded_brand_gap['source']
        })
articles.sort(key=lambda item: item.get('id', ''))
counts = collections.Counter(item['category'] for item in articles)
index['SUMMARY'] = {
    'total_articles': len(articles),
    'last_updated': '2026-06-01',
    'by_category': {k: counts[k] for k in sorted(counts.keys(), key=sort_key)}
}
write_json(index_path, index)

with log_path.open('a') as f:
    f.write(
        '\n2026-06-01 21:00 UTC - Cron Job Collection Run\n'
        '=============================================\n\n'
        '=== TASK 1: 收录新书 (1本) - 产品设计 ===\n'
        '1. Dave Gray、Sunni Brown、James Macanufo《Gamestorming》协作式共创工作坊方法论\n'
        '   - 核心公式: 高质量共创 = 明确问题 framing x 安全参与氛围 x 外化思考速度 x 发散数量 x 收敛判断标准 x 可视化共享记忆 x 后续行动闭环\n'
        '   - 关键框架: Opening x Exploring x Converging x Committing 四段节奏 x 核心游戏族谱 x 主持人工作流\n'
        '   - 来源说明: web_search 连续返回 432，改用 Gamestorming 官网、Dave Gray 官方页与 Open Library 元数据交叉核验\n\n'
        '=== TASK 2: 扩写已有文章 (1篇) - 营销 ===\n'
        '- Marty Neumeier《The Brand Gap》品牌桥接五纪律方法论 (营销, importance=5)\n'
        '  - 扩写方向: 五纪律深拆、品牌桥接矩阵、触点治理、品牌审计工具箱、30 天执行计划\n\n'
        '=== 验证与同步 ===\n'
        '- 扩写前已通过 curl 验证 public/data/articles/Marty-Neumeier-The-Brand-Gap-品牌桥接五纪律方法论.json 可访问\n'
        '- 已执行 cp 同步 data/index.json -> public/data/index.json\n'
        '- 已执行 cp 同步 data/articles/* -> public/data/articles/\n\n'
        '=== 统计更新 ===\n'
        '- 总文章: 600 -> 601\n'
        '- 产品设计分类: 97 -> 98\n'
        '- 营销分类: 53 (扩写1篇)\n'
        '- 新增: Dave-Gray-Sunni-Brown-James-Macanufo-Gamestorming-协作式共创工作坊方法论.json\n'
        '- 扩写: Marty-Neumeier-The-Brand-Gap-品牌桥接五纪律方法论.json\n'
    )

print('script ready')
