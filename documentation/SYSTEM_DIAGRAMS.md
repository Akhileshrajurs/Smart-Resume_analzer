# System Architecture and Diagrams
## Smart AI Resume Analyzer - MCA Final Year Project

### 1. High-Level System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       CLIENT LAYER                               │
│               (Web Browser - Any Device)                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │ HTTP/HTTPS
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                  PRESENTATION LAYER                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Streamlit Web Framework                     │   │
│  │  • Page Routing  • UI Components  • Session Management  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  Home    │  │ Analyzer │  │ Builder  │  │Dashboard │      │
│  │  Page    │  │  Page    │  │  Page    │  │  Page    │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└──────────────────────┬──────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                  APPLICATION LAYER                               │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│  │    Resume      │  │    Resume      │  │   Dashboard    │   │
│  │   Analyzer     │  │   Builder      │  │   Manager      │   │
│  │  (Standard)    │  │ (Templates)    │  │  (Analytics)   │   │
│  └────────────────┘  └────────────────┘  └────────────────┘   │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐   │
│  │  Job Search    │  │   Feedback     │  │    Admin       │   │
│  │  (Scraping)    │  │   System       │  │  Management    │   │
│  └────────────────┘  └────────────────┘  └────────────────┘   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                    ML/AI LAYER                                   │
│                                                                  │
│  ┌───────────────────────────────────────────────────────┐     │
│  │        Custom ML ATS Scorer (NEW - YOUR WORK)         │     │
│  │                                                        │     │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │     │
│  │  │   TF-IDF     │  │   Cosine     │  │   Skills   │ │     │
│  │  │Vectorization │  │  Similarity  │  │ Extraction │ │     │
│  │  └──────────────┘  └──────────────┘  └────────────┘ │     │
│  │                                                        │     │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │     │
│  │  │   Section    │  │   Format     │  │   Action   │ │     │
│  │  │   Analysis   │  │   Scoring    │  │    Verbs   │ │     │
│  │  └──────────────┘  └──────────────┘  └────────────┘ │     │
│  └───────────────────────────────────────────────────────┘     │
│                           │                                     │
│                           │ Optional Enhancement                │
│                           ▼                                     │
│  ┌───────────────────────────────────────────────────────┐     │
│  │          Google Gemini AI (External API)              │     │
│  │      • Advanced Analysis  • Content Generation        │     │
│  └───────────────────────────────────────────────────────┘     │
│                                                                  │
│  ┌───────────────────────────────────────────────────────┐     │
│  │              NLP Processing Layer                     │     │
│  │   • spaCy  • NLTK  • Pattern Matching  • NER         │     │
│  └───────────────────────────────────────────────────────┘     │
└──────────────────────┬──────────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────────┐
│                    DATA LAYER                                    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              SQLite Database (Local)                   │    │
│  │                                                         │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐  │    │
│  │  │ resume_data  │  │resume_skills │  │  resume_   │  │    │
│  │  │              │  │              │  │  analysis  │  │    │
│  │  └──────────────┘  └──────────────┘  └────────────┘  │    │
│  │                                                         │    │
│  │  ┌──────────────┐  ┌──────────────┐                   │    │
│  │  │ admin_logs   │  │    admin     │                   │    │
│  │  └──────────────┘  └──────────────┘                   │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              File Processing Layer                     │    │
│  │                                                         │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐  │    │
│  │  │ PDF Parser   │  │  OCR Engine  │  │   DOCX     │  │    │
│  │  │(pdfplumber)  │  │(Tesseract)   │  │  Parser    │  │    │
│  │  └──────────────┘  └──────────────┘  └────────────┘  │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │           Web Scraping Layer (Selenium)                │    │
│  │     • LinkedIn Jobs  • Job Portals  • Companies       │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Database Entity-Relationship Diagram

