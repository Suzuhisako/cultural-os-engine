"""
Cultural OS Scenario Router
This module intercepts raw user scenarios, categorizes them into one of the 
15 Cultural OS pairings, and injects hyper-specific compliance constraints.
"""

SCENARIO_TARGET_MAP = {
    # 1. Employment & Separation
    "termination_vs_severance": {
        "keywords": ["firing", "layoff", "severance", "dismissal", "termination", "redundancy", "let go"],
        "forced_constraints": "exact geographic labor laws, statutory severance pay formulas, mandatory notice periods, and unfair dismissal protections"
    },
    # 2. Time & Boundaries
    "overtime_vs_wellbeing": {
        "keywords": ["overtime", "weekend work", "working hours", "burnout", "rest days", "right to disconnect", "after hours"],
        "forced_constraints": "local statutory working hour limits, mandatory rest period durations, regional overtime compensation rates, and right-to-disconnect legislation"
    },
    # 3. Compliance & Ethics
    "gift_giving_vs_bribery": {
        "keywords": ["gift", "entertainment", "hospitality", "dinner", "token of appreciation", "bribe", "kickback", "favor"],
        "forced_constraints": "regional corporate anti-bribery laws, statutory compliance thresholds for business gifts, and local corporate governance etiquette"
    },
    # 4. Compensation & Equity
    "pay_equity_vs_market_rate": {
        "keywords": ["salary", "wage transparency", "pay gap", "minimum wage", "market rate", "compensation", "bonus structure"],
        "forced_constraints": "local pay transparency laws, gender pay gap reporting mandates, statutory minimum wage rates, and local compensation norms"
    },
    # 5. Remote & Workplace Flexibility
    "remote_monitoring_vs_privacy": {
        "keywords": ["remote work", "work from home", "wfh", "monitoring", "surveillance", "spyware", "tracking", "keystroke"],
        "forced_constraints": "regional employee data privacy laws (e.g., GDPR/local variants), statutory limitations on workplace surveillance, and remote worker rights"
    },
    # 6. Workplace Safety & Health
    "sick_leave_vs_productivity": {
        "keywords": ["sick leave", "medical certificate", "illness", "mental health day", "absence", "time off for health"],
        "forced_constraints": "local statutory paid sick leave allocations, mandatory medical certificate requirements, and employer obligations regarding long-term illness"
    },
    # 7. Leaves of Absence
    "parental_leave_vs_career_progression": {
        "keywords": ["maternity leave", "paternity leave", "parental leave", "childcare leave", "nursing leave", "pregnancy"],
        "forced_constraints": "exact statutory parental and maternity leave durations, government-funded wage allowances, and regional job protection laws for returning parents"
    },
    # 8. Workplace Conduct
    "harassment_reporting_vs_retaliation": {
        "keywords": ["harassment", "bullying", "discrimination", "whistleblower", "retaliation", "reporting culture", "toxic"],
        "forced_constraints": "local anti-harassment statutes, legal whistleblower protection frameworks, and employer liabilities regarding hostile work environments"
    },
    # 9. Performance Management
    "pip_vs_constructive_dismissal": {
        "keywords": ["pip", "performance plan", "underperformance", "written warning", "probation", "coaching"],
        "forced_constraints": "local legal standards for performance improvement plans, documentation burdens of proof, and regional definitions of constructive dismissal"
    },
    # 10. Diversity & Inclusion
    "quota_mandates_vs_meritocracy": {
        "keywords": ["quota", "diversity target", "board representation", "affirmative action", "hiring bias", "inclusion metric"],
        "forced_constraints": "national or regional diversity quota mandates, statutory employment equity laws, and legally permitted positive action boundaries"
    },
    # 11. Contractual Agreements
    "non_compete_vs_freedom_of_career": {
        "keywords": ["non-compete", "nda", "non-disclosure", "poaching", "exclusivity", "moonlighting"],
        "forced_constraints": "local enforceability of non-compete clauses, statutory geographic or time limitations, and regional laws protecting employee mobility"
    },
    # 12. Collective Bargaining
    "unionization_vs_management_direct_drive": {
        "keywords": ["union", "collective bargaining", "strike", "labor council", "works council", "syndicate"],
        "forced_constraints": "regional works council formation thresholds, statutory union protections, collective bargaining agreement extensions, and local strike laws"
    },
    # 13. Data & Intellectual Property
    "ip_ownership_vs_creator_rights": {
        "keywords": ["intellectual property", "patent", "copyright", "invention", "source code", "proprietary code"],
        "forced_constraints": "local statutory definitions of employee-created inventions, mandatory inventor remuneration laws, and default IP assignment terms"
    },
    # 14. Holiday & Religious Accommodations
    "statutory_holidays_vs_business_continuity": {
        "keywords": ["public holiday", "annual leave", "religious accommodation", "vacation days", "paid time off", "pto"],
        "forced_constraints": "statutory minimum annual leave allocations, mandatory holiday premium pay rates, and legal frameworks for religious accommodation requests"
    },
    # 15. Independent Contracting
    "freelancer_vs_disguised_employment": {
        "keywords": ["contractor", "freelancer", "gig worker", "misclassification", "sole proprietor", "independent consultant"],
        "forced_constraints": "local statutory classification tests (e.g., control or economic dependence checks), penalties for disguised employment, and gig worker protection laws"
    }
}

def build_precision_engine_prompt(user_scenario: str, target_country: str) -> str:
    """
    Scans the user input against the 15 Cultural OS pairings, extracts 
    the mandatory regulatory anchors, and outputs a highly targeted prompt.
    """
    cleaned_input = user_scenario.lower()
    
    # Default safety anchors if no keyword matches perfectly
    selected_constraints = "applicable statutory labor standards, local compliance frameworks, and established regional corporate customs"
    detected_framework_pairing = "General Compliance Context"
    
    # Sequential scanning across all 15 custom pairings
    for pairing, config in SCENARIO_TARGET_MAP.items():
        if any(keyword in cleaned_input for keyword in config["keywords"]):
            selected_constraints = config["forced_constraints"]
            detected_framework_pairing = pairing
            break # Stop at the first precise match to avoid cross-triggers
            
    # Compile the final structured prompt for the search/generation engine
    precision_prompt = (
        f"You are operating as a precise localized compliance engine for: {target_country}.\n"
        f"User Scenario Input: '{user_scenario}'\n\n"
        f"CRITICAL ENGINE PARAMETERS:\n"
        f"1. You must cross-reference current and exact {selected_constraints} within {target_country}.\n"
        f"2. Do not offer generalized advice. Extract the concrete legal, statutory, or cultural boundaries relevant to this scenario.\n"
        f"3. Note: This scenario falls under the Cultural OS architecture bucket: [{detected_framework_pairing}]."
    )
    
    return precision_prompt