// $.(document).ready(function(){ 

// Submit form on Enter key press
$('#question').keypress((e) => { 
  if (this.which === 13) { 
    $('#question').submit(); 
  };
});

// Listen Form send and use POST request
$(function() {

  let $question;
  $question = $('#question');

  $question.on('submit', function(e) {
    e.preventDefault();
    $.post(
      '/api/getAnswer', // route for response file
      {
        question : $('#question input:text').val(), 
      }, // datas
      // function callback: to manage the return (alias "sucess")
      // Fill "dialog" with input text
      function(data) {
        let $list;
        $list = $('#dialog ul');
        $list.append('<li>' + data['answer'] + '</li>');
        $('#question input:text').val('');
      },
    )
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

// Mapbox
$(function () {
mapboxgl.accessToken = 'pk.eyJ1Ijoicm9sLTEiLCJhIjoiY2tncnhvOHZtMGpleTJ4cXdrenN0aGMzYSJ9.DikocYiTLvwfLSvHwD42Hw';
var map = new mapboxgl.Map({
    container: 'mapbox',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-0.50, 44.80], // starting position [lng, lat]
    zoom: 9 // starting zoom
  });
});