```
┌─────────────────────────────────────────┐
│           resume_data                   │
│─────────────────────────────────────────│
│ ⊕ id (PK)                    INTEGER   │◄────────┐
│   name                       TEXT      │         │
│   email                      TEXT      │         │
│   phone                      TEXT      │         │
│   linkedin                   TEXT      │         │
│   github                     TEXT      │         │
│   portfolio                  TEXT      │         │
│   summary                    TEXT      │         │
│   target_role                TEXT      │         │
│   target_category            TEXT      │         │
│   education                  TEXT      │         │
│   experience                 TEXT      │         │
│   projects                   TEXT      │         │
│   skills                     TEXT      │         │
│   template                   TEXT      │         │
│   created_at                 TIMESTAMP │         │
└─────────────────────────────────────────┘         │
                                                     │
                    ┌────────────────────────────────┤
                    │                                │
                    │ 1:N                         1:N│
                    │                                │
┌───────────────────▼─────────────────┐ ┌───────────▼───────────────────┐
│        resume_skills                │ │     resume_analysis           │
│─────────────────────────────────────│ │───────────────────────────────│
│ ⊕ id (PK)              INTEGER     │ │ ⊕ id (PK)          INTEGER   │
│ ⊗ resume_id (FK)       INTEGER     │ │ ⊗ resume_id (FK)   INTEGER   │
│   skill_name            TEXT        │ │   ats_score         REAL      │
│   skill_category        TEXT        │ │   keyword_match     REAL      │
│   proficiency_score     REAL        │ │   format_score      REAL      │
│   created_at            TIMESTAMP   │ │   section_score     REAL      │
└─────────────────────────────────────┘ │   missing_skills    TEXT      │
                                        │   recommendations   TEXT      │
                                        │   created_at        TIMESTAMP │
                                        └───────────────────────────────┘

┌─────────────────────────────────────────┐
│              admin                      │
│─────────────────────────────────────────│
│ ⊕ id (PK)                    INTEGER   │
│   email                      TEXT      │
│   password                   TEXT      │
│   created_at                 TIMESTAMP │
└─────────────────────────────────────────┘
                   │
                   │ 1:N
                   │
┌──────────────────▼──────────────────────┐
│           admin_logs                    │
│─────────────────────────────────────────│
│ ⊕ id (PK)                    INTEGER   │
│   admin_email                TEXT      │
│   action                     TEXT      │
│   timestamp                  TIMESTAMP │
└─────────────────────────────────────────┘

Legend:
⊕ Primary Key (PK)
⊗ Foreign Key (FK)
1:N One-to-Many Relationship
```

### 3. Custom ML Scorer Algorithm Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                     INPUT: Resume Text                          │
│              + Job Description (Optional)                       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PREPROCESSING PHASE                           │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Lowercase    │→ │  Remove      │→ │  Tokenize    │         │
│  │ Conversion   │  │  Special     │  │  & Normalize │         │
│  └──────────────┘  │  Characters  │  └──────────────┘         │
│                    └──────────────┘                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              FEATURE EXTRACTION PHASE                           │
│                                                                  │
│  ┌──────────────────────────────────────────────────────┐      │
│  │          Skills Extraction                           │      │
│  │  • Pattern Matching (100+ skills)                    │      │
│  │  • Named Entity Recognition (spaCy)                  │      │
│  │  • Category Assignment (7 categories)                │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │         Section Detection                            │      │
│  │  • Experience  • Education  • Skills                 │      │
│  │  • Summary    • Projects                             │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │         Action Verb Analysis                         │      │
│  │  • Strong verb identification                        │      │
│  │  • Usage frequency                                   │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │         Format Quality Check                         │      │
│  │  • Length  • Contact info  • Structure               │      │
│  │  • Bullet points  • Quantifiable metrics             │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │     TF-IDF Vectorization (if job desc provided)     │      │
│  │  • Create document vectors                           │      │
│  │  • Calculate term weights                            │      │
│  └──────────────────────────────────────────────────────┘      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   SCORING PHASE                                 │
│                                                                  │
│  ┌──────────────────────────────────────────────────────┐      │
│  │  Component 1: Skills Score (25% weight)             │      │
│  │  Score = min(100, (total_skills / 15) × 100)        │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │  Component 2: Section Completeness (20% weight)     │      │
│  │  Score = (found_sections / total_sections) × 100    │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │  Component 3: Format Quality (20% weight)           │      │
│  │  Score = Σ(format_factors) max 100                  │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │  Component 4: Action Verbs (15% weight)             │      │
│  │  Score = min(100, (unique_verbs / 10) × 100)        │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│  ┌──────────────────────────▼──────────────────────────┐      │
│  │  Component 5: Keyword Match (20% weight)            │      │
│  │  Score = cosine_similarity(resume, job) × 100       │      │
│  │  (Only if job description provided)                  │      │
│  └──────────────────────────────────────────────────────┘      │
│                             │                                    │
│                             ▼                                    │
│  ┌──────────────────────────────────────────────────────┐      │
│  │        Weighted Aggregation                          │      │
│  │                                                       │      │
│  │  Overall_Score = Σ(component_score × weight)        │      │
│  │                                                       │      │
│  │  = (0.25 × skills) + (0.20 × sections) +            │      │
│  │    (0.20 × format) + (0.15 × verbs) +               │      │
│  │    (0.20 × keyword_match)                            │      │
│  └──────────────────────────────────────────────────────┘      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              RECOMMENDATION GENERATION                          │
│                                                                  │
│  IF score < threshold THEN add recommendation                   │
│  • Low skills → "Add more technical skills"                     │
│  • Missing sections → "Add [section_name]"                      │
│  • Poor format → "Improve formatting"                           │
│  • Few action verbs → "Use more action verbs"                   │
│  • Low keyword match → "Align with job description"             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       OUTPUT                                    │
│                                                                  │
│  • Overall Score (0-100)                                        │
│  • Component Scores (5 components)                              │
│  • Skills Found (categorized)                                   │
│  • Strengths (list)                                             │
│  • Weaknesses (list)                                            │
│  • Recommendations (actionable items)                           │
│  • Assessment (Excellent/Good/Fair/Needs Work)                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4. User Flow Diagram

