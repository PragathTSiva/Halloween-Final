from crew import HalloweenPartyCrew

def run_crew():
    inputs = {
        'out_dates': ['2024-10-24', '2024-10-25', '2024-10-26', '2024-10-27'],
        'num_people': 4,
        'interests': ['Basketball', 'Rainbow Six Siege', 'Mcdonalds Food', 'Gambling'],
        'location': 'University of Illinois at Urbana-Champaign',
        'age': 21,
        'budget': 500
    }

    result = HalloweenPartyCrew().crew().kickoff(inputs=inputs)
    print(result)

run_crew()