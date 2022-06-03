import textstat
def calculate_readability(inputs_,method):
    """
    Calculates different readability measures using the textstat package.
    inputs_: input text -> list type
    method - one of the following:
    1. flesch_reading_ease, 
    2. smog_index, 
    3. flesch_kincaid_grade, 
    4. coleman_liau_index, 
    5. automated_readability_index,
    6. dale_chall_readability_score,
    7. linsear_write_formula,
    8. gunning_fog
    9. text_standard
    """
    readability_score = []
    try:
        if method == "fre":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.flesch_reading_ease(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "smog":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.smog_index(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "fkg":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.flesch_kincaid_grade(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "coleman":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.coleman_liau_index(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
        elif method == "auto":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.automated_readability_index(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "dale":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.dale_chall_readability_score(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "linsear":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.linsear_write_formula(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "gunning":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.gunning_fog(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
        elif method == "standard":
            missed = 0
            for text in inputs_:
                try:
                    readability_score.append(textstat.text_standard(str(text)))
                except:
                    missed += 1
                    readability_score.append(0)
            print("The program could not calculate score for: {}".format(missed))
            return readability_score
    except:
        print("Please use appropriate method")
            