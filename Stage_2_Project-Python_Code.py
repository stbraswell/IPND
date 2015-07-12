#Generates the complete html text for the current concept
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
</div>
'''
    full_html_text = html_stage + html_title + html_description + html_note + html_end
    return full_html_text

#Generates the text for the Table of Contents links
def get_toc_html(linklist):
    toc_html ='''<!-- TOC Links
    '''
    for e in linklist:
        toc_html = toc_html + '''
        '''+ e
    toc_html = toc_html +'''
    -->'''
    return toc_html

#Gets the text of the "Stage ID" from the current concept
def get_stage_id(concept):
    start_location = concept.find('STAGE:')
    end_location = concept.find('TITLE:')
    stage = concept[start_location+7 : end_location-1]
    stage = stage.lower()
    return stage

#Gets the text of the "Title" from the current concept
def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

#Gets the text of the "Description" from the current concept
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

# takes in the text of the current concept and creates "list1" which contains the positions of the text 'NOTE: '
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

#takes in the text of the current concept and output of list_positions_in_string, outputs the text string of each NOTE as a list          
def stringlist(text,strings):
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

#formats the NOTE's in the current concept as a list
def get_notes(concept):
    if 'NOTE: ' not in concept:
        note_code = ''
    else:    
        position_of_notes = list_positions_in_string(concept)
        number_of_notes = len(position_of_notes) - 1
        note_list = stringlist(concept, position_of_notes)
        i = 0
        note_code = ''
        for e in note_list:
            note_code = note_code +'''            <li>''' + e + '''</li>''' + '\n'
        note_code = note_code.rstrip('\n')
    return note_code

#Gets the URL of the examples and returns the html code to genereate the link
def get_example_links(concept,title):
    if 'EXAMPLE:' not in concept:
        link_html = ''
    else:
        start_location = concept.find('EXAMPLE:')
        end_location = concept.find('STAGE:')
        link = concept[start_location+8 :end_location-1]
        link_html = '''        <li><a href="''' + link + '''"> Examples of ''' + title + '''</a></li>'''
    return link_html

#Takes in the full input text and which concept number is needed; outputs the text of only that specific concept
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

TEST_TEXT = """STAGE: STAGE-2-14
TITLE: Structured Data: Lists
DESCRIPTION: A list is a sequence of Anything - characters, strings, numbers...even other lists!
NOTE: Lists take the form: <list> = [<expression>,<expression>,...]
NOTE: Empty list => []
NOTE: Elements of a list start from 0 so: [0,1,2,3...]
NOTE: When defining a list, especially a long list, you can split the <expression>'s up
NOTE: You can even index within an indexed list. i.e. list1 = [['Troy','is'],['cool','!']- print list1[1][1] => will print the 2nd element of the 2nd list in the list, in this case '!'
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
STAGE: stage-2-17
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
STAGE: stage-2-18
TITLE: Problem Solving
DESCRIPTION: Problem solving isn't just about understanding the problem, it's also about understanding how to solve it.  Breaking the porblem up into multiple part and tackling the smaller parts one at a time makes it eaiser. Understanding the inputs and outputs is a must, but understanding the relationship between them is KEY!
NOTE: Rule 0: Don't Panic
NOTE: Rule 1: What are the inputs (and how are they represented)?
NOTE: Rule 2: What are the outputs?
NOTE: Rule 3: Solve the Problem!
NOTE: Simple Mechanical Solution
NOTE: 
EXAMPLE:https://drive.google.com/open?id=0B2DsntQwDC9dfmRvcjhSYlAyeEhQbEZ1Wm9xYzE3M3pyeVJrQUtIS3RRemZMYzFoMXM1a3c
"""

# generates the full html code for the complete input text
def generate_all_html(text):
    text = text.replace('<','&lt;')
    text = text.replace('>','&gt;')
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    all_toc_links = []
    current_toc_link = ''
    while concept != '':
        stage = get_stage_id(concept)
        title = get_title(concept)
        description = get_description(concept)
        notes = get_notes(concept)
        example = get_example_links(concept,title)
        concept_html = generate_html(stage,title,description,notes,example)
        all_html = all_html + concept_html
        current_toc_link = '''<li><a href="#''' + stage + '''">''' + title + '''</a></li>'''
        all_toc_links.append(current_toc_link)
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    toc_links = get_toc_html(all_toc_links)
    all_html = all_html + toc_links
    return all_html


print generate_all_html(TEST_TEXT)

