BORDER_SIZE='2px'

// Get Specific Cookie 
function getCookie(name) {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();   
  
      if (cookie.indexOf(name + '=') === 0) {
        return cookie.substring(name.length+1);
      }
    }
    return null;
}

// Subject Clicked
function subjectClicked(subject) {
    //console.log(subject);
    const grade = getCookie('grade');
    location.href = "/subject?subject="+subject+"&grade="+grade;
}


// Load Subject Buttons
function loadSubjects() {
    fetch('files/subjects.json').then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            const subjects = json['subjects'];
            const wrapper = document.getElementsByClassName('buttons-wrapper')[0];
            for(var i=0; i<=subjects.length; i=i+2) {
                if(i+1 < subjects.length) {
                    // Get Subject Info
                    var s1 = subjects[i];
                    var s2 = subjects[i+1];

                    // Create Elements
                    var element1 = document.createElement('div');
                    var element2 = document.createElement('div');
                    
                    // Add Text
                    element1.textContent = s1['name'];
                    element1.eng = s1['eng']; 
                    element2.textContent = s2['name'];
                    element2.eng = s2['eng'];
                    
                    // Add Style
                    element1.className = "button";
                    element1.style.backgroundColor = s1['background'];
                    element1.style.border = BORDER_SIZE+' solid '+s1['outline'];

                    element2.className = "button";
                    element2.style.backgroundColor = s2['background'];
                    element2.style.border = BORDER_SIZE+' solid '+s2['outline']

                    // Determine Width
                    var num = i+1;
                    if(num%3 == 0 && num != 1) {
                        element1.style.width = '7rem';
                        element2.style.width = '8rem';
                    } else {
                        element1.style.width = '10rem';
                        element2.style.width = '5rem';
                    }
                    
                    // Append to subject-buttons
                    var subjectButtons = document.createElement('div');
                    subjectButtons.className = "subject-buttons";
                    
                    subjectButtons.appendChild(element2);
                    subjectButtons.appendChild(document.createElement('div'));
                    subjectButtons.appendChild(element1);

                    // Append to buttons-wrapper
                    wrapper.appendChild(subjectButtons);
                } else {
                    // Handle a case where the current subject is the last one on the list
                    var s1 = subjects[i];
                    var element1 = document.createElement('div');
                    element1.textContent = s1['name']; 
                    element1.eng = s1['eng'];
                    element1.className = "button";
                    element1.style.backgroundColor = s1['background'];
                    element1.style.border = BORDER_SIZE+' solid '+s1['outline'];
                    element1.style.width = '19rem'; // takes the whole line
                    var subjectButtons = document.createElement('div');
                    subjectButtons.appendChild(element1);
                    wrapper.appendChild(subjectButtons);
                }
            }
        }
    ).then(() => {
        const wrapper = document.getElementsByClassName('buttons-wrapper')[0];
        for (const childContainer of wrapper.children) {
            for (const child of childContainer.children) {
                if (child.textContent.length>0) {
                    child.onclick = () => {
                        subjectClicked(child.eng);
                    }
                }
            }
        }
    });
}