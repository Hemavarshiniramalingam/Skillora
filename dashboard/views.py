from django.shortcuts import render

STUDENT = {
    'name': 'Aarav Mehta',
    'major': 'Computer Science',
    'year': 'Final Year',
    'readiness_score': 88,
    'profile_completion': 82,
    'location': 'Bengaluru, India',
    'resume_status': 'Updated 2 days ago',
}

TOP_MATCHES = [
    {
        'title': 'AI Product Intern',
        'company': 'Nexa Labs',
        'match': 96,
        'location': 'Remote',
        'deadline': '2026-09-10',
        'slug': 'ai-product-intern',
        'type': 'Internship',
        'missing_skills': ['System Design', 'SQL Optimization'],
    },
    {
        'title': 'Data Science Fellow',
        'company': 'Insight Works',
        'match': 91,
        'location': 'Hyderabad',
        'deadline': '2026-09-15',
        'slug': 'data-science-fellow',
        'type': 'Fellowship',
        'missing_skills': ['Tableau', 'Machine Learning Ops'],
    },
    {
        'title': 'Frontend Engineer Intern',
        'company': 'PixelForge',
        'match': 87,
        'location': 'Pune',
        'deadline': '2026-09-18',
        'slug': 'frontend-engineer-intern',
        'type': 'Internship',
        'missing_skills': ['Testing', 'Accessibility'],
    },
]

SKILL_GAPS = [
    {'skill': 'System Design', 'priority': 'High', 'progress': 55},
    {'skill': 'SQL Optimization', 'priority': 'Medium', 'progress': 70},
    {'skill': 'Communication', 'priority': 'High', 'progress': 62},
]

INTERNSHIPS = [
    {
        'title': 'AI Product Intern',
        'company': 'Nexa Labs',
        'location': 'Remote',
        'match': 96,
        'deadline': '2026-09-10',
        'type': 'Internship',
        'slug': 'ai-product-intern',
        'description': 'Work on AI-driven product discovery and build prototypes for student-focused use cases.',
        'missing_skills': ['System Design', 'SQL Optimization'],
    },
    {
        'title': 'Data Analyst Intern',
        'company': 'MetricsHub',
        'location': 'Bengaluru',
        'match': 89,
        'deadline': '2026-09-12',
        'type': 'Internship',
        'slug': 'data-analyst-intern',
        'description': 'Analyze user behavior data to shape product insights and dashboarding decisions.',
        'missing_skills': ['Excel Automation', 'Campaign Analysis'],
    },
    {
        'title': 'Frontend Engineer Intern',
        'company': 'PixelForge',
        'location': 'Pune',
        'match': 87,
        'deadline': '2026-09-18',
        'type': 'Internship',
        'slug': 'frontend-engineer-intern',
        'description': 'Create polished interfaces and work with design systems for web experiences.',
        'missing_skills': ['Testing', 'Accessibility'],
    },
]

SCHOLARSHIPS = [
    {
        'title': 'Women in Tech Excellence Scholarship',
        'provider': 'CodeRise Foundation',
        'eligibility': 94,
        'deadline': '2026-09-14',
        'location': 'India',
        'slug': 'women-in-tech-excellence-scholarship',
        'description': 'Supports students pursuing technology and product innovation with mentoring and funding.',
        'requirements': ['CGPA above 8.5', 'Essay Submission', 'Leadership Experience'],
    },
    {
        'title': 'Future Builders Grant',
        'provider': 'SkillForge',
        'eligibility': 88,
        'deadline': '2026-09-28',
        'location': 'Global',
        'slug': 'future-builders-grant',
        'description': 'Funds student innovators with a strong technical project portfolio and community impact.',
        'requirements': ['Portfolio Review', 'Project Demo', 'Recommendation Letter'],
    },
    {
        'title': 'AI Research Access Award',
        'provider': 'OpenVista Labs',
        'eligibility': 83,
        'deadline': '2026-10-02',
        'location': 'Remote',
        'slug': 'ai-research-access-award',
        'description': 'Provides research access and financial sponsorship for machine learning students.',
        'requirements': ['Research Statement', 'Python Experience', 'Academic Transcript'],
    },
]

TRACKER_ITEMS = [
    {'title': 'Google Summer of Code', 'status': 'Saved', 'company': 'Google', 'stage': 'Reviewing'},
    {'title': 'Product Analyst Role', 'status': 'Applied', 'company': 'Nexa Labs', 'stage': 'Portfolio check'},
    {'title': 'AI Fellowship', 'status': 'Interview', 'company': 'Insight Works', 'stage': 'Technical round'},
    {'title': 'Research Grant', 'status': 'Decision', 'company': 'OpenVista Labs', 'stage': 'Awaiting result'},
]


def dashboard(request):
    context = {
        'student': STUDENT,
        'top_matches': TOP_MATCHES,
        'skill_gaps': SKILL_GAPS,
    }
    return render(request, 'dashboard.html', context)


def internships(request):
    return render(request, 'internships.html', {'internships': INTERNSHIPS})


def internship_detail(request, slug):
    internship = next(item for item in INTERNSHIPS if item['slug'] == slug)
    return render(request, 'internship_detail.html', {'internship': internship})


def scholarships(request):
    return render(request, 'scholarships.html', {'scholarships': SCHOLARSHIPS})


def scholarship_detail(request, slug):
    scholarship = next(item for item in SCHOLARSHIPS if item['slug'] == slug)
    return render(request, 'scholarship_detail.html', {'scholarship': scholarship})


def profile(request):
    return render(request, 'profile.html', {'student': STUDENT})


def tracker(request):
    return render(request, 'tracker.html', {'tracker_items': TRACKER_ITEMS})
