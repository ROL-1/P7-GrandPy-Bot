// Fill Empty_zone with input text
$(function() {

  var $list, $question;
  $list = $('#dialog ul');
  $question = $('#question');

  $question.on('submit', function(e) {
    e.preventDefault();
    var text = $('#question input:text').val();
    $list.append('<li>' + text + '</li>');
    $('#question input:text').val('');
  }); 

});


// Scrollspy smooth
$(function () {
  $('header a').on('click', function(e) {
  e.preventDefault();
  var hash = this.hash;
  $('html, body').animate({
    scrollTop: $(this.hash).offset().top
  }, 1000, function(){
    window.location.hash = hash;
  });
  });
});