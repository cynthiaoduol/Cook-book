$(document).ready(function() {
  $(".overlay").mouseover(function(){
    $(".btn-hidden").slideDown();
  });

  $(".overlay").mouseout(function(){
    $(".btn-hidden").slideUp();
  });


});