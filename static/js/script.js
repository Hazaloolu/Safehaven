var navbar = document.querySelector('.navbar');
navbar.style.display = 'none';
    var menu = document.querySelector('#menu')
menu.addEventListener('click', function () {
  if (navbar.style.display === 'none') {
    navbar.style.display = 'block';
    navbar.classList.add('fade-in');
  } else {
    navbar.style.display = 'none';
    navbar.classList.remove('fade-in');
  }
});







// Get all FAQ toggle buttons
const faqToggles = document.querySelectorAll('.faq-toggle');

// Add click event listeners to each button
faqToggles.forEach((toggle) => {
  toggle.addEventListener('click', () => {
    const faqAnswer = toggle.parentElement.nextElementSibling;

    // Toggle the active class on the clicked button
    toggle.classList.toggle('active');

    // Toggle the display of the answer
    if (faqAnswer.style.display === 'none') {
      faqAnswer.style.display = 'block';
    } else {
      faqAnswer.style.display = 'none';
    }
  });
});






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









// Mobile view navbar

var navbar = document.querySelector('.navbar');
navbar.style.display = 'none';
    var menu = document.querySelector('#menu')
menu.addEventListener('click', function () {
  if (navbar.style.display === 'none') {
    navbar.style.display = 'block';
    navbar.classList.add('fade-in');
  } else {
    navbar.style.display = 'none';
    navbar.classList.remove('fade-in');
  }
});