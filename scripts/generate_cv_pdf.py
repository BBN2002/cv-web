#!/usr/bin/env python3
"""Generate Beining Bao academic CV PDF (PhD student status)."""

from pathlib import Path

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUT = Path(__file__).resolve().parents[1] / "output" / "pdf" / "BaoBeining_CV_EN.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

ACCENT = HexColor("#4a6fa5")
SOFT = HexColor("#555555")
LINE = HexColor("#cfd8e6")


def styles():
    base = getSampleStyleSheet()
    s = {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            alignment=TA_CENTER,
            textColor=black,
            spaceAfter=2 * mm,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            alignment=TA_CENTER,
            textColor=SOFT,
            spaceAfter=3 * mm,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=ACCENT,
            spaceBefore=2.2 * mm,
            spaceAfter=1.0 * mm,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.2,
            alignment=TA_JUSTIFY,
            textColor=black,
            spaceAfter=1.0 * mm,
        ),
        "item_title": ParagraphStyle(
            "ItemTitle",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=12,
            textColor=black,
            spaceBefore=0.8 * mm,
        ),
        "item_meta": ParagraphStyle(
            "ItemMeta",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=8.2,
            leading=10.5,
            textColor=SOFT,
            spaceAfter=0.4 * mm,
        ),
        "item_body": ParagraphStyle(
            "ItemBody",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.8,
            textColor=black,
            spaceAfter=0.8 * mm,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.5,
            leftIndent=2 * mm,
            textColor=black,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=SOFT,
            alignment=TA_CENTER,
        ),
    }
    return s


def section(title, s):
    return [
        Paragraph(title.upper(), s["h1"]),
        HRFlowable(width="100%", thickness=0.8, color=LINE, spaceAfter=2 * mm),
    ]


