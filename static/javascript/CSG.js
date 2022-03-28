function outputStars(div, rating){
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
