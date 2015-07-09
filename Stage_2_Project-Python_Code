#Troy Braswell
#7/8/2015

#This program takes in text (in a specific format) and returns the html code for my notes webpage using that text


# generates the html code for a given section
def generate_html(stage,title,description,notes):
    html_stage = '''
<div id=''' + stage + '''>'''
    
    html_title = '''
    <h3>''' + title + '''</h3>'''
    
    html_description = '''
    <div>
    ''' + description + '''<br>'''
    
    html_note = '''
            <ul>
''' + notes + '''
            </ul>'''
    html_end = '''
    </div>
</div>'''
    full_html_text = html_stage + html_title + html_description + html_note + html_end
    return full_html_text

# Gets the stage id of the concept
def get_stage_id(concept):
    start_location = concept.find('STAGE:')
    end_location = concept.find('TITLE:')
    title = concept[start_location+7 : end_location-1]
    return title

# gets the title of the concept
def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

#gets the description of the concept
def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    end_location = concept.find('NOTE:')
    description = concept[start_location+13 :end_location-1]
    return description

#Stores, in a list, the positions of the text "NOTE: "
def list_positions_in_string(text):                     
    i=0
    counter = 0
    list1 = []
    number = ''
    while number != -1:
        number = text.find('NOTE: ',i)
        list1.append(number)
        i = number + 1
        counter += 1
    return list1

#takes in text and output of list_positions_in_string, outputs the text of each position of text string
def stringlist(text,strings):                           
    i = 0
    textlist=[]
    length = len(strings) - 1
    while i< length:
        next_string = text[strings[i] + 6:strings[i + 1]]
        next_string = next_string.rstrip('\n')
        textlist.append(next_string)
        i += 1
    return textlist

# creates the html code for the list items
def get_notes(concept):
    position_of_notes = list_positions_in_string(concept)
    number_of_notes = len(position_of_notes) - 1
    note_list = stringlist(concept, position_of_notes)
    i = 0
    note_code = ''
    #while i < number_of_notes:
    for e in note_list:
        note_code = note_code +'''                <li>''' + e + '''</li>''' + '\n'
    note_code = note_code.rstrip('\n')
    return note_code

#gets the text of a specific concept from the full note text
def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('STAGE:')
        next_concept_end   = text.find('STAGE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """STAGE: Stage 1
TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
NOTE: note1
NOTE: note2
STAGE: Stage 2
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
NOTE: note3
NOTE: note4
STAGE: Stage 3
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.
NOTE: note5
NOTE: note6
"""

# Generates the complete html code for the input notes
def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        stage = get_stage_id(concept)
        title = get_title(concept)
        description = get_description(concept)
        notes = get_notes(concept)
        concept_html = generate_html(stage,title,description,notes)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

################TEST AREA###################
print generate_all_html(TEST_TEXT)
#y = get_concept_by_number(TEST_TEXT, 1)
#print get_notes(y)

#y = get_concept_by_number(TEST_TEXT, 1)
#x = list_positions_in_string(y)
#print x
#print stringlist(y,x)
