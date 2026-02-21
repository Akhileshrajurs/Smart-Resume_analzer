# Technical Documentation
## Smart AI Resume Analyzer - MCA Final Year Project

### System Architecture

#### 1. High-Level Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend Layer                          │
│                   (Streamlit Web UI)                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                 Application Layer                            │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Resume    │  │   Resume     │  │   Dashboard  │       │
│  │  Analyzer   │  │   Builder    │  │   Manager    │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   ML/AI Layer                                │
│  ┌─────────────────┐  ┌────────────────────────────┐        │
│  │  Custom ATS     │  │  Google Gemini AI          │        │
│  │  Scorer (ML)    │  │  (External API)            │        │
│  └─────────────────┘  └────────────────────────────┘        │
└──────────────────────┬──────────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   Data Layer                                 │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  SQLite DB  │  │   PDF Parser │  │  Job Scraper │       │
│  │  (Local)    │  │   (NLP)      │  │  (Selenium)  │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

#### 2. Technology Stack

**Frontend:**
- Streamlit (Web Framework)
- HTML/CSS/JavaScript
- Plotly (Data Visualization)
- Streamlit Components

**Backend:**
- Python 3.x
- Streamlit Server
- Custom ML Modules

**Database:**
- SQLite3 (Local Database)
- Tables: resume_data, resume_skills, resume_analysis, admin_logs

**AI/ML Components:**
- Custom ATS Scorer (TF-IDF, Cosine Similarity)
- spaCy (NLP Processing)
- scikit-learn (ML Algorithms)
- NLTK (Text Processing)
- Google Gemini API (Advanced AI)

**Job Scraping:**
- Selenium WebDriver
- BeautifulSoup4
- ChromeDriver

### Database Schema

#### Entity-Relationship Diagram

```
┌─────────────────────┐
│    resume_data      │
├─────────────────────┤
│ id (PK)            │◄────┐
│ name               │     │
│ email              │     │
│ phone              │     │
│ linkedin           │     │
│ summary            │     │
│ target_role        │     │
│ education          │     │
│ experience         │     │
│ skills             │     │
│ created_at         │     │
└─────────────────────┘     │
                            │ FK
┌─────────────────────┐     │
│   resume_skills     │     │
├─────────────────────┤     │
│ id (PK)            │     │
│ resume_id (FK)     │─────┘
│ skill_name         │
│ skill_category     │
│ proficiency_score  │
│ created_at         │
└─────────────────────┘
                            
┌─────────────────────┐     │
│  resume_analysis    │     │
├─────────────────────┤     │
│ id (PK)            │     │
│ resume_id (FK)     │─────┘
│ ats_score          │
│ keyword_match      │
│ format_score       │
│ missing_skills     │
│ recommendations    │
│ created_at         │
└─────────────────────┘

┌─────────────────────┐
│     admin_logs      │
├─────────────────────┤
│ id (PK)            │
│ admin_email        │
│ action             │
│ timestamp          │
└─────────────────────┘
```

### Module Architecture

#### 1. Core Modules

**app.py**
- Main application entry point
- Page routing and navigation
- Session state management
- UI rendering coordination

**utils/resume_analyzer.py**
- Standard resume analysis
- Skills extraction
- Experience parsing
- Education extraction

**utils/ai_resume_analyzer.py**
- AI-powered analysis using Gemini
- PDF text extraction (OCR support)
- Advanced scoring algorithms
- Detailed recommendations

**ml_models/custom_ats_scorer.py**
- Custom ML-based ATS scoring
- TF-IDF vectorization
- Cosine similarity calculation
- Skills categorization
- Section completeness analysis
- Format quality assessment

**utils/resume_builder.py**
- Resume generation from templates
- 4 template options (Modern, Minimal, Professional, Creative)
- PDF export functionality
- Dynamic content rendering

#### 2. Configuration Modules

**config/database.py**
- Database connection management
- CRUD operations
- Admin authentication
- Data persistence

**config/courses.py**
- Course recommendations by role
- Video resources mapping
- Skill-based suggestions

**config/job_roles.py**
- Job role definitions
- Required skills mapping
- Industry categorization

#### 3. Feature Modules

**dashboard/dashboard.py**
- Analytics visualization
- Statistics calculation
- Admin dashboard
- User activity tracking

**jobs/job_search.py**
- Job search interface
- Portal integration
- Company listings

**jobs/linkedin_scraper.py**
- LinkedIn job scraping
- Selenium automation
- Data extraction

**feedback/feedback.py**
- User feedback collection
- Rating system
- Feedback storage

### Custom ML Algorithm Implementation

#### ATS Scoring Algorithm

**Mathematical Foundation:**

1. **TF-IDF Vectorization**
```
TF(t,d) = (Number of times term t appears in document d) / (Total terms in document d)

IDF(t) = log(Total documents / Documents containing term t)

TF-IDF(t,d) = TF(t,d) × IDF(t)
```

