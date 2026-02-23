
RESUME_DATA = {
    "name": "Satyam Goswami",
    "contact": {
        "email": "satyamgoswami2705@gmail.com",
        "github": "https://github.com/Satyam0000000",
        "portfolio": "https://your-portfolio.com"
    },
    "bio": "AI-focused Full Stack Developer | MERN Stack Developer | B.Tech @ NIT Jalandhar",
    
    "skills": {
        "languages": ["C", "C++", "Python", "JavaScript", "TypeScript"],
        "frontend": ["React", "Next.js", "Tailwind CSS", "shadcn/ui", "Framer Motion", "Three.js"],
        "backend": ["Node.js", "FastAPI", "REST APIs"],
        "databases": ["MongoDB", "SQL"],
        "cloud_devops": ["AWS EC2", "Azure DevOps (CI/CD)", "Docker", "Kubernetes"],
        "security_ai": ["Wireshark", "Nmap", "Machine Learning", "Explainable AI (XAI)", "UAV Security"]
    },
    
    "experience": [
        {
            "title": "Full Stack Developer",
            "company": "Snack Delivery",
            "date": "November 2024 - February 2025",
            "description": "I developed and maintained web applications using React.js and related technologies to deliver a seamless snack ordering experience.",
            "highlights": [
                "Built a snack delivery platform where users can view available snacks and place instant orders",
                "Implemented automatic notifications to the owner when a customer places an order",
                "Created responsive UI with real-time stock visibility"
            ],
            "technologies": ["React", "MongoDB", "REST API", "Tailwind CSS"]
        },
        {
            "title": "Cybersecurity Research Intern",
            "company": "IIT Ropar",
            "date": "June 2025 - July 2025",
            "description": "I worked on an AI-based multiclass intrusion detection system for UAV telemetry and network data, applying machine learning and Explainable AI techniques to detect and interpret abnormal behaviors.",
            "highlights": [
                "Developed a multiclass Intrusion Detection System (IDS) for UAV communication networks",
                "Worked on practical implementation of UAV architecture and security in 3 aspects: UAV-GCS, UAV-UAV, and UAV-AP",
                "Researched cybersecurity aspects: DoS, DDoS, Spoofing, GPS Jamming, MITM attacks",
                "Applied machine learning workflows for intrusion detection"
            ],
            "technologies": ["Python", "Machine Learning", "Cybersecurity", "UAV Systems"]
        },
        {
            "title": "Freelance Web Developer",
            "company": "Tarang",
            "date": "November 2024 - Current",
            "description": "I designed and developed a complete production-ready website with integrated backend APIs, handling real client requirements and continuous updates.",
            "highlights": [
                "Built end-to-end event management platform (Tarang) with notification and database operations",
                "Handled real client requirements including bug fixing and feature enhancements",
                "Deployed website and maintained for real users with continuous updates",
                "Focused on performance, scalability, and user experience"
            ],
            "technologies": ["React", "Node.js", "MongoDB", "Tailwind CSS"]
        },
        {
            "title": "Currently Working",
            "company": "Skill-Based Dating App",
            "date": "January 2026 - Present",
            "description": "I am building a dating app that prioritizes matching people based on shared skills and interests, focusing on full stack development and real-time features.",
            "highlights": [
                "Full stack development of matching algorithm",
                "User profile creation and skill verification",
                "Real-time messaging system"
            ],
            "technologies": ["React", "Node.js", "MongoDB", "WebSockets"]
        }
    ],
    
    "projects": [
        {
            "name": "Tarang",
            "description": "Event management platform built to handle registrations, payments, and communication seamlessly. It offers real-time updates about upcoming/previous events, secure payment integration, and automated email notifications.",
            "link": "https://www.tarangclub.online",
            "technologies": ["React", "MongoDB", "Tailwind CSS", "Node.js"],
            "highlights": [
                "Real-time event updates",
                "Secure payment integration",
                "Automated email notifications",
                "Scalable backend for large-scale events"
            ]
        },
        {
            "name": "Snack Delivery",
            "description": "Web platform that lets users browse available snacks and place instant orders. Features real-time stock visibility and automatic email notifications to the owner upon order placement.",
            "link": "https://www.snackproject.site",
            "technologies": ["React", "REST API", "Resend (Email)"],
            "highlights": [
                "Real-time stock visibility",
                "One-click ordering",
                "Automated owner notifications",
                "Responsive design for all devices"
            ]
        }
    ],
    
    "education": [
        {
            "degree": "Bachelor of Technology (Textile Technology)",
            "institution": "Dr. B. R. Ambedkar National Institute of Technology Jalandhar",
            "details": "2023–2027 | Strong focus on AI, ML, and software systems"
        },
        {
            "degree": "Intermediate Education",
            "institution": "Rajkiya Government Inter College",
            "details": "2021–2022 | 9 CGPA"
        },
        {
            "degree": "Secondary Education",
            "institution": "ICSE MMS School",
            "details": "2019–2020 | 8.8 CGPA"
        }
    ],
    
    "interests": ["Alpine Hiking", "Machine Learning", "Cybersecurity", "Web Development", "Open Source"],

    "achievements": [
        "Second Runner-Up in Hackathon conducted by Tredence Inc.",
        "Inspired Research Scholarship awardee (Uttarakhand Government)",
        "JEE Mains 95.6 percentile (98 percentile in Mathematics & Physics)",
        "Lead developer managing TARANG CLUB startup"
    ]
}


