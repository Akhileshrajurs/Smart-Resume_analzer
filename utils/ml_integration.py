import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml_models.custom_ats_scorer import CustomATSScorer

def analyze_resume_with_custom_ml(resume_text, job_description=None, target_role=None):
    scorer = CustomATSScorer()
    return scorer.score_resume(resume_text, job_description, target_role)

def compare_resume_with_job(resume_text, job_description):
    scorer = CustomATSScorer()
    return scorer.compare_with_job_description(resume_text, job_description)

def extract_skills_from_resume(resume_text):
    scorer = CustomATSScorer()
    return scorer.extract_skills(resume_text)

def get_ml_scorer_instance():
    return CustomATSScorer()

