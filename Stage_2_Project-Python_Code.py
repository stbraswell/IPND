def generate_html(stage,title,description,notes,example):
    html_stage = '''
<div id="''' + stage + '''">'''
    
    html_title = '''
    <h3>''' + title + '''</h3>'''
    
    html_description = '''
    <div>
    ''' + description + '''<br>'''
    
    html_note = '''
            <ul>
''' + notes + '''
    '''+ example

    html_end = '''
            </ul>
    </div>
</div>'''
    full_html_text = html_stage + html_title + html_description + html_note + html_end
    return full_html_text

# stage = "stage 1"
# title = "title 1"
# description = "description 1"
# note = "note 1"
    
# print generate_html(stage,title,description,note)

def get_stage_id(concept):
    start_location = concept.find('STAGE:')
    end_location = concept.find('TITLE:')
    stage = concept[start_location+7 : end_location-1]
    return stage

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    if 'NOTE: ' in concept:
        start_location = concept.find('DESCRIPTION:')
        end_location = concept.find('NOTE:')
        description = concept[start_location+13 :end_location-1]
    else:
        if 'EXAMPLE:' in concept:
            start_location = concept.find('DESCRIPTION:')
            end_location = concept.find('EXAMPLE:')
            description = concept[start_location+13 :end_location-1]
    return description

def list_positions_in_string(text):                     # takes in text string and creates "list1" which contains the position of 'hello'
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
            
def stringlist(text,strings):                           #takes in text and output of list_positions_in_string, outputs the text of each position of text string
    i = 0
    textlist=[]
    length = len(strings) - 2
    while i< length:
        next_string = text[strings[i] + 6:strings[i + 1]]
        next_string = next_string.rstrip('\n')
        textlist.append(next_string)
        i += 1
    next_string = text[strings[i] + 6:text.find('EXAMPLE:')]
    next_string = next_string.rstrip('\n')
    textlist.append(next_string)
    return textlist

def get_notes(concept):
    if 'NOTE: ' not in concept:
        note_code = ''
    else:    
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

def get_example_links(concept):
    if 'EXAMPLE:' not in concept:
        link_html = ''
    else:
        start_location = concept.find('EXAMPLE:')
        end_location = concept.find('STAGE:')
        link = concept[start_location+9 :end_location-1]
        link_html = '''<li><a href="''' + link + '''"> Examples </a></li>'''
    return link_html

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

TEST_TEXT = """STAGE: stage-2-14
TITLE: Structured Data: Lists
DESCRIPTION: A list is a sequence of Anything - characters, strings, numbers...even other lists!
NOTE: Lists take the form: <list> = [<expression>,<expression>,...]
NOTE: Empty list => []
NOTE: Elements of a list start from 0 so: [0,1,2,3...]
NOTE: When defining a list, especially a long list, you can split the <expression>'s up *****example*****
NOTE: You can even index within an indexed list. i.e. list1 = [['Troy','is'],['cool','!']- print list1[1][1] => will print the 4th element of the list, in this case '!'
EXAMPLE:https://drive.google.com/open?id=0B2DsntQwDC9dZ2dwemtaYjBfTzA
STAGE: stage-2-15
TITLE: List Mutations and Aliasing
DESCRIPTION: Lists support Mutations and Aliasing.  With mutation you are able to change the value of a list after it has been created.  With Aliasing, you can assign a list to two separate names; however if you mutate the list for one, you mutate it for both. 
EXAMPLE:https://drive.google.com/open?id=0B2DsntQwDC9dS3dDTXlncnY2MG8
STAGE: stage-2-16
TITLE: List Operations
DESCRIPTION: List operations allow you to perform certain tasks on lists
NOTE: The "append" operation lets you insert another element into an existing list: <list>.append(<element>)
NOTE: The "plus" operation is like concatination for lists: [1,2] + [3,4] => [1,2,3,4]
Note: The "len" operation outputs the number of elements in a list (this also works on strings): len([0,1]) => 2
EXAMPLE:https://drive.google.com/open?id=0B2DsntQwDC9dNm56SDFETVhERjA
STAGE: STAGE-2-17
TITLE: Sructured Data: For Loops
DESCRIPTION: For loops used on lists are similar to using While loops, however they make it easier because it essentially has a built in counter: the length of the list!
NOTE: for <name> in <list>:
NOTE: <name> is essentially the variable name
NOTE: For loop on list example:
NOTE: "Index" is used to find an element within a list.  It takes the form: &lt;list&gt;.index(&lt;value&gt;)
NOTE: Index always gives the 1st found position
NOTE: Index will return an error if the value is not found
NOTE: "in" is used to determine wether or not a value is in a list.  it takes the form: &lt;value&gt; in &lt;list&gt;
NOTE: if &lt;value&gt; is in the &lt;list&gt;, output is True otherwise, output is false
NOTE: &lt;value&gt; not in &lt;list&gt; -> is the opposite of "in".
EXAMPLE:https://drive.google.com/open?id=0B2DsntQwDC9dSUhTVlEwbTVZakE
"""


def generate_all_html(text):
    text = text.replace('<','&lt;')
    text = text.replace('>','&gt;')
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        stage = get_stage_id(concept)
        title = get_title(concept)
        description = get_description(concept)
        notes = get_notes(concept)
        example = get_example_links(concept)
        #notes = "STAGE NOTE"
        concept_html = generate_html(stage,title,description,notes,example)
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
