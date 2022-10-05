from Utils import SCORES_FILE_NAME


def add_score(level_difficulty):
    try:
        f = open(SCORES_FILE_NAME, "r")
        points_of_winning = f.read()
        points_of_winning += (level_difficulty * 3) + 5
    except:
        f = open(SCORES_FILE_NAME, "w")
        res = (int(level_difficulty) * 3) + 5
        f.write(str(res))
    finally:
        f.close()

