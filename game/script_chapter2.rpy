label chapter2_start:
    $ clear_dialogue_paralanguage()
    $ renpy.force_autosave()

    scene bg c2_01_rest_v1
    with trans_chapter_in

    # 01｜溪边：现有图仍是挑疱进行态，稳态差分待补；不把它当作收针结果。
    narrator "从大隋京城返乡，三人仍拣清静的山野小径。"
    narrator "草鞋结实省事，却磨脚。裴钱挑破脚底的水疱，朱敛照旧在旁说着风凉话。"
    narrator "陈平安踩着溪水，思绪渐远。"

    # 01-02｜返乡牵挂是陈平安的心声，同行者没有听见。
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "泥瓶巷祖宅，落魄山竹楼，魏檗说的买山事宜，还有骑龙巷两家铺子的生意……"
    cpa_thought "还有神仙坟那些泥菩萨、天官神像的修缮。"
    cpa_thought "以前从没想过这些，如今倒是总惦记着。"
    cpa_thought "回到了龙泉郡后，要先去书简湖看看顾璨。"
    cpa_thought "再去彩衣国探望那对夫妇和那位烧得一手家常菜的老嬷嬷。"
    cpa_thought "还有梳水国老剑圣宋雨烧，也必要见见的。"
    cpa_thought "还欠老前辈一顿火锅。"
    cpa_thought "还得和老前辈显摆显摆：我喜欢的姑娘，也喜欢我。哪有他说的那么可怕。"
    $ clear_dialogue_paralanguage()
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

    scene bg c2_01_pack_v1
    with trans_short
    narrator "歇过脚，三人重新收拾行装，沿山路继续往前。"

    scene bg c2_02_cpa_pq_v1
    with trans_location

    narrator "御江畔，黄庭国郡城。"
    narrator "上回来此，陈平安见过仙师野修肆意妄为，百姓求告无门。"
    narrator "崔东山也在这里收服了芝兰曹氏藏书楼的粉裙女童，与作威作福的青衣小童结下因果。"
    narrator "魏檗后来信说，青衣小童与陆沉有些渊源。陆沉留下金莲种子，嘱陈平安将来去北俱芦洲，助青衣小童走江化龙。"
    narrator "陈平安没有异议，也没怎么怀疑。"
    narrator "黄庭国的纳贡上国，已从大隋高氏换成了大骊宋氏。"
    narrator "大骊率先认可了紫阳府等仙家府邸，以及御江、寒食江、五岳的山水神祇，正是他们风头最盛的时候。"

    peiqian "离大骊边境还远，可离龙泉郡越来越近了。回家咯！"

    zl "听说落魄山有一位止境宗师后，我倒是想见识见识。"

    scene bg c2_02_observe_v1
    with trans_short

    # 02-03｜观察街面时的心中推演，不是在场宣战。
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "这次倒是没有遇上游戏人间的潇洒剑修。"
    cpa_thought "不然我不介意他们肆意伤人之时，将其打落飞剑。"
    cpa_thought "毕竟就算真遇上了元婴境修士，不敢说一战而胜之，"
    cpa_thought "但有朱敛这位远游境武夫压阵，护着大家脱身总归不难。"
    $ clear_dialogue_paralanguage()

    narrator "当年经过，一行人曾借宿于程老侍郎隐居山林的宅子。"
    scene bg c2_02_notice_v1
    with trans_short

    # 02-04｜现图已交代停步看街与远处来人，给一个可点击的无字镜头。
    window auto hide
    pause
    scene bg c2_02_invite_v1
    with trans_short

    narrator "来人是程老侍郎的长女。"

    wy "公子，家父与你们大骊北岳正神魏檗是好友。"
    wy "家父受朝廷招徕，如今在披云山林鹿书院任副山长，当年也曾招待过陈公子。"
    wy "离开黄庭国前，父亲叮嘱过：陈公子若再路过，我必须尽地主之谊，不可怠慢。"
    wy "前不久，我收到了一封从披云山寄来的家书，故而在附近一带等候已久。"
    wy "若是这些窥探冒犯了陈公子，还希望见谅。"
    wy "在这里，我诚心恳请陈公子去我那紫阳府做客几日。"

    scene bg c2_02_consider_v1
    with trans_short

    cpa "我着急赶路。"
    cpa "如果我今天婉拒了前辈，会不会给前辈带来麻烦？"

    wy "自然不会。"
    wy "不过我是真希望陈公子能留下住一两天。府里风景还不错，也有些拿得出手的山头特产。"
    wy "若是陈公子不答应，我虽不会被父亲和山岳正神责骂。"
    wy "可若是陈公子愿意给这个面子，"
    wy "我肯定能够被赏罚分明的父亲与魏正神记住这点小小的功劳。"

    scene bg c2_02_accept_v1
    with trans_short

    cpa "好吧，那我们就叨扰前辈一两天。"

    narrator "吴懿领着三人往江边去。"
    scene bg c2_03_quay_v2
    with trans_location

    narrator "临近码头，沿江街面渐渐开阔。"
    # 03-02｜让路前置，避免楼船出现后才补述行人去向。
    narrator "吴懿一挥袖，将行人轻轻移到街边。"

    scene bg c2_03_throw_v1
    with trans_short

    narrator "随即抛出一枚核雕小舟。"
    window auto hide
    scene bg c2_03_reveal_v2
    with trans_illusion

    # 03-03｜巨舟展开终态先无字停留，点击后再显示旁白。
    pause

    narrator "水雾散开，三层楼船低悬在街面上。"
    window auto hide
    scene bg c2_03_papers_v1
    with trans_short

    # 03-04｜先完整展示五张落符，点击后恢复原旁白。
    pause

    narrator "她松开手，一叠彩色符纸飘落。"
    
    scene bg c2_03_maids_v1
    with trans_illusion

    narrator "落地时，符纸已化作一群少女。"
    scene bg c2_03_board_v1
    with trans_short

    narrator "少女们搭好木板，让出登船的路。"

    wy "请公子登船。"

    peiqian "哇，我以后也要有楼船和符纸这么两件宝贝。"
    peiqian "砸锅卖铁也要买到手，因为实在是太有面子了！"

    cpa "看什么呢，走了。"

    scene bg c2_03_fly_v1
    with trans_passage

    narrator "众人登船后，楼船缓缓升空。转瞬，已在十数里外。"
    scene bg c2_03_river_v1
    with trans_passage

    narrator "船下，是蜿蜒近千里的御江。"
    narrator "看着脚下山水，陈平安忽然想起了家乡。"
    narrator "还有一路走过的郡县、集市，那些记在心头的高山秀水。"
    narrator "这趟返乡，还得去拜访嫁衣女鬼楚夫人。她的府邸悬着“秀水高风”。"
    narrator "当年憋在肚子里的一些话，得与她讲一讲。"

    scene bg c2_05_arrival_v1
    with trans_location

    wy "紫阳府到了，我们下船吧。"

    scene bg c2_05_greeting_v1
    with trans_short

    jixiang_shen "积香庙小神，拜见洞灵老祖，在此叩谢老祖的大恩大德！"

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

    wy "陈公子，上回同行的人怎么一个都不见了？我父亲最喜欢的那个红棉袄小姑娘呢？"

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
    wy "陈公子一行，是头一回来紫阳府吧？"

    cpa "是的。"

    wy "前面便是紫阳府。我先为各位安排住处。"

    cpa "劳烦了。"

    scene bg c2_05_lead_v1
    with trans_short

    narrator "沿河又走一程，府门已在望。"

    # 第七场：府门迎接、临河客楼入住与短暂安顿。
    window auto hide
    scene bg c2_07_gate_v1
    with trans_location

    narrator "“恭贺老祖出关！”"

    peiqian "这声音都跟打雷一样了。"

    wy "我百余年没有露面，难免让他们大惊小怪。陈公子只管与我并肩走。"

    cpa "真君今日回府，我跟在后面便是。"

    window auto hide
    scene bg c2_07_arrival_v1
    with trans_location

    narrator "住处是一座临河高楼。"

    window auto hide
    scene bg c2_07_house_rules_v1
    with trans_location

    wy "下边四层都可随意走动。上面两层，还请各位止步。"
    wy "诸位先歇一歇，晚间我在雪茫堂设宴。"

    cpa "有劳真君。"

    window auto hide
    scene bg c2_07_pq_furnishings_v1
    with trans_short

    narrator "吴懿告辞了。"

    peiqian "师父，这么多宝贝，我能看看吗？"

    cpa "看可以，别随意碰。"

    peiqian "记住了。"

    window auto hide
    scene bg c2_07_cpa_set_box_v1
    with trans_short

    # 07-05｜放箱只作短拍；下一张临窗图才是站稳后的结果。
    window hide
    pause

    window auto hide
    scene bg c2_07_window_talk_v1
    with trans_short

    zl "少爷，这位吴真君待客，可真够周到的。"

    cpa "受了人家的好意，该谢的要谢。住上一两日，我们便走。"

    # 客楼图已呈暮色；文字过场交代楼下张罗与时间继续推进。
    window auto hide
    scene black
    with trans_passage
    narrator "楼下有人张罗，天色渐渐暗了。"

    # 赴宴前保留原自动存档节点，紫阳府经历在本章完整收束。
    $ renpy.force_autosave()

    # 08-01｜入夜赴宴：陈、裴、朱沿廊而来，竹箱留在客楼。
    window auto hide
    scene bg c2_08_banquet_arrival_v2
    with trans_location

    narrator "入夜，三人前往雪茫堂赴宴。"
    narrator "赴宴的宾客中，还有白鹄江水神萧鸾夫人。"
    narrator "廊下，陈平安忽然停住脚步。"

    # 08-02｜先询认，再转为认出故人的笑意。
    window auto hide
    scene bg c2_08_recognition_v2
    with trans_short

    cpa "大侠！蜈蚣岭，破庙前，我们见过的。"

    sdx "你是？"

    cpa "破庙那次，我带着两个小家伙，一个青衣，一个粉裙。"
    cpa "除妖之后，大侠还提醒我，不是所有山上人，都肯容人带着成精的妖物。"

    window auto hide
    scene bg c2_08_recognized_v2
    with trans_short

    sdx "好嘛，原来是你来着！"

    cpa "这两年长高了，又换了行头。大侠认不出，也正常。"

    # 现稿地名称谓保留；紫气宫与雪茫堂的关系仍待核。
    sdx "好小子，不错不错！都混出大名堂了，能够在紫气宫吃饭喝酒了！"
    sdx "等会儿，估计咱们座位离得不会太远，到时候我们好好喝两杯。"

    narrator "当年蜈蚣岭，这汉子持着银色符器小刀，与人追剿一头狐魅，还险些与一拨官宦子弟起了冲突。"
    narrator "最后，还是他制住了那头心狠手辣的狐魅。那狐魅，好像自称青芽夫人。"
    narrator "江湖、侠士、降妖除魔，还有其中的险恶——陈平安最初的模糊印象，都来自那次偶遇。"
    # 08-03｜拍肩只停一页，旁观与后续交谈使用收手后的稳定状态。
    window auto hide
    scene bg c2_08_shoulder_pat_v2
    with trans_short

    narrator "孙登先一巴掌拍上陈平安肩头。陈平安只顾高兴，裴钱却瞪大了眼。"

    window auto hide
    scene bg c2_08_after_pat_v2
    with trans_short

    narrator "在裴钱眼里，一个黄庭国六境武夫，竟敢这样拍师父的肩。"
    narrator "朱敛微笑着暗想：崔东山若在，这个不长眼的莽夫，八成死定了。"

    sdx "这就是我跟你们提过的少年郎。年纪轻轻，拳意不俗，胆子更大。"
    sdx "当年不过三四境武道修为，就敢带着两个小妖行走江湖。"
    sdx "不过比起那帮官宦子弟的绣花枕头，这位少侠，江湖经验可就要老到多了……"

    # 08-04起专用图仍待补，离开本次已完成的廊下相认画面。
    window auto hide
    scene black
    with trans_short

    zyfs "小孙，你们可以边走边聊。"

    cpa "赴宴要紧。大侠姓孙？我叫陈平安，孙大侠直呼名字便好。"

    sdx "行，就喊你陈平安。"

    zyfs "你们怎么回事？难道要我们老祖和府主等你们落座才开席？"
    zyfs "萧鸾夫人，你真是好大的架子！赶紧跟上，真是婆婆妈妈！"

    narrator "到了堂口，吴懿亲自迎了上来。"
    wy "陈公子不到雪茫堂，我们可不敢擅自开席上菜。"

    # 现稿“他”的指代未定；保留原词，不据此新增挽臂人物或动作图。
    peiqian "他竟然挽着师父。"

    zl "你没见少爷都僵硬了吗？只不过碍于形势，不好直接推开罢了。"
    zl "少爷，少爷，你还真是无福消受美人恩。"

    narrator "包括府主黄楮在内，众人越看越疑：莫非是老祖的相好？"
    narrator "可老祖建府以来从无道侣，一心大道，也从未看重儿女情长。"
    narrator "又或是大骊宋氏来此游历的皇亲国戚？"

    wy "陈公子，我们紫阳府别的不说，这老蛟垂涎酒，名动四方，绝非自夸之辞。"
    wy "大隋弋阳高氏的一位皇帝老儿，也曾私下托黄庭国洪氏，每年来向我们讨六十坛。"
    wy "酒已备在案上。喝完，自有人添，绝不让诸位空杯。"
    wy "诸位只管痛饮，今夜我们不醉不归！"
    wy "这第一杯酒，敬陈公子莅临我紫阳府，蓬荜生辉！"

    # 09｜且慢行与善恶之问
    window auto hide
    scene black
    with trans_location
    # 镜01。紫阳府，夜。先听檐滴，廊内无人。
    narrator "雨已经停了，檐角还在滴水。"
    # 镜02–04。陈平安从柱后走来，草鞋踏在廊板上。
    narrator "陈平安沿着廊下慢慢走，一只手轻轻搭在栏杆上。"
    narrator "走到灯下，一滴檐水落在他手边。他低头看了一眼。"
    narrator "他想起在青鸾国酒楼里听来的一个故事。"
    # 镜05–06。“故事”落音，檐滴接到伞沿。伞向左走过，露出抬袖赶向屋檐的行人。
    narrator "撑伞的人在雨里，躲雨的人在檐下。"
    narrator "也想起陆抬说过的“留不住”，于是心里只剩一句话：且慢行——慢一点，才看得见人间的苦。"


    $ set_dialogue_paralanguage("陆抬·回忆")
    narrator "又记得陆抬曾经在飞鹰堡小院感慨，人间的遗憾，多是“留不住”三字。"
    narrator "最深的肺腑之言，不过是对种种风景、种种人的一句“且慢行”。"
    narrator "陆抬又说，我们很难对世间诸多苦难，真正感同身受。"
    narrator "所以当苦难临头，落在一个人的身上时，谁都会措手不及。"
    $ clear_dialogue_paralanguage()

    $ set_dialogue_paralanguage("忆述")
    narrator "那座观道观的观主老道人，以藕花福地的众生百态观道。"
    narrator "道法通天的无名老道人，显然可以掌控一座藕花福地的那条光阴长河，可快可慢，可停滞不前。"
    narrator "可是四座天下的光阴洪流，别说掌控，就是想要拦上一拦，据说连道祖都做不到。"
    narrator "故而至圣先师曾经观水有悟：“逝者如斯夫，不舍昼夜。”"
    $ clear_dialogue_paralanguage()

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "已经站得那么高、看得那么远的三教圣人，到底为何非要慢下来？"
    cpa_thought "至圣先师，佛祖，道祖，这三位有开天辟地之功的圣人，又到底在看什么？"
    cpa_thought "以至于一定要三座天下人间“且慢行”。"
    $ clear_dialogue_paralanguage()

    $ set_dialogue_paralanguage("忆述")
    narrator "第一次与崔东山游历黄庭国，一次在山巅，崔东山陪着他一起练拳，曾经笑言："
    cds_memory "历史的车轮前行之时，必然要碾碎许多花草。"
    cds_memory "这不是帝王心性的无情之语，而是一位中土醇儒的悲悯之言。"
    cds_memory "那个读书人，希望所有看到这句话的掌权者，或是当时就坐在那辆马车上的大人物，能够低头看一眼那些稀烂的花草。"
    $ clear_dialogue_paralanguage()

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "世道慢慢变好，需要担心吗？只要是变好，方向是对的，再慢都无所谓，当然不需要担心。"
    cpa_thought "若是世道在变得糟糕，比如历史车轮，以迅猛势头一碾而过，一路碾碎无数花草，哪怕有人想要低头去看一眼，也未必看得清楚。"
    cpa_thought "又何谈弥补？所以才要慢上一些？"
    cpa_thought "因为若是慢慢而行，哪怕是岔入了一条错误的大道，慢慢而错，是不是就意味着有了修改的机会？又或者，人间苦难可以少一些？"
    $ clear_dialogue_paralanguage()

  
    narrator "陈平安沿着长廊慢慢走，走到尽头便折回来。"

    narrator "陈平安此时此刻，并不知道在一个人自己都浑然不觉的内心深处，每一个深刻的念头，就像心田里的种子。"
    narrator "会抽芽，可能许多会半路夭折，可有些会在某天开花结果。"

    narrator "陈平安更不会知道，那些以刻刀用心刻在竹简上的文字，那些被他反复咀嚼和念叨，甚至会在大太阳的天气里，让裴钱去晒一晒记载着他由衷认可、视为美好的竹简上的文字。"
    narrator "不管好坏，也不管道理对错，都是在他心田撒下的种子。"

    narrator "陈平安并不是孤例，事实上，世人一样会如此，只是未必会用刀刻竹简的方式去具象化。"
    narrator "爹娘的某句牢骚，夫子先生的某句教诲，一翻而过又从头翻回再看的书上语句，某个听了很多遍终于在某天蓦然开窍的老话、道理，看过的青山绿水，错过的心仪女子，走散的朋友，皆是所有人心田里的一粒粒种子，等待着开花。"

    narrator "陈平安哪里知道这些。他只当自己是在廊下散步散心。"

    narrator "人身小天地之中，拥有水字印的那座水府当中，绿衣小童们都停下了手头忙碌的事情，一个个屏气凝神。"
    narrator "而拥有金色文胆的那座府邸，外边盘踞着那条酣睡的真气火龙。"
    narrator "府邸里边，背负长剑、腰挂几本金色小书本的金色儒衫小人儿，一身金光越发凝练，熠熠生辉，如一尊神祇塑金身。"
    narrator "只是从那个全身金光流淌的儒衫小人儿身上，不断有星星点点的金色光彩流溢飘散出去，显然并不稳固。"
    narrator "他等着陈平安停下脚步，心里满是期待。可陈平安还在廊下慢慢走。"

    # 返乡途中的旧事。三种回答都接回朱敛问话后的同一段回忆。
    $ set_dialogue_paralanguage("返乡路上·回忆")
    narrator "这次离开山崖书院，路上陈平安问了朱敛和石柔一个问题。"

    cpa_memory "如果杀一个无错的好人，可以救十人，救不救。"

    narrator "两人摇头。"

    cpa_memory "那救千人呢？救万人呢？"

    narrator "石柔开始犹豫了。"

    zl_memory "哪怕可以救整个天下人，我也不杀那个人。"

    cpa_memory "为何？"

    zl_memory "我担心自己就是那个被杀的人。"
    zl_memory "少爷，你呢。"

    menu:
        "杀一个，救更多人。":
            cpa_memory "……"
            narrator "话到嘴边，陈平安没有说出口。这个答案太轻了。"

        "不杀。":
            cpa_memory "不杀。"
            narrator "可这答案也未必经得起真正的处境。"

        "我答不出。":
            pass

    cpa_memory "我也给不了答案，或许只有真正走到那一步，我才可能知道我的本性和选择。"
    $ clear_dialogue_paralanguage()

    # 回到当下。陈平安听不到气府里的心声。
    narrator "气府内，金色儒衫小人儿急得几次想冲出府门。"
    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "真想给那个陈平安几个大栗暴！你想岔了，想这些暂时注定没有结果的天大难题做什么？"
    jssr_thought "莫要不务正业，莫要与一桩千载难逢的机缘擦肩而过！"
    jssr_thought "你先前所思所想的大方向，才是对的！"
    jssr_thought "快快将那个至关重要的“慢”字，那个被世俗天地无比忽略的字眼，再想得更远一些，更深一些！"
    jssr_thought "只要想通透了，这就是你陈平安未来跻身上五境的大道契机！"
    $ clear_dialogue_paralanguage()

    narrator "只是这些内幕，它若是直白告诉了陈平安，反而会让陈平安陷入一种无比糟糕的心境。"

    narrator "陈平安终于在栏边停下脚步。两座府邸的金色儒衫小人和绿衣童子们，都充满了期待。"
    narrator "然后绿衣童子们面面相觑，突然间哄然大笑起来。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "原来陈平安站定之后，那一刻的纯粹心念，竟是开始想念一个姑娘了。"
    cpa_thought "而且想法特别不那么正人君子，竟是想着下次在剑气长城与她重逢，可不能只是牵牵手了，要胆子更大些。"
    cpa_thought "若是宁姑娘不愿意，大不了就是给打一顿骂几句，相信两人还是会在一起的。"
    cpa_thought "可如果万一宁姑娘其实是愿意的，等着他陈平安主动呢？"
    cpa_thought "你是个大老爷们啊，没点气魄，扭扭捏捏，像话吗？"
    $ clear_dialogue_paralanguage()

    narrator "陈平安有些困了，便转身往房里走。他边走边用拳头轻击手掌，给自己鼓气。"

    cpa "不像话，肯定不像话！"
    cpa "再说了，倒悬山那边，你又不是没抱过宁姑娘，只是那次光顾着发蒙了，啥个滋味都记不住，这怎么行？"
    cpa "亲个小嘴儿……陈平安找死啊，你？"
    cpa "不能想这个，这个有些快了。你不刚想了那么多慢吗？与宁姑娘还是要慢些，文火慢炖，也是好的……"
    cpa "好个屁的好……"

    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "陈平安你大爷啊！"
    $ clear_dialogue_paralanguage()

    narrator "绿衣小童们一个个捧腹大笑，满地打滚。"

    # 宴后临窗夜谈。
    window auto hide
    scene black
    with trans_location
    narrator "宴散，回到临河高楼。裴钱已经睡下，窗外落着小雨。"
    narrator "陈平安临窗坐着，望着河面散开的灯影。"

    zl "少爷，还不歇着？"
    cpa "还不困。坐会儿？"

    narrator "朱敛坐下。陈平安给他斟了杯酒，又望向窗外。"

    cpa "看着这条河，忽然想起崔东山说过的一件事。"
    cpa "他说三教圣人都在试着各用各的办法，让那条注定势不可当的光阴长河，流得慢上一些。"

    zl "怎么个减慢？"
    cpa "仙家山头是一物，人间城池是一物。战争，又是一物。能够让人心神沉浸其中的百家学问，好像也是。"
    zl "崔东山说得神神道道，老奴算是更迷糊了。"
    cpa "我一样不懂。"
    zl "那么少爷想要懂得这些玄之又玄的大道吗？"

    window auto hide
    scene black
    with trans_time

    narrator "翌晨，三人辞别紫阳府，继续返乡。"
    # 玩家可见的留客伏笔；不将国师指令提前写成陈平安已知信息。
    narrator "吴懿将接待的经过传讯给父亲。客人已按她的邀请，留宿了一夜。"

    jump chapter3_start

    return
