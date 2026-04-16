#!/usr/bin/env python3
"""生成一个带有中国法律陷阱的中文版自由职业者服务协议 PDF。"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUTPUT_PATH = "sample-contract.pdf"

def register_chinese_fonts():
    """注册中文字体 (优先 Windows 黑体)。"""
    font_paths = [
        "C:\\Windows\\Fonts\\simhei.ttf",
        "C:\\Windows\\Fonts\\simsun.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "simhei.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont('ChineseFont', path))
                return 'ChineseFont'
            except:
                continue
    return 'Helvetica'

CHINESE_FONT = register_chinese_fonts()

def build_contract():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
        leftMargin=1*inch,
        rightMargin=1*inch,
    )

    styles = getSampleStyleSheet()
    
    # 定义中文字体样式
    title_style = ParagraphStyle(
        'ContractTitle', parent=styles['Title'],
        fontName=CHINESE_FONT, fontSize=16, spaceAfter=10, alignment=TA_CENTER,
    )
    heading_style = ParagraphStyle(
        'SectionHead', parent=styles['Heading2'],
        fontName=CHINESE_FONT, fontSize=11, spaceBefore=14, spaceAfter=6,
    )
    body_style = ParagraphStyle(
        'ContractBody', parent=styles['Normal'],
        fontName=CHINESE_FONT, fontSize=9.5, leading=14, alignment=TA_JUSTIFY, spaceAfter=6,
    )
    small_style = ParagraphStyle(
        'SmallPrint', parent=body_style,
        fontSize=8, textColor=colors.grey,
    )

    story = []

    # ── 标题 ──
    story.append(Paragraph("独立顾问服务协议 (测试用本)", title_style))
    story.append(Spacer(1, 10))

    # ── 前言 ──
    story.append(Paragraph(
        '本服务协议（以下简称“<b>本协议</b>”）由以下双方于 2026 年 3 月 1 日签署：', body_style))
    story.append(Paragraph('<b>甲方：Nexus Digital Solutions LLC (中国区办事处)</b>', body_style))
    story.append(Paragraph('<b>乙方：独立承包商 (即顾问)</b>', body_style))
    story.append(Spacer(1, 10))

    # ── 第一条：服务范围 ──
    story.append(Paragraph("第一条 服务内容与修订", heading_style))
    story.append(Paragraph(
        "1.1 乙方应负责甲方网站的全面重构与开发。甲方有权随时单方面修改服务规格。", body_style))
    story.append(Paragraph(
        "<b>1.2 无限制修改：</b>乙方应提供不限次数的修改服务，直到甲方完全满意为止，且甲方无需支付任何额外费用。", body_style))

    # ── 第二条：报酬与支付 ──
    story.append(Paragraph("第二条 报酬与支付 (风险点：超长账期)", heading_style))
    story.append(Paragraph(
        "2.1 本项目总费用为人民币 15,000 元。所有款项将在甲方确认验收后的 120 个工作日内支付。", body_style))
    story.append(Paragraph(
        "2.2 甲方有权根据其主观判断，以“成果不符合预期”为由拒绝支付任何阶段性款项。", body_style))

    # ── 第三条：知识产权 ──
    story.append(Paragraph("第三条 知识产权 (风险点：剥夺署名权)", heading_style))
    story.append(Paragraph(
        "3.1 乙方在本项目中创作的所有作品、代码及素材，其所有权及著作权（包括署名权）自创作完成之日起永久归甲方所有。乙方声明放弃所有人格权。", body_style))

    # ── 第四条：竞业限制 (陷阱：无补偿金) ──
    story.append(Paragraph("第四条 竞业限制与禁止招揽", heading_style))
    story.append(Paragraph(
        "<b>4.1 竞业限制：</b>乙方在协议期限内及合同终止后的 24 个月内，不得直接或间接从事任何与甲方竞争的业务。<b>本条款不设任何额外的经济补偿。</b>", body_style))

    # ── 第五条：违约责任 (陷阱：超高违约金) ──
    story.append(Paragraph("第五条 违约责任", heading_style))
    story.append(Paragraph(
        "5.1 若乙方未能按期交付任何阶段性成果，乙方应向甲方支付相当于<b>合同总额 50% (即 7,500 元)</b> 的违约金。此金额不作为对甲方损失的预估，而是作为惩罚性赔偿。", body_style))

    # ── 第六条：数据处理 (风险点：违反 PIPL) ──
    story.append(Paragraph("第六条 数据保护与个人信息", heading_style))
    story.append(Paragraph(
        "6.1 乙方同意将其个人手机通讯录、社交账号好友列表等信息完整同步至甲方服务器。甲方可根据需要将此类数据分享给任意第三方合作伙伴，无需另行通知乙方。", body_style))

    # ── 第七条：争议解决 (陷阱：管辖权) ──
    story.append(Paragraph("第七条 法律适用与管辖", heading_style))
    story.append(Paragraph(
        "7.1 本协议受英属维尔京群岛 (BVI) 法律管辖。任何争议应提交至英属维尔京群岛法院通过诉讼解决。", body_style))

    story.append(Spacer(1, 20))

    # ── 签字 ──
    story.append(Paragraph("甲方 (盖章): ____________________", body_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("乙方 (签字): ____________________", body_style))

    story.append(Spacer(1, 30))
    story.append(Paragraph("<i>注：本文件为 AI 法律助手测试专用样本，包含多处法律陷阱。</i>", small_style))

    # 构建 PDF
    try:
        doc.build(story)
        print(f"✅ 中文测试合同已生成: {OUTPUT_PATH}")
    except Exception as e:
        print(f"❌ 生成失败: {e}")

if __name__ == "__main__":
    if CHINESE_FONT == 'Helvetica':
        print("警告: 未找到中文字体，PDF 可能显示为乱码。请确保系统中安装了黑体 (SimHei)。")
    build_contract()
