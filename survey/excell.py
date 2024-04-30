    # excel_file = export_survey_responses_to_excel(survey_id)
    # print(f"Excel file '{excel_file}' containing survey responses has been created.")


def export_survey_responses_to_excel(survey_id):
    # Get the survey
    survey = Survey.objects.get(id=survey_id)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Create a dictionary to store question prompts and their corresponding column index
    question_column_mapping = {}

    # Write headers
    ws.append([' '])

    # Get all questions for the survey
    questions = Question.objects.filter(survey=survey)

    # Write question prompts as headers
    for idx, question in enumerate(questions, start=2):  # Starting from column 2
        ws.cell(row=1, column=idx, value=question.prompt)
        question_column_mapping[question.id] = idx

    # Get all submissions for the survey
    submissions = Submission.objects.filter(survey=survey)

    # Iterate over submissions
    for submission in submissions:
        # Get user associated with the submission
        user = submission.answer_set.first().user

        # Get user's username
        user_username = user.username

        # Write user's username in the first column
        ws.append([user_username])

        # Create a dictionary to store user's answers for each question
        user_answers_dict = {}

        # Iterate over user's answers
        for answer in submission.answer_set.all():
            # Get question and option text
            question_id = answer.option.question.id
            option_text = answer.option.text

            # Store answer for each question
            user_answers_dict[question_id] = option_text

        # Write user's answers in the corresponding columns
        for question_id, column_idx in question_column_mapping.items():
            answer_text = user_answers_dict.get(question_id, '')
            ws.cell(row=ws.max_row, column=column_idx, value=answer_text)

    # Save workbook
    file_name = f"{survey.title}_responses.xlsx"
    wb.save(file_name)

    return file_name