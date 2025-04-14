// Quiz application functionality
document.addEventListener('DOMContentLoaded', function() {
    // Add interactivity to question cards
    const questionCards = document.querySelectorAll('.question-card');
    questionCards.forEach(card => {
        // Adding subtle hover animation
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-5px)';
            card.style.boxShadow = '0 0.5rem 1rem rgba(0, 0, 0, 0.15)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
            card.style.boxShadow = '0 0.125rem 0.25rem rgba(0, 0, 0, 0.075)';
        });
    });

    // Form validation for quiz submission
    const quizForm = document.querySelector('.quiz-form');
    if (quizForm) {
        quizForm.addEventListener('submit', (e) => {
            const radioGroups = quizForm.querySelectorAll('input[type="radio"]');
            const groupNames = new Set();

            radioGroups.forEach(radio => {
                groupNames.add(radio.name);
            });

            let allAnswered = true;
            groupNames.forEach(name => {
                const answered = quizForm.querySelector(`input[name="${name}"]:checked`);
                if (!answered) {
                    allAnswered = false;
                }
            });

            if (!allAnswered) {
                e.preventDefault();
                alert('Please answer all questions before submitting!');
            }
        });
    }
});
