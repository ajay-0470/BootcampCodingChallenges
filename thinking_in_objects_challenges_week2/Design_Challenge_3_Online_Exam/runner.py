"""
Design Challenge 3: Online Exam
There is an online exam to be portal, where a list of question is to be created. Every question belongs
to a category and a topic. The question can be of any type such as multiple choice question,
paragraph question, etc.
Design the OO model for the above problem statement and implement the code to
• Find out the total number of question
• List all question belonging to a topic
• List all question belonging to a topic and category
"""
from onlineexam import SubjectCategory, KnowledgeTopic, ChoiceQuestion, DescriptiveQuestion, ExamManager

programming = SubjectCategory(1, "Programming")

databases = SubjectCategory(2, "Databases")

python_topic = KnowledgeTopic(1, "Python")
sql_topic = KnowledgeTopic(2, "SQL")

exam = ExamManager()

q1 = ChoiceQuestion(
    1,
    "Which keyword is used to define a function in Python?",
    programming,

    python_topic,
    ["func", "define", "def", "function"],
    "def"
)

q2 = DescriptiveQuestion(
    2,
    "Explain lists in Python.",
    programming,
    python_topic,
    150
)

q3 = ChoiceQuestion(
    3,
    "Which command is used to retrieve data from a table?",
    databases,
    sql_topic,

    ["GET", "SELECT", "FETCH", "READ"],
    "SELECT"
)

exam.add_question(q1)
exam.add_question(q2)

exam.add_question(q3)


print("Total Questions:", exam.total_questions())

print("\nQuestions for topic Python:")
for q in exam.get_questions_by_topic("Python"):
    print( q.get_details())

print("\nQuestions for topic Python and category Programming:")
for q in exam.get_questions_by_topic_and_category("Python", "Programming"):
    print( q.get_details())
