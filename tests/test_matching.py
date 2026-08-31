from matching.services import (
    calculate_career_readiness,
    calculate_skill_gap,
    evaluate_scholarship_eligibility,
    generate_30_day_roadmap,
    internship_match_score,
)


def test_internship_match_score_uses_skill_overlap():
    student_skills = ["python", "sql", "pandas", "machine learning", "django"]
    required_skills = ["python", "machine learning", "sql", "flask", "aws"]

    result = internship_match_score(student_skills, required_skills)

    assert result["match_score"] > 60
    assert "flask" in result["missing_skills"]
    assert "aws" in result["missing_skills"]


def test_skill_gap_lists_missing_skills_in_order():
    student_skills = ["python", "sql"]
    required_skills = ["python", "sql", "pandas", "tensorflow"]

    result = calculate_skill_gap(student_skills, required_skills)

    assert result["missing_skills"] == ["pandas", "tensorflow"]


def test_scholarship_eligibility_scores_rule_based_criteria():
    profile = {
        "degree": "BSc Computer Science",
        "current_year": 3,
        "cgpa": 3.6,
        "field_of_study": "Computer Science",
        "family_income": 35000,
        "documents": ["transcript", "income_proof", "recommendation_letter"],
    }
    scholarship = {
        "degree": ["BSc Computer Science", "BSc Software Engineering"],
        "min_cgpa": 3.0,
        "year": [2, 3, 4],
        "field": ["Computer Science", "Software Engineering"],
        "max_income": 50000,
        "required_documents": ["transcript", "income_proof"],
    }

    result = evaluate_scholarship_eligibility(profile, scholarship)

    assert result["eligible"] is True
    assert result["eligibility_score"] >= 80
    assert result["missing_requirements"] == []


def test_career_readiness_score_is_between_zero_and_hundred():
    profile = {
        "skills": ["python", "sql", "machine learning"],
        "projects": 3,
        "certifications": 2,
        "experience_years": 1,
    }

    result = calculate_career_readiness(profile)

    assert 0 <= result["score"] <= 100
    assert result["profile_completeness"] >= 0


def test_roadmap_generates_steps_for_missing_skills():
    profile = {"skills": ["python", "sql"]}
    required_skills = ["python", "sql", "pandas", "machine learning"]

    roadmap = generate_30_day_roadmap(profile, required_skills)

    assert len(roadmap) >= 3
    assert any("pandas" in step.lower() for step in roadmap)
