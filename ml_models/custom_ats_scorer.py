import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass


class CustomATSScorer:
    def __init__(self):
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except:
            self.nlp = None
        
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=500,
            ngram_range=(1, 3),
            stop_words='english',
            min_df=1
        )
        
        self.skill_categories = {
            'programming_languages': ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'go', 'rust', 'php', 'swift', 'kotlin', 'typescript', 'scala', 'r', 'matlab'],
            'frameworks': ['react', 'angular', 'vue', 'django', 'flask', 'spring', 'express', 'nodejs', 'fastapi', 'laravel', 'rails', '.net', 'asp.net'],
            'databases': ['mysql', 'postgresql', 'mongodb', 'redis', 'cassandra', 'oracle', 'sql server', 'dynamodb', 'elasticsearch', 'neo4j', 'sqlite'],
            'cloud_devops': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'gitlab', 'terraform', 'ansible', 'circleci', 'travis ci', 'helm'],
            'data_science': ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy', 'data analysis', 'statistics', 'nlp', 'computer vision', 'ai', 'neural networks'],
            'web_technologies': ['html', 'css', 'rest api', 'graphql', 'websockets', 'ajax', 'json', 'xml', 'responsive design', 'bootstrap', 'tailwind'],
            'soft_skills': ['leadership', 'communication', 'teamwork', 'problem solving', 'critical thinking', 'time management', 'collaboration', 'agile', 'scrum', 'project management']
        }
        
        self.all_skills = []
        for category in self.skill_categories.values():
            self.all_skills.extend(category)
        
        self.required_sections = ['experience', 'education', 'skills', 'summary', 'projects']
        self.strong_action_verbs = ['achieved', 'developed', 'implemented', 'designed', 'led', 'managed', 'created', 'optimized', 'improved', 'increased', 'reduced', 'built', 'launched', 'established', 'coordinated', 'analyzed', 'engineered']
    
    def preprocess_text(self, text):
        if not text:
            return ""
        text = text.lower()
        text = re.sub(r'[^\w\s\-\+\#\.]', ' ', text)
        text = ' '.join(text.split())
        return text
    
    def extract_skills(self, text):
        text_lower = text.lower()
        found_skills = {category: [] for category in self.skill_categories.keys()}
        
        for category, skills_list in self.skill_categories.items():
            for skill in skills_list:
                pattern = r'\b' + re.escape(skill) + r'\b'
                if re.search(pattern, text_lower):
                    found_skills[category].append(skill)
        
        if self.nlp:
            doc = self.nlp(text[:100000])
            for ent in doc.ents:
                if ent.label_ in ['SKILL', 'PRODUCT', 'ORG']:
                    skill_text = ent.text.lower()
                    if skill_text not in self.all_skills and len(skill_text) > 2:
                        found_skills['other'] = found_skills.get('other', [])
                        if skill_text not in found_skills['other']:
                            found_skills['other'].append(skill_text)
        
        return found_skills
    
    def calculate_keyword_match_score(self, resume_text, job_description):
        if not job_description or not resume_text:
            return 0.0
        
        try:
            resume_clean = self.preprocess_text(resume_text)
            job_clean = self.preprocess_text(job_description)
            documents = [resume_clean, job_clean]
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(documents)
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
            score = similarity * 100
            return min(100, max(0, score))
        except:
            return 0.0
    
    def analyze_section_completeness(self, resume_text):
        text_lower = resume_text.lower()
        sections_found = {}
        
        for section in self.required_sections:
            pattern = r'\b' + section + r'\b'
            sections_found[section] = bool(re.search(pattern, text_lower))
        
        found_count = sum(sections_found.values())
        completeness_score = (found_count / len(self.required_sections)) * 100
        
        return {
            'sections_found': sections_found,
            'completeness_score': completeness_score,
            'missing_sections': [s for s, found in sections_found.items() if not found]
        }
    
    def analyze_action_verbs(self, resume_text):
        text_lower = resume_text.lower()
        found_verbs = [verb for verb in self.strong_action_verbs if re.search(r'\b' + verb, text_lower)]
        unique_verbs = len(found_verbs)
        score = min(100, (unique_verbs / 10) * 100)
        
        return {
            'found_verbs': found_verbs,
            'unique_count': unique_verbs,
            'score': score
        }
    
    def calculate_keyword_density(self, resume_text, target_keywords):
        text_lower = resume_text.lower()
        total_words = len(text_lower.split())
        
        if total_words == 0:
            return {'density': 0, 'found_keywords': [], 'coverage': 0}
        
        found_keywords = []
        total_occurrences = 0
        
        for keyword in target_keywords:
            keyword_lower = keyword.lower()
            count = len(re.findall(r'\b' + re.escape(keyword_lower) + r'\b', text_lower))
            if count > 0:
                found_keywords.append({'keyword': keyword, 'count': count, 'density': (count / total_words) * 100})
                total_occurrences += count
        
        coverage = (len(found_keywords) / len(target_keywords)) * 100 if target_keywords else 0
        
        return {
            'density': (total_occurrences / total_words) * 100,
            'found_keywords': found_keywords,
            'coverage': coverage,
            'total_keywords': len(target_keywords),
            'matched_keywords': len(found_keywords)
        }
    
    def calculate_format_score(self, resume_text):
        score = 0
        factors = []
        word_count = len(resume_text.split())
        
        if 300 <= word_count <= 1500:
            score += 30
            factors.append("Appropriate length")
        elif word_count < 300:
            factors.append("Too short")
        else:
            factors.append("Too long")
        
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text):
            score += 15
            factors.append("Email present")
        else:
            factors.append("Missing email")
        
        if re.search(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', resume_text):
            score += 15
            factors.append("Phone present")
        else:
            factors.append("Missing phone")
        
        bullet_patterns = [r'•', r'\*', r'-\s', r'\d+\.']
        if any(re.search(pattern, resume_text) for pattern in bullet_patterns):
            score += 20
            factors.append("Well-structured")
        else:
            factors.append("Add bullet points")
        
        numbers = re.findall(r'\b\d+%|\$\d+|\d+\+', resume_text)
        if len(numbers) >= 3:
            score += 20
            factors.append("Quantifiable achievements")
        else:
            factors.append("Add metrics")
        
        return {'score': min(100, score), 'word_count': word_count, 'factors': factors}
    
    def score_resume(self, resume_text, job_description=None, target_role=None):
        results = {
            'overall_score': 0,
            'component_scores': {},
            'skills_found': {},
            'recommendations': [],
            'strengths': [],
            'weaknesses': []
        }
        
        skills_found = self.extract_skills(resume_text)
        results['skills_found'] = skills_found
        total_skills = sum(len(skills) for skills in skills_found.values())
        skills_score = min(100, (total_skills / 15) * 100)
        results['component_scores']['skills'] = skills_score
        
        if total_skills < 10:
            results['recommendations'].append("Add more technical skills")
            results['weaknesses'].append("Limited skill diversity")
        else:
            results['strengths'].append(f"Good skill diversity ({total_skills} skills)")
        
        section_analysis = self.analyze_section_completeness(resume_text)
        results['component_scores']['sections'] = section_analysis['completeness_score']
        results['section_analysis'] = section_analysis
        
        if section_analysis['missing_sections']:
            results['recommendations'].append(f"Add missing sections: {', '.join(section_analysis['missing_sections'])}")
            results['weaknesses'].append("Missing key sections")
        else:
            results['strengths'].append("All sections present")
        
        format_analysis = self.calculate_format_score(resume_text)
        results['component_scores']['format'] = format_analysis['score']
        results['format_analysis'] = format_analysis
        
        if format_analysis['score'] < 70:
            results['recommendations'].append("Improve formatting")
            results['weaknesses'].append("Formatting needs work")
        else:
            results['strengths'].append("Well-formatted")
        
        verb_analysis = self.analyze_action_verbs(resume_text)
        results['component_scores']['action_verbs'] = verb_analysis['score']
        results['action_verb_analysis'] = verb_analysis
        
        if verb_analysis['unique_count'] < 5:
            results['recommendations'].append("Use more action verbs")
            results['weaknesses'].append("Limited action verbs")
        else:
            results['strengths'].append(f"Good action verbs ({verb_analysis['unique_count']} unique)")
        
        if job_description:
            keyword_score = self.calculate_keyword_match_score(resume_text, job_description)
            results['component_scores']['keyword_match'] = keyword_score
            
            if keyword_score < 60:
                results['recommendations'].append("Improve keyword alignment")
                results['weaknesses'].append("Low keyword match")
            else:
                results['strengths'].append(f"Good keyword alignment ({keyword_score:.1f}%)")
            
            try:
                job_words = [word for word in job_description.lower().split() if len(word) > 4]
                top_keywords = [word for word, count in Counter(job_words).most_common(20)]
                density_analysis = self.calculate_keyword_density(resume_text, top_keywords)
                results['keyword_density'] = density_analysis
                
                if density_analysis['coverage'] < 50:
                    results['recommendations'].append("Include more job keywords")
            except:
                pass
        
        weights = {
            'skills': 0.25,
            'sections': 0.20,
            'format': 0.20,
            'action_verbs': 0.15,
            'keyword_match': 0.20 if job_description else 0
        }
        
        if not job_description:
            total_weight = sum(w for k, w in weights.items() if k != 'keyword_match')
            weights = {k: (v / total_weight) for k, v in weights.items() if k != 'keyword_match'}
        
        overall_score = sum(results['component_scores'].get(component, 0) * weight for component, weight in weights.items())
        results['overall_score'] = round(overall_score, 2)
        
        if overall_score >= 80:
            results['assessment'] = "Excellent"
        elif overall_score >= 70:
            results['assessment'] = "Good"
        elif overall_score >= 60:
            results['assessment'] = "Fair"
        else:
            results['assessment'] = "Needs Work"
        
        return results
    
    def compare_with_job_description(self, resume_text, job_description):
        resume_skills = self.extract_skills(resume_text)
        job_skills = self.extract_skills(job_description)
        
        all_resume_skills = set()
        for skills in resume_skills.values():
            all_resume_skills.update(skills)
        
        all_job_skills = set()
        for skills in job_skills.values():
            all_job_skills.update(skills)
        
        matching_skills = all_resume_skills.intersection(all_job_skills)
        missing_skills = all_job_skills - all_resume_skills
        
        return {
            'matching_skills': list(matching_skills),
            'missing_skills': list(missing_skills),
            'match_percentage': (len(matching_skills) / len(all_job_skills) * 100) if all_job_skills else 0,
            'resume_skills': resume_skills,
            'job_skills': job_skills
        }


def score_resume_with_custom_model(resume_text, job_description=None, target_role=None):
    scorer = CustomATSScorer()
    return scorer.score_resume(resume_text, job_description, target_role)
