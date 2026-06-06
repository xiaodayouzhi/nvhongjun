import streamlit as st
import pyttsx3
import os
from PIL import Image
import requests
from io import BytesIO
import tempfile

# 页面配置
st.set_page_config(
    page_title="巾帼长征路——女红军历史交互式讲述",
    page_icon="🚩",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 侧边栏导航
st.sidebar.title("🚩 巾帼长征路")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "导航菜单",
    ["首页", "故事讲述", "互动问答", "英雄人物"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
这是一个交互式的女红军历史讲述网站，
仿照数字长征讲述者网站设计，
带你了解长征中女英雄们的动人故事。
""")

# 首页
if page == "首页":
    st.title("巾帼长征路——女红军历史交互式讲述")
    st.subheader("她们用柔弱的肩膀，扛起了革命的重担")
    
    # 展示女红军历史照片
    try:
        img_url = "https://aka.doubaocdn.com/s/5wpj1wYIds"
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, caption="1934年，长征途中的三名女红军战士", use_column_width=True)
    except:
        st.warning("图片加载失败")
    
    st.markdown("""
在二万五千里的长征路上，有这样一群特殊的战士，她们剪掉长发，换上戎装，告别了家乡的亲人，
用女性特有的坚韧与温柔，在战火纷飞中走出了一条属于自己的英雄之路。

据统计，参加长征的女红军约有2000多名，她们中有的是党的高级干部，有的是普通的战士，
有的是医护人员，有的是宣传工作者。她们和男战士一样，爬雪山、过草地，啃树皮、吃草根，
经历了常人难以想象的艰难困苦，却从未退缩。

她们不仅要面对敌人的围追堵截，还要克服生理和心理的重重考验，用自己的行动诠释了什么是革命信仰，
什么是巾帼不让须眉。她们的故事，是长征史上最动人的篇章之一，值得我们永远铭记。
    """)
    
    # 统计数据卡片
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("参加长征的女红军", "约2000+", "来自全国10多个省份")
    with col2:
        st.metric("胜利到达陕北的", "约700+", "大部分牺牲在长征路上")
    with col3:
        st.metric("女红军中的开国将军", "1位", "李贞，新中国第一位女将军")
    
    st.success("👈 请从左侧导航栏选择不同的功能，探索女红军的动人故事")

# 故事讲述页面
elif page == "故事讲述":
    st.title("📖 女红军的动人故事")
    st.markdown("选择一个故事，聆听她们的传奇经历，感受那段峥嵘岁月")
    
    # 故事库
    stories = {
        "半条被子的温暖": {
            "content": """
在湖南汝城县沙洲村，3名女红军借宿在徐解秀老人家中。当时的徐解秀家一贫如洗，连一床完整的被子都没有，
只有一张破草席和一件烂蓑衣。

这3名女红军看到老人家里的情况，心里十分难受。她们自己也只有一床被子，是从江西出发时带出来的。
临走的时候，她们决定把这床被子留给老人。但是徐解秀说什么也不肯要，她说："你们还要赶路，没有被子怎么行？"

推来推去，最后，一名女红军拿出剪刀，把这床被子剪成了两半，一半留给了徐解秀，一半自己带走了。
她对徐解秀说："大姐，这半条被子你留下，等革命胜利了，我们再回来给你送一床新的被子。"

徐解秀老人后来常常说："什么是共产党？共产党就是自己只有一条被子，也要剪下半条给老百姓的人。"
这个故事，也成为了共产党人与人民群众荣辱与共、风雨同舟的最好见证。
            """,
            "author": "三位无名女红军",
            "location": "湖南汝城沙洲村"
        },
        "矮个子女英雄危秀英": {
            "content": """
危秀英是江西瑞金人，身高不到一米四，看起来小小的个子，却有着无比强大的力量。

1935年，在贵州的深山里，省委书记廖志高得了高烧，昏迷不醒，当时敌人正在围剿，大部队已经转移了，
只剩下危秀英和廖志高两个人。

危秀英没有放弃，她解下自己捆行李的粗麻绳，把廖志高绑在自己的背上，就这样，她背着一个比自己重很多的成年人，
在深山里走了整整两天两夜，饿了就吃点野菜，渴了就喝点山泉水，终于把廖志高安全地带回了部队。

当时所有人都不敢相信，这么小的个子，竟然能背着一个大男人走了这么远的路。危秀英说："我当时就想着，
无论如何，我都要把他带回去，他是我们的干部，不能丢在这里。"

就是这样一个小小的女红军，用自己的行动，创造了一个奇迹。
            """,
            "author": "危秀英",
            "location": "贵州深山"
        },
        "带病长征的邓六金": {
            "content": """
邓六金是福建闽西人，参加长征的时候，她才20多岁。在长征途中，她得了痢疾，一天要拉十几次，
还发起了高烧，身体弱得像要瘫在地上一样。

领导看她这样，就把马让给她骑，但是她根本骑不住，一上去就掉下来。战友们都劝她留下来，
但是她摇摇头说："我不能留下来，我一定要跟着部队，就算是爬，我也要爬到陕北去。"

就这样，她拖着病体，一步一步地跟着大部队，有时候走不动了，就拉着马尾巴走。
过草地的时候，她的病还没好，但是她还是坚持着，帮着抬担架，照顾伤员，从来没有喊过一声苦。

后来她回忆说："那时候，心里就只有一个念头，就是一定要跟上部队，不能掉队，
因为我知道，只要跟着党，跟着红军，就一定能走到胜利的地方。"
            """,
            "author": "邓六金",
            "location": "川陕甘边境"
        },
        "红25军的七仙女": {
            "content": """
红25军长征的时候，有7个年轻的女护士，她们被大家称为"七仙女"。
她们最大的才22岁，最小的只有15岁，都是来自河南、湖北的农村姑娘。

她们跟着部队一路行军，一路上负责照顾伤员，给伤员包扎、喂药、洗衣服。
当时药品非常紧缺，她们就自己想办法，用盐水给伤员消毒，用草药给伤员治病。
有时候没有药，她们就用嘴把伤员伤口里的脓吸出来。

过秦岭的时候，天气非常冷，她们都穿着单衣，脚都冻烂了，但是她们还是坚持着，
没有一个人掉队。最后，这7个姑娘全部跟着部队走到了陕北，成为了一段佳话。
            """,
            "author": "红25军七仙女医护小组",
            "location": "鄂豫陕根据地"
        }
    }
    
    # 选择故事
    story_name = st.selectbox("选择你想了解的故事", list(stories.keys()))
    selected_story = stories[story_name]
    
    # 展示故事信息
    st.subheader(story_name)
    col1, col2 = st.columns(2)
    with col1:
        st.caption(f"讲述者：{selected_story['author']}")
    with col2:
        st.caption(f"发生地点：{selected_story['location']}")
    
    st.markdown("---")
    st.markdown(selected_story['content'])
    
    # 本地语音讲述功能
    st.markdown("---")
    if st.button("🔊 播放语音讲述", help="点击生成本地语音，聆听故事的音频版本，不需要联网！"):
        with st.spinner("正在本地生成语音，请稍候..."):
            try:
                # 初始化本地TTS
                engine = pyttsx3.init()
                # 设置中文语音
                voices = engine.getProperty('voices')
                # 尝试找到中文语音
                for voice in voices:
                    if 'chinese' in voice.id.lower() or 'china' in voice.id.lower():
                        engine.setProperty('voice', voice.id)
                        break
                engine.setProperty('rate', 150)  # 语速
                
                # 生成临时音频文件
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                    temp_file = fp.name
                
                engine.save_to_file(selected_story['content'], temp_file)
                engine.runAndWait()
                
                # 播放音频
                st.audio(temp_file, format='audio/mp3')
                
                # 清理临时文件
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                
                st.success("✅ 语音生成完成，点击播放按钮开始聆听！")
            except Exception as e:
                st.error(f"语音生成失败：{str(e)}，你也可以直接阅读文字内容哦")

# 互动问答页面
elif page == "互动问答":
    st.title("💬 互动问答")
    st.markdown("有什么关于女红军的问题，都可以问我哦！我会尽力为你解答")
    
    # 预设问答库
    qa_pairs = {
        "长征中有多少女红军": "据统计，参加长征的女红军约有2000多名，她们来自全国各个省份，其中红四方面军的女红军人数最多，约有1000多人。她们中有的是干部，有的是战士，有的是医护人员，在长征中承担了各种不同的任务。最终胜利到达陕北的女红军约有700多人，大部分女红军都牺牲在了长征路上。",
        "女红军在长征中都做什么": "女红军在长征中承担了非常多的任务，她们有的要和男战士一样行军打仗，有的负责照顾伤员、救死扶伤，有的负责宣传群众、筹措粮草，还有的负责架桥修路、保障后勤。除此之外，她们还要照顾年幼的小红军，帮助战友们缝补衣服，用自己的方式，为长征的胜利做出了巨大的贡献。",
        "女红军过雪山草地的时候遇到了什么困难": "过雪山草地的时候，女红军遇到的困难比男战士还要多。雪山海拔高，空气稀薄，天气寒冷，很多女红军都穿着单衣，冻得浑身发抖；草地里到处都是沼泽，一不小心就会陷进去，而且没有食物，很多人只能吃草根、煮皮带。除此之外，她们还要克服女性生理上的特殊困难，但是她们都坚持了下来，没有一个人轻易放弃。",
        "半条被子的故事是真的吗": "是的，半条被子的故事是真实发生的。这个故事的主人公徐解秀老人一直活到了2016年，享年91岁。她生前一直念叨着那三位女红军，一直等着她们回来。2016年，习近平总书记在纪念红军长征胜利80周年大会上，专门讲述了这个故事，让更多的人知道了这段感人的历史。",
        "有哪些著名的女红军": "长征中有很多著名的女红军，比如邓颖超、蔡畅、康克清、张琴秋、李贞、危秀英、邓六金、贺子珍等等，她们都是了不起的女英雄，有的后来成为了新中国的领导人，有的为革命事业奉献了自己的一生。其中李贞后来成为了新中国第一位女将军。",
        "女红军可以结婚吗": "在红军队伍里，是允许结婚的，但是有严格的规定，比如'二八五团'的规定，就是年龄要满28岁，党龄要满5年，职务要够团级，才能结婚。所以很多女红军都是符合条件之后才结婚的，很多夫妻都是一起参加的长征，互相扶持着走完了这段路。",
        "长征中女红军有牺牲吗": "当然有，很多女红军都牺牲在了长征路上。比如在腊子口战斗中，一支女红军连队为了掩护大部队，和敌人展开了殊死搏斗，最后70多名女战士全部牺牲，很多人都没有留下名字。还有很多女红军在过草地的时候，因为饥饿、疾病，或者陷入沼泽，永远地留在了那里。"
    }
    
    # 初始化聊天会话
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 显示历史消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("输入你的问题，比如：长征中有多少女红军？"):
        # 显示用户消息
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 生成回答
        with st.chat_message("assistant"):
            # 简单的关键词匹配
            response = "抱歉，我还不太明白这个问题，你可以问问我关于女红军的数量、她们的任务、半条被子的故事这些问题哦！"
            for key in qa_pairs:
                if key in prompt or prompt in key:
                    response = qa_pairs[key]
                    break
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# 英雄人物页面
elif page == "英雄人物":
    st.title("👩 女红军英雄谱")
    st.markdown("认识这些了不起的女英雄们，她们的故事值得我们永远铭记")
    
    # 展示女红军人物卡片
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.subheader("邓颖超")
            st.markdown("""
周恩来总理的夫人，参加长征的时候，她正患有肺结核，身体非常虚弱。
但是她坚持跟着大部队，一路上还帮着照顾伤员，做宣传工作。过草地的时候，
她甚至把自己的干粮分给了其他战士，自己饿了好几天。
            """)
            st.divider()
        
        with st.container():
            st.subheader("危秀英")
            st.markdown("""
就是我们之前提到的那个矮个子女英雄，她身高不到一米四，却背着省委书记走出了敌人的包围圈。
她后来担任了江西省妇联主任，为妇女解放事业做出了很大的贡献。
            """)
            st.divider()
        
        with st.container():
            st.subheader("张琴秋")
            st.markdown("""
张琴秋是红四方面军妇女独立师的师长，她是红军中唯一的女师长。
她带领着女战士们打了很多胜仗，被称为"红军中的花木兰"。
后来她成为了新中国的纺织工业部副部长。
            """)
            st.divider()
        
        with st.container():
            st.subheader("贺子珍")
            st.markdown("""
毛泽东主席的夫人，她在长征路上为了掩护伤员，身中数弹，
身上留下了十几块弹片，但是她依然坚持走完了长征。
她为革命事业奉献了自己的一切。
            """)
    
    with col2:
        with st.container():
            st.subheader("邓六金")
            st.markdown("""
带病走完长征的女英雄，她后来担任了国务院机关事务管理局的副局长，
一直致力于儿童福利事业，是孩子们心中的"邓妈妈"。
            """)
            st.divider()
        
        with st.container():
            st.subheader("李贞")
            st.markdown("""
李贞是新中国第一位女将军，她参加了长征，一路上经历了无数的战斗。
她的一生充满了传奇，从一个童养媳，成长为了开国女将，
她的故事激励了无数的女性。
            """)
            st.divider()
        
        with st.container():
            st.subheader("康克清")
            st.markdown("""
朱德总司令的夫人，她是红军中有名的女司令，武功高强，能征善战。
长征路上，她负责指挥后卫部队，多次打退敌人的追击，保护了大部队的安全。
            """)
            st.divider()
        
        with st.container():
            st.subheader("蔡畅")
            st.markdown("""
中国妇女运动的先驱，她是最早参加革命的女性之一。
长征路上，她虽然年纪比较大，但是从来没有掉队，还经常鼓励年轻的战士们。
后来她担任了全国妇联主席，为妇女解放事业奋斗了一生。
            """)
    
    # 底部的图片
    try:
        img_url = "https://aka.doubaocdn.com/s/wmoB1wYIds"
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        st.markdown("---")
        st.image(img, caption="103岁的长征女红军张文，她是众多女英雄中的一位幸存者", use_column_width=True)
    except:
        pass
