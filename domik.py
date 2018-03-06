import random, numpy as np


def left_border(x):
    return 48.0/65.0*x+677.0/1300.0+0.1


def right_border(x):
    return -48.0/65.0*x+1637.0/1300.0+0.1


def answer_noising(answer_list, noise_level):
    noised_answers = []
    for answer in answer_list:
        noised_answer = answer
        if random.random() < noise_level:
            noised_answer = abs(noised_answer - 1)
        noised_answers.append(noised_answer)
    return noised_answers


def coords_noising(coords_list, noise_level):
    noised_coords = np.copy(coords_list)
    for point in noised_coords:
        point[0] += (random.random() - 0.5)*noise_level
        point[1] += (random.random() - 0.5)*noise_level
        while not (0 <= point[0] <= 1 and 0 <= point[1] <= 1):
            point[0] += (random.random() - 0.5)*noise_level
            point[1] += (random.random() - 0.5)*noise_level
    return noised_coords


def create_dataset(N, answer_noise=0.0, coords_noise=0.0):
    points = np.array([[random.random(), random.random()] for i in range(N)])
    answers = []
    for j in range(N):
        answer = 0
        x = points[j][0]
        y = points[j][1]
        if not (0.247 < y < 0.503 and 0.372 < x < 0.628):
            if y <= 0.75:
                if 0.175 <= x <= 0.825:
                    answer = 1
            else:
                if 0.175 <= x <= 0.5 and y <= left_border(x):
                    answer = 1
                if 0.5 <= x <= 0.825 and y <= right_border(x):
                    answer = 1
        answers.append(answer)
    points = coords_noising(points, coords_noise)
    answers = answer_noising(answers, answer_noise)
    return points, answers