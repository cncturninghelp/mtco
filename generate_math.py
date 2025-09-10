import csv
import random

def generate_multiplication_tables():
    """Generate multiplication facts from 2x2 to 20x20"""
    questions = []
    
    for i in range(2, 21):
        for j in range(2, 21):
            answer = i * j
            
            # Generate believable wrong answers
            wrong_options = []
            
            # Add nearby products
            if i > 1:
                wrong_options.append((i-1) * j)
            if i < 20:
                wrong_options.append((i+1) * j)
            if j > 1:
                wrong_options.append(i * (j-1))
            if j < 20:
                wrong_options.append(i * (j+1))
            
            # Add common mistakes
            wrong_options.append(answer - 10)
            wrong_options.append(answer + 10)
            wrong_options.append(answer - 1)
            wrong_options.append(answer + 1)
            
            # Filter out invalid or duplicate answers
            wrong_options = list(set([w for w in wrong_options if w > 0 and w != answer]))
            
            # Randomly select 3 wrong answers
            if len(wrong_options) >= 3:
                selected_wrongs = random.sample(wrong_options, 3)
            else:
                # Fallback if not enough options
                selected_wrongs = wrong_options + [answer + 20, answer + 30, answer - 20]
                selected_wrongs = [w for w in selected_wrongs if w > 0 and w != answer][:3]
            
            # Determine difficulty
            if i <= 10 and j <= 10:
                difficulty = "easy"
            elif i <= 12 and j <= 12:
                difficulty = "medium"
            elif i <= 15 and j <= 15:
                difficulty = "hard"
            else:
                difficulty = "very hard"
            
            questions.append({
                "prompt": f"{i} x {j}",
                "answer": str(answer),
                "choices": "|".join(map(str, selected_wrongs)),
                "topic": "Multiplication",
                "family": f"Times_{i}",
                "difficulty": difficulty,
                "explain": f"{i} times {j} equals {answer}"
            })
    
    return questions

def generate_addition_problems(count=200):
    """Generate addition problems with varying difficulty"""
    questions = []
    
    # Easy additions (sum < 100)
    for _ in range(count // 3):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        answer = a + b
        
        wrongs = [
            answer - 10, answer + 10,
            answer - 1, answer + 1,
            answer - 5, answer + 5
        ]
        wrongs = [w for w in wrongs if w > 0 and w != answer]
        selected_wrongs = random.sample(wrongs, min(3, len(wrongs)))
        
        questions.append({
            "prompt": f"{a} + {b}",
            "answer": str(answer),
            "choices": "|".join(map(str, selected_wrongs)),
            "topic": "Addition",
            "family": "Addition_Easy",
            "difficulty": "easy",
            "explain": ""
        })
    
    # Medium additions (sum 100-500)
    for _ in range(count // 3):
        a = random.randint(50, 250)
        b = random.randint(50, 250)
        answer = a + b
        
        wrongs = [answer - 10, answer + 10, answer - 100, answer + 100]
        selected_wrongs = random.sample(wrongs, 3)
        
        questions.append({
            "prompt": f"{a} + {b}",
            "answer": str(answer),
            "choices": "|".join(map(str, selected_wrongs)),
            "topic": "Addition",
            "family": "Addition_Medium",
            "difficulty": "medium",
            "explain": ""
        })
    
    # Hard additions (sum > 500)
    for _ in range(count - 2 * (count // 3)):
        a = random.randint(200, 999)
        b = random.randint(200, 999)
        answer = a + b
        
        wrongs = [answer - 10, answer + 10, answer - 100, answer + 100]
        selected_wrongs = random.sample(wrongs, 3)
        
        questions.append({
            "prompt": f"{a} + {b}",
            "answer": str(answer),
            "choices": "|".join(map(str, selected_wrongs)),
            "topic": "Addition",
            "family": "Addition_Hard",
            "difficulty": "hard",
            "explain": ""
        })
    
    return questions

def generate_subtraction_problems(count=200):
    """Generate subtraction problems"""
    questions = []
    
    for i in range(count):
        # Ensure positive results
        a = random.randint(50, 1000)
        b = random.randint(1, a - 1)
        answer = a - b
        
        wrongs = [
            answer - 10, answer + 10,
            answer - 1, answer + 1,
            a + b  # Common mistake: adding instead
        ]
        wrongs = [w for w in wrongs if w > 0 and w != answer]
        selected_wrongs = random.sample(wrongs, min(3, len(wrongs)))
        
        difficulty = "easy" if answer < 100 else "medium" if answer < 500 else "hard"
        
        questions.append({
            "prompt": f"{a} - {b}",
            "answer": str(answer),
            "choices": "|".join(map(str, selected_wrongs)),
            "topic": "Subtraction",
            "family": f"Subtraction_{difficulty.capitalize()}",
            "difficulty": difficulty,
            "explain": ""
        })
    
    return questions

def generate_division_problems(count=100):
    """Generate division problems with whole number results"""
    questions = []
    
    # Generate divisions that result in whole numbers
    for _ in range(count):
        divisor = random.randint(2, 20)
        quotient = random.randint(2, 50)
        dividend = divisor * quotient
        
        wrongs = [
            quotient - 1, quotient + 1,
            quotient - 2, quotient + 2,
            quotient - 10, quotient + 10
        ]
        wrongs = [w for w in wrongs if w > 0 and w != quotient]
        selected_wrongs = random.sample(wrongs, 3)
        
        difficulty = "easy" if quotient <= 10 else "medium" if quotient <= 25 else "hard"
        
        questions.append({
            "prompt": f"{dividend} / {divisor}",
            "answer": str(quotient),
            "choices": "|".join(map(str, selected_wrongs)),
            "topic": "Division",
            "family": f"Division_{difficulty.capitalize()}",
            "difficulty": difficulty,
            "explain": f"{dividend} divided by {divisor} equals {quotient}"
        })
    
    return questions

def save_to_csv(questions, filename="math_facts.csv"):
    """Save questions to CSV file - using ASCII encoding to avoid issues"""
    with open(filename, 'w', newline='', encoding='ascii', errors='replace') as f:
        fieldnames = ['prompt', 'answer', 'choices', 'topic', 'family', 'difficulty', 'explain']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(questions)
    print(f"Saved {len(questions)} questions to {filename}")

# Generate all questions
all_questions = []

print("Generating multiplication tables...")
all_questions.extend(generate_multiplication_tables())

print("Generating addition problems...")
all_questions.extend(generate_addition_problems(200))

print("Generating subtraction problems...")
all_questions.extend(generate_subtraction_problems(200))

print("Generating division problems...")
all_questions.extend(generate_division_problems(100))

# Shuffle all questions to mix topics
random.shuffle(all_questions)

# Save to CSV
save_to_csv(all_questions)

print(f"\nTotal questions generated: {len(all_questions)}")
print(f"Topics included: Multiplication (2-20), Addition, Subtraction, Division")
print(f"File saved as: math_facts.csv")