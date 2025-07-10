''' ------- SIMPLE QUIZ APP ------- '''

def quiz():
    qn = {
        '1. Name the biggest animal on the Earth?' : 'Blue Whale',
        '2. What is the ultimate source of energy on the Earth?' : 'Sun',
        '3. How many continents are there on Earth?': '7',
        '4. What gas do plants absorb from the atmosphere?': 'Carbon Dioxide',
        '5. Who invented the telephone?': 'Alexander Graham Bell',
        '6. What is the capital of India?':  'New Delhi',
        '7. Who is known as the Father of the Nation in India?': 'Mahatma Gandhi',
        '8. How many days are there in a leap year?': '366',
        '9. What is the boiling point of water in Celsius?': '100',
        '10. Which planet is known as the Red Planet?': 'Mars',
        '11. Who wrote the national anthem of India?': 'Rabindranath Tagore',
        '12. Which is the longest river in the world?': 'Nile',
        '13. What is the currency of Japan?': 'Yen',
        '14. How many colors are there in a rainbow?': '7',
        '15. Which animal is known as the ship of the desert?': 'Camel',
        '16. What is the chemical symbol for water?': 'H2O',
        '17. Who discovered gravity?': 'Isaac Newton',
        '18. Which is the smallest continent?': 'Australia',
        '19. What is the capital of Maharashtra?': 'Mumbai',
        '20. Who invented the light bulb?': 'Thomas Edison',
        '21. How many legs does a spider have?': '8',
        '22. What do bees make?': 'Honey',
        '23. Who is the current President of India?': 'Droupadi Murmu',
        '24. What is the hardest substance on Earth?': 'Diamond',
        '25. How many states are there in India?': '28',
        '26. Which organ pumps blood in the human body?': 'Heart',
        '27. Which gas do humans breathe in for survival?': 'Oxygen',
        '28. What is the fastest land animal?': 'Cheetah',
        '29. Which bird is known for mimicking human speech?': 'Parrot',
        '30. Which festival is known as the festival of lights?': 'Diwali',
        '31. What is the largest organ in the human body?': 'Skin',
        '32. What is the square root of 144?': '12',
        '33. Who is known as the Iron Man of India?': 'Sardar Vallabhbhai Patel',
        '34. What is the capital of the USA?': 'Washington D.C.',
        '35. Who discovered electricity?': 'Benjamin Franklin',
        '36. Which Indian is known for his role in space research and was called the Missile Man?': 'APJ Abdul Kalam',
        '37. How many players are there in a cricket team?': '11',
        '38. What is the national flower of India?': 'Lotus',
        '39. Who was the first man to walk on the moon?': 'Neil Armstrong',
        '40. What is the national bird of India?': 'Peacock',
        '41. Which animal is called the King of the Jungle?': 'Lion',
        '42. What is the main source of vitamins and minerals?': 'Fruits and Vegetables',
        '43. Which part of the plant conducts photosynthesis?': 'Leaf',
        '44. Which festival marks the victory of good over evil in Hindu mythology?': 'Dussehra',
        '45. Which is the largest ocean in the world?': 'Pacific Ocean',
        '46. What is the color of chlorophyll?': 'Green',
        '47. What do we call animals that eat both plants and meat?': 'Omnivores',
        '48. Which planet is closest to the sun?': 'Mercury',
        '49. Which country gifted the Statue of Liberty to the USA?': 'France',
        '50. What is the national sport of India?': 'Hockey' 
         }
    
    return qn
print('Welcome To The Quiz Game!')
print('Here are the question(s) --\n') 

q = quiz()
score = 0 

for question, correct_answer in q.items():
    print(question)
    ans = input('Write your answer: ').strip()

    if ans.lower() == correct_answer.lower():
        print('Correct\n')
        score += 1
    else:
        print(f'Wrong! The correct answer is: {correct_answer}\n')

total_questions = len(q)
percentage = (score / total_questions) * 100

print(f'Quiz over! Your score is: {score}/{len(q)}')
print(f'Percentage: {percentage:.2f}%') 