def build():
    s = styles()
    story = []

    story.append(Paragraph("BEINING BAO", s["name"]))
    story.append(
        Paragraph(
            "PhD Student, AI of Health &amp; Life Science (Biostatistics) | City University of Hong Kong<br/>"
            "Research Assistant, Hong Kong Institute of AI for Science (HKAI-Sci)<br/>"
            "Email: beininbao2-c@my.cityu.edu.hk | Tel: +852 8495 6787 | "
            "Homepage: https://bbn2002.github.io/cv-web/",
            s["contact"],
        )
    )

    story += section("Research Interests", s)
    story.append(
        Paragraph(
            "AI for health and life sciences; medical large language models; privacy-preserving EHR transformation "
            "and clinical text generation; medical knowledge graphs; large-scale recommendation and language models; "
            "AI safety and reproducible machine learning.",
            s["body"],
        )
    )

    story += section("Education", s)
    story.append(Paragraph("Ph.D. in AI of Health &amp; Life Science (Biostatistics)", s["item_title"]))
    story.append(
        Paragraph(
            "City University of Hong Kong, Hong Kong &nbsp;&nbsp;|&nbsp;&nbsp; Sept 2026 - Jun 2030 (expected)",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Status: Current PhD student. Advisor: Prof. Jun Yan. Collaborators/advisors: Prof. Maolin Wang, "
            "Senior Engineer Yao Wang. Prior mentor: Prof. Xiangyu Zhao (Department of Data Science).",
            s["item_body"],
        )
    )

    story.append(Paragraph("M.Sc. in Data Science", s["item_title"]))
    story.append(
        Paragraph(
            "City University of Hong Kong, Hong Kong &nbsp;&nbsp;|&nbsp;&nbsp; Aug 2025 - Jun 2026",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Graduated with distinction (First Class Honours). Research training in data science, AI for Science, "
            "medical AI, and reproducible machine learning.",
            s["item_body"],
        )
    )

    story.append(Paragraph("B.Sc. in Business Studies (Double Degree)", s["item_title"]))
    story.append(
        Paragraph(
            "Lancaster University, UK / Beijing Jiaotong University, China &nbsp;&nbsp;|&nbsp;&nbsp; Sept 2020 - Jun 2025",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Undergraduate training in analytics, business research, and data-driven decision making.",
            s["item_body"],
        )
    )

    story += section("Research / Work Experience", s)
    story.append(Paragraph("Research Assistant, AI for Science", s["item_title"]))
    story.append(
        Paragraph(
            "HKAI-Sci, City University of Hong Kong &nbsp;&nbsp;|&nbsp;&nbsp; Jan 2026 - Present",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Research on medical LLMs, privacy-preserving clinical data transformation, medical knowledge graphs, "
            "and AI safety; model implementation, experiments, paper writing, and reproducible research code. "
            "Supervisor: Prof. Jun Yan.",
            s["item_body"],
        )
    )

    story.append(Paragraph("Large Language Model Intern", s["item_title"]))
    story.append(
        Paragraph(
            "Tencent (WeChat Search / Hunyuan), Beijing &nbsp;&nbsp;|&nbsp;&nbsp; Dec 2024 - Mar 2025",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Text preprocessing for medical/legal documents; prompt and synthetic-data pipelines; improved retrieval "
            "efficiency and labeling consistency.",
            s["item_body"],
        )
    )

    story.append(Paragraph("Data Operations Intern", s["item_title"]))
    story.append(
        Paragraph("Joy Media, Hangzhou &nbsp;&nbsp;|&nbsp;&nbsp; Jul 2023 - Sept 2023", s["item_meta"])
    )
    story.append(
        Paragraph(
            "KOL live-stream and short-video analytics; competitive analysis to guide content strategy and operations.",
            s["item_body"],
        )
    )

    story.append(Paragraph("Data Research Intern", s["item_title"]))
    story.append(
        Paragraph(
            "Beijing International Big Data Exchange Co., Ltd. &nbsp;&nbsp;|&nbsp;&nbsp; Aug 2022 - Sept 2022",
            s["item_meta"],
        )
    )
    story.append(
        Paragraph(
            "Industry and competitor research; data-driven reports for product planning and marketing strategy.",
            s["item_body"],
        )
    )

    story += section("Selected Publications", s)
    story.append(
        Paragraph(
            "* marks myself. Selected accepted / published works:",
            s["item_body"],
        )
    )

    pubs = [
        (
            "<b>GRAND: A Robust Diffusion Framework for Multi-Granularity Graph Anomaly Detection in Web Platforms.</b> "
            "Maolin Wang, <b>Beining Bao*</b>, Hongyu Chen, Zichun Liu, Lang Fu, Jun Chu, Langzhang Liang, Zenglin Xu. "
            "TheWebConf 2026 (Web4Good), CCF-A. DOI: 10.1145/3774904.3793012."
        ),
        (
            "<b>A Serial Two-Stage Framework for Robust Multimodal Fake News Detection via Adaptive Reasoning.</b> "
            "Maolin Wang, Ziting Mai, Zichun Liu, <b>Beining Bao*</b>, Hongyu Chen, et al. "
            "ACM SIGKDD 2026, CCF-A."
        ),
        (
            "<b>Rethinking Semantic-Collaborative Integration: Why Alignment Is Not Enough.</b> "
            "Maolin Wang, Dongze Wu, Jianing Zhou, Hongyu Chen, <b>Beining Bao*</b>, Yu Jiang, et al. "
            "ACM SIGIR 2026 (Perspectives), CCF-A. DOI: 10.1145/3805712.3808539."
        ),
        (
            "<b>MuSeR: Scalable Long-sequence Recommendation with Multi-interest Modeling.</b> "
            "Yongkang Fu, <b>Beining Bao*</b>, Yu Jiang, Xiangyu Zhao, et al., Maolin Wang. "
            "IEEE ICDM 2026 (Applied Track), CCF-B. Deployed at Baidu. arXiv:2609.23677."
        ),
        (
            "<b>Deep Tensor Factorization for Modeling Non-Uniform Temporal Dynamics with Adaptive Temporal Smoothing.</b> "
            "Hongyu Chen, <b>Beining Bao*</b> (co-first), Zichun Liu, Tianshuo Wei, Maolin Wang, Xiaopeng Li, Hing Cheung So. "
            "IEEE SAM 2026."
        ),
        (
            "<b>Privacy-Preserving EHR Data Transformation via Geometric Operators: A Human-AI Co-Design Technical Report.</b> "
            "Maolin Wang&#8224;, <b>Beining Bao*</b>&#8224;, et al., Jun Yan. arXiv:2603.22954, 2026."
        ),
        (
            "<b>Housing Rental Information Management and Prediction System Based on CatBoost Algorithm - A Case Study of Halifax Region.</b> "
            "Shuangrun Shao, Bingxi Zhao, Xiangen Cui, Yihong Dai, <b>Beining Bao*</b>. IJCRS 2024 / LNCS, CCF-B."
        ),
    ]
    for p in pubs:
        story.append(Paragraph("&#8226; " + p, s["item_body"]))

    story.append(
        Paragraph(
            "<b>Selected manuscript under review:</b> From Impulse to Interest: Curiosity-Aware Click Modeling for "
            "Long-Term Preference Estimation. Chengxi Wei, <b>Beining Bao*</b>, Hongyu Chen, et al. ACM RecSys 2026 "
            "(Main Track), under review.",
            s["item_body"],
        )
    )

    story += section("Selected Projects &amp; Honours", s)
    story.append(
        Paragraph(
            "&#8226; Intelligent Elderly Care Matching Platform (YangLaoTong), Nov 2024 - May 2025: fuzzy matching, "
            "TF-IDF, CatBoost over 26,000+ nursing homes; IBM Watson dialogue; 2,086 questionnaires with NLP refinement.",
            s["item_body"],
        )
    )
    story.append(
        Paragraph(
            "&#8226; Honours: Third place, IJCRS International Data Mining Competition Final (2024); "
            "Best Project Award, MSc in Data Science (2026); Excellence Award, National College Student Data Analysis "
            "Popular Science Knowledge Competition (Oct 2023).",
            s["item_body"],
        )
    )

    story += section("Skills", s)
    story.append(
        Paragraph(
            "Python, PyTorch, scikit-learn, CatBoost, Transformers, Graph ML, Medical LLMs, Medical knowledge graphs, "
            "AI safety, LLM prompting &amp; data generation, reproducible pipelines. Languages: English, Mandarin.",
            s["body"],
        )
    )

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(SOFT)
        canvas.drawCentredString(
            A4[0] / 2,
            12 * mm,
            f"Beining Bao | PhD CV | Page {doc.page}",
        )
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=16 * mm,
        title="Beining Bao - Curriculum Vitae",
        author="Beining Bao",
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUT)


if __name__ == "__main__":
    build()
