from __future__ import annotations

from .models import Internship, Scholarship, Student


def calculate_student_match_scores(student: Student):
    """Compute a simple score between a student and each opportunity."""
    internships = Internship.objects.all()
    scholarships = Scholarship.objects.all()

    opportunities = []
    preferred_keywords = {keyword.strip().lower() for keyword in (student.preferred_fields or "").split(",") if keyword.strip()}

    for internship in internships:
        score = 0.0
        if student.major and student.major.lower() in (internship.description or "").lower():
            score += 30
        if student.gpa > 0:
            score += min(student.gpa * 15, 30)
        skills = {skill.strip().lower() for skill in (internship.skills_required or "").split(",") if skill.strip()}
        overlap = len(preferred_keywords.intersection(skills))
        score += overlap * 20
        opportunities.append({"type": "internship", "id": internship.id, "score": round(score, 2)})

    for scholarship in scholarships:
        score = 0.0
        if student.gpa >= 3.0:
            score += 25
        if student.major and student.major.lower() in (scholarship.eligibility or "").lower():
            score += 25
        eligibility_words = {word.strip().lower() for word in (scholarship.eligibility or "").split() if word.strip()}
        overlap = len(preferred_keywords.intersection(eligibility_words))
        score += overlap * 10
        opportunities.append({"type": "scholarship", "id": scholarship.id, "score": round(score, 2)})

    return sorted(opportunities, key=lambda item: item["score"], reverse=True)
