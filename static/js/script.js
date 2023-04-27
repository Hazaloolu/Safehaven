function openCity(evt, stepName) {
  // hide all tab content sections
  document.querySelectorAll('.tabcontent').forEach(function (tab) {
    tab.style.display = 'none';
  });

  // remove the "active" class from all tab links
  document.querySelectorAll('.tablinks').forEach(function (tab) {
    tab.classList.remove('active');
  });

  // show the tab content with the specified stepName ID
  document.getElementById(stepName).style.display = 'block';

  // add the "active" class to the clicked tab link
  evt.currentTarget.classList.add('active');
}
// Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();



// select the search field
const SearchList = document.querySelector('#search-list')

// add a focus event listener
SearchList.addEventListener('focus', function () {
  // set the outline color to green when the field is focused
  SearchList.style.outlineColor = '#00897b'
})

// add a blur event listener





// change the color of the checkbox when clicked





// Add accomodation page

function showPage(pageNumber) {
  if (pageNumber == 1) {
    // Show page 1 and hide page 2
    document.getElementById('page-1').style.display = 'block';
    document.getElementById('page-2').style.display = 'none';
  } else if (pageNumber == 2) {
    // Validate form fields on page 1
    var form = document.forms[0];
    var state = form.state.value;
    var school = form.school.value;
    var LGA = form.LGA.value;
    var hostel_name = form.Hostel_name.value;
    var address = form.Address.value;

    // Display error message if any of the required fields are empty
    if (!state || !school || !LGA || !hostel_name || !address) {
      document.getElementById('error-message').style.display = 'flex';
      return;
    }

    // Show page 2 and hide page 1
    document.getElementById('page-1').style.display = 'none';
    document.getElementById('page-2').style.display = 'block';
  }
}


//close the error message
var closeBtn = document.getElementById('close_btn')
var errMsg = document.getElementById('error-message')

// Add a click event listener to the "close" button
closeBtn.addEventListener('click', function () {
  // Hide the error message
  errMsg.style.display = 'none';
});


// Upload image
  
const selectBtn = document.querySelectorAll('.upload_btn')
const inputFile = document.querySelectorAll('.file')
const imgArea = document.querySelectorAll('.img-area')

selectBtn.forEach((btn, index) => {
  btn.addEventListener('click', function() {
    inputFile[index].click()
  })
})

inputFile.forEach((file, index) => {
  file.addEventListener('change', function(){
    const image = this.files[0]
    console.log(image)
    const reader = new FileReader();
    reader.onload = () =>{
      const imgUrl = reader.result
      const img = document.createElement('img');
      img.src = imgUrl;
      img.title = image.name; // set the title attribute to the file name
      imgArea[index].appendChild(img)
    }
    reader.readAsDataURL(image) 
  })
})







// nav bar profile card display

var card = document.querySelector('.profile-card');
card.style.display = 'none';

var showButton = document.querySelector('#show');
showButton.addEventListener('click', function () {
  if (card.style.display === 'none') {
    card.style.display = 'block';
    card.classList.add('fade-in');
  } else {
    card.style.display = 'none';
    card.classList.remove('fade-in');
  }
});





var currentURL = window.location.protocol + '//' + window.location.host + window.location.pathname;
console.log(currentURL)