```
                      ┌──────────────┐
                      │  User Opens  │
                      │     App      │
                      └──────┬───────┘
                             │
                             ▼
                      ┌──────────────┐
                      │  Home Page   │
                      │  (Landing)   │
                      └──────┬───────┘
                             │
                ┌────────────┼────────────┬────────────┐
                │            │            │            │
        ┌───────▼──────┐ ┌──▼────────┐ ┌─▼─────────┐ │
        │   Resume     │ │  Resume   │ │   Job     │ │
        │   Analyzer   │ │  Builder  │ │  Search   │ │
        └───────┬──────┘ └──┬────────┘ └─┬─────────┘ │
                │            │            │            │
        ┌───────▼──────┐     │            │            │
        │ Upload Resume│     │            │            │
        │  (PDF/DOCX)  │     │            │            │
        └───────┬──────┘     │            │            │
                │            │            │            │
        ┌───────▼──────┐     │            │            │
        │  Select Role │     │            │            │
        │  (Optional)  │     │            │            │
        └───────┬──────┘     │            │            │
                │            │            │            │
        ┌───────▼──────────┐ │            │            │
        │  Add Job Desc.   │ │            │            │
        │   (Optional)     │ │            │            │
        └───────┬──────────┘ │            │            │
                │            │            │            │
                ▼            │            │            │
        ┌──────────────────┐ │            │            │
        │  Custom ML       │ │            │            │
        │  Processing      │ │            │            │
        │  (3-5 seconds)   │ │            │            │
        └───────┬──────────┘ │            │            │
                │            │            │            │
                ▼            │            │            │
        ┌──────────────────┐ │            │            │
        │  Display Results │ │            │            │
        │  • Score         │ │            │            │
        │  • Breakdown     │ │            │            │
        │  • Recommendations│ │            │            │
        └───────┬──────────┘ │            │            │
                │            │            │            │
                ▼            ▼            ▼            ▼
        ┌────────────────────────────────────────────────┐
        │          Download Report / Save Data            │
        └────────────────────────────────────────────────┘
```

### 5. Module Interaction Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                          app.py                                  │
│                     (Main Controller)                            │
└────┬─────────┬─────────┬─────────┬──────────┬─────────┬─────────┘
     │         │         │         │          │         │
     │         │         │         │          │         │
     ▼         ▼         ▼         ▼          ▼         ▼
┌─────────┐ ┌──────┐ ┌────────┐ ┌────────┐ ┌─────┐ ┌──────────┐
│ Resume  │ │Resume│ │Dashboard│ │  Job   │ │Admin│ │ Feedback │
│Analyzer │ │Builder│ │ Manager │ │ Search │ │Panel│ │  System  │
└────┬────┘ └───┬──┘ └────┬────┘ └────┬───┘ └──┬──┘ └────┬─────┘
     │          │         │           │        │        │
     │          │         │           │        │        │
     ▼          ▼         │           ▼        │        │
┌──────────────────┐     │      ┌───────────┐ │        │
│ Custom ATS       │     │      │ LinkedIn  │ │        │
│ Scorer (ML)      │◄────┘      │ Scraper   │ │        │
│ [YOUR WORK]      │            └───────────┘ │        │
└────────┬─────────┘                          │        │
         │                                    │        │
         │                                    │        │
         ▼                                    ▼        ▼
┌──────────────────┐                    ┌─────────────────┐
│  NLP Processing  │                    │    Database     │
│  • spaCy         │                    │    (SQLite)     │
│  • NLTK          │────────────────────►                 │
│  • TF-IDF        │                    │  • resume_data  │
└──────────────────┘                    │  • admin_logs   │
                                        └─────────────────┘
