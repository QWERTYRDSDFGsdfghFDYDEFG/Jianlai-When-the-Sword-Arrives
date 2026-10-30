# 第二章定稿：2026-10-29 用户确认的完整修改稿（写作块92746）。
# 正文与确认稿对应；缺图处保留文字过场，既有图片和A2/B2界面不改。
label chapter2_start:
    $ clear_dialogue_paralanguage()
    $ clear_dialogue_pair()
    $ renpy.force_autosave()


    # 【返乡途中·溪边】
    window auto hide
    scene bg c2_01_rest_v1
    with trans_chapter_in
    narrator "离开山崖书院后，陈平安带着裴钱、朱敛，循着走过的旧路返乡。"

    narrator "出了大隋地界，三人仍多走清静的山野小径。"

    narrator "陈平安换回了草鞋，也替裴钱编了一双。上山下水倒方便，只是走得久了，终究磨脚。"

    narrator "溪边歇脚时，裴钱拿针挑破脚底的水疱。朱敛守在旁边，照旧说着风凉话。"

    narrator "陈平安脱了草鞋，将脚浸在溪水里。"

    narrator "书院渐渐远了，家乡还有许多路要走。那些从前不曾想过的琐事，却已经一件件浮上心头。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "泥瓶巷的祖宅，落魄山的竹楼……"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "魏檗说的买山事宜，骑龙巷两家铺子的生意，也该去看看。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "还有神仙坟，那些泥菩萨和天官神像的修缮。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "以前从没想过这些，如今倒是总惦记着。"

    $ clear_dialogue_paralanguage()
    narrator "他低头看着水里自己的脚。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "回到龙泉郡后，要先去书简湖看看顾璨。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "再去彩衣国，探望那对夫妇，还有那位烧得一手家常菜的老嬷嬷。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "梳水国的宋老前辈，也一定要见见。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "还欠他一顿火锅。"

    $ clear_dialogue_paralanguage()
    narrator "想到这里，陈平安笑了起来。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "还得跟老前辈显摆显摆。我喜欢的姑娘，也喜欢我，哪有他说的那么可怕。"

    $ clear_dialogue_paralanguage()
    # 收针后的稳定图待补，避免持续显示挑疱动作。
    window auto hide
    scene black
    with trans_short
    narrator "裴钱收好针，低头摆弄自己的草鞋。"

    narrator "陈平安看了她一眼。"

    narrator "他羡慕过崔东山、陆抬身上那股读书人的风流，却也没想过，样样都要照着他们学。"

    cpa "以后你和李槐他们一起走江湖，不用太拘束，更不用处处学我。"

    peiqian "我倒是想要学师父，可是想学师父也学不来嘞。"

    zl "裴钱啊，以后我编撰一部马屁宝典，一定在江湖上大卖。"

    zl "到时候挣来的银子，必须跟你平分才行。"

    peiqian "可不许反悔，咱俩五五分账！"

    zl "你啊，这辈子掉钱眼里，算是爬不出来了。"

    narrator "裴钱摇头晃脑，学起了李槐的腔调。"

    peiqian "不听不听，王八念经。"

    cpa "听李槐说，你们决定以后要一起四处挖宝？"

    zl "哎哟，神仙侠侣啊，这么小年纪就私订终身啦？"

    peiqian "我跟李槐是投缘的江湖朋友，没有情情爱爱。"

    peiqian "老厨子，你少在这里说混账的荤话。"

    narrator "她转向陈平安，又换了一副笑脸。"

    peiqian "师父，你可不用担心我将来胳膊肘往外拐。"

    peiqian "我不是书上那种见了男子就发昏的江湖女子。"

    peiqian "跟李槐挖着了值钱宝贝，早就说好了，一律平分。"

    peiqian "到时候我那份，肯定都往师父兜里装。"

    narrator "陈平安笑着，没有接话。"

    narrator "歇过脚，三人重新收拾行装，沿山路继续往前。"


    # 【黄庭国·御江畔郡城】
    window auto hide
    scene bg c2_02_cpa_pq_v1
    with trans_location
    narrator "这一日，三人走进了御江畔的那座郡城。"

    narrator "街市依旧热闹。"

    narrator "上回来这里，陈平安曾见过剑修御剑过街，惊得行人四处躲避。百姓遭了殃，也无处讨个公道。"

    narrator "那时的他，想管，也没有管的本事。"

    narrator "也是在这里，崔东山收服了芝兰曹氏藏书楼里的粉裙女童，以及在御江一带作威作福的青衣小童。"

    narrator "后来魏檗来信，说青衣小童与陆沉有些渊源。"

    narrator "陆沉留下了一颗金莲种子，也留下一个要求：将来陈平安去北俱芦洲，要帮青衣小童走江化龙。"

    narrator "这件事，陈平安应下了。"

    narrator "如今重走旧地，沿街的买卖照常开张，往来的百姓也照常过日子。"

    narrator "黄庭国纳贡的上国，却已经从大隋换成了大骊。"

    narrator "紫阳府、御江、寒食江与五岳的山水神祇，率先得到了大骊朝廷的认可，正是风头最盛的时候。"

    peiqian "离大骊边境还远，可离龙泉郡越来越近了。"

    peiqian "回家咯！"

    zl "听说落魄山有一位止境宗师后，我倒是想见识见识。"

    window auto hide
    scene bg c2_02_observe_v1
    with trans_short
    narrator "陈平安望过街面。"

    narrator "这一次，没有剑修从行人头顶呼啸而过。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "若再有人这样肆意伤人，总不能还只看着。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "真惹出山上的前辈，也未必没有说理的地方。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "实在说不通，有朱敛压阵，护着大家脱身，总归有些把握。"

    $ clear_dialogue_paralanguage()
    narrator "三人买过路上要用的东西，准备找一家客栈落脚。"

    window auto hide
    scene bg c2_02_notice_v1
    with trans_short
    # 保留既有可点击无字镜头。
    window auto hide
    pause
    narrator "刚到门前，陈平安与朱敛同时转头，望向街上。"

    narrator "一名高挑女子正朝他们走来。"


    # 【郡城·客栈门前】
    window auto hide
    scene bg c2_02_invite_v1
    with trans_short
    narrator "女子在三人面前停下，以大骊官话开口。"

    wy "陈公子，家父与你们大骊北岳正神魏檗是好友。"

    wy "如今在披云山林鹿书院任副山长。当年，也曾招待过陈公子。"

    narrator "陈平安记起了那座山林中的宅院。"

    narrator "当年护送李宝瓶他们求学，途经黄庭国，程老侍郎曾留他们借宿，盛情款待。"

    narrator "崔东山后来才告诉他，那位老侍郎，其实是一条蛰伏多年的老蛟。"

    narrator "眼前这名女子，便是老侍郎的长女，紫阳府的开山老祖吴懿。"

    wy "父亲离开黄庭国前叮嘱过，陈公子若再路过，我必须尽一尽地主之谊，不可怠慢。"

    wy "前不久，我收到一封从披云山寄来的家书，故而在附近等候已久。"

    wy "若是这些窥探冒犯了陈公子，还希望见谅。"

    wy "在这里，我诚心恳请陈公子，去我那紫阳府做客几日。"

    window auto hide
    scene bg c2_02_consider_v1
    with trans_short
    cpa "我着急赶路。"

    cpa "如果今天婉拒了前辈，会不会给前辈带来麻烦？"

    wy "自然不会。"

    wy "不过，我是真希望陈公子能留下住一两天。府里风景还不错，也有些拿得出手的山头特产。"

    wy "陈公子若是不答应，我不会被父亲和魏正神责骂。"

    wy "可若是愿意给这个面子，他们总能记住我这点小小的功劳。"

    window auto hide
    scene bg c2_02_accept_v1
    with trans_short
    narrator "陈平安稍作犹豫，点了点头。"

    cpa "好吧，那我们就叨扰前辈一两天。"

    narrator "吴懿笑着侧过身，领三人往江边去。"


    # 【郡城江畔·登船】
    window auto hide
    scene bg c2_03_quay_v1
    with trans_location
    narrator "临近码头，沿江街面渐渐开阔。"

    window auto hide
    scene bg c2_03_throw_v1
    with trans_short
    narrator "吴懿一挥袖，将行人轻轻移到街道两旁，随即抛出一枚核雕小舟。"

    window auto hide
    scene bg c2_03_reveal_v1
    with trans_illusion
    narrator "水雾在街面上弥漫开来。"

    narrator "雾气散去，一艘三层楼船已低悬在众人面前。"

    window auto hide
    scene bg c2_03_papers_v1
    with trans_short
    narrator "吴懿又拈出一叠彩色符纸，松开手。"

    window auto hide
    scene bg c2_03_maids_v1
    with trans_illusion
    narrator "符纸飘落，落地时，已变成一群姿容秀美的少女。"

    window auto hide
    scene bg c2_03_board_v1
    with trans_short
    narrator "她们从船上搬下木板，搭好登船的路。"

    wy "请公子登船。"

    narrator "裴钱仰着头，眼睛都舍不得眨。"

    narrator "楼船，符纸少女。"

    narrator "她暗暗记下这两样宝贝。将来自己也要买，砸锅卖铁都要买，实在太有面子了。"

    cpa "看什么呢，走了。"

    narrator "裴钱这才回过神，提着行山杖跟了上去。"

    window auto hide
    scene bg c2_03_fly_v1
    with trans_passage
    narrator "待众人站稳，楼船缓缓升空，御风而行。"

    narrator "街市退到身后，转眼便已远在十数里之外。"


    # 【楼船·御江上空】
    window auto hide
    scene bg c2_03_river_v1
    with trans_passage
    narrator "船下，是蜿蜒近千里的御江。"

    narrator "陈平安与裴钱站在栏杆旁，眺望脚下的山水。"

    narrator "沿途的郡县、集市，与那些走过便记在心里的山川，一处处从眼前掠过。"

    narrator "他又想起家乡那些人。"

    narrator "有的留在故乡，有的去了别处。各人有各人的去路，也不知道如今过得怎样。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "只盼他们心里，还留着家乡的青山绿水。"

    $ clear_dialogue_paralanguage()
    narrator "楼船越过河湾。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "这趟路上，还得去一趟楚夫人的府邸。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "那块‘秀水高风’的匾额，不知还在不在。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "当年憋在肚子里的几句话，总得与她讲一讲。"

    $ clear_dialogue_paralanguage()
    narrator "那是他早年经过的地方。"

    narrator "府中住着的，是一位嫁衣女鬼。"


    # 【紫阳府外·铁券河畔】
    window auto hide
    scene bg c2_05_arrival_v1
    with trans_location
    narrator "楼船穿过云雾，降向峰峦之间。"

    narrator "远处，一片恢宏建筑临河而立。"

    wy "到了。我们从这里下船。"

    narrator "众人走下楼船。"

    narrator "吴懿收起核雕小舟，那些少女也重新化作符纸。她没有将符纸收入袖中，而是随手拂向河面。"

    narrator "符纸散成一阵灵气，融入水中。"

    window auto hide
    scene bg c2_05_greeting_v1
    with trans_short
    narrator "河对岸立刻出现一名高瘦老者，朝吴懿跪地叩首。"

    jixiang_shen "积香庙小神，拜见洞灵老祖，在此叩谢老祖的大恩大德！"

    wy "无事就退回你的积香庙。"

    window auto hide
    scene bg c2_05_after_v1
    with trans_short
    narrator "老者连忙起身，化作一缕带着金光的青烟，没入河中。"

    narrator "吴懿转向陈平安，重新露出笑容。"

    wy "出门就是这点不好，很难有清净。"

    narrator "陈平安点了点头。"

    cpa "理解。"

    window auto hide
    scene bg c2_05_lead_v1
    with trans_short
    wy "各位请随我来。"

    narrator "三人跟上她，沿河而行。"

    narrator "朱敛凑近裴钱，压低声音。"

    zl "你刚才怎么不和你的同道中人把臂言欢？"

    narrator "裴钱瞥了他一眼。"

    peiqian "我懒得理你。"


    # 【沿河入府】
    window auto hide
    scene bg c2_06_talk_v1
    with trans_short
    narrator "脚下的青石路平整光洁。"

    narrator "裴钱看着石面里自己的倒影，走了几步，又低头看一眼。"

    wy "陈公子，上回同行的人，怎么一个都不见了？"

    wy "我父亲最喜欢的那个红棉袄小姑娘呢？"

    cpa "都在大隋那边求学。"

    window auto hide
    scene bg c2_06_thought_v1
    with trans_short
    narrator "吴懿似有些遗憾，脚步却没有停。"

    $ set_dialogue_paralanguage("吴懿·心声")
    wy_thought "可惜了，那个于禄……卢氏王朝的亡国太子。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("吴懿·心声")
    wy_thought "那一身浓郁龙气，简直就是世间最美味的食物。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("吴懿·心声")
    wy_thought "当年父亲没有下手，我在他眼皮子底下，哪里敢妄动。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("吴懿·心声")
    wy_thought "只是不知，将来还有没有机会。借着那份龙气，说不定便能破境。"

    $ clear_dialogue_paralanguage()
    window auto hide
    scene bg c2_06_talk_v1
    with trans_short
    narrator "这些念头，她没有说出口。"

    narrator "再开口时，仍是待客的口吻。"

    wy "府门就在前头。我先为各位安排住处。"

    cpa "劳烦了。"


    # 【紫阳府·府门】
    window auto hide
    scene bg c2_07_gate_v1
    with trans_location
    narrator "沿河再走一程，府门外的白玉广场已在眼前。"

    narrator "迎候的人依次站开。吴懿刚走近，众人便一同跪下。"

    ziyang_crowd "恭贺老祖出关！"

    peiqian "这声音都跟打雷一样了。"

    narrator "吴懿抬了抬手，众人随之起身。"

    wy "我百余年没有露面，难免让他们大惊小怪。"

    narrator "陈平安落后半步，让她先行。"

    narrator "吴懿也停了一步。"

    narrator "一个声音直接传入陈平安心中。"

    wy_telepathy "陈公子不必如此客气。你是贵客，只管与我并肩同行。"

    narrator "陈平安笑着摇头。"

    cpa "真君今日回府，我跟在后面便是。"

    narrator "吴懿看了他一眼，没有再坚持，转身先行。"

    narrator "广场上的人群分开一条道路。"

    narrator "三人随她穿过府门，往府中去。"


    # 【暮色·客楼】
    window auto hide
    scene bg c2_07_arrival_v1
    with trans_location
    narrator "吴懿将三人安顿在紫气宫一带的一座临河高楼里。"

    narrator "楼有六层，除了供人起居的屋舍，处处摆着古物珍宝。"

    window auto hide
    scene bg c2_07_house_rules_v1
    with trans_short
    wy "下边四层都可随意走动。上面两层，还请各位止步。"

    wy "诸位先歇一歇，晚间我在雪茫堂设宴。"

    cpa "有劳真君。"

    window auto hide
    scene bg c2_07_pq_furnishings_v1
    with trans_short
    narrator "吴懿告辞后，裴钱仍在打量屋里的陈设。"

    peiqian "师父，这么多宝贝，我能看看吗？"

    cpa "看可以，别随意碰。"

    peiqian "记住了。"

    window auto hide
    scene bg c2_07_cpa_set_box_v1
    with trans_short
    # 放箱图只作短拍；后续文字接站稳的临窗图。
    window auto hide
    pause
    window auto hide
    scene bg c2_07_window_talk_v1
    with trans_short
    narrator "陈平安放下竹箱，在窗边站定。"

    narrator "朱敛走了过来。"

    zl "少爷，这位吴真君待客，可真够周到的。"

    cpa "受了人家的好意，该谢的要谢。住上一两日，我们便走。"

    narrator "裴钱又去看那些陈设。"

    # 宴前廊下专用图待补，室内图中的裴钱不跟入长谈。
    window auto hide
    scene black
    with trans_location
    narrator "陈平安与朱敛来到四楼廊下。"


    # 【宴前·四楼廊下】
    window auto hide
    scene black
    with trans_location
    narrator "陈平安递给朱敛一壶酒，自己摘下腰间的养剑葫。"

    narrator "两人望着楼外的铁券河。"

    cpa "看着这条河，忽然想起崔东山说过的一件事。"

    cpa "他说三教圣人都在试着换一种办法，让那条光阴长河，流得慢上一些。"

    zl "怎么个减慢？"

    narrator "陈平安拍了拍栏杆。"

    cpa "仙家山头，人间城池，还有战争。"

    cpa "能够让人心神沉浸其中的百家学问，好像也是。"

    zl "崔东山说得神神道道，老奴算是更迷糊了。"

    narrator "陈平安喝了口酒。"

    cpa "我一样不懂。"

    zl "那么少爷想要懂得这些玄之又玄的大道吗？"

    narrator "陈平安想了想。"

    cpa "如果可以不懂，就不懂好了。"

    zl "少爷已经懂得够多了，确实不必事事都去追本溯源。"

    narrator "陈平安转头看他。"

    cpa "朱敛，你这见缝插针拍马屁的习惯，能不能改改？"

    narrator "朱敛晃了晃手里的酒壶。"

    zl "为什么要改？改了，能有酒喝？"

    cpa "倒也是。"

    narrator "朱敛笑着喝了一口。"

    zl "少爷往后一个人去北俱芦洲，真不能带上老奴？"

    zl "身边没个烧火做饭的厨子，也没个溜须拍马的扈从，多没劲？"

    cpa "你就老老实实留在落魄山吧。我还是希望你能在武道上更上一层楼。"

    cpa "那个崔姓老人的喂拳法子，既然适合我，当然更适合你。"

    cpa "以后裴钱总要自己去游历江湖。哪怕走得再远，甚至跟李槐去了别洲。"

    cpa "若是那时候你已跻身山巅境，有你暗中护送，我就放心了。"

    narrator "朱敛点了点头，用酒壶碰了碰他的养剑葫。"

    narrator "两人各饮了一口。"

    cpa "朱敛，能不能讲讲你年轻时走江湖的事？"

    zl "无数糊涂账，无数风流债。"

    zl "说这些，我怕少爷会没了喝酒的兴致。"

    cpa "说说看。"

    cpa "你送给裴钱的那几本江湖演义，我都偷偷看过好几遍了。"

    cpa "写得是好。不过书斋文人想象中的江湖，总觉得不够实在。"

    cpa "想听听你亲身走过的。"

    zl "好啊，容老奴娓娓道来。"

    zl "少爷你是不晓得，当年老奴是何等年少风流。"

    zl "江湖上有多少仙子女侠，仰慕得那叫一个死去活来，痴心不改。"

    narrator "朱敛越说越起劲，从哪位仙子如何倾心，说到哪位女侠始终不肯相忘。"

    narrator "陈平安听了一阵，拍了拍他的肩，转身进了屋。"

    narrator "朱敛抱着酒壶，望着他的背影。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "你有宁姑娘了，你有宁姑娘了。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "胆敢胡思乱想，会被她打死的。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "难道想一想也不成？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "不成，不成。一见着她，哪里藏得住。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "真挨了打，你敢还手吗？"

    $ clear_dialogue_paralanguage()
    narrator "楼下有人往来张罗。"

    narrator "暮色渐渐深了，雪茫堂那边亮起灯火。"


    # 【入夜·紫气宫长廊】
    $ renpy.force_autosave()
    window auto hide
    scene bg c2_08_banquet_arrival_v2
    with trans_location
    narrator "入夜，三人前往雪茫堂。"

    narrator "竹箱留在住处，陈平安背着长剑，裴钱仍带着行山杖。"

    narrator "雪茫堂是紫气宫中款待贵客的地方。"

    narrator "三人绕过影壁，在两条长廊相接处，碰见另一拨赴宴的客人。"

    narrator "为首的是白鹄江水神萧鸾夫人。她身边跟着婢女，还有几个同行的江湖朋友。"

    narrator "陈平安停步，让他们先行。"

    narrator "萧鸾朝他点头致意。"

    narrator "走在后面的一个汉子，却让陈平安多看了一眼。"

    window auto hide
    scene bg c2_08_recognition_v2
    with trans_short
    cpa "大侠？"

    narrator "那汉子正低头往前走，没有留意。"

    cpa "大侠！蜈蚣岭，破庙前，我们见过的。"

    narrator "汉子这才停下，转头望来。"

    sdx "你是？"

    narrator "陈平安快步走近。"

    # 旧事插镜，但陈仍在当下向孙登先说话。
    window auto hide
    scene bg c2_08_wugong_memory_v1
    with trans_short
    cpa "破庙那次，我带着两个小家伙，一个青衣，一个粉裙。"

    cpa "除妖之后，大侠还提醒我，不是所有山上人，都肯容人带着成精的妖物。"

    window auto hide
    scene bg c2_08_recognized_v2
    with trans_short
    narrator "孙登先认出了他，笑了起来。"

    sdx "好嘛，原来是你来着！"

    cpa "这两年长高了，又换了行头。大侠认不出，也正常。"

    sdx "好小子，不错不错！都混出大名堂了，能够在紫气宫吃饭喝酒了！"

    sdx "等会儿，估计咱们座位离得不会太远，到时候好好喝两杯。"

    cpa "好。"

    narrator "当年蜈蚣岭，这汉子持着一把银色符器小刀，与人追剿一头狐魅，还险些与一拨官宦子弟起了冲突。"

    narrator "最后，那个自称青芽夫人的狐魅，还是被他们制住了。"

    narrator "何谓侠士，如何降妖除魔，江湖又有怎样的险恶。"

    narrator "陈平安最初的许多印象，都来自那次偶遇。"

    narrator "没想到，竟能在这里重逢。"

    window auto hide
    scene bg c2_08_shoulder_pat_v2
    with trans_short
    narrator "孙登先一巴掌拍上他的肩头。"

    window auto hide
    scene bg c2_08_after_pat_v2
    with trans_short
    narrator "陈平安只顾高兴，裴钱却瞪大了眼。"

    narrator "在她眼里，这个陌生汉子，竟敢这么重地拍师父的肩。"

    narrator "朱敛在旁笑着，没有插话。"

    narrator "孙登先转向同行的人。"

    sdx "这就是我跟你们提过的少年郎。年纪轻轻，拳意不俗，胆子更大。"

    sdx "当年不过三四境武道修为，就敢带着两个小妖行走江湖。"

    sdx "比起那帮官宦子弟的绣花枕头，这位少侠，江湖经验可就要老到多了……"

    window auto hide
    scene bg c2_08_corridor_v1
    with trans_short
    show cpa c2_08_cpa_listen_v1 at c2_08_slot(0.25, -0.04)
    show sdx c2_08_sdx_listen_v1 at c2_08_slot(0.75, -0.04)
    with trans_short
    narrator "同行的一位老者轻声提醒。"

    companion_elder "小孙，你们可以边走边聊。"

    show cpa c2_08_cpa_talk_v1 at c2_08_slot(0.25)
    show sdx c2_08_sdx_listen_v1 at c2_08_slot(0.75, -0.10)
    cpa "赴宴要紧。大侠姓孙？"

    cpa "我叫陈平安，孙大侠直呼名字便好。"

    show cpa c2_08_cpa_listen_v1 at c2_08_slot(0.25, -0.10)
    show sdx c2_08_sdx_talk_v1 at c2_08_slot(0.75)
    sdx "行，就喊你陈平安。"

    show cpa c2_08_cpa_listen_v1 at c2_08_slot(0.25, -0.04)
    show sdx c2_08_sdx_listen_v1 at c2_08_slot(0.75, -0.04)
    narrator "众人继续往前。"

    narrator "廊道尽头，一名紫阳府管事匆匆走来。"

    ziyang_steward "你们怎么回事？难道要我们老祖和府主等你们落座才开席？"

    window auto hide
    hide cpa
    hide sdx
    with trans_short
    ziyang_steward "萧鸾夫人，你真是好大的架子！"

    narrator "萧鸾停了一下，没有答话。"

    ziyang_steward "赶紧跟上，真是婆婆妈妈！"

    narrator "说罢，他转身便走。"

    narrator "孙登先小声骂了一句。"

    narrator "陈平安没有说话，随众人走向堂口。"


    # 【夜·雪茫堂】
    window auto hide
    scene black
    with trans_location
    narrator "萧鸾一行先跨过门槛，在靠近堂门的位置落座。"

    narrator "她此次有求于紫阳府。"

    narrator "先前与府主黄楮谈妥的事情，终究还得看吴懿的意思。"

    narrator "陈平安随后走到堂口。"

    window auto hide
    scene bg c2_08_greet_v1
    with trans_short
    narrator "方才还高坐主位的吴懿，亲自迎了上来。"

    wy "陈公子不到雪茫堂，我们可不敢擅自开席上菜。"

    # 挽臂采用定稿旁白承接；不重新启用已停用的挽臂CG。
    window auto hide
    scene bg c2_08_hall_v1
    with trans_short
    narrator "她挽住陈平安的手臂，引他往里走。"

    narrator "陈平安的身子僵了一下，众目睽睽之下，又不好直接挣开。"

    narrator "裴钱凑近朱敛，小声说道。"

    peiqian "她竟然挽着师父。" (show_portrait="c2_08_pq_surprise")

    zl "你没见少爷都僵硬了吗？只不过碍于形势，不好直接推开罢了。" (show_portrait="c2_08_zl_tease")

    narrator "朱敛压低声音笑了笑。"

    zl "少爷啊少爷，你还真是无福消受美人恩。" (show_portrait="c2_08_zl_tease")

    # 席位群像和后续宴饮专用图待补，不把堂口当作落座画面。
    window auto hide
    scene black
    with trans_short
    narrator "包括府主黄楮在内，众人越看越疑。"

    narrator "莫非是老祖的相好？"

    narrator "可老祖建府以来从无道侣，一心大道，也没听说过她看重儿女情长。"

    narrator "又或是大骊宋氏来此游历的皇亲国戚？"

    narrator "吴懿将陈平安带到主位左首的几案前，松开手，回到自己的座位。"

    narrator "裴钱与朱敛也在近旁落座。"

    narrator "孙登先隔着堂中席位望过来，一时有些发怔。"

    wy "陈公子，我们紫阳府别的不说，这老蛟垂涎酒，名动四方，绝非自夸之辞。"

    wy "大隋弋阳高氏的一位皇帝老儿，也曾私下托黄庭国洪氏，每年来向我们讨六十坛。"

    wy "酒已备在案上。喝完，自有人添，绝不让诸位空杯。"

    wy "诸位只管痛饮，今夜我们不醉不归！"

    narrator "她起身举杯。"

    wy "这第一杯酒，敬陈公子莅临我紫阳府，蓬荜生辉！"

    narrator "堂中宾客纷纷起身。"

    narrator "陈平安也端起酒杯，向吴懿还礼。"

    cpa "多谢真君款待。"

    narrator "他饮尽杯中酒。"

    narrator "落座时，看见裴钱正捧着一杯果酿，小口小口地尝。"

    narrator "菜肴陆续端上几案。"

    narrator "吴懿说了两桩山上趣事，堂中便响起一片笑声。"

    narrator "陈平安听着，没觉得有多好笑。"

    narrator "四周的人却都笑得十分自然。"

    narrator "靠近门口的席位上，萧鸾夫人起身举杯。"

    xiaoluan "萧鸾代白鹄江水神府，敬真君一杯。"

    narrator "吴懿看着她，没有接话。"

    narrator "堂中的声音渐渐低了，那杯酒仍端在萧鸾手中。"

    wy "白鹄江？离咱们紫阳府多远来着？"

    narrator "黄楮忙起身回答，两家只隔着一条铁券河，三百里水路。"

    wy "那也不远啊。"

    xiaoluan "多年未曾登门拜会，是萧鸾失礼。我自罚一杯，向真君赔罪。"

    narrator "她正要饮酒，吴懿抬手止住。"

    wy "小小紫阳府，哪里当得起江水正神的罚酒？"

    narrator "吴懿转向黄楮。"

    wy "人家不来，你便不会主动去拜访？非要江神夫人登门见你？"

    wy "我看，该罚的是你。自罚三杯吧。"

    narrator "黄楮面朝萧鸾，一连喝了三杯。"

    narrator "萧鸾放下那杯始终没能喝入口的酒，取来三坛酒，摆在案前。"

    xiaoluan "黄府主这三杯，是紫阳府大人有大量。"

    xiaoluan "萧鸾也该自罚三坛，向真君赔罪。"

    narrator "她揭开泥封，仰头喝了下去。"

    narrator "一坛，又一坛。"

    narrator "第三只空坛放下时，她转过脸，用手背抵住嘴。"

    narrator "吴懿这才点头。"

    wy "以后两家，也算半个亲戚了。逢年过节，记得多串门。"

    narrator "吴懿看了看陈平安，又转向萧鸾。"

    wy "不过，今日有这个机会，还得谢过陈公子。就不意思意思？"

    xiaoluan "理当如此。"

    narrator "她重新拿起一坛酒，揭泥封的手指已经有些发颤。"

    narrator "陈平安站了起来。"

    narrator "他看了看自己的酒杯，又看向她怀里的酒坛。"

    cpa "真君，我酒量一般。不如我与江神娘娘，都只以杯饮酒？"

    cpa "我喝一杯，她却要喝一坛，于情于理，都说不过去。"

    wy "那可不行。她敬我三坛，敬陈公子却只用一杯，岂不是失礼？"

    narrator "吴懿笑着看他。"

    wy "莫非陈公子起了怜香惜玉的心思？倒也巧，江神夫人孑然一身多年——"

    narrator "陈平安拎起案上的酒坛，打断了她。"

    cpa "真君，说不过你。我也认罚。"

    cpa "半坛罚酒，剩下半坛，回敬江神娘娘。"

    narrator "他先向主位举坛，饮下半坛，又转向萧鸾。"

    cpa "敬江神娘娘。"

    narrator "他将剩下的酒饮尽。"

    narrator "萧鸾也仰起酒坛。"

    narrator "这第四坛喝完，她赶紧坐下，用衣袖遮住了嘴。"

    narrator "吴懿笑了起来，堂中的交谈声也随之重新响起。"

    narrator "有人离席敬酒，有人招呼添菜。"

    narrator "孙登先端起酒杯，朝陈平安的席位望了一眼，却迟迟没有起身。"

    narrator "正犹豫时，陈平安已经带着裴钱，走到了他的案前。"

    cpa "孙大侠，敬你一杯。"

    narrator "孙登先怔了一下，随即笑着站起来。"

    narrator "碰杯时，陈平安把杯沿放低了些。"

    narrator "孙登先也往下让，陈平安又低了一点。"

    narrator "两人饮尽杯中酒。"

    sdx "从哪儿学来的酒桌规矩，俗气得很。"

    sdx "我也当不起这份礼数。"

    cpa "孙大侠，当得起。"

    sdx "不就抓了个狐魅，至于让你记到现在？"

    narrator "陈平安笑着替两人添满。"

    cpa "人间路窄酒杯宽。与孙大侠再走一个。"

    narrator "两人又碰了一杯，各自饮尽。"

    sdx "好家伙，劝酒的本事也不小。"

    narrator "陈平安也笑了，脸上已有了酒意。"

    narrator "告别孙登先时，他朝堂门看了一眼。"

    narrator "先前催促众人赴宴的管事，一直守在那里。瞧见陈平安望来，忙低下头去。"

    narrator "陈平安举了举手里的空杯，这才带着裴钱往回走。"

    peiqian "那老头儿，可会狗眼看人低。师父，你也不生气？"

    cpa "这有什么好生气的。"

    narrator "裴钱看了一眼身后的席位，声音更低了些。"

    peiqian "师父是想着孙大侠他们好吧？"

    narrator "陈平安拍了拍她的脑袋。"

    cpa "就你聪明。"

    narrator "快到几案前，裴钱又扯了扯他的袖子。"

    peiqian "师父，我能不能也尝一小口？"

    cpa "你说呢？"

    peiqian "我觉得可以喝那么一小杯。"

    peiqian "我也想人间路窄酒杯宽。"

    cpa "喝你的果酿。"

    narrator "裴钱老老实实坐回自己的小凳。"


    # 【夜·返回客楼】
    window auto hide
    scene black
    with trans_location
    narrator "酒宴将尽，吴懿先起身离席。"

    narrator "陈平安带着裴钱、朱敛出了雪茫堂，沿来路返回客楼。"

    narrator "身后的说笑声渐渐远了。"

    narrator "裴钱提着行山杖，一路哼着从师父那里学来的家乡俗语。"

    peiqian "燕子低飞蛇过道，蚂蚁搬家山戴帽……"

    zl "裴女侠，行行好，放过老奴的耳朵吧。"

    narrator "裴钱正要回嘴，朱敛忽然伸出手，掌心向上。"

    zl "下雨了。"

    narrator "细雨落在石路上。"

    narrator "三人加快脚步，赶回高楼。"

    narrator "朱敛在二楼停下，裴钱回了三楼的住处。"

    narrator "陈平安独自上到四楼，在廊下走了一阵拳桩。"

    narrator "待酒气散去，他才回房点灯读书。"

    narrator "从山崖书院借来的几本典籍，还没有读完。今晚翻开的，是一本佛经。"

    narrator "灯下，书页慢慢翻过。"

    narrator "过了些时候，檐外的雨声停了。"


    # 【深夜·四楼廊下】
    window auto hide
    scene black
    with trans_location
    narrator "陈平安合上书，走出房门。"

    narrator "栏杆上还留着雨珠。"

    narrator "他扶着栏杆走了几步，掌心的雨珠散开，又聚拢，微微沁凉。"

    window auto hide
    scene bg c2_14_rain_after_v1
    with trans_short
    narrator "他摊开手，低头看了一会儿。"

    narrator "檐外是铁券河，河外是夜色里的青山。"

    window auto hide
    scene black
    with trans_short
    narrator "陈平安跃上栏杆，慢慢走向另一头。"

    narrator "他想起青鸾国酒楼里听过的一桩旧事。"

    narrator "一个僧人撑伞走在雨中，一个儒生站在檐下躲雨。"

    narrator "赶路遇上雨，总要找一处屋檐。"

    narrator "又想起陆抬在飞鹰堡说过，人间许多遗憾，不过“留不住”三字。"

    narrator "对那些风景、那些人，最想说的，往往就是一句“且慢行”。"

    narrator "陆抬还说，人很难对别人的苦真正感同身受。等到落在自己身上，又总是措手不及。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "且慢行。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "慢。"

    $ clear_dialogue_paralanguage()
    narrator "宴前同朱敛说过的那番话，也重新浮上心头。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "三教圣人站得那么高，看得那么远。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "究竟为何，也要人间慢下来？"

    $ clear_dialogue_paralanguage()
    narrator "他记起从前与崔东山游历黄庭国时，两人在山巅练拳，崔东山说过的几句话。"

    cds_memory "历史的车轮往前走，难免碾碎许多花草。"

    cds_memory "说这话的读书人，是盼着车上的人，肯低头看一眼。"

    narrator "夜廊寂静，陈平安走到栏杆尽头，转身往回走。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "世道若是在变好，慢一些，好像也没什么可担心的。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "可若是走错了呢？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "车轮过去得太快，想低头看看，也未必看得清。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "又怎么弥补？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "所以才要慢一些？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "慢慢走错，是不是就还有改过来的机会？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "那些被碾碎的花草，是不是也能少一些？"

    $ clear_dialogue_paralanguage()
    narrator "气府之内，金色儒衫小人抬起头。"

    narrator "它身上的金光渐渐凝聚，又有细碎光点散了出去。"

    narrator "它静静等着。"

    narrator "廊下的陈平安仍在往前走。"

    narrator "念及那些被碾碎的花草，他又想起离开山崖书院后，在路上问过朱敛的一个难题。"


    # 【返乡路上的旧日问答】
    cpa_memory "若是杀一个没有做错事的好人，就能救十个人，杀不杀？"

    narrator "那时，朱敛摇了摇头。"

    cpa_memory "一千人呢？"

    cpa_memory "一万人？"

    zl_memory "哪怕能救整个天下，我也不杀那个人。"

    cpa_memory "为何？"

    zl_memory "我担心自己就是那个被杀的人。"

    zl_memory "少爷，你呢？"

    cpa_memory "我也给不了答案。"

    cpa_memory "或许只有真正走到那一步，才知道自己的本心和选择。"


    # 【当下·四楼廊下】
    narrator "夜色中的高楼上，陈平安仍是独自一人。"

    narrator "气府里的金色儒衫小人已经急得走到门边。"

    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "你想岔了！"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "这些眼下想不出结果的难题，偏要在这时候去想？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "你先前所想的大方向，才是对的。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "那个‘慢’字，再往深处想一想！"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "这可是你将来跻身上五境的大道契机！"

    $ clear_dialogue_paralanguage()
    narrator "这些心语，陈平安一句也没有听见。"

    narrator "小人知道，这份机缘若是直接点破，反倒会乱了陈平安此刻的心境。"

    narrator "它只能等。"

    narrator "陈平安终于停下脚步。"

    narrator "金色儒衫小人也站住了。"

    narrator "廊下，陈平安忽然笑了一下。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "下回见着宁姑娘，不能又只是牵牵手吧？"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "她若是不愿意……"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "可万一，她其实愿意呢？"

    $ clear_dialogue_paralanguage()
    narrator "他跳下栏杆，朝房门走去。"

    narrator "走了两步，又以拳击掌，给自己鼓了鼓气。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "又不是没抱过。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "上回只顾发蒙，什么滋味都没记住。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "这怎么行。"

    $ clear_dialogue_paralanguage()
    narrator "到了门口，他的脚步又慢了下来。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "还是慢些。"

    $ clear_dialogue_paralanguage()
    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "与她，慢些也好。"

    $ clear_dialogue_paralanguage()
    narrator "气府里的小人仰面倒了下去。"

    $ set_dialogue_paralanguage("气府内·心声")
    jssr_thought "陈平安你大爷啊！"

    $ clear_dialogue_paralanguage()
    narrator "骂过之后，它心口那一点已经凝住的金光，仍未散去。"

    narrator "小人怔了一会儿，也笑了起来。"


    # 【深夜·房内】
    window auto hide
    scene black
    with trans_location
    narrator "灯还亮着。"

    narrator "陈平安回到桌前，将方才合上的书重新翻开。"

    narrator "书上说，有些人的心，就像一面照妖镜。"

    narrator "他看着灯火，却想起泥瓶巷的祖宅。"

    narrator "他倒希望自己的本心，只是家里桌上的一盏油灯。"

    narrator "借着那一点光，照得见屋里的尘埃，也照得见窗台上那只种着小草的陶盆。"

    narrator "若有客人来，便也能看见。"

    narrator "陈平安伏在桌前，下巴搁在手背上，望着那点光亮。"

    narrator "归乡在即，有一件事，他隐约觉得，迟早得由自己去面对。"

    narrator "他想过许多种可能，觉得都不怕。"

    narrator "唯独牵涉到一个人，便不敢再往下想。"

    $ set_dialogue_paralanguage("陈平安·心声")
    cpa_thought "天底下的道理，没有亲疏之别。"

    $ clear_dialogue_paralanguage()
    narrator "这是他自己说过的话。"

    narrator "灯芯轻轻响了一声。"

    narrator "他许久没有再翻页。"


    # 【翌晨·辞别紫阳府】
    window auto hide
    scene black
    with trans_passage
    narrator "天色渐亮。"

    narrator "三人收拾行装。陈平安重新背起竹箱，裴钱拿好行山杖，随朱敛一道下楼。"

    narrator "辞别紫阳府，归乡的路还要继续走。"


    # 【同日·紫阳府】
    window auto hide
    scene black
    with trans_location
    narrator "客人离开后，吴懿将接待的经过传讯给父亲。"

    narrator "陈平安一行，已按她的邀请留宿了一夜。"

    $ clear_dialogue_pair()
    jump chapter3_start
