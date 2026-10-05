label chapter2_start:
    $ renpy.force_autosave()

    scene bg c2_01_rest_v1
    with trans_chapter_in

    narrator "从大隋京城走回大骊龙郡的返乡路，陈平安熟门熟路，仍旧拣山野小径赶路，四下清静。"
    narrator "离开大隋边境后，他换回草鞋，结实省事却也磨脚；裴钱拿针挑破脚底水疱时，朱敛照旧在旁说风凉话。"
    narrator "陈平安当时就坐在溪涧旁，脱了草鞋，踩在水里，思绪飘远。"

    cpa "泥瓶巷祖宅，落魄山竹楼，魏檗说的买山事宜，骑龙巷两座铺子的生意，"
    cpa "神仙坟那些泥菩萨、天官神像的修缮，林林总总，"
    cpa "许多都是陈平安以前没有过的念想，经常心心念念想起。"
    cpa "回到了龙泉郡后，要先去书简湖看看顾璨。"
    cpa "再去彩衣国探望那对夫妇和那位烧得一手家常菜的老嬷嬷。"
    cpa "还有梳水国老剑圣宋雨烧，也必要见见的。"
    cpa "还欠老前辈一顿火锅。"
    cpa "还得和老前辈显摆显摆，心爱的姑娘也喜欢自己，没宋老前辈说的那么可怕。"
    cpa "以后你和李槐他们一起走江湖，不用太拘束，更不用处处学我。"

    peiqian "我倒是想要学师父，可是想学师父也学不来嘞。"

    zl "裴钱啊，以后我编撰一部马屁宝典，一定在江湖上大卖。"
    zl "到时候挣来的银子，必须跟你平分才行。"

    peiqian "可不许反悔，咱俩五五分账！"

    zl "你啊，这辈子掉钱眼里，算是爬不出来了。"

    peiqian "不听不听，王八念经。"

    cpa "听李槐说你们决定以后要一起四处挖宝？"

    zl "哎哟，神仙侠侣啊，这么小年纪就私订终身啦？"

    peiqian "我跟李槐是投缘的江湖朋友，没有情情爱爱。"
    peiqian "老厨子，你少在这里说混账的荤话。"
    peiqian "师父，你可不用担心我将来胳膊肘往外拐。"
    peiqian "我不是书上那种见了男子就发昏的江湖女子。"
    peiqian "跟李槐挖着了所有值钱宝贝，与他说好了，一律平分。"
    peiqian "到时候我那份，肯定都往师父兜里装。"

    scene bg c2_02_cpa_pq_v1
    with trans_location

    narrator "一行人顺顺当当地走到御江畔的黄庭国郡城。"
    narrator "当年陈平安与崔东山路过此地，见识过小国州郡里仙师野修的放纵，百姓求告无门。"
    narrator "正是在这座郡城内，崔东山曾在芝兰曹氏藏书楼收服粉裙女童，又与作威作福的青衣小童结下因果。"
    narrator "后来听魏檗书信说，那青衣小童与陆沉有些渊源，陆沉还留下一颗金莲种子，嘱陈平安将来在北俱芦洲助其走江化龙。"
    narrator "陈平安对此没有异议，甚至没有太多怀疑。"
    narrator "郡城依旧热闹，似乎纳贡上国从大隋高氏变成大骊宋氏，"
    narrator "黄庭国百姓对此并无太多感触，日子依旧悠哉。"
    narrator "与此同时，黄庭国紫阳府、御江、寒食江、五岳，"
    narrator "成为率先被大骊朝廷认可的仙家府邸与山水神祇，风头一时无两。"

    peiqian "虽说离着大骊边境还有一段不短的路程，"
    peiqian "可终究距离龙泉郡越走越近，回家咯。"

    zl "听说落魄山有一位止境宗师后，我倒是想见识见识。"

    scene bg c2_02_observe_v1
    with trans_short

    # 这段配音不需要文字
    cpa "这次倒是没有遇上游戏人间的潇洒剑修。"
    cpa "不然我不介意他们肆意伤人之时，将其打落飞剑。"
    cpa "毕竟就算真遇上了元婴境修士，不敢说一战而胜之，"
    cpa "但有朱敛这位远游境武夫压阵，护着大家脱身总归不难。"

    narrator "如当年一行人，曾借宿于黄庭国户部老侍郎隐于山林的私人宅邸。"
    narrator "程老侍郎与大骊北岳正神魏檗相交，又受朝廷招徕，如今在披云山林鹿书院任副山长。"
    scene bg c2_02_notice_v1
    with trans_short

    narrator "当陈平安刚要带头走入一家客栈的时候，"
    narrator "与朱敛一起转头望向大街，一个面容冷漠的高挑女子姗姗而来。"
    scene bg c2_02_invite_v1
    with trans_short

    narrator "走到陈平安他们身前露出微笑，正是那程老侍郎的长女，奉父命前来相邀。"

    wy "公子，家父与你们大骊北岳正神魏檗是好友。"
    wy "如今担任林鹿书院副山长，而且当年曾经招待过陈公子。"
    wy "离开黄庭国之前，父亲交代过我。"
    wy "若是以后陈公子路过此地，我必须尽一尽地主之谊，不可怠慢。"
    wy "前不久，我收到了一封从披云山寄来的家书，故而在附近一带等候已久。"
    wy "若是这些窥探冒犯了陈公子，还希望见谅。"
    wy "在这里，我诚心恳请陈公子去我那紫阳府做客几日。"

    scene bg c2_02_consider_v1
    with trans_short

    cpa "着急赶路。"
    cpa "如果我今天婉拒了前辈，会不会给前辈带来麻烦？"

    wy "自然不会。"
    wy "不过我是真希望陈公子能够在紫阳府逗留一两天。"
    wy "那边风景还不错，一些个山头特产，还算拿得出手。"
    wy "若是陈公子不答应，我虽不会被父亲和山岳正神责骂。"
    wy "可若是陈公子愿意给这个面子，"
    wy "我肯定能够被赏罚分明的父亲与魏正神记住这点小小的功劳。"

    scene bg c2_02_accept_v1
    with trans_short

    cpa "好吧，那我们就叨扰前辈一两天。"

    narrator "女子侧身引路，带着陈平安三人沿街往江边走去。"
    scene bg c2_03_quay_v1
    with trans_location

    narrator "临近码头，街面渐渐开阔，挑担的行人与搬货的脚夫往来其间。"
    narrator "街旁石阶通向水边，御江上船只往来，江风吹动几人的衣角。"
    narrator "女子在码头旁一段开阔的沿江街面上停下脚步。"

    scene bg c2_03_throw_v1
    with trans_short

    narrator "一枚核雕小舟，被女子丢出。"
    scene bg c2_03_reveal_v1
    with trans_illusion

    narrator "水雾弥漫间，蓦然变出一艘雕栏画栋的袖珍楼船，高三层。"
    narrator "乘坐四五十人不在话下。"
    narrator "好在抛掷这枚核雕法宝之际，女子已经默默挥袖，"
    narrator "将街上行人轻飘飘扯到了街道两旁。"
    scene bg c2_03_papers_v1
    with trans_short

    narrator "与此同时，她从袖中拈出一叠色彩不一的符纸，松手后，符纸飘落在地。"
    scene bg c2_03_maids_v1
    with trans_illusion

    narrator "出现了一个个亭亭玉立、姿容秀美的少女，顾盼生辉。"
    narrator "根本认不出她们片刻之前还是一叠符箓纸人。"
    scene bg c2_03_board_v1
    with trans_short

    narrator "她们手脚伶俐，迅速从楼船上搬出一条登船木板。"

    wy "请公子登船。"

    peiqian "哇，我以后也要有楼船和符纸这么两件宝贝。"
    peiqian "砸锅卖铁也要买到手，因为实在是太有面子了！"

    cpa "看什么呢，走了。"

    scene bg c2_03_fly_v1
    with trans_passage

    narrator "在众目睽睽之下，楼船缓缓升空，御风远游，速度极快，转瞬十数里。"
    scene bg c2_03_river_v1
    with trans_passage

    narrator "站在这艘紫阳府老祖宗的仙家渡船上，脚底下就是那条蜿蜒近千里的御江。"
    narrator "陈平安站在栏杆旁，跟裴钱一起眺望地面上风景如画的山山水水。"
    narrator "陈平安没来由地想起了家乡。"
    narrator "以及去往龙泉郡一路上的郡县、小镇集市，那些陈平安走过了就被牢牢记在心头的高山秀水。"
    narrator "在这次返乡路上，陈平安还要去一趟那座悬挂秀水高风的嫁衣女鬼楚夫人的府邸。"
    narrator "当年憋在肚子里的一些话，得与她讲一讲。"

    scene bg c2_05_arrival_v1
    with trans_location

    wy "紫阳府到了，我们下船吧。"

    scene bg c2_05_greeting_v1
    with trans_short

    narrator "积香庙小神，拜见洞灵老祖，在此叩谢老祖的大恩大德！"

    wy "无事就退回你的积香庙。"

    scene bg c2_05_after_v1
    with trans_short

    wy "出门就是这点不好，很难有清净。"

    cpa "理解。"

    scene bg c2_05_lead_v1
    with trans_short

    wy "各位请随我来。"

    zl "你刚才怎么不和你的同道中人把臂言欢？"

    peiqian "我懒得理你。"

    # 06-01a：河岸双人交谈，承接第五场引路。
    scene bg c2_06_talk_v1
    with trans_short

    wy "陈公子，上次与你同行的众人当中，比如我父亲最喜欢的红棉袄小姑娘，他们怎么一个都不见了？"

    cpa "都在大隋那边求学。"

    # 06-01b：吴懿闭口出神；这些念头只有玩家读到。
    window auto hide
    scene bg c2_06_thought_v1
    with trans_short
    $ set_dialogue_paralanguage("吴懿·心声")

    wy_thought "可惜了，那个于禄……卢氏王国的太子。"
    wy_thought "那一身浓郁龙气，简直就是世间最美味的食物。"
    wy_thought "连父亲都还没下手，我又哪里敢妄动。只是不知，将来还有没有机会饱餐一顿。"
    wy_thought "说不定吃完了，我就能破开那个该死的金丹境瓶颈。"

    $ clear_dialogue_paralanguage()
    window auto hide
    scene bg c2_06_talk_v1
    with trans_short

    # 06-02起压缩为沿河入府、短暂安顿；旧分镜页数见压缩记录。
    wy "陈公子一行应该是第一次来紫阳府吧？"

    cpa "是的。"

    wy "前面便是紫阳府。我先为各位安排住处。"

    cpa "劳烦了。"

    scene bg c2_05_lead_v1
    with trans_short

    narrator "沿河再走了一程，府门已经在望。"

    # 府内专用图尚未制作，以文字过场承接，避免沿用河岸交谈图。
    window auto hide
    scene black
    with trans_location

    narrator "府门前，迎候的众人俯身行礼。一声‘恭贺老祖出关’，响过广场。"

    peiqian "这声音都跟打雷一样了。"

    wy "我百余年没有露面，难免让他们大惊小怪。陈公子只管与我并肩走。"

    cpa "真君今日回府，我跟在后面便是。"

    narrator "吴懿没有再劝，亲自领他们穿过人群。"
    narrator "不多时，三人被安顿在一座临河高楼里。"

    wy "下边四层都可随意走动。上面两层，还请各位止步。"
    wy "诸位先歇一歇，晚间我在雪茫堂设宴。"

    cpa "有劳真君。"

    narrator "吴懿告辞后，裴钱已经绕着楼里的陈设看了一圈。"

    peiqian "师父，这么多宝贝，我能看看吗？"

    cpa "看可以，别随意碰。"

    peiqian "记住了。"

    narrator "陈平安放下竹箱，走到窗边。"

    zl "少爷，这位吴真君待客，可真够周到的。"

    cpa "受了人家的好意，该谢的要谢。住上一两日，我们便走。"

    narrator "楼下有人往来张罗，天色渐渐暗了。"

    jump chapter3_start

    return
