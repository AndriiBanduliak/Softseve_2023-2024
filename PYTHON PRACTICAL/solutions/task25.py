def valid_email(email):
    try:
        user_info, domain_info = email.split('@')
        if not user_info or not domain_info:
            return "Email is not valid"
        if '..' in domain_info or '.' not in domain_info:
            return "Email is not valid"
        if '_' in domain_info or '_' in user_info:
            return "Email is not valid"
        if email.count('@') > 1:
            return "Email is not valid"
        return "Email is valid"
    except ValueError:
        return "Email is not valid"
