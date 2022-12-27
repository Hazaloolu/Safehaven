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


//close the error message
var closeBtn = document.getElementById('close_btn') 
var errMsg = document.getElementById('error-message')

      // Add a click event listener to the "close" button
      closeBtn.addEventListener('click', function() {
            // Hide the error message
      errMsg.style.display = 'none';
      });






      
          

