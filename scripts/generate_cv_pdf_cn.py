#!/usr/bin/env python3
"""Generate formal Chinese table-style CV PDF from BaoBeining_中文CV_CN content."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "BaoBeining_CV_CN.pdf"
DESKTOP_OUT = Path(
    "/Users/bbn/Desktop/参与文献&topics 📖/PhD 💼/个人资料&相关资料/BaoBeining_CV_CN.pdf"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

# Prefer single-file Unicode TTF for reliable CJK rendering
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
pdfmetrics.registerFont(TTFont("CN", FONT_PATH))

BLACK = colors.black
GRAY = colors.HexColor("#333333")
HEADER_BG = colors.HexColor("#f2f2f2")
LINE = colors.HexColor("#222222")


def S(name, size=9, leading=12, align=TA_LEFT, bold=False):
    return ParagraphStyle(
        name,
        fontName="CN",
        fontSize=size,
        leading=leading,
        alignment=align,
        textColor=BLACK,
        spaceBefore=0,
        spaceAfter=0,
    )


st_title = S("title", 16, 20, TA_CENTER)
st_h = S("h", 11, 15, TA_LEFT)
st_label = S("label", 9, 12, TA_CENTER)
st_cell = S("cell", 9, 12, TA_LEFT)
st_body = S("body", 9, 13, TA_JUSTIFY)
st_small = S("small", 8.5, 11.5, TA_JUSTIFY)
st_sec = S("sec", 10.5, 14, TA_LEFT)


def P(text, style=st_body):
    return Paragraph(str(text).replace("\n", "<br/>"), style)


def section_banner(text):
    t = Table([[P(text, st_sec)]], colWidths=[178 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), HEADER_BG),
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def info_table():
    # Formal 个人情况 table close to original docx
    data = [
        [
            P("姓名", st_label),
            P("包贝宁", st_cell),
            P("性别", st_label),
            P("男", st_cell),
            P("国籍", st_label),
            P("中国", st_cell),
        ],
        [
            P("民族", st_label),
            P("蒙古族", st_cell),
            P("政治面貌", st_label),
            P("共青团员", st_cell),
            P("出生年月", st_label),
            P("2002.05", st_cell),
        ],
        [
            P("证件类型", st_label),
            P("身份证", st_cell),
            P("证件号码", st_label),
            P("152301200205136213", st_cell),
            P("", st_cell),
            P("", st_cell),
        ],
        [
            P("现单位", st_label),
            P("香港城市大学", st_cell),
            P("职务/职称", st_label),
            P("博士研究生（在读）", st_cell),
            P("", st_cell),
            P("", st_cell),
        ],
        [
            P("户籍地", st_label),
            P("内蒙古自治区通辽市", st_cell),
            P("婚姻状况", st_label),
            P("未婚", st_cell),
            P("", st_cell),
            P("", st_cell),
        ],
        [
            P("联系方式", st_label),
            P("移动电话", st_label),
            P("15204759850", st_cell),
            P("电子邮箱", st_label),
            P("beininbao2-c@my.cityu.edu.hk", st_cell),
            P("", st_cell),
        ],
        [
            P("家庭地址", st_label),
            P("内蒙古自治区通辽市科尔沁区", st_cell),
            P("", st_cell),
            P("", st_cell),
            P("", st_cell),
            P("", st_cell),
        ],
    ]

    # column widths totaling ~178mm
    col_w = [22 * mm, 28 * mm, 24 * mm, 36 * mm, 24 * mm, 44 * mm]
    t = Table(data, colWidths=col_w, repeatRows=0)
    style_cmds = [
        ("GRID", (0, 0), (-1, -1), 0.7, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BACKGROUND", (0, 0), (0, -1), HEADER_BG),
        ("BACKGROUND", (2, 0), (2, 1), HEADER_BG),
        ("BACKGROUND", (4, 0), (4, 1), HEADER_BG),
        ("BACKGROUND", (2, 2), (2, 4), HEADER_BG),
        ("BACKGROUND", (0, 5), (1, 5), HEADER_BG),
        ("BACKGROUND", (3, 5), (3, 5), HEADER_BG),
        ("BACKGROUND", (0, 6), (0, 6), HEADER_BG),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        # merge cells for long fields
        ("SPAN", (3, 2), (5, 2)),  # id number
        ("SPAN", (3, 3), (5, 3)),  # title
        ("SPAN", (3, 4), (5, 4)),  # marriage
        ("SPAN", (4, 5), (5, 5)),  # email
        ("SPAN", (1, 6), (5, 6)),  # address
    ]
    t.setStyle(TableStyle(style_cmds))
    return t


def block_table(title, body_flowables):
    inner = [[section_banner(title)]]
    for f in body_flowables:
        inner.append([f])
    t = Table(inner, colWidths=[178 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.8, LINE),
                ("LEFTPADDING", (0, 1), (-1, -1), 5),
                ("RIGHTPADDING", (0, 1), (-1, -1), 5),
                ("TOPPADDING", (0, 1), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 3),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def build():
    story = []
    story.append(P("包贝宁简历", st_title))
    story.append(Spacer(1, 3 * mm))
    story.append(section_banner("个人情况"))
    story.append(info_table())
    story.append(Spacer(1, 3 * mm))

    intro = (
        "包贝宁，香港城市大学生物统计专业博士研究生（在读），历史研究围绕图异常检测以及大语言模型在医疗以及科学研究场景中的应用与加速，"
        "当前主要研究医疗数据知识的隐空间表示、隐私保护临床数据生成以及电子病历数据变换相关研究。"
        "以学生一作在 CCF-A 级国际会议 TheWebConf 2026 发表并接收；另有工作被 SIGIR 2026、KDD 2026、ICDM 2026（Applied Track）等接收，"
        "并有多篇工作投稿至 ICML、CVPR、ACL、RecSys 等会议等待审阅。"
        "当前重点面向 AI for Science 场景设计低计算量、可解释的数据变换与隐私机制，以及隐私保护临床文本生成与数据变换方法，"
        "后续将与成都实验室合作参与湿实验等交叉研究，支撑安全可复现的科学发现。"
    )
    story.append(block_table("个人简介（100字左右）", [P(intro, st_body)]))
    story.append(Spacer(1, 2.5 * mm))

    edu = [
        P("（1）2026-09至2030-06：香港城市大学，生物统计，博士（在读），导师：闫峻、王茂林、王尧", st_small),
        P("（2）2025-08至2026-06：香港城市大学，数据科学，硕士，导师：王茂林、闫峻、王尧、赵翔宇", st_small),
        P("（3）2020-09至2025-06：北京交通大学，工商管理，学士，导师：王振", st_small),
        P("（4）2020-09至2025-06：兰卡斯特大学（Lancaster University）（双学位），Business Study，学士，导师：王振", st_small),
    ]
    story.append(block_table("教育背景", edu))
    story.append(Spacer(1, 2.5 * mm))

    work = [
        P(
            "（1）2025-12至今：香港城市大学 AI for Science 研究院（HKAI-Sci），研究助理（在读博士期间同步开展）"
            "<br/>围绕医疗 AI for Science 与隐私数据变换开展研究，主导并以第一作者身份完成数据变换研究报告并 online 于 arXiv，"
            "相关工作投稿/发表于 CUSR、KDD 等。",
            st_small,
        ),
        P(
            "（2）2024-12至2025-03：腾讯公司（北京），大语言模型实习生"
            "<br/>参与微信搜索场景下混元大模型相关工作，对法律、医疗等领域文档进行文本预处理与质量控制，"
            "设计基于提示词与合成数据的标注与检索管线，提升检索效率与标签一致性。",
            st_small,
        ),
        P(
            "（3）2023-07至2023-09：Joy Media，数据运营实习生"
            "<br/>负责 KOL 直播及短视频数据分析，建立对标头部账号的运营指标体系，撰写竞品分析报告，为内容策略优化与运营流程改进提供数据支撑。",
            st_small,
        ),
        P(
            "（4）2022-08至2022-09：北京国际大数据交易所股份有限公司，数据研究实习生"
            "<br/>参与行业与竞品调研，基于公开数据与内部指标撰写研究报告，为产品规划与市场推广提供决策参考。",
            st_small,
        ),
    ]
    story.append(block_table("工作经历", work))
    story.append(Spacer(1, 2.5 * mm))

    duty = [
        P(
            "2025-12至今：香港城市大学 AI for Science，研究助理（RA）"
            "<br/>以研究助理与项目骨干身份参与隐私保护临床文本生成、EHR 数据几何变换及 AI for Science 工作流等方向科研工作，"
            "并协助与香港城市大学成都实验室的联合项目沟通与推进。",
            st_small,
        )
    ]
    story.append(block_table("学术职务或社会职务", duty))
    story.append(Spacer(1, 2.5 * mm))

    pubs = [
        P("一、论文", st_h),
        P(
            "Wang M, Bao B, Chen H, Liu Z, Fu L, Chu J, Liang L, Xu Z. GRAND: A Robust Diffusion Framework for "
            "Multi-Granularity Graph Anomaly Detection in Web Platforms. TheWebConf 2026 (Web4Good). 2026. "
            "(DOI: 10.1145/3774904.3793012)<br/>"
            "（本人标注：学生第一作者；CCF-A，已接收）",
            st_small,
        ),
        P(
            "Wang M, Mai Z, Liu Z, Bao B, Chen H, et al. A Serial Two-Stage Framework for Robust Multimodal Fake News "
            "Detection via Adaptive Reasoning. ACM SIGKDD 2026. 2026.<br/>"
            "（本人标注：第四作者；CCF-A，已接收）",
            st_small,
        ),
        P(
            "Wang M, Wu D, Zhou J, Chen H, Bao B, Jiang Y, Zhang C, Wang C, Liu J, Sha L. Rethinking Semantic Collaborative "
            "Integration: Why Alignment Is Not Enough. ACM SIGIR 2026. 2026. "
            "(DOI: 10.1145/3805712.3808539; arXiv:2604.22195)<br/>"
            "（本人标注：第五作者；CCF-A，已接收）",
            st_small,
        ),
        P(
            "Fu Y, Bao B, Jiang Y, Zhao X, et al., Wang M. MuSeR: Scalable Long-sequence Recommendation with Multi-interest "
            "Modeling. IEEE ICDM 2026, Applied Track. 2026. (arXiv:2609.23677)<br/>"
            "（本人标注：第二作者；CCF-B，Applied Track，已接收；百度真实场景部署）",
            st_small,
        ),
        P(
            "Chen H, Bao B, Liu Z, Wei T, Wang M, Li X, So HC. Deep Tensor Factorization for Modeling Non-Uniform Temporal "
            "Dynamics with Adaptive Temporal Smoothing. IEEE SAM 2026. 2026.<br/>"
            "（本人标注：共同一作；已接收）",
            st_small,
        ),
        P(
            "Shao S, Zhao B, Cui X, Dai Y, Bao B. Housing Rental Information Management and Prediction System Based on "
            "CatBoost Algorithm – A Case Study of Halifax Region. IJCRS 2024 / LNCS 14840.<br/>"
            "（本人标注：第五作者；CCF-B，已接收）",
            st_small,
        ),
        P(
            "其他合作论文：作为第 2–5 作者，参与多篇投稿至 ICML、CVPR、ACL Rolling Review、RecSys 等会议的工作"
            "（含 RecSys 主会稿 From Impulse to Interest: Curiosity-Aware Click Modeling for Long-Term Preference Estimation，第二作者），"
            "目前均处于评审阶段。",
            st_small,
        ),
        P("二、基金项目", st_h),
        P("目前暂无基金项目。", st_small),
        P("三、专利", st_h),
        P("目前暂无已授权或公开的发明专利。", st_small),
        P("四、其他科研成果及获奖荣誉", st_h),
        P("（一）科研实践与系统建设", st_h),
        P(
            "CLEAR-Note / ReaL-Guard：参与隐私增强临床文本生成管线与统一评估框架落地，完成 MIMIC-IV 上隐私–效用折中实验。",
            st_small,
        ),
        P(
            "EHR-Privacy-Agent：封装列向几何算子 T1/T2/T3 为隐私技能，实现 ICU 生命体征与实验室指标低计算量可见脱敏。",
            st_small,
        ),
        P(
            "住房租赁信息管理与预测系统（Halifax，2024-07）：CatBoost + Tableau；IJCRS 2024 论文与竞赛三等奖。",
            st_small,
        ),
        P(
            "智能养老匹配平台“养老通”（2024-11至2025-05）：26,000+ 机构、2,086 问卷，模糊匹配/TF-IDF/CatBoost + IBM Watson。",
            st_small,
        ),
        P("（二）获奖荣誉", st_h),
        P("2024 年 IJCRS 国际数据挖掘竞赛总决赛三等奖。", st_small),
        P("2026 年香港城市大学数据科学硕士 Best Project Award。", st_small),
        P("2023 年全国大学生数据分析科普知识竞赛优秀奖。", st_small),
        P("（三）科研能力与技能概况", st_h),
        P(
            "熟练掌握机器学习与深度学习工具，具备图机器学习、推荐系统建模与评测、大语言模型提示工程与数据合成经验；"
            "熟悉实验设计、可复现科研代码管理与中英文技术写作。",
            st_small,
        ),
    ]
    story.append(block_table("代表性成果", pubs))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("CN", 8)
        canvas.setFillColor(GRAY)
        canvas.drawCentredString(A4[0] / 2, 10 * mm, f"包贝宁简历 | 第 {doc.page} 页")
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=12 * mm,
        bottomMargin=14 * mm,
        title="包贝宁简历",
        author="包贝宁",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    DESKTOP_OUT.parent.mkdir(parents=True, exist_ok=True)
    DESKTOP_OUT.write_bytes(OUT.read_bytes())
    print(OUT)
    print(DESKTOP_OUT)


if __name__ == "__main__":
    build()
