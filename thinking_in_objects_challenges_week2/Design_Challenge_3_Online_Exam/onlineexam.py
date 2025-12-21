class SubjectCategory:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name


class KnowledgeTopic:
    def __init__(self, topic_id, topic_name):
        self.topic_id = topic_id
        self.topic_name = topic_name


class BaseQuestion:
    def __init__(self, question_id, question_text, category, topic):
        self.question_id = question_id
        self.question_text = question_text

        self.category = category
        self.topic = topic

    def get_details(self):
        return self.question_text


class ChoiceQuestion(BaseQuestion):
    def __init__(self, question_id, question_text, category, topic, options, correct_option):
        super().__init__(question_id, question_text, category, topic)
        self.options = options

        self.correct_option = correct_option


class DescriptiveQuestion(BaseQuestion):
    def __init__(self, question_id, question_text, category, topic, word_limit):

        super().__init__(question_id, question_text, category, topic)
        self.word_limit = word_limit


class ExamManager:
    def __init__(self):
        self.questions = []


    def add_question(self, question):
        self.questions.append(question)

    def total_questions(self):
        return len(self.questions)

    def get_questions_by_topic(self, topic_name):
        result = []
        for question in self.questions:
            if question.topic.topic_name == topic_name:
                result.append(question)
        return result



    def get_questions_by_topic_and_category(self, topic_name, category_name):
        result = []
        for question in self.questions:
            if question.topic.topic_name == topic_name and question.category.category_name == category_name:
                result.append(question)
        return result
