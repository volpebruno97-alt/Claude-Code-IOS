from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define colors
PRIMARY = RGBColor(0, 102, 204)  # Blue
SECONDARY = RGBColor(51, 51, 51)  # Dark gray
ACCENT = RGBColor(255, 153, 0)  # Orange
SUCCESS = RGBColor(76, 175, 80)  # Green
WARNING = RGBColor(255, 152, 0)  # Amber
DANGER = RGBColor(244, 67, 54)  # Red
WHITE = RGBColor(255, 255, 255)
LIGHT_BG = RGBColor(245, 245, 245)

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = PRIMARY

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(60)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(2))
        tf = sub_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(32)
        p.font.color.rgb = ACCENT
        p.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, items, layout_type="bullets"):
    """Add a content slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Title bar
    title_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY
    title_shape.line.color.rgb = PRIMARY

    title_frame = title_shape.text_frame
    title_frame.margin_bottom = Inches(0.1)
    title_frame.margin_left = Inches(0.3)
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Content
    if layout_type == "bullets":
        content_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(8.4), Inches(5.5))
        tf = content_box.text_frame
        tf.word_wrap = True

        for i, item in enumerate(items):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = item
            p.font.size = Pt(20)
            p.font.color.rgb = SECONDARY
            p.space_after = Pt(12)
            p.level = 0

def add_two_column_slide(prs, title, left_items, right_items, left_title="", right_title=""):
    """Add two-column slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Title bar
    title_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.9))
    title_shape.fill.solid()
    title_shape.fill.fore_color.rgb = PRIMARY
    title_shape.line.color.rgb = PRIMARY
    tf = title_shape.text_frame
    tf.margin_left = Inches(0.3)
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Left column title
    if left_title:
        left_title_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.1), Inches(4.5), Inches(0.4))
        tf = left_title_box.text_frame
        p = tf.paragraphs[0]
        p.text = left_title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT

    # Left content
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.6), Inches(4.5), Inches(5.5))
    tf = left_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(left_items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = "✓ " + item
        p.font.size = Pt(16)
        p.font.color.rgb = SECONDARY
        p.space_after = Pt(8)

    # Right column title
    if right_title:
        right_title_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.1), Inches(4.3), Inches(0.4))
        tf = right_title_box.text_frame
        p = tf.paragraphs[0]
        p.text = right_title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = ACCENT

    # Right content
    right_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.6), Inches(4.3), Inches(5.5))
    tf = right_box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(right_items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = "✓ " + item
        p.font.size = Pt(16)
        p.font.color.rgb = SECONDARY
        p.space_after = Pt(8)

def add_phase_slide(prs, phase_num, phase_name, duration, tasks, deliverables):
    """Add a phase detail slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Phase header with color
    header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(1.2))
    header.fill.solid()
    header.fill.fore_color.rgb = PRIMARY
    header.line.color.rgb = PRIMARY

    tf = header.text_frame
    tf.margin_left = Inches(0.3)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = f"Phase {phase_num}: {phase_name} ({duration})"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = WHITE

    # Tasks section
    tasks_title = slide.shapes.add_textbox(Inches(0.5), Inches(1.4), Inches(9), Inches(0.3))
    tf = tasks_title.text_frame
    p = tf.paragraphs[0]
    p.text = "📋 Key Tasks"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT

    tasks_box = slide.shapes.add_textbox(Inches(0.7), Inches(1.8), Inches(4.5), Inches(3))
    tf = tasks_box.text_frame
    tf.word_wrap = True
    for i, task in enumerate(tasks[:4]):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = "• " + task
        p.font.size = Pt(14)
        p.font.color.rgb = SECONDARY
        p.space_after = Pt(6)

    # Deliverables section
    deliv_title = slide.shapes.add_textbox(Inches(5.3), Inches(1.4), Inches(4.2), Inches(0.3))
    tf = deliv_title.text_frame
    p = tf.paragraphs[0]
    p.text = "✅ Deliverables"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = SUCCESS

    deliv_box = slide.shapes.add_textbox(Inches(5.3), Inches(1.8), Inches(4.2), Inches(3))
    tf = deliv_box.text_frame
    tf.word_wrap = True
    for i, deliv in enumerate(deliverables):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = "✓ " + deliv
        p.font.size = Pt(14)
        p.font.color.rgb = SECONDARY
        p.space_after = Pt(6)

# ========================
# SLIDE 1: TITLE SLIDE
# ========================
add_title_slide(prs, "Personal AI Data Center", "Complete Professional Workflow Guide")

# ========================
# SLIDE 2: PROJECT OVERVIEW
# ========================
add_content_slide(prs, "📊 Project Overview", [
    "🏠 Your own private AI assistant running 24/7 on Raspberry Pi 5",
    "💾 Complete file storage and management system (2TB)",
    "🤖 Claude AI integrated with file access capabilities",
    "🌐 Beautiful web dashboard for easy interaction",
    "🔐 100% private - your data never leaves your home",
    "⏱️ Timeline: 4-6 weeks | Effort: 35-47 hours"
])

# ========================
# SLIDE 3: SYSTEM ARCHITECTURE
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
bg = slide.background
fill = bg.fill
fill.solid()
fill.fore_color.rgb = WHITE

title_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.9))
title_shape.fill.solid()
title_shape.fill.fore_color.rgb = PRIMARY
title_shape.line.color.rgb = PRIMARY
tf = title_shape.text_frame
tf.margin_left = Inches(0.3)
p = tf.paragraphs[0]
p.text = "🏗️ System Architecture"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = WHITE

# Layer 1
layer1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(1.2), Inches(8), Inches(0.8))
layer1.fill.solid()
layer1.fill.fore_color.rgb = PRIMARY
tf = layer1.text_frame
p = tf.paragraphs[0]
p.text = "🖥️ User Layer: Web Dashboard | Telegram Bot | Mobile App"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Arrow
arrow1 = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(4.8), Inches(2.1), Inches(0.4), Inches(0.3))
arrow1.fill.solid()
arrow1.fill.fore_color.rgb = ACCENT

# Layer 2
layer2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(2.5), Inches(8), Inches(0.8))
layer2.fill.solid()
layer2.fill.fore_color.rgb = ACCENT
tf = layer2.text_frame
p = tf.paragraphs[0]
p.text = "⚙️ API Layer: FastAPI Backend | Claude AI Integration"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Arrow
arrow2 = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(4.8), Inches(3.4), Inches(0.4), Inches(0.3))
arrow2.fill.solid()
arrow2.fill.fore_color.rgb = ACCENT

# Layer 3
layer3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(3.8), Inches(8), Inches(0.8))
layer3.fill.solid()
layer3.fill.fore_color.rgb = SUCCESS
tf = layer3.text_frame
p = tf.paragraphs[0]
p.text = "📁 Data Layer: PostgreSQL Database | 2TB File Storage"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# Arrow
arrow3 = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(4.8), Inches(4.7), Inches(0.4), Inches(0.3))
arrow3.fill.solid()
arrow3.fill.fore_color.rgb = ACCENT

# Layer 4
layer4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1), Inches(5.1), Inches(8), Inches(0.8))
layer4.fill.solid()
layer4.fill.fore_color.rgb = WARNING
tf = layer4.text_frame
p = tf.paragraphs[0]
p.text = "🍓 Infrastructure: Raspberry Pi 5 | Ubuntu Server | Docker"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = WHITE
p.alignment = PP_ALIGN.CENTER

# ========================
# SLIDE 4: TIMELINE OVERVIEW
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
bg = slide.background
fill = bg.fill
fill.solid()
fill.fore_color.rgb = WHITE

title_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.9))
title_shape.fill.solid()
title_shape.fill.fore_color.rgb = PRIMARY
title_shape.line.color.rgb = PRIMARY
tf = title_shape.text_frame
tf.margin_left = Inches(0.3)
p = tf.paragraphs[0]
p.text = "📅 Project Timeline"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = WHITE

# Week 1
week1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.3), Inches(1.8), Inches(5.5))
week1.fill.solid()
week1.fill.fore_color.rgb = RGBColor(200, 230, 255)
tf = week1.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Week 1\n\nHardware Setup\n&\nDatabase"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = PRIMARY
p.alignment = PP_ALIGN.CENTER

# Week 2
week2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.6), Inches(1.3), Inches(1.8), Inches(5.5))
week2.fill.solid()
week2.fill.fore_color.rgb = RGBColor(255, 230, 200)
tf = week2.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Week 2\n\nBackend\n&\nAI"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = ACCENT
p.alignment = PP_ALIGN.CENTER

# Week 3
week3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.7), Inches(1.3), Inches(1.8), Inches(5.5))
week3.fill.solid()
week3.fill.fore_color.rgb = RGBColor(200, 255, 200)
tf = week3.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Week 3\n\nDashboard\n&\nSecurity"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = SUCCESS
p.alignment = PP_ALIGN.CENTER

# Week 4
week4 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.3), Inches(1.8), Inches(5.5))
week4.fill.solid()
week4.fill.fore_color.rgb = RGBColor(255, 255, 200)
tf = week4.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Week 4\n\nOptimization"
p.font.size = Pt(14)
p.font.bold = True
p.font.color.rgb = RGBColor(200, 150, 0)
p.alignment = PP_ALIGN.CENTER

# Week 5-6
week5 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.3), Inches(1.4), Inches(5.5))
week5.fill.solid()
week5.fill.fore_color.rgb = RGBColor(255, 200, 200)
tf = week5.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Week 5-6\n\nTesting\n&\nGo-Live"
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = DANGER
p.alignment = PP_ALIGN.CENTER

# ========================
# PHASE SLIDES
# ========================

# Phase 1
add_phase_slide(prs, 1, "Hardware Setup & OS Installation", "1-2 hours",
    ["Assemble Raspberry Pi with cooling case", "Flash Ubuntu Server to SD card", "Initial system configuration", "SSH access setup"],
    ["Running Ubuntu Server", "SSH connectivity", "Network connection"])

# Phase 2
add_phase_slide(prs, 2, "Storage & Database Setup", "2-3 hours",
    ["Connect 2TB SSD via Inateck enclosure", "Format and mount storage", "Configure auto-mount", "Install & setup PostgreSQL"],
    ["2TB SSD mounted", "PostgreSQL running", "Database created"])

# Phase 3
add_phase_slide(prs, 3, "Backend API & Core Services", "4-6 hours",
    ["Deploy FastAPI backend", "Create file management endpoints", "Build database models", "Configure auto-restart service"],
    ["API running on port 8000", "File endpoints working", "Database integration"])

# Phase 4
add_phase_slide(prs, 4, "AI Integration", "3-4 hours",
    ["Integrate Claude API", "Implement file reading", "Add conversation history", "Enable streaming responses"],
    ["Claude AI responding", "File access working", "Conversation persistence"])

# Phase 5
add_phase_slide(prs, 5, "Web Dashboard Development", "6-8 hours",
    ["Create React dashboard", "Build chat interface", "Add file browser", "Implement real-time updates"],
    ["Dashboard at port 3000", "Chat working", "Mobile responsive"])

# Phase 6
add_phase_slide(prs, 6, "Authentication & Security", "3-4 hours",
    ["Implement JWT authentication", "Add user registration/login", "Configure HTTPS/SSL", "Add rate limiting"],
    ["User authentication", "HTTPS enabled", "Security audit passed"])

# Phase 7
add_phase_slide(prs, 7, "Advanced Features", "4-5 hours",
    ["Full-text search", "Conversation export", "Backup system", "Project management"],
    ["Search functional", "Export working", "Backups running"])

# Phase 8
add_phase_slide(prs, 8, "Optimization & Deployment", "3-4 hours",
    ["Performance testing", "Database optimization", "Memory optimization", "Setup monitoring"],
    ["99.9% uptime", "Response < 2s", "Monitoring active"])

# Phase 9
add_phase_slide(prs, 9, "Testing & Quality Assurance", "4-5 hours",
    ["Unit testing", "Integration testing", "Security testing", "Load testing"],
    ["All tests passing", "Zero critical bugs", "Security approved"])

# Phase 10
add_phase_slide(prs, 10, "Documentation & Training", "2-3 hours",
    ["Create user guides", "Write admin manual", "Document API", "Build knowledge base"],
    ["Complete docs", "Video tutorials", "Troubleshooting guide"])

# Phase 11
add_phase_slide(prs, 11, "Deployment & Go-Live", "2-3 hours",
    ["Final system checks", "Database backup", "Deploy to production", "Post-launch verification"],
    ["System live", "Monitoring active", "Support ready"])

# ========================
# SLIDE: EFFORT BREAKDOWN
# ========================
slide = prs.slides.add_slide(prs.slide_layouts[6])
bg = slide.background
fill = bg.fill
fill.solid()
fill.fore_color.rgb = WHITE

title_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(10), Inches(0.9))
title_shape.fill.solid()
title_shape.fill.fore_color.rgb = PRIMARY
title_shape.line.color.rgb = PRIMARY
tf = title_shape.text_frame
tf.margin_left = Inches(0.3)
p = tf.paragraphs[0]
p.text = "⏱️ Time & Effort Breakdown"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = WHITE

# Create effort table
effort_data = [
    ("Phase", "Duration", "Effort"),
    ("1", "1-2h", "Low"),
    ("2", "2-3h", "Medium"),
    ("3", "4-6h", "High"),
    ("4", "3-4h", "High"),
    ("5", "6-8h", "High"),
    ("6", "3-4h", "High"),
    ("7", "4-5h", "Medium"),
    ("8", "3-4h", "Medium"),
    ("9", "4-5h", "Medium"),
    ("10", "2-3h", "Low"),
    ("11", "2-3h", "Medium"),
]

row_height = 0.35
col1_left = 1
col1_width = 1.5
col2_left = col1_left + col1_width + 0.3
col2_width = 2
col3_left = col2_left + col2_width + 0.3
col3_width = 2

for idx, (phase, duration, effort) in enumerate(effort_data):
    y_pos = 1.2 + (idx * row_height)

    # Phase
    box = slide.shapes.add_textbox(Inches(col1_left), Inches(y_pos), Inches(col1_width), Inches(row_height))
    tf = box.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = phase
    p.font.size = Pt(14)
    p.font.bold = (idx == 0)
    p.font.color.rgb = WHITE if idx == 0 else SECONDARY

    if idx == 0:
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(col1_left), Inches(y_pos), Inches(col1_width), Inches(row_height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = PRIMARY
        shape.line.color.rgb = PRIMARY
        p.alignment = PP_ALIGN.CENTER

    # Duration
    box = slide.shapes.add_textbox(Inches(col2_left), Inches(y_pos), Inches(col2_width), Inches(row_height))
    tf = box.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = duration
    p.font.size = Pt(14)
    p.font.bold = (idx == 0)
    p.font.color.rgb = WHITE if idx == 0 else SECONDARY

    if idx == 0:
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(col2_left), Inches(y_pos), Inches(col2_width), Inches(row_height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = PRIMARY
        shape.line.color.rgb = PRIMARY
        p.alignment = PP_ALIGN.CENTER

    # Effort
    box = slide.shapes.add_textbox(Inches(col3_left), Inches(y_pos), Inches(col3_width), Inches(row_height))
    tf = box.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = effort
    p.font.size = Pt(14)
    p.font.bold = (idx == 0)
    p.font.color.rgb = WHITE if idx == 0 else SECONDARY

    if idx == 0:
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(col3_left), Inches(y_pos), Inches(col3_width), Inches(row_height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = PRIMARY
        shape.line.color.rgb = PRIMARY
        p.alignment = PP_ALIGN.CENTER

# Total
total_y = 1.2 + (len(effort_data) * row_height) + 0.3
total_box = slide.shapes.add_textbox(Inches(1), Inches(total_y), Inches(7.5), Inches(0.5))
tf = total_box.text_frame
p = tf.paragraphs[0]
p.text = "TOTAL: 35-47 HOURS OVER 4-6 WEEKS"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = SUCCESS
p.alignment = PP_ALIGN.CENTER

# ========================
# SLIDE: SUCCESS METRICS
# ========================
add_two_column_slide(prs, "📈 Success Metrics",
    ["Uptime: > 99.9%", "Response time: < 2s", "Memory usage: < 4GB", "Disk usage: < 80%"],
    ["Chat response: < 5s", "File upload: < 10s", "Dashboard load: < 3s", "Mobile: 100% responsive"],
    "System Performance", "User Experience")

# ========================
# SLIDE: SECURITY & PRIVACY
# ========================
add_two_column_slide(prs, "🔐 Security & Privacy",
    ["End-to-end encryption", "Local-only data", "JWT authentication", "HTTPS/SSL enabled"],
    ["Access logging", "Daily backups", "Permission control", "Audit trail"],
    "Protection", "Monitoring")

# ========================
# SLIDE: LAUNCH CHECKLIST
# ========================
add_content_slide(prs, "✅ Launch Checklist", [
    "Pre-Launch (1 week before): All phases 80%+ complete, security audit passed, monitoring ready",
    "Launch Day: Database backup, monitoring active, support team ready, deployment scripts tested",
    "Post-Launch (24 hours): Verify stability, collect feedback, check performance, run team debrief"
])

# ========================
# SLIDE: GETTING STARTED
# ========================
add_content_slide(prs, "🚀 Getting Started", [
    "1️⃣ Order hardware: Raspberry Pi 5, SSD, PSU, cables (£130)",
    "2️⃣ Wait for delivery: 3-5 business days",
    "3️⃣ Start Phase 1: Hardware assembly and OS installation",
    "4️⃣ Follow the workflow: Complete each phase systematically",
    "5️⃣ Go live: Deploy and start using your AI data center!"
])

# ========================
# SLIDE: SUPPORT & RESOURCES
# ========================
add_content_slide(prs, "📚 Support & Resources", [
    "📖 Complete documentation included in project",
    "🐳 Docker compose files for easy deployment",
    "🔧 Troubleshooting guides for common issues",
    "💬 Step-by-step implementation guides",
    "🎯 Pre-configured scripts and templates"
])

# ========================
# SLIDE: FINAL SLIDE
# ========================
add_title_slide(prs, "Ready to Build?", "Let's create your personal AI data center!")

# Save
output_path = "/home/user/Claude-Code-IOS/Personal_AI_Data_Center_Workflow.pptx"
prs.save(output_path)
print(f"✅ Professional Workflow PowerPoint created: {output_path}")
print(f"📊 Total slides: {len(prs.slides)}")
