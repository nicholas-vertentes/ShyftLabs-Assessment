let curPage = 'HomePage';

const sidebarOptions = document.querySelectorAll(".sidebar li");
sidebarOptions.forEach(option => option.addEventListener("click", function()
  {
    switchMenu(option.textContent)
    loadPage(option.textContent);
  }));

function loadPage(pageName) {
  // Make an AJAX request to fetch the content of the selected page
  fetch(`${pageName}.html`)
      .then(response => response.text())
      .then(data => {
          document.getElementById('content').innerHTML = data;

          if (pageName == "Students"){
           createStudentDOM(data);
          }
    
      })
      .catch(error => console.error('Error loading page:', error));
}

// Initial load (e.g., Home page)
window.onload = function () {
  loadPage(curPage);

  sidebarOptions.forEach(option =>
  {
    if (option.textContent == curPage){
      option.classList.add('active');
    }
  });
};

function switchMenu(newMenu){
  sidebarOptions.forEach(option =>
    {
      if (option.textContent == curPage){
        option.classList.remove('active');
      }
      if (option.textContent == newMenu){
        option.classList.add('active');
      }
    });
  curPage = newMenu;
}


function createStudentDOM(data){
  const studentFormFields = document.querySelectorAll(".studentForm input");
  let firstName = document.querySelector("#firstName");
  let lastName = document.querySelector("#lastName");
  let birthday = document.querySelector("#birthday");
  const studentFormSubmit = document.querySelector("#studentFormSubmit");
  
  studentFormSubmit.addEventListener("click", function() {
      if (validateStudentFormFields(studentFormFields)){
        if (validate10YearsOld(birthday.value)){

          let newStudent = {
            firstName: firstName.value,
            lastName: lastName.value,
            birthday: birthday.value
          };

          postStudentForm(newStudent, studentFormFields);
        }
        else{
          let newDiv = '<div style="margin-top: 10px; color: red;" class="newDiv">Must be at least 10</div>'
          birthday.insertAdjacentHTML('afterend', newDiv)
          birthday.classList.add('invalidInput')

          setTimeout(() => {
            const newDiv = document.querySelector('.newDiv');
              if (newDiv) {
                newDiv.remove();
              }
              birthday.classList.remove('invalidInput')
          }, 3000);
        }
      }
  });
}

function validateStudentFormFields(studentFormFields){
  allFieldsPopulated = true;

  studentFormFields.forEach(field =>{
    if (field.value == ""){
      field.classList.add('invalidInput');
      allFieldsPopulated = false;
    }
    else {
      field.classList.remove('invalidInput');
    }
  })

  return allFieldsPopulated;
}

function validate10YearsOld(birthday){
  if(calculateAge(birthday) < 10){
    return false;
  }
  
  return true;
}

function calculateAge(birthday){
  let userBirthdate = new Date(birthday);
  let curDate = new Date();

  let differenceMs = curDate - userBirthdate;

  let ageDate = new Date(differenceMs);
  let age = Math.abs(ageDate.getUTCFullYear() - 1970);

  return age;
}

function postStudentForm(newStudent, studentFormFields){
  fetch('/addStudent', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newStudent)
  })
  .then(response => response.text())
  .then(data => {
    console.log('Success:', data);

    studentFormFields.forEach(field =>{
      field.classList.add('successfulInput');
    })
    setTimeout(() => {
      studentFormFields.forEach(field =>{
        field.classList.remove('successfulInput');
      });
      loadPage(curPage);
    }, 3000); // 3000 milliseconds = 3 seconds

  })
  .catch(error => {
    console.error('Error:', error);
  });
}