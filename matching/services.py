from __future__ import annotations

from collections import OrderedDict
from typing import Any


def calculate_skill_gap(student_skills: list[str], required_skills: list[str]) -> dict[str, Any]:
    """Return the missing skills while preserving the required order."""
    student_set = {skill.strip().lower() for skill in student_skills if skill and str(skill).strip()}
    missing = []
    seen = set()

    for skill in required_skills:
        normalized = str(skill).strip().lower()
        if not normalized:
            continue
        if normalized not in student_set and normalized not in seen:
            missing.append(normalized)
            seen.add(normalized)

    return {"missing_skills": missing}


def internship_match_score(student_skills: list[str], required_skills: list[str]) -> dict[str, Any]:
    """Compute a pragmatic internship match score using TF-IDF similarity and required-skill coverage."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    student_set = {str(skill).strip().lower() for skill in student_skills if str(skill).strip()}
    required_set = {str(skill).strip().lower() for skill in required_skills if str(skill).strip()}
    matched_required = len(required_set.intersection(student_set))
    coverage_ratio = (matched_required / len(required_set)) if required_set else 1.0

    student_text = " ".join(student_skills)
    required_text = " ".join(required_skills)
    vectorizer = TfidfVectorizer(lowercase=True)
    vectors = vectorizer.fit_transform([student_text, required_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    gap = calculate_skill_gap(student_skills, required_skills)
    similarity_score = float(similarity) * 100
    coverage_score = coverage_ratio * 100
    bonus = 10 if coverage_ratio >= 0.5 else 0
    match_score = max(0.0, min(100.0, round((0.6 * similarity_score) + (0.4 * coverage_score) + bonus, 2)))

    return {
        "match_score": match_score,
        "missing_skills": gap["missing_skills"],
        "similarity": float(similarity),
        "coverage": round(coverage_score, 2),
    }


def evaluate_scholarship_eligibility(profile: dict[str, Any], scholarship: dict[str, Any]) -> dict[str, Any]:
    """Evaluate scholarship eligibility using weighted rule-based checks."""
    score = 0
    criteria = OrderedDict()

    degree = str(profile.get("degree", "")).strip()
    allowed_degrees = [str(item).strip() for item in scholarship.get("degree", [])]
    if degree and degree in allowed_degrees:
        score += 25
        criteria["degree"] = "passed"
    else:
        criteria["degree"] = "missing or invalid"

    current_year = profile.get("current_year")
    allowed_years = scholarship.get("year", [])
    if current_year in allowed_years:
        score += 15
        criteria["year"] = "passed"
    else:
        criteria["year"] = "missing or invalid"

    cgpa = float(profile.get("cgpa", 0) or 0)
    min_cgpa = float(scholarship.get("min_cgpa", 0) or 0)
    if cgpa >= min_cgpa:
        score += 25
        criteria["cgpa"] = "passed"
    else:
        criteria["cgpa"] = "below minimum"

    field = str(profile.get("field_of_study", "")).strip()
    allowed_fields = [str(item).strip() for item in scholarship.get("field", [])]
    if field and field in allowed_fields:
        score += 15
        criteria["field"] = "passed"
    else:
        criteria["field"] = "missing or invalid"

    income = float(profile.get("family_income", 0) or 0)
    max_income = float(scholarship.get("max_income", 999999999) or 999999999)
    if income <= max_income:
        score += 10
        criteria["income"] = "passed"
    else:
        criteria["income"] = "above limit"

    required_docs = [str(item).strip().lower() for item in scholarship.get("required_documents", [])]
    submitted_docs = {str(item).strip().lower() for item in profile.get("documents", [])}
    missing_docs = [doc for doc in required_docs if doc not in submitted_docs]
    if not missing_docs:
        score += 10
        criteria["documents"] = "passed"
    else:
        criteria["documents"] = "missing: " + ", ".join(missing_docs)

    eligibility_score = min(100, max(0, score))
    eligible = eligibility_score >= 70 and not missing_docs

    return {
        "eligible": eligible,
        "eligibility_score": eligibility_score,
        "missing_requirements": missing_docs,
        "criteria": dict(criteria),
    }


def calculate_career_readiness(profile: dict[str, Any]) -> dict[str, Any]:
    """Compute a career readiness score based on profile completeness and experience."""
    skills = profile.get("skills", [])
    skill_score = min(40, len(skills) * 5)
    project_score = min(20, int(profile.get("projects", 0) or 0) * 5)
    cert_score = min(20, int(profile.get("certifications", 0) or 0) * 10)
    experience_years = float(profile.get("experience_years", 0) or 0)
    experience_score = min(20, experience_years * 10)

    total = skill_score + project_score + cert_score + experience_score
    score = max(0, min(100, round(total, 2)))

    return {
        "score": score,
        "profile_completeness": round(min(100, (len(skills) / 10) * 100 if skills else 0), 2),
        "skill_score": skill_score,
        "project_score": project_score,
        "cert_score": cert_score,
        "experience_score": experience_score,
    }


def generate_30_day_roadmap(profile: dict[str, Any], required_skills: list[str]) -> list[str]:
    """Create a simple 30-day roadmap based on missing skills."""
    gap = calculate_skill_gap(profile.get("skills", []), required_skills)
    missing = gap["missing_skills"]
    roadmap = []

    roadmap.append("Week 1: Build a strong foundation in the core skills: " + ", ".join(missing[:2]))
    if len(missing) > 1:
        roadmap.append("Week 2: Practice project-based tasks using " + missing[1] if len(missing) > 1 else "core tools")
    roadmap.append("Week 3: Complete at least one mini-project that demonstrates " + ", ".join(missing[: min(2, len(missing))]))
    roadmap.append("Week 4: Review, refine, and prepare for portfolio submission with a final project using " + ", ".join(missing[: min(3, len(missing))]))

    if missing:
        roadmap.insert(0, "Day 1-7: Focus on mastering " + missing[0] + " and related fundamentals.")
    else:
        roadmap.insert(0, "Day 1-7: Review your current strengths and prepare a portfolio highlight.")

    return roadmap
