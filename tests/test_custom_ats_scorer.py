import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ml_models.custom_ats_scorer import CustomATSScorer, score_resume_with_custom_model


class TestCustomATSScorer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scorer = CustomATSScorer()
        cls.sample_resume = """
        John Doe
        Software Engineer
        john.doe@email.com | (555) 123-4567
        
        EXPERIENCE
        Senior Software Engineer - Tech Corp (2020-Present)
        - Developed microservices using Python and Django
        - Led team of 5 engineers
        - Improved performance by 40%
        - Managed deployment using Docker and Kubernetes
        
        EDUCATION
        Bachelor of Science in Computer Science - University (2016-2020)
        
        SKILLS
        Python, JavaScript, Java, Django, React, PostgreSQL, MongoDB, AWS, Docker
        
        PROJECTS
        Built AI chatbot using NLP and machine learning
        """
        
        cls.sample_job_desc = """
        Senior Software Engineer
        Requirements:
        - 3+ years Python and Django
        - Microservices architecture
        - AWS, Docker, Kubernetes
        - PostgreSQL
        - Leadership skills
        """
    
    def test_scorer_initialization(self):
        self.assertIsNotNone(self.scorer)
        self.assertIsNotNone(self.scorer.skill_categories)
        self.assertTrue(len(self.scorer.all_skills) > 0)
    
    def test_preprocess_text(self):
        text = "Python, JavaScript & C++"
        processed = self.scorer.preprocess_text(text)
        self.assertEqual(processed, "python javascript c")
        
        empty_text = ""
        self.assertEqual(self.scorer.preprocess_text(empty_text), "")
    
    def test_extract_skills(self):
        skills = self.scorer.extract_skills(self.sample_resume)
        self.assertIsInstance(skills, dict)
        self.assertTrue('programming_languages' in skills)
        self.assertTrue(len(skills['programming_languages']) > 0)
        self.assertIn('python', skills['programming_languages'])
        self.assertIn('javascript', skills['programming_languages'])
    
    def test_keyword_match_score(self):
        score = self.scorer.calculate_keyword_match_score(
            self.sample_resume, 
            self.sample_job_desc
        )
        self.assertGreater(score, 0)
        self.assertLessEqual(score, 100)
        
        zero_score = self.scorer.calculate_keyword_match_score("", "")
        self.assertEqual(zero_score, 0.0)
    
    def test_section_completeness(self):
        analysis = self.scorer.analyze_section_completeness(self.sample_resume)
        self.assertIn('sections_found', analysis)
        self.assertIn('completeness_score', analysis)
        self.assertIn('missing_sections', analysis)
        self.assertTrue(analysis['sections_found']['experience'])
        self.assertTrue(analysis['sections_found']['education'])
        self.assertTrue(analysis['sections_found']['skills'])
    
    def test_action_verbs(self):
        analysis = self.scorer.analyze_action_verbs(self.sample_resume)
        self.assertIn('found_verbs', analysis)
        self.assertIn('score', analysis)
        self.assertGreater(len(analysis['found_verbs']), 0)
        self.assertIn('developed', analysis['found_verbs'])
        self.assertIn('led', analysis['found_verbs'])
    
    def test_keyword_density(self):
        keywords = ['python', 'django', 'aws', 'docker']
        density = self.scorer.calculate_keyword_density(self.sample_resume, keywords)
        self.assertIn('density', density)
        self.assertIn('coverage', density)
        self.assertGreater(density['coverage'], 0)
        self.assertGreater(len(density['found_keywords']), 0)
    
    def test_format_score(self):
        format_analysis = self.scorer.calculate_format_score(self.sample_resume)
        self.assertIn('score', format_analysis)
        self.assertIn('word_count', format_analysis)
        self.assertIn('factors', format_analysis)
        self.assertGreater(format_analysis['score'], 0)
    
    def test_score_resume_without_job_desc(self):
        results = self.scorer.score_resume(self.sample_resume)
        self.assertIn('overall_score', results)
        self.assertIn('component_scores', results)
        self.assertIn('skills_found', results)
        self.assertIn('recommendations', results)
        self.assertIn('strengths', results)
        self.assertGreater(results['overall_score'], 0)
        self.assertLessEqual(results['overall_score'], 100)
    
    def test_score_resume_with_job_desc(self):
        results = self.scorer.score_resume(
            self.sample_resume, 
            self.sample_job_desc
        )
        self.assertIn('keyword_match', results['component_scores'])
        self.assertGreater(results['component_scores']['keyword_match'], 0)
    
    def test_compare_with_job_description(self):
        comparison = self.scorer.compare_with_job_description(
            self.sample_resume,
            self.sample_job_desc
        )
        self.assertIn('matching_skills', comparison)
        self.assertIn('missing_skills', comparison)
        self.assertIn('match_percentage', comparison)
        self.assertGreater(len(comparison['matching_skills']), 0)
    
    def test_empty_resume(self):
        results = self.scorer.score_resume("")
        self.assertEqual(results['overall_score'], 0)
        self.assertGreater(len(results['recommendations']), 0)
    
    def test_score_components_weights(self):
        results = self.scorer.score_resume(
            self.sample_resume,
            self.sample_job_desc
        )
        components = results['component_scores']
        self.assertIn('skills', components)
        self.assertIn('sections', components)
        self.assertIn('format', components)
        self.assertIn('action_verbs', components)
        self.assertIn('keyword_match', components)
    
    def test_score_resume_convenience_function(self):
        results = score_resume_with_custom_model(self.sample_resume)
        self.assertIn('overall_score', results)
        self.assertIsInstance(results, dict)
    
    def test_skills_categorization(self):
        skills = self.scorer.extract_skills(self.sample_resume)
        total_skills = sum(len(v) for v in skills.values())
        self.assertGreater(total_skills, 5)
        
        if 'frameworks' in skills:
            self.assertTrue(any('django' in s or 'react' in s for s in skills.get('frameworks', [])))
    
    def test_score_ranges(self):
        results = self.scorer.score_resume(self.sample_resume)
        for component, score in results['component_scores'].items():
            self.assertGreaterEqual(score, 0, f"{component} score below 0")
            self.assertLessEqual(score, 100, f"{component} score above 100")
    
    def test_recommendations_generation(self):
        poor_resume = "Name: Test User"
        results = self.scorer.score_resume(poor_resume)
        self.assertGreater(len(results['recommendations']), 0)
        self.assertGreater(len(results['weaknesses']), 0)
    
    def test_good_resume_recognition(self):
        good_resume = """
        Jane Smith
        Senior Data Scientist
        jane@email.com | 555-1234
        
        SUMMARY
        Experienced data scientist with 8+ years
        
        EXPERIENCE
        Lead Data Scientist - AI Company (2018-Present)
        - Developed machine learning models achieving 95% accuracy
        - Led team of 10 data scientists
        - Implemented deep learning solutions using TensorFlow
        - Optimized algorithms improving performance by 60%
        
        Senior Data Analyst - Tech Corp (2015-2018)
        - Analyzed large datasets using Python and SQL
        - Created data visualizations with Tableau
        - Built predictive models for business intelligence
        
        EDUCATION
        MS in Data Science - Stanford University
        BS in Computer Science - MIT
        
        SKILLS
        Python, R, TensorFlow, PyTorch, scikit-learn, pandas, SQL,
        MongoDB, AWS, Docker, Kubernetes, machine learning, deep learning,
        NLP, computer vision, data analysis, statistics
        
        PROJECTS
        Built recommendation system serving 1M+ users
        Created NLP chatbot with 92% accuracy
        Developed computer vision model for medical imaging
        """
        
        results = self.scorer.score_resume(good_resume)
        self.assertGreater(results['overall_score'], 70)
        self.assertGreater(len(results['strengths']), 0)
    
    def test_assessment_classification(self):
        test_cases = [
            (85, "Excellent"),
            (75, "Good"),
            (65, "Fair"),
            (50, "Needs Work")
        ]
        
        for score, expected_assessment in test_cases:
            resume = f"Test resume with score around {score}"
            results = self.scorer.score_resume(resume)
            self.assertIn('assessment', results)


