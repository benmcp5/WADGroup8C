let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("img-div");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none"; 
  }

  slides[slideIndex-1].style.display = "block"; 
}


function outputStars(div, rating ){
  var stars = div
  var star=[5];
  for(let i = 0; i < 5;i++){
      star[i] = document.createElement("span");
      if(i<rating){
          star[i].className = 'fa fa-star checked';
      }else{
          star[i].className = 'fa fa-star';
      }
      stars.appendChild(star[i]);
  }
}