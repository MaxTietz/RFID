$(document).ready(function(){
  $('input[type=radio]').click(function(){
    if (document.querySelector('input[name="user"]:checked').value == "new") {
      $('.existing').addClass("d-none");
      $('.new').removeClass("d-none");
    } else if (document.querySelector('input[name="user"]:checked').value == "existing") {
      $('.new').addClass("d-none");
      $('.existing').removeClass("d-none");
    }
  });
});
