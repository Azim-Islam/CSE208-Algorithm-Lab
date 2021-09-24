#list of available notes
notes = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
notes.reverse()
print(f"Available notes {notes}")

amount = 1730
number_of_notes = 0

for note_value in notes:
    if amount//note_value >= 1: #5/2 = 2.5 and 5//2 = 2
        number_of_notes += amount//note_value
        print(f"Number of {note_value} taka notes required : {amount//note_value}")
        amount -= amount//note_value * note_value
        
print(f"Number of notes required = {number_of_notes}")