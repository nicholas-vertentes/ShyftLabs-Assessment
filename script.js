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
  const firstName = document.querySelector("#firstName");
  const lastName = document.querySelector("#lastName");
  const birthday = document.querySelector("#birthday");
  const studentFormSubmit = document.querySelector("#studentFormSubmit");
  
  studentFormSubmit.addEventListener("click", function() {
      if (validateStudentFormFields()){
        if (validate10YearsOld()){
          // postStudentForm();
        }
      }
  });

  function validateStudentFormFields(){
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

  function validate10YearsOld(){
    if(calculateAge() < 10){
      return false;
    }
    
    return true;
  }

  function calculateAge(){
    let userBirthdate = new Date(birthday.value);
    let curDate = new Date();

    let differenceMs = curDate - userBirthdate;

    let ageDate = new Date(differenceMs);
    let age = Math.abs(ageDate.getUTCFullYear() - 1970);

    return age;
  }
}

