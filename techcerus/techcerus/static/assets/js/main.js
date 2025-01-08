// declarations of constants and variables
var navLinks = document.getElementsByClassName('navLinks');
const humburgerBtn = document.getElementById('humburgerBtn');
const navSmall = document.getElementById('navSmall');


// event listeners
for (var i = 0; i < navLinks.length; i++) {
  navLinks[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}

humburgerBtn.addEventListener('click', ()=> {
  if(navSmall.classList.contains('d-none')) {
    navSmall.classList.remove('d-none');
    navSmall.classList.add('d-block');
  }

  else if (navSmall.classList.contains('d-block')) {
    navSmall.classList.remove('d-block');
    navSmall.classList.add('d-none');
  }
});