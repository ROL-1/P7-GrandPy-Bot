// $.(document).ready(function(){ 

// Submit form on Enter key press
$('#question').keypress((e) => { 
  if (this.which === 13) { 
    $('#question').submit(); 
  };
});

// Fill "dialog" with input text
function Insert_dialog(data) {
  let $list;
  $list = $('#dialog ul');
  $list.append('<li>' + "Votre question : " + data['answer'] + '</li>');
  // $list.append('<li>' + data['geo_coord_results'] + '</li>');
  $list.append('<li>' + "L'adresse est la suivante : " + data['geo_adress_results'] + '</li>');
  $list.append('<li>' + "Et pour votre information : " + data['wiki_results'] + '</li></br>');  
};

// Mapbox
function Mapbox(data) {
  mapboxgl.accessToken = 'pk.eyJ1Ijoicm9sLTEiLCJhIjoiY2tncnhvOHZtMGpleTJ4cXdrenN0aGMzYSJ9.DikocYiTLvwfLSvHwD42Hw';
  var map = new mapboxgl.Map({
    container: 'mapbox',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: data['geo_coord_results'], // [-0.50, 44.80], // starting position [lng, lat]
    zoom: 9 // starting zoom
  });
  var marker = new mapboxgl.Marker()
    .setLngLat(data['geo_coord_results'])
    .addTo(map);
};

// Listen Form send and use POST request
$(function() {
  $('#question').on('submit', function(e) {
    $('#loading').show();
    e.preventDefault();
    $.post(
      '/api/getAnswer', // route for response file
      {
        question : $('#question input:text').val(), 
      }, // datas
      // function callback: to manage the return (alias "sucess")
      function(data) {
        // Insert user question and answers in "dialog" "div"
        Insert_dialog(data);
        // Clean input form
        $('#question input:text').val('');
        // Display and refresh map position with coordinates.
        $('#jb_map').show("slow");
        $('#loading').hide();
        Mapbox(data);
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

