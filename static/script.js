// select the search field
const SearchList = document.querySelector('#search-list')

// add a focus event listener
SearchList.addEventListener('focus',function(){
    // set the outline color to green when the field is focused
    SearchList.style.outlineColor='#00897b'
})

// add a blur event listener
SearchList.addEventListener('blur',function(){

    // set the outline color to default
    SearchList.style.outlineColor=" "
})





// change the color of the checkbox when clicked

var checkbox = document.getElementById('checkbox')

//Add a click event listener
checkbox.addEventListener('click', function(){
    checkbox.style.backgroundColor='green'
})





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
    var price = form.price.value;

    // Display error message if any of the required fields are empty
    if (!state || !school || !LGA || !hostel_name || !price) {
      document.getElementById('error-message').style.display = 'flex';
      return;
    }

    // Show page 2 and hide page 1
    document.getElementById('page-1').style.display = 'none';
    document.getElementById('page-2').style.display = 'block';
  }
}


      
          

  // image uploading

  // Get the container element for the image upload buttons and file inputs
// const imgArea = document.querySelector('.upload_div');

// // Get the list of all file input elements and buttons inside the container element
// const fileInputs = imgArea.querySelectorAll('.file');
// const uploadButtons = imgArea.querySelectorAll('.upload_btn');

// // Loop through the file input elements and buttons
// for (let i = 0; i < fileInputs.length; i++) {
//   // Get the current file input and button
//   const inputFile = fileInputs[i];
//   const selectImageButton = uploadButtons[i];

//   // Set up event listeners for the file input and button
//   selectImageButton.addEventListener('click', () => inputFile.click());
//   inputFile.addEventListener('change', () => {
//     // When a file is selected, read it as a data URL and create an image element
//     const reader = new FileReader();
//     reader.onload = () => {
//       const imgUrl = reader.result;
//       const img = document.createElement('img');
//       img.src = imgUrl;

//       // Append the image element to the container element
//       imgArea.appendChild(img);
//     };
//     reader.readAsDataURL(inputFile.files[0]);
//   });
// }


//uploading image

var uploadBtns = document.querySelector('.upload_btn')
var InputBtn = document.querySelector('.file')
 
uploadBtns.addEventListener('click',function(){
  InputBtn.click()
})