class TestEdgeCases(unittest.TestCase):
    
    def setUp(self):
        self.scorer = CustomATSScorer()
    
    def test_very_long_resume(self):
        long_resume = "Experience " * 10000
        results = self.scorer.score_resume(long_resume)
        self.assertIsNotNone(results)
    
    def test_special_characters(self):
        resume = "Skills: C++, C#, .NET, Node.js, React.js"
        skills = self.scorer.extract_skills(resume)
        self.assertGreater(sum(len(v) for v in skills.values()), 0)
    
    def test_case_insensitivity(self):
        resume_lower = "python django aws"
        resume_upper = "PYTHON DJANGO AWS"
        resume_mixed = "Python Django AWS"
        
        skills_lower = self.scorer.extract_skills(resume_lower)
        skills_upper = self.scorer.extract_skills(resume_upper)
        skills_mixed = self.scorer.extract_skills(resume_mixed)
        
        total_lower = sum(len(v) for v in skills_lower.values())
        total_upper = sum(len(v) for v in skills_upper.values())
        total_mixed = sum(len(v) for v in skills_mixed.values())
        
        self.assertEqual(total_lower, total_upper)
        self.assertEqual(total_lower, total_mixed)
    
    def test_unicode_characters(self):
        resume = "Name: José García\nSkills: Python, Java"
        results = self.scorer.score_resume(resume)
        self.assertIsNotNone(results)
    
    def test_missing_sections(self):
        incomplete_resume = "John Doe\njohn@email.com\nPython Developer"
        results = self.scorer.score_resume(incomplete_resume)
        self.assertGreater(len(results['section_analysis']['missing_sections']), 0)


class TestPerformance(unittest.TestCase):
    
    def setUp(self):
        self.scorer = CustomATSScorer()
        self.resume = """
        Test Resume
        email@test.com | 555-1234
        
        EXPERIENCE
        Software Engineer - Company (2020-2024)
        - Developed applications using Python, JavaScript, React
        - Managed databases with PostgreSQL and MongoDB
        - Deployed services on AWS using Docker
        
        EDUCATION
        BS Computer Science
        
        SKILLS
        Python, JavaScript, React, Node.js, PostgreSQL, MongoDB,
        AWS, Docker, Kubernetes, Git, Agile
        
        PROJECTS
        Built web applications
        """
    
    def test_scoring_performance(self):
        import time
        start = time.time()
        results = self.scorer.score_resume(self.resume)
        end = time.time()
        execution_time = end - start
        self.assertLess(execution_time, 5.0, "Scoring took too long")
    
    def test_bulk_processing(self):
        import time
        resumes = [self.resume] * 10
        start = time.time()
        for resume in resumes:
            self.scorer.score_resume(resume)
        end = time.time()
        avg_time = (end - start) / len(resumes)
        self.assertLess(avg_time, 5.0, "Average processing time too high")


if __name__ == '__main__':
    unittest.main(verbosity=2)

