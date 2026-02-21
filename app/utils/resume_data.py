"""
Resume knowledge base for the AI agent
This data is used to provide context-aware responses about Satyam's experience
"""

RESUME_DATA = {
    "name": "Satyam Goswami",
    "contact": {
        "email": "satyamgoswami2705@gmail.com",
        "github": "https://github.com/Satyam0000000",
        "portfolio": "https://your-portfolio.com"
    },
    "bio": "Full Stack Developer and Cybersecurity Enthusiast | Intelligent Systems Integration | Alpine Hiker",
    
    "skills": {
        "languages": ["Python", "JavaScript", "TypeScript", "HTML", "CSS"],
        "frontend": ["React JS", "React Router", "Tailwind CSS", "Framer Motion", "Three.js", "React Three Fiber"],
        "backend": ["Node.js", "FastAPI", "REST APIs"],
        "databases": ["MongoDB"],
        "devops": ["Git", "Docker", "Vite"],
        "tools": ["Figma"],
        "other": ["Machine Learning", "Cybersecurity", "UAV Systems"]
    },
    
    "experience": [
        {
            "title": "Full Stack Developer",
            "company": "Snack Delivery",
            "date": "November 2024 - February 2025",
            "description": "Developing and maintaining web applications using React.js and other related technologies.",
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
            "description": "Conducted research on cybersecurity for UAV communication networks.",
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
            "description": "Designed and developed a complete production-ready website with integrated backend APIs.",
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
            "description": "Building a dating app that prioritizes matching people based on shared skills and interests.",
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
            "degree": "Computer Science Engineering",
            "institution": "Chandigarh University",
            "details": "Specialized in AI/ML and Cybersecurity"
        }
    ],
    
    "interests": ["Alpine Hiking", "Machine Learning", "Cybersecurity", "Web Development", "Open Source"]
}


def get_resume_context() -> str:
    """
    Converts resume data into a formatted string for LLM context
    """
    context = f"""
I am {RESUME_DATA['name']}, a {RESUME_DATA['bio']}.

SKILLS:
- Languages: {', '.join(RESUME_DATA['skills']['languages'])}
- Frontend: {', '.join(RESUME_DATA['skills']['frontend'])}
- Backend: {', '.join(RESUME_DATA['skills']['backend'])}
- Databases: {', '.join(RESUME_DATA['skills']['databases'])}
- DevOps/Tools: {', '.join(RESUME_DATA['skills']['devops'] + RESUME_DATA['skills']['tools'])}

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
    
    context += f"\nCONTACT: {RESUME_DATA['contact']['email']}\n"
    
    return context