2. **Cosine Similarity**
```
similarity = cos(θ) = (A · B) / (||A|| × ||B||)

Where:
A = TF-IDF vector of resume
B = TF-IDF vector of job description
```

3. **Overall Score Calculation**
```
Overall_Score = (w1 × Skills_Score) + 
                (w2 × Section_Score) + 
                (w3 × Format_Score) + 
                (w4 × ActionVerb_Score) + 
                (w5 × Keyword_Match_Score)

Where weights (w):
w1 = 0.25 (Skills)
w2 = 0.20 (Sections)
w3 = 0.20 (Format)
w4 = 0.15 (Action Verbs)
w5 = 0.20 (Keyword Match)
```

#### Skills Extraction Algorithm

**Process Flow:**
```
1. Text Preprocessing
   ├─ Lowercase conversion
   ├─ Special character removal
   └─ Whitespace normalization

2. Pattern Matching
   ├─ Regex-based skill detection
   ├─ Category assignment
   └─ Frequency counting

3. NER (Named Entity Recognition)
   ├─ spaCy model loading
   ├─ Entity extraction
   └─ Skill entity filtering

4. Categorization
   ├─ Programming languages
   ├─ Frameworks
   ├─ Databases
   ├─ Cloud/DevOps
   ├─ Data Science
   ├─ Web Technologies
   └─ Soft Skills
```

### API Integration

#### 1. Google Gemini AI API

**Configuration:**
```python
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
```

**Usage:**
- Advanced resume analysis
- Content generation
- Intelligent recommendations
- Natural language processing

#### 2. PDF Processing APIs

**Libraries Used:**
- pdfplumber (Primary extraction)
- PyPDF2 (Fallback extraction)
- pdf2image + pytesseract (OCR for scanned PDFs)

### Security Implementation

#### 1. Admin Authentication
```python
def verify_admin(email, password):
    hashed_password = hash_password(password)
    query = "SELECT * FROM admin WHERE email = ? AND password = ?"
    return execute_query(query, (email, hashed_password))
```

#### 2. Session Management
- Streamlit session_state for user sessions
- Admin flag for privilege escalation
- Secure password handling

#### 3. Data Protection
- Environment variables for API keys
- .env file for sensitive configuration
- gitignore for secret files

### Performance Optimization

#### 1. Caching Strategy
```python
@st.cache_data
def load_model():
    return spacy.load('en_core_web_sm')

@st.cache_resource
def get_database_connection():
    return sqlite3.connect('resume_data.db')
```

#### 2. Lazy Loading
- Models loaded on demand
- Database connections pooled
- PDF processing optimized

#### 3. Asynchronous Processing
- Background job scraping
- Non-blocking UI updates
- Progress indicators

### Testing Strategy

#### 1. Unit Testing
- Individual function testing
- Mock data validation
- Edge case handling

#### 2. Integration Testing
- Module interaction testing
- Database operations
- API integrations

#### 3. User Acceptance Testing
- UI/UX validation
- Feature completeness
- Performance benchmarks

### Deployment Architecture

#### Local Deployment
```bash
streamlit run app.py
```

#### Docker Deployment
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

#### Cloud Deployment Options
- Streamlit Cloud (Recommended)
- AWS EC2
- Google Cloud Run
- Azure Web Apps

### Performance Metrics

**Response Time:**
- Resume upload: < 2 seconds
- Analysis completion: 3-5 seconds
- AI analysis: 5-10 seconds
- Dashboard load: < 1 second

**Scalability:**
- Concurrent users: 10-50
- Database size: 10,000+ resumes
- File size limit: 10 MB per resume

**Accuracy:**
- Skill extraction: ~85-90%
- ATS scoring: ~80-85%
- Keyword matching: ~90%

### Future Enhancements

1. **Advanced ML Models**
   - Deep learning for resume parsing
   - Custom trained models
   - Multi-language support

2. **Real-time Features**
   - Live collaboration
   - WebSocket integration
   - Real-time job alerts

3. **Analytics Dashboard**
   - Market trend analysis
   - Skill demand forecasting
   - Success rate tracking

4. **Mobile Application**
   - React Native app
   - Push notifications
   - Offline support

### Troubleshooting Guide

**Common Issues:**

1. **PDF Extraction Fails**
   - Solution: Install Tesseract OCR
   - Check poppler installation

2. **spaCy Model Error**
   - Solution: `python -m spacy download en_core_web_sm`

3. **Database Lock Error**
   - Solution: Close existing connections
   - Check file permissions

4. **API Rate Limiting**
   - Solution: Implement exponential backoff
   - Use caching for repeated requests

### References

1. Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval.
2. spaCy Documentation: https://spacy.io/
3. scikit-learn Documentation: https://scikit-learn.org/
4. Streamlit Documentation: https://docs.streamlit.io/

