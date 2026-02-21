# Installation Guide - MCA Enhanced Version

## Prerequisites

### Required Software

1. **Python 3.8 or higher**
   ```bash
   python --version  # Should show 3.8+
   ```

2. **pip (Python package manager)**
   ```bash
   pip --version
   ```

3. **Git**
   ```bash
   git --version
   ```

### Optional (for OCR features)

4. **Tesseract OCR**
   - **Windows:** Download from https://github.com/UB-Mannheim/tesseract/wiki
   - **macOS:** `brew install tesseract`
   - **Linux:** `sudo apt-get install tesseract-ocr`

5. **Chrome/Chromium** (for job scraping)

---

## Step-by-Step Installation

### 1. Clone Repository

```bash
git clone [your-repo-url]
cd Smart-AI-Resume-Analyzer
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- streamlit (Web framework)
- scikit-learn (ML library)
- spacy (NLP)
- nltk (Text processing)
- pandas, numpy (Data processing)
- google-generativeai (Optional AI)
- And more...

### 4. Download Language Models

```bash
# Download spaCy English model
python -m spacy download en_core_web_sm

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 5. Configure Environment (Optional)

For AI-enhanced features (optional):

```bash
# Create .env file in utils directory
cp utils/.env.example utils/.env

# Edit utils/.env and add:
# GOOGLE_API_KEY=your_key_here
```

Get API key from: https://aistudio.google.com/app/apikey

---

## Verify Installation

### 1. Run Tests

```bash
# Run custom ML model tests
python run_tests.py

# Or use pytest directly
python -m pytest tests/ -v
```

Expected output:
```
======================== 23 passed in X.XXs =========================
```

### 2. Test Custom ML Model

```bash
python -c "from ml_models import CustomATSScorer; print('✅ Custom ML model loaded successfully')"
```

### 3. Start Application

```bash
streamlit run app.py
```

Application should open in browser at: http://localhost:8501

---

## Troubleshooting

### Issue: "spaCy model not found"

**Solution:**
```bash
python -m spacy download en_core_web_sm
```

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt --force-reinstall
```

### Issue: "Tesseract not found"

**Solution:**
- Windows: Install from https://github.com/UB-Mannheim/tesseract/wiki
- Add Tesseract to PATH
- macOS: `brew install tesseract`
- Linux: `sudo apt-get install tesseract-ocr`

### Issue: "Port 8501 already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: "PDF extraction fails"

**Solution:**
1. Install Tesseract OCR
2. Check poppler installation
3. Try with different PDF file

### Issue: "Import error in tests"

**Solution:**
```bash
# Make sure you're in project root
cd Smart-AI-Resume-Analyzer

# Run tests with python path
PYTHONPATH=. python -m pytest tests/
```

---

## Development Setup

### Additional Tools

1. **VS Code** (Recommended)
   - Python extension
   - Pylint
   - Black formatter

2. **PyCharm** (Alternative)
   - Professional or Community edition

### Install Development Dependencies

```bash
pip install pytest pytest-cov black pylint
```

### Code Formatting

```bash
black ml_models/ tests/
```

### Linting

```bash
pylint ml_models/custom_ats_scorer.py
```

---

## Docker Installation (Optional)

### Build Image

```bash
docker build -t resume-analyzer .
```

### Run Container

```bash
docker run -p 8501:8501 resume-analyzer
```

---

## System Requirements

### Minimum Requirements

- **CPU:** Dual-core processor
- **RAM:** 4GB
- **Storage:** 2GB free space
- **OS:** Windows 10, macOS 10.14+, or Linux (Ubuntu 20.04+)

### Recommended Requirements

- **CPU:** Quad-core processor
- **RAM:** 8GB
- **Storage:** 5GB free space
- **OS:** Windows 11, macOS 12+, or Linux (Ubuntu 22.04+)

---

## Quick Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] spaCy model downloaded
- [ ] NLTK data downloaded
- [ ] Tests passing (23/23)
- [ ] Application starts successfully
- [ ] Custom ML model works
- [ ] Resume upload works
- [ ] Analysis generates scores

---

## Getting Help

### Check Logs

```bash
# View Streamlit logs
tail -f ~/.streamlit/logs/streamlit.log
```

### Debug Mode

```bash
streamlit run app.py --logger.level=debug
```

### Test Individual Components

```bash
# Test custom ML scorer only
python -c "
from ml_models import CustomATSScorer
scorer = CustomATSScorer()
print('Scorer initialized:', scorer is not None)
"
```

---

## Next Steps

After successful installation:

1. **Read Documentation:**
   - `documentation/TECHNICAL_DOCUMENTATION.md`
   - `documentation/PROJECT_REPORT.md`

2. **Run Tests:**
   - `python run_tests.py`

3. **Start Application:**
   - `streamlit run app.py`

4. **Upload Resume:**
   - Navigate to Resume Analyzer
   - Upload PDF/DOCX file
   - View analysis results

---

## Support

For issues or questions:
- Check `documentation/` folder
- Review test cases in `tests/`
- Contact: [YOUR EMAIL]

---

**Installation complete! 🎉**

Your enhanced MCA version of Smart AI Resume Analyzer is ready to use.