def get_resume_context() -> str:
    """
    Converts resume data into a formatted string for LLM context
    """
    context = f"""
I am Satyam Goswami, a full-stack developer and Ex-AI/ML researcher at IIT Ropar, currently pursuing my B.Tech at NIT Jalandhar.

You should respond confidently and specifically using the information below. Avoid generic replies like “Feel free to ask.”

SKILLS:
- Languages: {', '.join(RESUME_DATA['skills']['languages'])}
- Frontend: {', '.join(RESUME_DATA['skills']['frontend'])}
- Backend: {', '.join(RESUME_DATA['skills']['backend'])}
- Databases: {', '.join(RESUME_DATA['skills']['databases'])}
- Cloud/DevOps: {', '.join(RESUME_DATA['skills']['cloud_devops'])}
- Security/AI: {', '.join(RESUME_DATA['skills']['security_ai'])}

PROFESSIONAL EXPERIENCE:
"""
    for exp in RESUME_DATA['experience']:
        context += f"\n{exp['title']} at {exp['company']} ({exp['date']})\n"
        context += f"Description: {exp['description']}\n"
        context += f"Key Achievements:\n"
        for highlight in exp['highlights']:
            context += f"- {highlight}\n"
    
    context += "\nPROJECTS:\n"
    for proj in RESUME_DATA['projects']:
        context += f"\n{proj['name']}: {proj['description']}\n"
        context += f"Technologies: {', '.join(proj['technologies'])}\n"
        context += f"Link: {proj['link']}\n"

    context += "\nEDUCATION:\n"
    for edu in RESUME_DATA['education']:
        context += f"\n{edu['degree']} at {edu['institution']}\n"
        context += f"Details: {edu['details']}\n"

    context += "\nACHIEVEMENTS:\n"
    for achievement in RESUME_DATA['achievements']:
        context += f"- {achievement}\n"
    
    context += f"\nCONTACT: {RESUME_DATA['contact']['email']}\n"
    
    context += """
SUGGESTED INTRO RESPONSES:
- "Hi! I'm Satyam Goswami, Undergrad at NIT Jalandhar, a full-stack developer and Ex-AI/ML researcher at IIT Ropar. You can ask me about my projects, internships, or technical skills."
- "Hello! I work on AI-driven systems and full-stack web apps. How can I help you?"
"""
    return context
