# Git Commands - Phase 4 Integration

## Commit & Push Workflow

### Step 1: Check Status
```bash
git status
git log --oneline -5
```

### Step 2: Stage All Changes
```bash
# Stage everything
git add .

# Or stage specific files
git add opportunity_app/
git add skillora/
git add Dockerfile docker-compose.yml
git add requirements.txt
git add API_INTEGRATION_GUIDE.md README.md
git add validate_setup.py setup.sh setup.bat
git add .github/
git add .env.example .gitignore
```

### Step 3: Review Changes
```bash
git status
git diff --cached --stat
git diff --cached skillora/settings/base.py  # View specific changes
```

### Step 4: Commit
```bash
git commit -m "Add API, Celery, and deployment infrastructure (Phase 4)

- Implement REST API with 6 endpoints for opportunities/applications
- Add 5 database models: Student, Internship, Scholarship, Application, MatchResult
- Implement matching algorithm with scoring system
- Set up Celery with Redis broker and 2 periodic tasks
- Add Docker and docker-compose for development
- Configure environment-based settings (dev/prod)
- Create CI/CD workflow for automated testing
- Add comprehensive documentation and validation scripts

Addresses Phase 4 requirements from specification.
"
```

### Step 5: Push to Remote
```bash
# First time pushing this branch
git push -u origin feature/integration-devops

# Subsequent pushes
git push origin feature/integration-devops
```

### Step 6: Create Pull Request
On GitHub:
1. Go to repository
2. Click "Pull Requests"
3. Click "New Pull Request"
4. Select: base = `develop`, compare = `feature/integration-devops`
5. Add description:

```markdown
## Phase 4: API, Notifications & Integration/DevOps

### Overview
This PR implements the complete REST API layer, Celery-based notifications, and deployment infrastructure for OpportunityAI.

### Key Changes
- ✅ REST API with 6 endpoints for opportunities/applications
- ✅ 5 database models (Student, Internship, Scholarship, Application, MatchResult)
- ✅ Matching algorithm with scoring system
- ✅ Celery integration with Redis broker
- ✅ Docker and docker-compose for development
- ✅ Environment-based settings (dev/prod)
- ✅ CI/CD workflow for automated testing
- ✅ Comprehensive documentation

### Files Changed
- 25+ files created/modified
- 1,370+ lines of code/documentation
- New Python packages: djangorestframework, celery, redis, python-dotenv

### Testing
- [x] `python manage.py check` passes
- [x] `python validate_setup.py` passes
- [x] All models import successfully
- [x] All API endpoints defined
- [x] Celery tasks discoverable
- [x] Docker builds successfully

### Deployment
Run automated setup:
```bash
./setup.sh  # or setup.bat on Windows
python validate_setup.py
```

### Related Issues
- Closes #[issue-number]
- Blocks [other-issue]
- Depends on [other-pr]
```

## Integration Workflow (After Merge)

### Pull Latest Develop
```bash
git checkout develop
git pull origin develop
```

### Merge Feature Branches
```bash
# Check out other team member's branch
git merge feature/their-branch

# If conflicts, resolve them
git add .  # After resolving
git commit -m "Merge feature/their-branch into develop"

# Or use GitHub PR merge
```

### Verify Integration
```bash
python manage.py check
python manage.py test
python validate_setup.py
```

### Push Back to Develop
```bash
git push origin develop
```

## Branch Cleanup

### Delete Local Branch
```bash
git branch -d feature/integration-devops
```

### Delete Remote Branch
```bash
git push origin --delete feature/integration-devops
```

## Common Git Tasks

### View Branch History
```bash
git log feature/integration-devops --oneline -10
git log feature/integration-devops --oneline develop..feature/integration-devops
```

### Compare Branches
```bash
git diff develop feature/integration-devops --stat
git diff develop feature/integration-devops
```

### Revert Changes
```bash
# If not yet committed
git checkout -- opportunity_app/models.py

# If already committed
git revert <commit-hash>
git reset --soft HEAD~1  # Uncommit last change

# Discard all changes
git reset --hard origin/feature/integration-devops
```

### Update Branch from Develop
```bash
git fetch origin
git rebase origin/develop
# or
git merge origin/develop
```

### Squash Commits
```bash
git rebase -i HEAD~3  # Interactive rebase last 3 commits
# Then mark commits as "squash" (s) and reorder as needed
```

## Troubleshooting

### Large Files Warning
```bash
# If accidentally added large files
git rm --cached filename
echo "filename" >> .gitignore
git commit -m "Remove large file and add to gitignore"
```

### Wrong Branch Committed
```bash
# Create new branch from current HEAD
git branch feature/correct-branch

# Reset current branch to before commits
git reset --hard origin/develop

# Switch to new branch
git checkout feature/correct-branch
```

### Forgot to Add Files
```bash
# Add missing files
git add forgotten-file.py

# Add to previous commit (amend)
git commit --amend --no-edit
git push origin feature/integration-devops --force-with-lease
```

### Merge Conflicts

When merging develop or other branches:

```bash
# See conflicts
git status
git diff

# Edit files to resolve conflicts
vim filename  # or use IDE

# Mark as resolved
git add filename

# Complete merge
git commit -m "Resolve merge conflicts with develop"
```

## CI/CD Status

GitHub Actions workflow will:
1. ✅ Run on every commit to PR
2. ✅ Install dependencies
3. ✅ Run `python manage.py check`
4. ✅ Run test suite
5. ✅ Report status back to PR

### View CI Status
```bash
git log --all --oneline --graph -15
# Look for CI status badge in PR
```

## Release/Deployment

### Merge to Main (Release)
```bash
git checkout main
git pull origin main
git merge develop
git tag v1.0.0  # Or appropriate version
git push origin main --tags
```

### Deploy Tag
```bash
docker pull myrepo/skillora:v1.0.0
docker run -d -p 8000:8000 myrepo/skillora:v1.0.0
```

## Reference

### Useful Git Aliases
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'
```

### Full Workflow Command Sequence
```bash
# Create and switch to branch
git checkout -b feature/integration-devops develop

# Make changes (already done via file creation)

# Stage and commit
git add .
git commit -m "Add API, Celery, and deployment infrastructure (Phase 4)"

# Push
git push -u origin feature/integration-devops

# After PR review and approval, merge via GitHub UI or:
git checkout develop
git pull origin develop
git merge --no-ff feature/integration-devops
git push origin develop
git branch -d feature/integration-devops
git push origin --delete feature/integration-devops
```

---

**Next Step:** Run `git add .` and `git commit` to save all Phase 4 changes!