```

### 6. TF-IDF and Cosine Similarity Visualization

```
Resume Document Vector Space:

                  Dimension 2 (e.g., "Python")
                            ▲
                            │
                            │    ● Resume Vector
                            │   ╱│
                            │  ╱ │
                            │ ╱  │
                            │╱   │
                            ╱    │
            cosine(θ)      ╱θ    │
            = similarity  ╱      │
                        ╱        │
                       ●─────────┼────────────►
                 Job Desc        │         Dimension 1
                  Vector         │         (e.g., "Java")
                                │
                                │
                                ▼

Similarity Score = cos(θ) = (A · B) / (||A|| × ||B||)

Where:
- A = TF-IDF vector of resume
- B = TF-IDF vector of job description
- θ = Angle between vectors
- Smaller angle = Higher similarity = Better match
```

### 7. Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT ENVIRONMENT                       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Local Machine (Windows/Mac/Linux)                     │    │
│  │                                                         │    │
│  │  • Python 3.8+                                         │    │
│  │  • Virtual Environment                                  │    │
│  │  • Git Version Control                                  │    │
│  │  • VS Code / PyCharm                                    │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                             │
                             │ git push
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PRODUCTION ENVIRONMENT                         │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │         Streamlit Cloud / AWS / Azure                  │    │
│  │                                                         │    │
│  │  ┌──────────────────────────────────────────────┐     │    │
│  │  │     Web Server (Streamlit Server)            │     │    │
│  │  │     Port: 8501                               │     │    │
│  │  └──────────────────────────────────────────────┘     │    │
│  │                       │                                │    │
│  │  ┌────────────────────▼──────────────────────────┐    │    │
│  │  │     Application Container                     │    │    │
│  │  │     • Python Runtime                          │    │    │
│  │  │     • Dependencies (requirements.txt)         │    │    │
│  │  │     • ML Models                                │    │    │
│  │  └────────────────────┬──────────────────────────┘    │    │
│  │                       │                                │    │
│  │  ┌────────────────────▼──────────────────────────┐    │    │
│  │  │     Data Storage                              │    │    │
│  │  │     • SQLite Database (Local)                 │    │    │
│  │  │     • Uploaded Files (Temp)                   │    │    │
│  │  └───────────────────────────────────────────────┘    │    │
│  │                                                         │    │
│  │  ┌──────────────────────────────────────────────┐     │    │
│  │  │     External Services                         │     │    │
│  │  │     • Google Gemini API (Optional)           │     │    │
│  │  │     • Selenium Grid (Job Scraping)           │     │    │
│  │  └──────────────────────────────────────────────┘     │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
                             │
                             │ HTTPS
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         END USERS                                │
│            Access via: https://your-app.streamlit.app           │
└─────────────────────────────────────────────────────────────────┘
```

### 8. Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                              │
│                                                                  │
│  Layer 1: Authentication                                        │
│  ┌──────────────────────────────────────────────────────┐      │
│  │  • Admin Login (Email + Password)                    │      │
│  │  • Session State Management                          │      │
│  │  • Password Hashing                                   │      │
│  └──────────────────────────────────────────────────────┘      │
│                          │                                       │
│  Layer 2: Authorization                                         │
│  ┌──────────────────────▼──────────────────────────────┐      │
│  │  • Role-Based Access Control                         │      │
│  │  • Admin-only features                               │      │
│  │  • User session validation                            │      │
│  └──────────────────────────────────────────────────────┘      │
│                          │                                       │
│  Layer 3: Data Protection                                       │
│  ┌──────────────────────▼──────────────────────────────┐      │
│  │  • Environment Variables (.env)                      │      │
│  │  • API Key Protection                                │      │
│  │  • SQL Injection Prevention                          │      │
│  │  • XSS Protection                                    │      │
│  └──────────────────────────────────────────────────────┘      │
│                          │                                       │
│  Layer 4: Privacy                                               │
│  ┌──────────────────────▼──────────────────────────────┐      │
│  │  • Local ML Processing (no data sent to cloud)      │      │
│  │  • Temporary file cleanup                            │      │
│  │  • Optional API usage                                │      │
│  └──────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

---

**Note:** These diagrams provide visual representation of system architecture, database design, algorithm flow, and deployment structure for the Smart AI Resume Analyzer project.

For implementation details, refer to TECHNICAL_DOCUMENTATION.md  
For research context, refer to RESEARCH_ANALYSIS.md  
For contribution details, refer to ORIGINALITY_CONTRIBUTIONS.md

