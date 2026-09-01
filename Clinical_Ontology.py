# Structured knowledge base: chief complaints -> follow-up questions -> red flags
# Plus standard history sections asked for every patient regardless of complaint.

CHIEF_COMPLAINT_ONTOLOGY = {

    "chest_pain": {
        "follow_up_questions": [
            "Where exactly is the pain located?",                          
            "When did it start — suddenly or gradually?",                 
            "How would you describe the pain — sharp, dull, burning, cramping?",  
            "Does the pain spread anywhere else, like your arm, jaw, or back?",   
            "Is there anything else happening along with the pain — sweating, nausea, breathlessness?", 
            "Is the pain constant or does it come and go?",               
            "Does anything make it better or worse — rest, exertion, breathing, food?",  
            "On a scale of 1 to 10, how severe is the pain?"              
        ],
        "red_flags": [
            "chest pain with breathlessness",
            "chest pain with sweating",
            "chest pain radiating to arm or jaw",
            "chest pain with fainting or dizziness"
        ]
    },

    "fever": {
        "follow_up_questions": [
            "How many days have you had the fever?",
            "Is it continuous, or does it come and go (with chills)?",
            "Do you get chills or shivering with the fever?",
            "Have you measured the temperature — how high does it go?",
            "Any other symptoms with it — cough, body ache, rash, joint pain, loose motions?",
            "Have you taken any medication for it? Did it help?"
        ],
        "red_flags": [
            "fever with neck stiffness",
            "fever with severe headache and confusion",
            "fever with difficulty breathing",
            "fever lasting more than 7 days"
        ]
    },

    "abdominal_pain": {
        "follow_up_questions": [
            "Where in the abdomen is the pain — upper, lower, left, right, or all over?",
            "When did it start, and was it sudden or gradual?",
            "What kind of pain is it — cramping, sharp, burning, constant ache?",
            "Does the pain move or spread anywhere?",
            "Any nausea, vomiting, bloating, or change in bowel habits with it?",
            "Does eating make it better or worse?",
            "How severe is the pain on a scale of 1 to 10?"
        ],
        "red_flags": [
            "abdominal pain with rigid/board-like abdomen",
            "abdominal pain with vomiting blood",
            "abdominal pain with fainting",
            "severe pain with fever"
        ]
    },

    "breathlessness": {
        "follow_up_questions": [
            "When did the breathlessness start?",
            "Does it happen at rest, or only with exertion?",
            "Is it constant or does it come in episodes?",
            "Any associated chest pain, cough, or swelling in legs?",
            "Do you have to sit up at night to breathe comfortably?",
            "Any past history of asthma, heart disease, or lung problems?"
        ],
        "red_flags": [
            "breathlessness at rest",
            "breathlessness with chest pain",
            "breathlessness with blue lips/fingertips",
            "sudden onset severe breathlessness"
        ]
    },

    "headache": {
        "follow_up_questions": [
            "Where is the headache located — one side, both sides, front, back?",
            "When did it start, and how long does it last?",
            "How would you describe it — throbbing, dull, band-like, stabbing?",
            "Any associated symptoms — nausea, vomiting, sensitivity to light/sound, blurred vision?",
            "Does anything trigger it or make it worse?",
            "Have you had headaches like this before?"
        ],
        "red_flags": [
            "worst headache of life / sudden severe onset",
            "headache with fever and neck stiffness",
            "headache with confusion or altered consciousness",
            "headache with weakness on one side of body"
        ]
    },

    "cough": {
        "follow_up_questions": [
            "How long have you had the cough?",
            "Is it dry or does it bring up phlegm/mucus?",
            "What color is the phlegm, if any — clear, yellow, green, blood-stained?",
            "Any fever, chest pain, or breathlessness with it?",
            "Is it worse at any particular time — night, morning, with activity?",
            "Any history of smoking or TB exposure?"
        ],
        "red_flags": [
            "cough with blood",
            "cough with breathlessness",
            "cough lasting more than 2-3 weeks",
            "cough with significant unexplained weight loss"
        ]
    },
}


# Standard history sections asked for EVERY patient, regardless of complaint 

STANDARD_HISTORY_SECTIONS = {

    "past_medical_surgical_history": [
        "Do you have any long-term illnesses — diabetes, high blood pressure, thyroid, heart disease, asthma, TB?",
        "Have you had any surgeries in the past? If yes, when and for what?",
        "Have you ever been hospitalized before? For what reason?"
    ],

    "drug_and_allergy_history": [
        "Are you currently taking any medications regularly? Please name them if you can.",
        "Are you allergic to any medicines, food, or substances?",
        "Have you ever had a bad reaction to any medication?"
    ],

    "family_history": [
        "Does anyone in your immediate family have diabetes, high blood pressure, heart disease, or cancer?",
        "Any family history of similar complaints as yours?"
    ],

    "personal_history": [
        "Do you smoke or use any tobacco products? If yes, how much and for how long?",
        "Do you consume alcohol? If yes, how often?",
        "Can you describe your general diet — vegetarian/non-vegetarian, regular meal timing?",
        "What is your occupation?",
        "How is your sleep and appetite generally?",
        "For female patients: any relevant menstrual or obstetric history?"
    ],

    "review_of_systems": [
        "Any recent unexplained weight loss or weight gain?",
        "Any issues with urination — frequency, burning, blood in urine?",
        "Any issues with bowel movements — constipation, diarrhea, blood in stool?",
        "Any joint pains, swelling, or skin issues?",
        "Any recent changes in vision, hearing, or balance?"
    ],
}


# AYUSH-specific (Dashavidha Pariksha)

AYUSH_DASHAVIDHA_PARIKSHA = {
    "prakriti": "What is your basic body constitution — do you tend to be more Vata (thin, dry, anxious), Pitta (medium build, warm, irritable), or Kapha (heavy build, calm, slow digestion)?",
    "vikriti": "What imbalance or deviation from your normal state are you currently experiencing?",
    "sara": "General assessment of tissue quality/excellence.",
    "samhanana": "Assessment of body compactness/build.",
    "pramana": "Assessment of body measurements/proportions.",
    "satmya": "What foods, climates, or habits suit you well vs. don't suit you?",
    "sattva": "Assessment of mental strength/psychological resilience.",
    "ahara_shakti": "How is your digestive capacity — appetite, digestion, food tolerance?",
    "vyayama_shakti": "How much physical exertion/exercise can you comfortably tolerate?",
    "vaya": "Age-related constitutional assessment.",
}