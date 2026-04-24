from pyscript import document

class Classmate: 
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject    

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."


classmate_list = [
    Classmate("Ebtisam", "Ruby", "English"),
    Classmate("Vaughn", "Ruby", "Science"),
    Classmate("Queeny", "Ruby", "English"),
    Classmate("Samantha", "Ruby", "Math"),
    Classmate("Miguel", "Ruby", "Philosophy")
]

def add_classmate_func(event):
   
    name_input = document.querySelector('#name')
    section_input = document.querySelector('#section')
    subject_input = document.querySelector('#subject')

    if name_input.value and section_input.value and subject_input.value:
        
        new_person = Classmate(name_input.value, section_input.value, subject_input.value)
        classmate_list.append(new_person)

      
        name_input.value = ""
        section_input.value = ""
        subject_input.value = ""
        
     
        display_list(None)
    else:
        container = document.querySelector("#list-container")
        container.innerHTML = "Please fill all fields!"

def display_list(event):
    container = document.querySelector("#list-container")
    container.innerHTML = ""
    
    for person in classmate_list:
        new_div = document.createElement("div")
        new_div.style.marginBottom = "8px"
        new_div.innerText = person.introduce()
        container.appendChild(new_div)
