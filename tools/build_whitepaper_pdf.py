#!/usr/bin/env python3
import re, sys
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, ListFlowable, ListItem, Preformatted

SRC = Path(sys.argv[1] if len(sys.argv)>1 else 'whitepaper/DPP-Whitepaper-v1.0.md')
OUT = Path(sys.argv[2] if len(sys.argv)>2 else 'site/DPP-Whitepaper-v1.0.pdf')
text = SRC.read_text(encoding='utf-8')

navy = colors.HexColor('#101827'); ink = colors.HexColor('#172033'); muted = colors.HexColor('#586174'); accent = colors.HexColor('#3b67d9'); rule = colors.HexColor('#d8deea'); pale = colors.HexColor('#f3f6fb')
styles = getSampleStyleSheet()
body = ParagraphStyle('Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.5, leading=14, textColor=ink, spaceAfter=7)
h1 = ParagraphStyle('H1', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=navy, spaceBefore=13, spaceAfter=8, keepWithNext=True)
h2 = ParagraphStyle('H2', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=accent, spaceBefore=10, spaceAfter=5, keepWithNext=True)
quote = ParagraphStyle('Quote', parent=body, leftIndent=18, rightIndent=18, borderColor=accent, borderWidth=0, borderPadding=8, backColor=pale, fontName='Helvetica-Oblique')
small = ParagraphStyle('Small', parent=body, fontSize=8, leading=11, textColor=muted)
cover_title = ParagraphStyle('CoverTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=30, leading=34, textColor=navy, alignment=TA_CENTER, spaceAfter=14)
cover_sub = ParagraphStyle('CoverSub', parent=body, fontSize=14, leading=19, alignment=TA_CENTER, textColor=muted)
cover_meta = ParagraphStyle('CoverMeta', parent=body, fontSize=9.5, leading=15, alignment=TA_CENTER, textColor=ink)
code = ParagraphStyle('Code', fontName='Courier', fontSize=7.5, leading=10, textColor=ink, backColor=pale, leftIndent=8, rightIndent=8, borderPadding=6)

def inline(s):
    s = escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)
    s = re.sub(r'`(.+?)`', r'<font name="Courier">\1</font>', s)
    return s

def footer(canvas, doc):
    canvas.saveState(); w,h=LETTER
    canvas.setStrokeColor(rule); canvas.line(0.72*inch,0.55*inch,w-0.72*inch,0.55*inch)
    canvas.setFont('Helvetica',7.5); canvas.setFillColor(muted)
    canvas.drawString(0.72*inch,0.34*inch,'Dog5pk Production Protocol | Whitepaper v1.0 | DPP v1.3')
    canvas.drawRightString(w-0.72*inch,0.34*inch,f'{doc.page}')
    canvas.restoreState()

def parse_table(lines):
    rows=[]
    for line in lines:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-{3,}:?',c or '-') for c in cells): continue
        rows.append([Paragraph(inline(c), small) for c in cells])
    if not rows: return None
    t=Table(rows, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('GRID',(0,0),(-1,-1),0.35,rule),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    return t

story=[]
story += [Spacer(1,1.25*inch), Paragraph('THE DOG5PK PRODUCTION PROTOCOL', cover_title), Paragraph('A Production Standard for Dependable Human-AI Collaboration', cover_sub), Spacer(1,0.42*inch)]
meta = '<b>Whitepaper Version:</b> 1.0<br/><b>Protocol Baseline:</b> DPP v1.3<br/><b>Author:</b> Dog5pk<br/><b>Status:</b> Public Whitepaper<br/><b>Date:</b> August 2026<br/><b>License:</b> CC BY 4.0'
story += [Paragraph(meta, cover_meta), Spacer(1,0.48*inch), Paragraph('<i>Reality is the benchmark. Finished work is the objective.</i>', cover_sub), Spacer(1,0.25*inch), Paragraph('<b>STEP FORWARD OR STEP ASIDE.</b>', cover_meta), PageBreak()]

heads=[]
for ln in text.splitlines():
    if ln == '## Abstract' or re.match(r'^## \d+\. ', ln) or ln.startswith('## Appendix '):
        heads.append(ln[3:])
story += [Paragraph('Contents', h1)]
toc_style = ParagraphStyle('toc',parent=body,fontSize=9,leading=12,leftIndent=8,spaceAfter=2)
for x in heads:
    story.append(Paragraph(inline(x), toc_style))
story.append(PageBreak())

lines=text.splitlines()
# Skip Markdown title/subtitle/metadata already represented by the cover.
start=0
for idx, ln in enumerate(lines):
    if ln.strip() == '---':
        start = idx + 1
        break
lines = lines[start:]
i=0; in_code=False; codebuf=[]; bullets=[]; nums=[]
def flush_lists():
    global bullets, nums
    if bullets:
        story.append(ListFlowable([ListItem(Paragraph(inline(x),body), leftIndent=12) for x in bullets], bulletType='bullet', leftIndent=18)); bullets=[]
    if nums:
        story.append(ListFlowable([ListItem(Paragraph(inline(x),body), leftIndent=12) for x in nums], bulletType='1', start='1', leftIndent=20)); nums=[]
while i<len(lines):
    ln=lines[i].rstrip()
    if ln.startswith('```'):
        flush_lists()
        if in_code:
            story.append(Preformatted('\n'.join(codebuf),code)); codebuf=[]; in_code=False
        else: in_code=True
        i+=1; continue
    if in_code: codebuf.append(ln); i+=1; continue
    if not ln or ln=='---': flush_lists(); i+=1; continue
    if ln.startswith('# '): i+=1; continue
    if ln.startswith('## '):
        flush_lists()
        if ln.startswith('## Appendix A:'):
            story.append(PageBreak())
        story.append(Paragraph(inline(ln[3:]),h1)); i+=1; continue
    if ln.startswith('### '): flush_lists(); story.append(Paragraph(inline(ln[4:]),h2)); i+=1; continue
    if ln.startswith('> '): flush_lists(); story.append(Paragraph(inline(ln[2:]),quote)); i+=1; continue
    if ln.startswith('|') and i+1<len(lines) and lines[i+1].startswith('|'):
        flush_lists(); tb=[]
        while i<len(lines) and lines[i].startswith('|'): tb.append(lines[i]); i+=1
        t=parse_table(tb)
        if t: story.append(t); story.append(Spacer(1,7))
        continue
    m=re.match(r'^- (.+)$',ln)
    if m: bullets.append(m.group(1)); i+=1; continue
    m=re.match(r'^\d+\. (.+)$',ln)
    if m: nums.append(m.group(1)); i+=1; continue
    flush_lists()
    para=[ln]; i+=1
    while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,3} |---$|> |```|\|)',lines[i]) and not re.match(r'^(- |\d+\. )',lines[i]):
        para.append(lines[i].strip()); i+=1
    story.append(Paragraph(inline(' '.join(para)),body))
flush_lists()

OUT.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(OUT), pagesize=LETTER, rightMargin=0.72*inch,leftMargin=0.72*inch,topMargin=0.7*inch,bottomMargin=0.72*inch,title='Dog5pk Production Protocol Whitepaper v1.0',author='Dog5pk',subject='DPP v1.3 production standard for dependable human-AI collaboration')
doc.build(story,onFirstPage=lambda canvas, doc: None,onLaterPages=footer)
print(OUT)
