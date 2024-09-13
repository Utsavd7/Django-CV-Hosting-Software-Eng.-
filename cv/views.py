from django.shortcuts import render

def cv_view(request):
    context = {
        'name': 'Utsav Doshi',
        'location': 'Mumbai, India',
        'phone': '+1 347-228-1955',
        'email': 'uvd2003@nyu.edu',
        'linkedin': 'https://www.linkedin.com/in/utsavd7',
        'github': 'https://github.com/Utsavd7',
        'education': [
            {'degree': 'MS in Computer Science', 'institution': 'New York University', 'honors': 'Honors: (CGPA: NA)'},
            {'degree': 'B.Tech. in Computer Science and Engineering with AI and ML', 
             'institution': 'SRM Institute of Science and Technology', 'honors': 'CGPA: 9.49/10, GPA: 3.985/4, Top 3% of the Entire Department'}
        ],
        'experience': [
        {
        'company': 'SRM’s Directorate of Learning and Development', 
        'location': 'Chennai, India', 
        'type': 'Full-time',
        'position': 'Student Developer, TA, RA', 
        'start_date': 'December 2021', 
        'end_date': 'June 2024',
        'responsibilities': [
            'Engaged in the design and development of an AI-based Automated Descriptive Answer Evaluation System using BERT and BM25 models to replace human-intervened evaluation with 98.1% accuracy.',
            'Developing and testing a mathematical model for algorithm validity, aiming for compatibility and effectiveness in evaluating answer papers for 8000 students.',
            'Teaching assistant & Research Assistant for Applied Machine Learning (18CSE481T) under University Director.'
            ]
        },
        {
        'company': 'Launchr Tech', 
        'location': 'New Delhi, India (Remote)', 
        'type': 'Internship',
        'position': 'Web Designing and Software Development Intern', 
        'start_date': 'April 2023', 
        'end_date': 'August 2023',
        'responsibilities': [
            'Develop and maintain websites with efficient updates, optimize with SEO/SEM strategies, and deliver AI tools to double website traffic, achieving a 20% global traffic engagement increase in 2023.',
            'Enhance SaaS tools for e-commerce sellers, increasing productivity and customer sales by 40%.'
            ]
        },
        {
        'company': 'Microsoft', 
        'location': 'Redmond, United States (Remote)', 
        'type': 'Mentorship',
        'position': 'Industrial Research Mentorship', 
        'start_date': 'March 2023', 
        'end_date': 'May 2023',
        'responsibilities': [
            'Mentored by the Sr. Director at Microsoft Corporation, utilizing cutting-edge technologies like the GLIDE model for Generative AI image creation, conducting weekly online meetings for insights and feedback.',
            'Initiated innovative models for generating unique images, ensuring no replication of existing artists\' content, with 96% precision.'
            ]
        },
        {
        'company': 'VCOM Technologies PVT LTD', 
        'location': 'Mumbai, India (Hybrid)', 
        'type': 'Internship',
        'position': 'Software Development Intern', 
        'start_date': 'November 2022', 
        'end_date': 'April 2023',
        'responsibilities': [
            'Implemented an AI-powered SD-WAN management system, reducing network downtime by 25% and improving performance by 30% through real-time network adjustments.',
            'Launched an AI tool optimizing WAN data transmission, reducing latency by 20% and cutting WAN-related costs by 15% with efficient bandwidth utilization.'
            ]
        },
        {
        'company': 'Blackbox', 
        'location': 'Singapore (Remote)', 
        'type': 'Part-time',
        'position': 'Machine Learning Research Team Member', 
        'start_date': 'January 2022', 
        'end_date': 'March 2022',
        'responsibilities': [
            'Collaborated with a team of five members in the development of Bayesian model cross-validation.',
            'Provided effective solutions to improve accuracy to 97.73% by analyzing data and identifying issues.'
            ]
        }   
        ],
        'skills': [
            'C, C++, Python, Java, JavaScript, HTML, CSS, SQL, R, MySQL, Oracle SQL, MongoDB, PL/SQL',
            'TensorFlow, Keras, Scikit Learn, PyTorch, Huggingface, Django, Matplotlib, Numpy, SciPy, Pandas, Tkinter, React',
            'Git, GitHub',
            'Adobe Photography Suite, Figma, Photography, Wix, UX/UI',
            'English, Hindi, French, Gujarati, Marathi'
        ],
        'projects': [
        {
            'name': 'pix2pix: Image-to-image translation', 
            'description': 'This project illustrates the process of constructing and training a pix2pix conditional generative adversarial network (cGAN). The objective of this network is to learn how to convert input images into corresponding output images.'
        },
        {
            'name': 'Computer Vision and Perception for Self-Driving Cars', 
            'description': 'A variety of techniques are included in this project, such as road segmentation, 2D object detection, object tracking, 3D data visualization, multi-task learning, and Birds Eye View.'
        },
        {
            'name': 'Bayesian Model Cross Validation Machine-Learning', 
            'description': 'Developed a Gaussian Naïve Bayes Classifier model to predict whether a person makes over 50K a year. The model yields a very good performance as indicated by the model accuracy, which was found to be 0.8083.'
        }
        ],
        'achievements': [
            'Member of International Association of Engineers',
            'Hackathons: ReskilllxSparkAR (Team 2nd position), ACM Hackathon (Faculty Team Runner up), Barclays Hackathon (Top 20/2000)',
            'Microsoft Learn Student Ambassadors, SRM - Team Advisor, Team Manager, Domain Lead, Core Team Member (2020-Present)',
            'Google Developer Students Club, SRM - Domain Lead, Core Team Member (2021-2023)',
            'Best Photography Award (2018) & Diploma, National Institute of Photography'
        ]
    }
    return render(request, 'cv/cv.html', context)
