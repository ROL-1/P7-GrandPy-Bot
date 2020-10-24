$(function() {

    var $list, $question;
    $list = $('ul');
    $question = $('#question');
  
    $question.on('submit', function(e) {
      e.preventDefault();
      var text = $('input:text').val();
      $list.append('<li>' + text + '</li>');
      $('input:text').val('');
    }); 

  });