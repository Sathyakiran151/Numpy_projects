import numpy as np

# Input marks
marks = np.array(list(map(int, input("Enter student marks: ").split())))

print("\nMarks:", marks)

# Mean
mean_marks = np.mean(marks)
print("Mean:", mean_marks)

# Median
median_marks = np.median(marks)
print("Median:", median_marks)

# Standard deviation
std_marks = np.std(marks)
print("Standard Deviation:", std_marks)

# Highest and lowest
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Students above average
above_avg = marks[marks > mean_marks]
print("Marks above average:", above_avg)

# Count above average
print("Number of students above average:", above_avg.size)