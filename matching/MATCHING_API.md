# Matching API

This document describes the public functions exposed by the matching engine.

## internship_match_score(student_skills, required_skills)

Returns a dictionary with:
- `match_score`: percentage between 0 and 100
- `missing_skills`: list of required skills the student does not have
- `similarity`: raw cosine similarity value between 0 and 1

Example:
```python
from matching.services import internship_match_score

result = internship_match_score(
    ["python", "sql"],
    ["python", "sql", "pandas", "machine learning"],
)
```

## calculate_skill_gap(student_skills, required_skills)

Returns:
- `missing_skills`: ordered list of required skills not present in the student profile

## evaluate_scholarship_eligibility(profile, scholarship)

Input profile keys:
- `degree`
- `current_year`
- `cgpa`
- `field_of_study`
- `family_income`
- `documents`

Input scholarship keys:
- `degree`
- `min_cgpa`
- `year`
- `field`
- `max_income`
- `required_documents`

Returns:
- `eligible`: boolean
- `eligibility_score`: percentage between 0 and 100
- `missing_requirements`: documents or criteria not satisfied
- `criteria`: individual rule results

## calculate_career_readiness(profile)

Input keys:
- `skills`
- `projects`
- `certifications`
- `experience_years`

Returns a score and breakdown:
- `score`
- `profile_completeness`
- `skill_score`
- `project_score`
- `cert_score`
- `experience_score`

## generate_30_day_roadmap(profile, required_skills)

Returns a list of action-oriented weekly roadmap tasks based on the current skill gap.
