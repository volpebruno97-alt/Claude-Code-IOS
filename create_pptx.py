from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Define colors
PRIMARY_COLOR = RGBColor(0, 102, 204)  # Blue
SECONDARY_COLOR = RGBColor(51, 51, 51)  # Dark Gray
ACCENT_COLOR = RGBColor(255, 153, 0)  # Orange
WHITE = RGBColor(255, 255, 255)
LIGHT_GRAY = RGBColor(240, 240, 240)

def add_title_slide(prs, title, subtitle=""):
    """Add a title slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = PRIMARY_COLOR

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(54)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.alignment = PP_ALIGN.CENTER

    # Subtitle
    if subtitle:
        subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(2))
        subtitle_frame = subtitle_box.text_frame
        subtitle_frame.word_wrap = True
        p = subtitle_frame.paragraphs[0]
        p.text = subtitle
        p.font.size = Pt(28)
        p.font.color.rgb = ACCENT_COLOR
        p.alignment = PP_ALIGN.CENTER

def add_content_slide(prs, title, content_items):
    """Add a content slide with bullet points"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout

    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
    title_frame = title_box.text_frame
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    # Title underline
    line = slide.shapes.add_shape(1, Inches(0.5), Inches(1.4), Inches(9), Inches(0))
    line.line.color.rgb = ACCENT_COLOR
    line.line.width = Pt(3)

    # Content
    content_box = slide.shapes.add_textbox(Inches(1), Inches(1.8), Inches(8.5), Inches(5))
    text_frame = content_box.text_frame
    text_frame.word_wrap = True

    for i, item in enumerate(content_items):
        if i == 0:
            p = text_frame.paragraphs[0]
        else:
            p = text_frame.add_paragraph()

        p.text = item
        p.font.size = Pt(18)
        p.font.color.rgb = SECONDARY_COLOR
        p.level = 0
        p.space_before = Pt(6)
        p.space_after = Pt(6)

