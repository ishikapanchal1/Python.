student_scores = {
    'joy': 55,
    'seema': 85,
    'diya': 55,
    'liza': 75,
    'dhruv': 95,
    'rohan': 60
}
highest_3 = dict(sorted(student_scores.items(), key=lambda item: item[1], reverse=True)[:3])
print("highest 3 Students with Highest Scores:")
for name, score in highest_3.items():
    print(f"{name}: {score}")

