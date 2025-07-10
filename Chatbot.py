import difflib

def chatbot():
    print("Chatbot: Welcome! How can I help you?")

    known_inputs = {
       
        "hello": "Hi there!",
        "how are you": "Surviving engineering... one deadline at a time.",
        "what's your name": "I'm your Python chatbot.",
        "who made you": "I was coded during a last-minute project, just like most college work.",
        "thanks": "You're welcome! Always happy to help.",
        "bye": "Goodbye! Finish your work and drink water.",
        "did you complete the assignment": "Not yet, still figuring out the question itself.",
        "when is the exam": "Exams are always 'next week' until the night before.",
        "did you study for internals": "Internal marks matter only until the exam ends 😅",
        "what's your cgpa": "CGPA? It’s classified information!",
        "open book exam easy ah": "Only if you can find the answer in time 😭",
        "how to pass without studying": "Group study, 2 photocopies, 1 pen drive, and a miracle.",
        "do you sleep": "I'm a bot. Sleep is for humans who skip lectures.",
        "i am sleepy": "Same here, bro. We move.",
        "i hate online classes": "You're not alone. We all muted our pain.",
        "lab exam ready?": "As ready as I am for a viva in quantum physics.",
        "how was your viva": "I spoke in English. Ma'am replied in disappointment.",
        "why are labs so long": "Because engineers learn patience first, not code.",
        "can i bunk class": "Only if you're cool with 65% attendance and 95% regret later."
        "i love coding": "That’s the spirit! Let’s debug life together.",
        "do you know dsa": "I know it... but I still fear recursion.",
        "suggest a programming language": "Start with Python, suffer with C++, cry with Java, die with JavaScript.",
        "explain oops": "Bro even the compiler gives error when I try that.",
        "what is a pointer": "It’s that thing you avoid till 3rd year.",
        "do you like maths": "Only when it's not in engineering syllabus.",
        "what is ai": "Something smarter than us... but still fails captcha.",
        "project ideas": "Make a chatbot that understands suffering. Wait... done ✅",
         "let's do project": "Sure! But only after chai and 2 hours of procrastination.",
        "where is everyone": "Probably in canteen or running from submissions.",
        "did you eat": "Only if Maggi counts.",
        "what’s in mess today": "Disappointment, with a side of confusion.",
        "wifi down?": "Yes. Again. As expected.",
        "chai break?": "Always down for chai. Mood > syllabus.",
        "plan for weekend": "Project + movie + guilt + regret = Weekend plan.",
        "motivate me": "You’ve survived internals, labs, and system crash — you got this 💪",
        "my brain is dead": "Reboot with coffee. If that fails, fake confidence and proceed.",
        "i feel like giving up": "Don't bro. Just fake it, pass, and rest later.",
        "i'm tired": "Sleep is important. But finishing this first is more important 😉",
        "why is engineering hard": "Because you're becoming a problem solver — through suffering.",
        "life is hard": "Agreed. That’s why we vibe through it together."

    }

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print(f"Chatbot: {known_inputs['bye']}")
            break

        match = difflib.get_close_matches(user_input, known_inputs.keys(), n=1, cutoff=0.6)

        if match:
            response = known_inputs[match[0]]
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I didn’t get that. You can try typing something like:")
            for cmd in known_inputs:
                print(f"- {cmd.capitalize()}")
chatbot()
