# print(" Question 2: In which year did the Bangladesh Liberation War take place?")
# print("Answer: The Bangladesh Liberation War took place in 1971.")
questions = [
  {
    "question": "Who is known as the 'Father of the Nation' of Bangladesh?",
    "options": ["a) Tajuddin Ahmad", "b) Sheikh Mujibur Rahman", "c) Ziaur Rahman", "d) Maulana Bhashani"],
    "answer": "b"
  },
  {
    "question": "In which year did the Bangladesh Liberation War take place?",
    "options": ["a) 1970", "b) 1971", "c) 1972", "d) 1973"],
    "answer": "b"
  },
  {
    "question": "What was the code name for the military operation launched by Pakistan on the night of March 25, 1971?",
    "options": ["a) Operation Searchlight", "b) Operation Jackpot", "c) Operation Gibraltar", "d) Operation Chengiz Khan"],
    "answer": "a"
  },
  {
    "question": "Where was the provisional government of Bangladesh (Mujibnagar Government) formed?",
    "options": ["a) Dhaka", "b) Chittagong", "c) Meherpur", "d) Sylhet"],
    "answer": "c"
  },
  {
    "question": "How many highest military gallantry awards, 'Bir Sreshtho', were given out after the war?",
    "options": ["a) 5", "b) 7", "c) 11", "d) 68"],
    "answer": "b"
  },
  {
    "question": "Into how many operational 'Sectors' was Bangladesh divided during the Liberation War?",
    "options": ["a) 4", "b) 7", "c) 11", "d) 64"],
    "answer": "c"
  },
  {
    "question": "What was the name of the guerrilla resistance movement formed by Bangladeshi fighters?",
    "options": ["a) Mukti Bahini", "b) Mitra Bahini", "c) Shanti Bahini", "d) Razakar"],
    "answer": "a"
  },
  {
    "question": "Who was the Commander-in-Chief of the Bangladesh Armed Forces during the war?",
    "options": ["a) General M. A. G. Osmani", "b) Major Khaled Mosharraf", "c) Major Ziaur Rahman", "d) Air Vice Marshal A. K. Khandker"],
    "answer": "a"
  },
  {
    "question": "On which date in 1971 did the Pakistani forces officially surrender at the Ramna Race Course?",
    "options": ["a) March 26", "b) December 14", "c) December 16", "d) January 10"],
    "answer": "c"
  },
  {
    "question": "Who was the Indian Army general who signed the Instrument of Surrender alongside Pakistan's General Niazi?",
    "options": ["a) Sam Manekshaw", "b) Jagjit Singh Aurora", "c) J. F. R. Jacob", "d) K. M. Cariappa"],
    "answer": "b"
  }
]

total=len(questions)
correct=0
fail=0
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Enter your answer (a/b/c/d): ").lower()
    if user_answer == q["answer"]:
            print("Correct!")
            correct=correct+1
    else:
            print("Incorrect. The correct answer is:", q["answer"])
            fail=fail+1
print("Congratulation 🎉 you have successfully finished this Kon banega Karoropari Game first round 👋 \n Your Total answearis  ",total," From ",total," Correct Answare is ",correct," ☕ Wrong answare is ",fail,"w😴"," \n SO your Final Point is ",correct)