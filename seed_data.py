# seed_data.py
from app import app, db
from models import Quiz, Question, Option


def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Option).delete()
        db.session.query(Question).delete()
        db.session.query(Quiz).delete()
        db.session.commit()

        # Create quizzes
        quizzes = [
            {
                'title': 'Chatbot automation with Python (Discord.py)',
                'description': 'Test your knowledge about creating Discord bots with Python.'
            },
            {
                'title': 'Web development with Python (Flask)',
                'description': 'Test your Flask web development skills.'
            },
            {
                'title': 'Artificial Intelligence development with Python',
                'description': 'Test your knowledge about AI concepts and Python implementations.'
            },
            {
                'title': 'Computer Vision (TensorFlow, ImageAI)',
                'description': 'Test your understanding of computer vision applications with Python.'
            },
            {
                'title': 'Natural Language Processing (BeautifulSoup, NLTK)',
                'description': 'Test your NLP knowledge and skills with Python libraries.'
            }
        ]

        for quiz_data in quizzes:
            quiz = Quiz(**quiz_data)
            db.session.add(quiz)

        db.session.commit()

        #########################################
        # Discord.py Quiz Questions (5 Soru)
        #########################################
        discord_quiz = Quiz.query.filter_by(title='Chatbot automation with Python (Discord.py)').first()
        discord_questions = [
            {
                'text': 'Which decorator is used to handle messages in Discord.py?',
                'options': [
                    {'text': '@client.command()', 'is_correct': False},
                    {'text': '@client.event()', 'is_correct': True},
                    {'text': '@client.listen()', 'is_correct': False},
                    {'text': '@client.respond()', 'is_correct': False}
                ]
            },
            {
                'text': 'What method starts the Discord bot?',
                'options': [
                    {'text': 'client.initialize()', 'is_correct': False},
                    {'text': 'client.run("TOKEN")', 'is_correct': True},
                    {'text': 'client.connect()', 'is_correct': False},
                    {'text': 'client.begin()', 'is_correct': False}
                ]
            },
            {
                'text': 'How to send a message to a channel?',
                'options': [
                    {'text': 'channel.post("Hello")', 'is_correct': False},
                    {'text': 'channel.send("Hello")', 'is_correct': True},
                    {'text': 'channel.message("Hello")', 'is_correct': False},
                    {'text': 'channel.respond("Hello")', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the default prefix for commands in Discord.py?',
                'options': [
                    {'text': '!', 'is_correct': False},
                    {'text': 'No default prefix', 'is_correct': True},
                    {'text': '/', 'is_correct': False},
                    {'text': '$', 'is_correct': False}
                ]
            },
            {
                'text': 'Which event triggers when the bot is ready?',
                'options': [
                    {'text': 'on_start()', 'is_correct': False},
                    {'text': 'on_ready()', 'is_correct': True},
                    {'text': 'on_connect()', 'is_correct': False},
                    {'text': 'on_login()', 'is_correct': False}
                ]
            }
        ]

        for question_data in discord_questions:
            question = Question(quiz_id=discord_quiz.id, text=question_data['text'])
            db.session.add(question)
            db.session.commit()
            for option_data in question_data['options']:
                option = Option(
                    question_id=question.id,
                    text=option_data['text'],
                    is_correct=option_data['is_correct']
                )
                db.session.add(option)

        #########################################
        # Flask Quiz Questions (5 Soru)
        #########################################
        flask_quiz = Quiz.query.filter_by(title='Web development with Python (Flask)').first()
        flask_questions = [
            {
                'text': 'What is Flask?',
                'options': [
                    {'text': 'A full-featured web framework', 'is_correct': False},
                    {'text': 'A micro web framework', 'is_correct': True},
                    {'text': 'A database ORM', 'is_correct': False},
                    {'text': 'A templating engine', 'is_correct': False}
                ]
            },
            {
                'text': 'Which templating engine does Flask use by default?',
                'options': [
                    {'text': 'Django Templates', 'is_correct': False},
                    {'text': 'Mako', 'is_correct': False},
                    {'text': 'Jinja2', 'is_correct': True},
                    {'text': 'Chameleon', 'is_correct': False}
                ]
            },
            {
                'text': 'How to access form data in Flask?',
                'options': [
                    {'text': 'request.args', 'is_correct': False},
                    {'text': 'request.form', 'is_correct': True},
                    {'text': 'request.data', 'is_correct': False},
                    {'text': 'request.json', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the default folder for static files in Flask?',
                'options': [
                    {'text': '/static', 'is_correct': True},
                    {'text': '/public', 'is_correct': False},
                    {'text': '/assets', 'is_correct': False},
                    {'text': '/resources', 'is_correct': False}
                ]
            },
            {
                'text': 'Which decorator is used for error handling in Flask?',
                'options': [
                    {'text': '@app.errorhandler()', 'is_correct': True},
                    {'text': '@app.fail()', 'is_correct': False},
                    {'text': '@app.catch()', 'is_correct': False},
                    {'text': '@app.exception()', 'is_correct': False}
                ]
            }
        ]

        for question_data in flask_questions:
            question = Question(quiz_id=flask_quiz.id, text=question_data['text'])
            db.session.add(question)
            db.session.commit()
            for option_data in question_data['options']:
                option = Option(
                    question_id=question.id,
                    text=option_data['text'],
                    is_correct=option_data['is_correct']
                )
                db.session.add(option)

        #########################################
        # AI Quiz Questions (5 Soru)
        #########################################
        ai_quiz = Quiz.query.filter_by(title='Artificial Intelligence development with Python').first()
        ai_questions = [
            {
                'text': 'Which library is used for machine learning in Python?',
                'options': [
                    {'text': 'Scikit-learn', 'is_correct': True},
                    {'text': 'Pandas', 'is_correct': False},
                    {'text': 'OpenCV', 'is_correct': False},
                    {'text': 'NLTK', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of a loss function?',
                'options': [
                    {'text': 'To measure model accuracy', 'is_correct': False},
                    {'text': 'To optimize model parameters', 'is_correct': True},
                    {'text': 'To visualize data', 'is_correct': False},
                    {'text': 'To preprocess data', 'is_correct': False}
                ]
            },
            {
                'text': 'Which algorithm is used for classification?',
                'options': [
                    {'text': 'Linear Regression', 'is_correct': False},
                    {'text': 'K-Means', 'is_correct': False},
                    {'text': 'Support Vector Machine (SVM)', 'is_correct': True},
                    {'text': 'PCA', 'is_correct': False}
                ]
            },
            {
                'text': 'What does "overfitting" mean?',
                'options': [
                    {'text': 'Model performs well on training data but poorly on new data', 'is_correct': True},
                    {'text': 'Model is too simple', 'is_correct': False},
                    {'text': 'Model has low accuracy', 'is_correct': False},
                    {'text': 'Model uses too much memory', 'is_correct': False}
                ]
            },
            {
                'text': 'Which activation function is commonly used in neural networks?',
                'options': [
                    {'text': 'ReLU', 'is_correct': False},
                    {'text': 'Sigmoid', 'is_correct': False},
                    {'text': 'Tanh', 'is_correct': False},
                    {'text': 'All of the above', 'is_correct': True}
                ]
            }
        ]

        for question_data in ai_questions:
            question = Question(quiz_id=ai_quiz.id, text=question_data['text'])
            db.session.add(question)
            db.session.commit()
            for option_data in question_data['options']:
                option = Option(
                    question_id=question.id,
                    text=option_data['text'],
                    is_correct=option_data['is_correct']
                )
                db.session.add(option)

        #########################################
        # Computer Vision Quiz Questions (5 Soru)
        #########################################
        cv_quiz = Quiz.query.filter_by(title='Computer Vision (TensorFlow, ImageAI)').first()
        cv_questions = [
            {
                'text': 'Which library is used for image processing in Python?',
                'options': [
                    {'text': 'OpenCV', 'is_correct': True},
                    {'text': 'NLTK', 'is_correct': False},
                    {'text': 'Pandas', 'is_correct': False},
                    {'text': 'Scikit-learn', 'is_correct': False}
                ]
            },
            {
                'text': 'What does CNN stand for?',
                'options': [
                    {'text': 'Convolutional Neural Network', 'is_correct': True},
                    {'text': 'Complex Neural Node', 'is_correct': False},
                    {'text': 'Centralized Normalization Network', 'is_correct': False},
                    {'text': 'Computer Vision Neural Net', 'is_correct': False}
                ]
            },
            {
                'text': 'Which function resizes an image in TensorFlow?',
                'options': [
                    {'text': 'tf.image.resize()', 'is_correct': True},
                    {'text': 'tf.math.resize()', 'is_correct': False},
                    {'text': 'tf.vision.scale()', 'is_correct': False},
                    {'text': 'tf.data.resize()', 'is_correct': False}
                ]
            },
            {
                'text': 'What is the purpose of pooling layers in CNN?',
                'options': [
                    {'text': 'To reduce spatial dimensions', 'is_correct': True},
                    {'text': 'To increase model complexity', 'is_correct': False},
                    {'text': 'To add more parameters', 'is_correct': False},
                    {'text': 'To normalize data', 'is_correct': False}
                ]
            },
            {
                'text': 'Which model is pre-trained for object detection in ImageAI?',
                'options': [
                    {'text': 'ResNet', 'is_correct': True},
                    {'text': 'BERT', 'is_correct': False},
                    {'text': 'GPT-3', 'is_correct': False},
                    {'text': 'YOLO', 'is_correct': False}
                ]
            }
        ]

        for question_data in cv_questions:
            question = Question(quiz_id=cv_quiz.id, text=question_data['text'])
            db.session.add(question)
            db.session.commit()
            for option_data in question_data['options']:
                option = Option(
                    question_id=question.id,
                    text=option_data['text'],
                    is_correct=option_data['is_correct']
                )
                db.session.add(option)

        #########################################
        # NLP Quiz Questions (5 Soru)
        #########################################
        nlp_quiz = Quiz.query.filter_by(title='Natural Language Processing (BeautifulSoup, NLTK)').first()
        nlp_questions = [
            {
                'text': 'What is the purpose of BeautifulSoup?',
                'options': [
                    {'text': 'Web scraping', 'is_correct': True},
                    {'text': 'Machine learning', 'is_correct': False},
                    {'text': 'Image processing', 'is_correct': False},
                    {'text': 'Data visualization', 'is_correct': False}
                ]
            },
            {
                'text': 'Which NLTK function tokenizes text into words?',
                'options': [
                    {'text': 'word_tokenize()', 'is_correct': True},
                    {'text': 'split()', 'is_correct': False},
                    {'text': 'sent_tokenize()', 'is_correct': False},
                    {'text': 'parse()', 'is_correct': False}
                ]
            },
            {
                'text': 'What are "stopwords"?',
                'options': [
                    {'text': 'Common words with little meaning', 'is_correct': True},
                    {'text': 'Grammatical errors', 'is_correct': False},
                    {'text': 'Proper nouns', 'is_correct': False},
                    {'text': 'Verb conjugations', 'is_correct': False}
                ]
            },
            {
                'text': 'Which library is used for stemming in NLTK?',
                'options': [
                    {'text': 'PorterStemmer', 'is_correct': True},
                    {'text': 'WordNetLemmatizer', 'is_correct': False},
                    {'text': 'SentimentAnalyzer', 'is_correct': False},
                    {'text': 'NGram', 'is_correct': False}
                ]
            },
            {
                'text': 'What does TF-IDF stand for?',
                'options': [
                    {'text': 'Term Frequency-Inverse Document Frequency', 'is_correct': True},
                    {'text': 'Text Filtering-Indexed Data Format', 'is_correct': False},
                    {'text': 'Tokenized Frequency-Integrated Data Field', 'is_correct': False},
                    {'text': 'Temporal Feature-Image Data Frame', 'is_correct': False}
                ]
            }
        ]

        for question_data in nlp_questions:
            question = Question(quiz_id=nlp_quiz.id, text=question_data['text'])
            db.session.add(question)
            db.session.commit()
            for option_data in question_data['options']:
                option = Option(
                    question_id=question.id,
                    text=option_data['text'],
                    is_correct=option_data['is_correct']
                )
                db.session.add(option)

        db.session.commit()
        print("Database seeded successfully!")


if __name__ == '__main__':
    seed_data()