def add_two_column_slide(prs, title, left_title, left_items, right_title, right_items):
    """Add a two-column slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # Background
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE

    # Title
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(9), Inches(0.7))
    title_frame = title_box.text_frame
    p = title_frame.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_COLOR

    # Left column
    left_header = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(4.5), Inches(0.5))
    left_header_frame = left_header.text_frame
    p = left_header_frame.paragraphs[0]
    p.text = left_title
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR

    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.9), Inches(4.5), Inches(5))
    left_frame = left_box.text_frame
    left_frame.word_wrap = True

    for i, item in enumerate(left_items):
        if i == 0:
            p = left_frame.paragraphs[0]
        else:
            p = left_frame.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(16)
        p.font.color.rgb = SECONDARY_COLOR
        p.space_after = Pt(4)

    # Right column
    right_header = slide.shapes.add_textbox(Inches(5.2), Inches(1.3), Inches(4.3), Inches(0.5))
    right_header_frame = right_header.text_frame
    p = right_header_frame.paragraphs[0]
    p.text = right_title
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR

    right_box = slide.shapes.add_textbox(Inches(5.2), Inches(1.9), Inches(4.3), Inches(5))
    right_frame = right_box.text_frame
    right_frame.word_wrap = True

    for i, item in enumerate(right_items):
        if i == 0:
            p = right_frame.paragraphs[0]
        else:
            p = right_frame.add_paragraph()
        p.text = "• " + item
        p.font.size = Pt(16)
        p.font.color.rgb = SECONDARY_COLOR
        p.space_after = Pt(4)

# Slide 1: Title Slide
add_title_slide(prs, "Personal AI Data Center", "A Complete Guide for Raspberry Pi 5")

# Slide 2: Overview
add_content_slide(prs, "What is This System?", [
    "🏠 Your own private, secure AI assistant running locally",
    "📁 Complete file storage and management system",
    "🤖 AI that can access your files and help with any task",
    "💻 Beautiful web dashboard for easy interaction",
    "🔐 Full privacy - your data never leaves your home",
    "⚡ Powered by Raspberry Pi 5 - efficient and reliable"
])

# Slide 3: Key Features
add_two_column_slide(prs, "Core Capabilities",
    "AI Assistant Features",
    [
        "Answer questions & provide research",
        "Access and analyze your files",
        "Help with project planning",
        "Financial tracking & analysis",
        "Writing & content creation",
        "Code generation & explanation"
    ],
    "System Features",
    [
        "File storage & organization",
        "Web-based dashboard UI",
        "User authentication",
        "Conversation history",
        "Task scheduling",
        "System monitoring"
    ]
)

# Slide 4: System Architecture
add_content_slide(prs, "System Architecture", [
    "🍓 Raspberry Pi 5: Central hub running everything",
    "🗄️ File Storage: Local NAS-style storage system",
    "🤖 AI Engine: Claude AI with file access capabilities",
    "🌐 Web Interface: Beautiful dashboard for interaction",
    "📊 Database: PostgreSQL for persistent data",
    "🔌 APIs: RESTful API for all components"
])

# Slide 5: Hardware Requirements
add_two_column_slide(prs, "Hardware Setup",
    "Essential",
    [
        "Raspberry Pi 5 (8GB RAM minimum)",
        "Power supply (27W recommended)",
        "MicroSD card (128GB+)",
        "Network cable or WiFi",
        "Cooling case with heatsinks",
        "Monitor (initial setup only)"
    ],
    "Storage Options",
    [
        "External SSD (1TB-4TB recommended)",
        "USB 3.0 enclosure",
        "Network attached storage (optional)",
        "Backup drive (recommended)",
        "Multiple drives for redundancy",
        "Hot-swap capability"
    ]
)

# Slide 6: Software Stack
add_content_slide(prs, "Software Components", [
    "🐧 Operating System: Ubuntu Server for Raspberry Pi",
    "🐍 Backend: Python FastAPI (same as Claude bot)",
    "📊 Database: PostgreSQL for data storage",
    "🌐 Frontend: React-based web dashboard",
    "🤖 AI: Claude API with file access plugins",
    "🔐 Auth: JWT authentication & encryption"
])

# Slide 7: System Components Deep Dive
add_two_column_slide(prs, "System Components",
    "File Management",
    [
        "Automated file indexing",
        "Full-text search capability",
        "File categorization & tagging",
        "Access control & permissions",
        "Backup & recovery system",
        "Compression & archiving"
    ],
    "AI Integration",
    [
        "File reading & analysis",
        "Context-aware responses",
        "Multi-file processing",
        "Task automation",
        "Research capabilities",
        "Learning from interactions"
    ]
)

# Slide 8: Web Dashboard
add_content_slide(prs, "User Interface Features", [
    "💬 Real-time chat with your AI assistant",
    "📂 File browser and management",
    "📈 Dashboard with system stats",
    "📋 Task management & scheduling",
    "💰 Finance tracking module",
    "🔐 Settings & security management"
])

# Slide 9: Data Security
add_two_column_slide(prs, "Security & Privacy",
    "Protection Measures",
    [
        "End-to-end encryption",
        "Local-only data storage",
        "JWT token authentication",
        "HTTPS/SSL encryption",
        "Regular backups",
        "Access logging"
    ],
    "Privacy Benefits",
    [
        "No cloud uploads needed",
        "Complete data ownership",
        "GDPR compliant",
        "No third-party access",
        "Custom data policies",
        "Full audit trail"
    ]
)

# Slide 10: Implementation Phases
add_content_slide(prs, "Implementation Roadmap", [
    "Phase 1: Hardware setup & OS installation",
    "Phase 2: Backend API & file storage system",
    "Phase 3: AI integration with file access",
    "Phase 4: Web dashboard development",
    "Phase 5: Advanced features & automation",
    "Phase 6: Optimization & 24/7 deployment"
])

# Slide 11: Timeline & Effort
add_two_column_slide(prs, "Development Timeline",
    "Phase Breakdown",
    [
        "Phase 1: 1-2 hours",
        "Phase 2: 4-6 hours",
        "Phase 3: 3-4 hours",
        "Phase 4: 6-8 hours",
        "Phase 5: 4-5 hours",
        "Phase 6: 2-3 hours"
    ],
    "Parallel Work",
    [
        "Total: ~20-28 hours",
        "Can be done incrementally",
        "Start using after Phase 3",
        "Add features as you go",
        "Community plugins available",
        "No downtime needed"
    ]
)

# Slide 12: Cost Breakdown
add_content_slide(prs, "Budget Estimation", [
    "Raspberry Pi 5 (8GB): $80-100",
    "Power supply: $15-20",
    "Cooling case: $20-30",
    "MicroSD card (128GB): $20-25",
    "External SSD (2TB): $100-150",
    "Cables & accessories: $20-30",
    "Total Hardware: ~$280-380 (one-time)"
])

# Slide 13: Getting Started Steps
add_content_slide(prs, "Getting Started", [
    "1️⃣ Purchase Raspberry Pi 5 and accessories",
    "2️⃣ Install Ubuntu Server OS",
    "3️⃣ Set up networking & SSH access",
    "4️⃣ Install Docker for containerization",
    "5️⃣ Deploy backend services",
    "6️⃣ Configure storage system",
    "7️⃣ Build and deploy web dashboard"
])

# Slide 14: Advanced Features (Future)
add_two_column_slide(prs, "Future Enhancements",
    "Smart Features",
    [
        "Voice assistant integration",
        "Mobile app companion",
        "IoT device control",
        "Email integration",
        "Calendar scheduling",
        "Notification system"
    ],
    "Power Features",
    [
        "Code execution environment",
        "Web scraping capabilities",
        "Real-time data processing",
        "Machine learning models",
        "API integrations",
        "Plugin ecosystem"
    ]
)

# Slide 15: Comparison with Alternatives
add_two_column_slide(prs, "Why This Approach?",
    "vs Cloud Solutions",
    [
        "✅ Complete privacy",
        "✅ No recurring costs",
        "✅ Full control",
        "✅ Faster responses",
        "✅ No bandwidth limits",
        "✅ Custom features"
    ],
    "vs Generic Smart Home",
    [
        "✅ Powerful AI included",
        "✅ Works offline",
        "✅ Grows with you",
        "✅ Open source friendly",
        "✅ Better integration",
        "✅ Extendable"
    ]
)

# Slide 16: Resources & Support
add_content_slide(prs, "Resources You'll Need", [
    "📚 Raspberry Pi documentation: raspberry.org",
    "📖 Ubuntu Server guide: ubuntu.com",
    "🐳 Docker guide: docker.com",
    "🔗 Claude API docs: anthropic.com",
    "💬 Community support: forums & Discord",
    "⚙️ GitHub repositories: code & examples"
])

# Slide 17: Q&A / Next Steps
add_title_slide(prs, "Ready to Build?", "Let's create your personal AI data center!")

# Save presentation
output_path = "/home/user/Claude-Code-IOS/Personal_AI_Data_Center_Guide.pptx"
prs.save(output_path)
print(f"✅ PowerPoint created: {output_path}")
