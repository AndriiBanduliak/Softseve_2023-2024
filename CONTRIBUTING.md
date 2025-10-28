# 🤝 Contributing Guidelines

Thank you for your interest in contributing to our Professional Development Portfolio! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)
- [Community Guidelines](#community-guidelines)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

### Prerequisites

- Git installed on your machine
- A GitHub account
- Basic knowledge of the technologies used in this project

### Fork and Clone

1. **Fork the repository**
   - Click the "Fork" button on the top right of the repository page
   - This creates a copy of the repository in your GitHub account

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/professional-development-portfolio.git
   cd professional-development-portfolio
   ```

3. **Add the original repository as upstream**
   ```bash
   git remote add upstream https://github.com/original-owner/professional-development-portfolio.git
   ```

## Development Process

### 1. Create a Branch

Always create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
# or
git checkout -b docs/update-readme
```

**Branch naming conventions:**
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Adding or updating tests

### 2. Make Your Changes

- Write clean, readable code
- Follow the coding standards outlined below
- Add comments where necessary
- Update documentation if needed

### 3. Test Your Changes

- Test your changes thoroughly
- Ensure existing functionality still works
- Run any existing tests
- Test on different browsers/devices if applicable

### 4. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add responsive navigation menu

- Implement mobile-first design approach
- Add hamburger menu for mobile devices
- Update CSS with media queries
- Test on various screen sizes"
```

**Commit message format:**
- Use imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Use the body to explain what and why, not how
- Reference issues when applicable

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Coding Standards

### HTML

- Use semantic HTML5 elements
- Include proper accessibility attributes
- Validate HTML using W3C validator
- Use consistent indentation (2 spaces)

```html
<!-- Good -->
<nav aria-label="Main navigation">
  <ul class="nav-list">
    <li><a href="/home" aria-current="page">Home</a></li>
  </ul>
</nav>

<!-- Avoid -->
<div class="nav">
  <div class="nav-item">Home</div>
</div>
```

### CSS

- Use meaningful class names
- Follow BEM methodology when appropriate
- Use CSS custom properties for theming
- Mobile-first responsive design

```css
/* Good */
.hero-section {
  padding: 2rem 1rem;
  background-color: var(--primary-color);
}

.hero-section__title {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

/* Avoid */
.div1 {
  padding: 20px 10px;
  background: #007bff;
}
```

### JavaScript

- Use modern ES6+ features
- Write descriptive variable and function names
- Add JSDoc comments for functions
- Handle errors gracefully

```javascript
/**
 * Validates user input for email format
 * @param {string} email - The email to validate
 * @returns {boolean} True if email is valid
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
```

### Python

- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Use meaningful variable names

```python
def calculate_total_price(items: list[dict], tax_rate: float = 0.08) -> float:
    """
    Calculate the total price including tax for a list of items.
    
    Args:
        items: List of dictionaries containing item prices
        tax_rate: Tax rate as a decimal (default: 0.08)
    
    Returns:
        Total price including tax
    """
    subtotal = sum(item['price'] for item in items)
    return subtotal * (1 + tax_rate)
```

## Pull Request Process

### Before Submitting

- [ ] Code follows the project's coding standards
- [ ] Self-review of your code has been performed
- [ ] Code has been commented, particularly in hard-to-understand areas
- [ ] Corresponding changes to documentation have been made
- [ ] Changes generate no new warnings or errors
- [ ] New and existing unit tests pass locally
- [ ] Any dependent changes have been merged and published

### Pull Request Template

When creating a Pull Request, please include:

1. **Description**: What changes were made and why
2. **Type of Change**: Bug fix, new feature, breaking change, etc.
3. **Testing**: How the changes were tested
4. **Screenshots**: If applicable, include before/after screenshots
5. **Checklist**: Complete the checklist above

### Review Process

1. **Automated Checks**: GitHub Actions will run automated tests
2. **Code Review**: At least one team member will review your code
3. **Feedback**: Address any feedback or requested changes
4. **Approval**: Once approved, your PR will be merged

## Issue Reporting

### Before Creating an Issue

- Check if the issue already exists
- Search through closed issues
- Verify you're using the latest version

### Creating a Good Issue

Use our issue templates when available, or include:

1. **Clear Title**: Brief description of the issue
2. **Description**: Detailed explanation of the problem
3. **Steps to Reproduce**: How to reproduce the issue
4. **Expected Behavior**: What should happen
5. **Actual Behavior**: What actually happens
6. **Environment**: OS, browser, version information
7. **Screenshots**: If applicable

### Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## Community Guidelines

### Communication

- Be respectful and inclusive
- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community

### Getting Help

- Check the documentation first
- Search existing issues and discussions
- Ask questions in a clear, specific manner
- Provide context and examples when asking for help

## Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes for significant contributions
- GitHub contributor statistics

## Questions?

If you have any questions about contributing, please:

1. Check the documentation
2. Search existing issues
3. Create a new issue with the `question` label
4. Contact the maintainers

---

Thank you for contributing to our project! 🎉