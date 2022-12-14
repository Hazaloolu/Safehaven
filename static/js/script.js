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





  